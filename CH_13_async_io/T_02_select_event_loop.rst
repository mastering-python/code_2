>>> import asyncio
>>> import selectors


>>> selector = selectors.SelectSelector()
>>> loop = asyncio.SelectorEventLoop(selector)
>>> asyncio.set_event_loop(loop)
