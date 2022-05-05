
class Slots(object):
    __slots__ = 'index', 'name', 'description'

    def __init__(self, index):
        self.index = index
        self.name = 'slot %d' % index
        self.description = 'some slot with index %d' % index


class NoSlots(object):

    def __init__(self, index):
        self.index = index
        self.name = 'slot %d' % index
        self.description = 'some slot with index %d' % index


try:
    import memory_profiler
except ImportError:
    print('Please install the memory profiler to run this example')
    print('pip install -U memory-profiler')
else:
    @memory_profiler.profile
    def main():
        slots = [Slots(i) for i in range(25000)]
        no_slots = [NoSlots(i) for i in range(25000)]
        return slots, no_slots

    if __name__ == '__main__':
        main()

