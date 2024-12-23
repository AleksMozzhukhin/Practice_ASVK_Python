import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)

    @property
    def window(self):
        try:
            return self._queue[0]
        except IndexError:
            return None

    def __contains__(self, filter_func):
        return any(filter_func(item) for item in self._queue)

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        item = self.get_nowait()
        self.put_nowait(item)

    async def get(self, filter=None):
        if filter is None or filter not in self:
            return await super().get()
        else:
            while not filter(self.window):
                self.later()
            return await super().get()
