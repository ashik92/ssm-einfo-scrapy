# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from pymongo import ReplaceOne
from pymongo.errors import AutoReconnect
from retry import retry

from fire_ant.pipeline import MongoAccess, BatchProcessing
from .settings import DATABASE_URL

logger = logging.getLogger(__name__)


class ExampleScrapyCompanyPipeline(MongoAccess, BatchProcessing):
    def __init__(self, db=None, batch_size=9):
        super().__init__(
            database_url=DATABASE_URL,
            db_name="timesbusinessdirectory",
            coll_name="crawled_company_data",
            db=db,
            batch_size=batch_size
        )

    def open_spider(self, spider):
        super().open_spider(spider)

        # will ignore if index exists
        self.collection.create_index([("company_uen", 1)], unique=True)

    @retry(AutoReconnect, tries=4, delay=20)
    def bulk_process_items(self, items, spider):
        logger.info("processing {} items...".format(len(items)))

        # bulk upserts
        ops = [
            ReplaceOne({"company_uen": comp["company_uen"]}, comp, upsert=True)
            for comp in items
            if comp["company_uen"] is not None
        ]

        if ops:
            result = self.collection.bulk_write(ops, ordered=False)

            logger.info({
                k: v
                for k, v in result.bulk_api_result.items()
                if k.startswith("write") or k.startswith("n")
            })
        else:
            logger.info("all items are invalid, nothing to process")
