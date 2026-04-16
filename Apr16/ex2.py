class MyIterator:
    def __init__(self):
        self._numtimes = 0

    def __next__(self):
        self._numtimes += 1
        if self._numtimes > 10:
            raise StopIteration
        else:
            return 125 + self._numtimes


class MyIterable:
    def __iter__(self):
        finger = MyIterator()
        return finger


obj = MyIterable()

for e in obj:
    print('---------')
    print(e)