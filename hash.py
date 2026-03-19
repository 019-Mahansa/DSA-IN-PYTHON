def get_hash(n):
    hash = 0
    for i in n:
        hash += ord(i)
    return hash % 100

print(get_hash("march 28"))

class hash_table:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
    
    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % 100
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

        
    

t = hash_table()
t.add("march 2", 100)
t.arr
