>>> import asyncio


>>> HOST = '127.0.0.1'
>>> PORT = 1234


>>> async def echo_client(message):
...     # Open the connection to the server
...     reader, writer = await asyncio.open_connection(HOST, PORT)
... 
...     print(f'Client sending {message!r}')
...     writer.write(message)
... 
...     # We need to drain and write the EOF to stop sending
...     writer.write_eof()
...     await writer.drain()
... 
...     async for line in reader:
...         print(f'Client received: {line!r}')
... 
...     writer.close()


>>> async def echo(reader, writer):
...     # Read all lines from the reader and send them back
...     async for line in reader:
...         print(f'Server received: {line!r}')
...         writer.write(line)
...         await writer.drain()
... 
...     writer.close()


>>> async def echo_server():
...     # Create a TCP server that listens on `HOST`/`PORT` and
...     # calls `echo` when a client connects.
...     server = await asyncio.start_server(echo, HOST, PORT)
... 
...     # Start listening
...     async with server:
...         await server.serve_forever()


>>> async def main():
...     # Create and run the echo server
...     server_task = asyncio.create_task(echo_server())
... 
...     # Wait a little for the server to start
...     await asyncio.sleep(0.01)
... 
...     # Create a client and send the message
...     await echo_client(b'test message')
... 
...     # Kill the server
...     server_task.cancel()


>>> asyncio.run(main())
Client sending b'test message'
Server received: b'test message'
Client received: b'test message'
