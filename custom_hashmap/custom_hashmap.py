from abstract_hashmap import AbstractHashMap


class HashMap(AbstractHashMap):
    def __init__(self, size=10):
        self.table = [[] for _ in range(size)]
        self.size = size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
            else:
                return None

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return True
        return False

    def __len__(self):
        return self.count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

