class PrimesIterator:
    def __init__(self):
        self._known_primes = []
        self._candidate = 2
    #
    def __next__(self):
        while True:
            is_prime = True
            for d in self._known_primes:
                if self._candidate % d == 0:
                    is_prime = False
                    break
                if d > self._candidate**0.5:
                    break

            if is_prime:
                self._known_primes.append(self._candidate)
                self._candidate += 1
                return self._candidate
            self._candidate += 1
    #

class Primes:
    def __iter__(self):
        finger = PrimesIterator()
        return finger

obj = Primes()
for e in obj:
    print('Нове просте число:', e)