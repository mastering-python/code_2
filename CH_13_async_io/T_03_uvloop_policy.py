import asyncio


class UvLoopPolicy(asyncio.DefaultEventLoopPolicy):
    def new_event_loop(self):
        try:
            from uvloop import Loop
            return Loop()
        except ImportError:
            return super().new_event_loop()


asyncio.set_event_loop_policy(UvLoopPolicy())
