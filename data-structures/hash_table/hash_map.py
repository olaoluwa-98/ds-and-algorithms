"""
This hashmap implementation assumes that keys are positive integers for simplicity sake
"""
class Item:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class HashMap:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        hash = self._hash(key)
        for item in self.table[hash]:
            if item.key == key:
                return
        self.table[hash].append(Item(key, value))
    
    def get(self, key):
        hash = self._hash(key)
        for item in self.table[hash]:
            if item.key == key:
                return item.value
        raise KeyError("Key not found")
    
    def remove(self, key):
        hash = self._hash(key)
        for index, item in enumerate(self.table[hash]):
            if item.key == key:
                del self.table[hash][index]
                return
        raise KeyError("Key not found")


# Test cases

# hashmap with 5 items
hash_map = HashMap(5)
hash_map.put(5, 'Hashmap')
hash_map.put(5, 'Hashmap')
assert hash_map.get(5) == 'Hashmap'

hash_map.put(10, 'Hashtable implementation')
assert hash_map.get(10) == 'Hashtable implementation'

hash_map.remove(10)

try:
    assert hash_map.get(10) == None
except KeyError as e:
    pass
