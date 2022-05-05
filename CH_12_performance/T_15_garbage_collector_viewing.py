import gc
import collections


if __name__ == '__main__':
    objects = collections.Counter()
    for object_ in gc.get_objects():
        objects[type(object_)] += 1

    print(f'Different object count: {len(objects)}')
    for object_, count in objects.most_common(10):
        print(f'{count}: {object_}')
