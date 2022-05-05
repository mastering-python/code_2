While the `sleep` command is available on most systems, Windows is
the notable exception. The Windows alternative for the `sleep`
command is the `timeout` command which is not the same but serves
the same purpose for these examples.

Alternatively I can recommand the Git for Windows installer which
allows you to install "optional Unix tools".

>>> import time
>>> import subprocess


>>> def subprocess_sleep():
...     print(f'Started sleep at: {time.time() - start:.1f}')
...     process = subprocess.Popen(['sleep', '0.1'])
...     process.wait()
...     print(f'Finished sleep at: {time.time() - start:.1f}')


>>> start = time.time()

First, we run this completely sequentially:
>>> for _ in range(2):
...     subprocess_sleep()
Started sleep at: 0.0
Finished sleep at: 0.1
Started sleep at: 0.1
Finished sleep at: 0.2

------------------------------------------------------------------------------


>>> import time
>>> import subprocess


>>> def subprocess_sleep():
...     print(f'Started sleep at: {time.time() - start:.1f}')
...     return subprocess.Popen(['sleep', '0.1'])


>>> start = time.time()

Now we start all processes immediately and only wait for output:
>>> processes = []
>>> for _ in range(2):
...     processes.append(subprocess_sleep())
Started sleep at: 0.0
Started sleep at: 0.0

The processes should be running in the background now:
>>> for process in processes:
...     returncode = process.wait()
...     print(f'Finished sleep at: {time.time() - start:.1f}')
Finished sleep at: 0.1
Finished sleep at: 0.1

------------------------------------------------------------------------------

>>> import time
>>> import asyncio


>>> async def async_process_sleep():
...     print(f'Started sleep at: {time.time() - start:.1f}')
...     process = await asyncio.create_subprocess_exec('sleep', '0.1')
...     await process.wait()
...     print(f'Finished sleep at: {time.time() - start:.1f}')


>>> async def main():
...     coroutines = []
...     for _ in range(2):
...         coroutines.append(async_process_sleep())
...     await asyncio.gather(*coroutines)


>>> start = time.time()
>>> asyncio.run(main())
Started sleep at: 0.0
Started sleep at: 0.0
Finished sleep at: 0.1
Finished sleep at: 0.1

------------------------------------------------------------------------------

>>> import time
>>> import asyncio


>>> async def run_python_script(script):
...     process = await asyncio.create_subprocess_exec(
...         'python3',
...         stdout=asyncio.subprocess.PIPE,
...         stdin=asyncio.subprocess.PIPE,
...     )
...     print(f'Executing: {script!r}')
...     stdout, stderr = await process.communicate(script)
...     print(f'stdout: {stdout!r}')


>>> asyncio.run(run_python_script(b'print("Hi~")'))
Executing: b'print("Hi~")'
stdout: b'Hi~\n'

------------------------------------------------------------------

>>> import asyncio


>>> async def run_script():
...     process = await asyncio.create_subprocess_exec(
...         'python3',
...         stdout=asyncio.subprocess.PIPE,
...         stdin=asyncio.subprocess.PIPE,
...     )
... 
...     # Write a simple Python script to the interpreter
...     process.stdin.write(b'print("Hi~")')
... 
...     # Make sure the stdin is flushed asynchronously
...     await process.stdin.drain()
...     # And send the end of file so the Python interpreter will
...     # start processing the input. Without this the process will
...     # stall forever.
...     process.stdin.write_eof()
... 
...     # Fetch the lines from the stdout asynchronously
...     async for line in process.stdout:
...         # Decode the output from bytes and strip the whitespace
...         # (newline) at the right
...         print('stdout:', line.rstrip())
... 
...     # Wait for the process to exit
...     await process.wait()


>>> asyncio.run(run_script())
stdout: b'Hi~'
