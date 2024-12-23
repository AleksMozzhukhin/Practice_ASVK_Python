import random
import asyncio

class Seq:
    _last_future = asyncio.Future()
    _last_future.set_result(None)

    def __init__(self, name):
        self.name = name
        self._prev_future = Seq._last_future
        self._current_future = asyncio.Future()
        Seq._last_future = self._current_future

    async def run(self):
        await self._prev_future
        print(self.name)
        self._current_future.set_result(self.name)
        return self.name
