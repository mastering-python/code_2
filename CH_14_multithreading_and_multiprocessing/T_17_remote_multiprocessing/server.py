import multiprocessing
from multiprocessing import managers

import constants
import functions

queue = multiprocessing.Queue()
manager = managers.BaseManager(address=('', constants.port),
                               authkey=constants.password)

manager.register('queue', callable=lambda: queue)
manager.register('primes', callable=functions.primes)

server = manager.get_server()
server.serve_forever()

