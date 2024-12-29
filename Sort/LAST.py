#Hash Modulo
def hash_modulo(key, size):
    return key % size
keys = [15, 27, 8, 12]
size = 10
hash_values = [hash_modulo(key, size) for key in keys]
print ("Modulo Hash Values:", hash_values)


#Middle of Square Hash Function
def hash_middle_of_square(key, size):
    squared_key = key ** 2
    squared_str = str(squared_key)
    mid = len(squared_str) // 2
    middle_digits = int(squared_str[mid - 1: mid + 1])
    return middle_digits % size
keys = [15, 27, 8, 12]
size = 10
hash_values = [hash_middle_of_square(key, size) for key in keys]
print("Middle of Square Hash Values:", hash_values)


#Folding Hash Function
def hash_folding(key, size):
    key_str = str(key)
    parts = [int(key_str[i:i+2]) for i in range(0, len(key_str), 2)]
    return sum(parts) % size
keys = [12345, 67890, 24680]
size = 10
hash_values = [hash_folding(key, size) for key in keys]
print("Folding Hash Values:", hash_values)

#Collision Resolution Techniques

#Separate Chaining
class HashTableSC:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash(self, key):
        return key % self.size
    def insert(self, key):
        index = self.hash(key)
        self.table[index].append(key)
    def display(self):
        for index, chain in enumerate(self.table):
            print(f"Index {index}: {chain}")
hash_table_sc = HashTableSC(10)
keys = [15, 25, 35, 45]
for key in keys:
    hash_table_sc.insert(key)
hash_table_sc.display()

#Open Addressing
#Linear Probing
class HashTableLP:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash(self, key):
        return key % self.size
    def insert(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key
    def display(self):
        for index, value in enumerate(self.table):
            print(f"Index {index}: {value}")
hash_table_lp = HashTableLP(10)
keys = [15, 25, 35, 45]
for key in keys:
    hash_table_lp.insert(key)
hash_table_lp.display()


#Quadratic Probing
class HashTableQP:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash(self, key):
        return key % self.size
    def insert(self, key):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            index = (index + i**2) % self.size
            i += 1
        self.table[index] = key
    def display(self):
        for index, value in enumerate(self.table):
            print(f"Index {index}: {value}")
hash_table_qp = HashTableQP(10)
keys = [15, 25, 35, 45]
for key in keys:
    hash_table_qp.insert(key)
hash_table_qp.display()


#Double Hashing
class HashTableDH:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash1(self, key):
        return key % self.size
    def hash2(self, key):
        return 1 + (key % (self.size - 1))
    def insert(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        while self.table[index] is not None:
            index = (index + step) % self.size
        self.table[index] = key
    def display(self):
        for index, value in enumerate(self.table):
            print(f"Index {index}: {value}")
hash_table_dh = HashTableDH(10)
keys = [15, 25, 35, 45]
for key in keys:
    hash_table_dh.insert(key)
hash_table_dh.display()
