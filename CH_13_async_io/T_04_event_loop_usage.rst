>>> import time
>>> import asyncio


>>> def printer(name):
...     print(f'Started {name} at {loop.time() - offset:.1f}')
...     time.sleep(0.2)
...     print(f'Finished {name} at {loop.time() - offset:.1f}')

>>> loop = asyncio.new_event_loop()
>>> _ = loop.call_at(loop.time() + .2, printer, 'call_at')
>>> _ = loop.call_later(.1, printer, 'call_later')
>>> _ = loop.call_soon(printer, 'call_soon')
>>> _ = loop.call_soon_threadsafe(printer, 'call_soon_threadsafe')

# Make sure we stop after a second

>>> _ = loop.call_later(1, loop.stop)

# Store the offset because the loop requires time to start

>>> offset = loop.time()

>>> loop.run_until_complete(asyncio.sleep(0))
Started call_soon at 0.0
Finished call_soon at 0.2
Started call_soon_threadsafe at 0.2
Finished call_soon_threadsafe at 0.4
Started call_later at 0.4
Finished call_later at 0.6
Started call_at at 0.6
Finished call_at at 0.8
