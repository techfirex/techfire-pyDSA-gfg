# hash(x) = x % BUCKET
# Watch Video for Example

class myHash:
    def __init__(self, b):
        self.BUCKET = b
        self.TABLE = [[] for x in range(b)] # [[], [], [], [], [], [], []]
    
    def insert(self, x):
        i = x % self.BUCKET
        self.TABLE[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        if x in self.TABLE[i]:
            self.TABLE[i].remove(x)
    
    def search(self, x):
        i = x % self.BUCKET
        return x in self.TABLE[i]

h = myHash(7)
h.insert(70) # [[70], [], [], [], [], [], []] 
h.insert(71) # [[70], [71], [], [], [], [], []]
h.insert(9) # [[70], [71], [9], [], [], [], []]
h.insert(56) # [[70, 56], [71], [9], [], [], [], []]
h.insert(72) # [[70, 56], [71], [9, 72], [], [], [], []]

print(h.search(56))
h.remove(56)
print(h.search(56))


