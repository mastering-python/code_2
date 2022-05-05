import multiprocessing


some_int = multiprocessing.Value('i', 123)
with some_int.get_lock():
    some_int.value += 10
print(some_int.value)

some_double_array = multiprocessing.Array('d', [1, 2, 3])
with some_double_array.get_lock():
    some_double_array[0] += 2.5
print(some_double_array[:])


from multiprocessing import shared_memory
# From process A we could write something
name = 'share_a'
share_a = shared_memory.SharedMemory(name, create=True, size=4)
share_a.buf[0] = 10

# From a different process we could access the data:
share_a = shared_memory.SharedMemory(name)
print(share_a.buf[0])

# Make sure to clean up after. And only once!
share_a.unlink()


from multiprocessing import shared_memory


shared_list = shared_memory.ShareableList(['Hi', 1, False, None])
# Changing type from str to bool here
shared_list[0] = True
# Don't forget to unlink()
shared_list.shm.unlink()
