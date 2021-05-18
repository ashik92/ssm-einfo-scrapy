from pymongo import MongoClient


class MongoAccess:
    """ Pipeline Mixin to open a connection to MongoDB
        arguments: require either <db, coll_name> or <database_url, db_name, coll_name>
        if db is not passed, the class will open/close the connection with database_url and db_name
        the mixin sets the following attributes: db, collection for pipeline to use
    """

    def __init__(self, *args, database_url='', db_name='', coll_name='', db=None, **kwargs):
        self.database_url = database_url
        self.db_name = db_name
        self.coll_name = coll_name
        self.db = db
        super().__init__(*args, **kwargs)

    def open_spider(self, spider):
        if self.db:
            self.mongo_client = None
        else:
            self.mongo_client = MongoClient(self.database_url)
            self.db = self.mongo_client[self.db_name]

        self.collection = self.db[self.coll_name]

        try:
            super().open_spider(spider)
        except AttributeError:
            pass

    def close_spider(self, spider):
        try:
            super().close_spider(spider)
        except AttributeError:
            pass

        if self.mongo_client:
            self.mongo_client.close()


class BatchProcessing:
    """ Pipeline Mixin to perform processing in batches
        after using this mixin, process_item method will not do anything
        unless the batch reaches <batch_size>
    """

    def __init__(self, *args, batch_size=100, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch_size = batch_size
        self.batch = []

    def bulk_process_items(self, items, spider):
        """ you need to implement this method in your pipeline class """
        raise NotImplementedError

    def process_item(self, item, spider):
        self.batch.append(item)

        if len(self.batch) >= self.batch_size:
            self.bulk_process_items(self.batch, spider)
            self.batch = []

        return item

    def close_spider(self, spider):
        # process remaining items
        if self.batch:
            self.bulk_process_items(self.batch, spider)
            self.batch = []

        try:
            super().close_spider(spider)
        except AttributeError:
            pass
