import asyncio
from contextlib import asynccontextmanager


class TaskList():
    def __init__(self):
        self.undone = []

    def append(self, coro):
        """ schedule a coroutine as task """
        self.undone = [t for t in self.undone if not t.done()]
        self.undone.append(asyncio.create_task(coro))

    def __iter__(self):
        return iter(self.undone)


@asynccontextmanager
async def task_group():
    """ ensure all async tasks created within the context are done when exiting """
    tasks = TaskList()

    try:
        yield tasks
    finally:
        for tsk in tasks:
            if not tsk.done():
                await tsk
