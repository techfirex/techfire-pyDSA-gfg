class myHash:
    def __init__(self, c):
        self.CAP = c
        self.TABLE = [-1] * c
        self.SIZE = 0
    
    def hash(self, x):
        return x % self.CAP

    def insert(self, x):
        if self.SIZE == self.CAP:
            return False
        
        if self.search(x) == True:
            return False
        
        i = self.hash(x)
        t = self.TABLE
        while t[i] not in (-1,-2):
            i = (i+1) % self.CAP
        t[i] = x

        self.SIZE = self.SIZE + 1
        return True
 
    def remove(self, x):
        h = self.hash(x)
        t = self.TABLE
        i = h

        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i+1) % self.CAP

            if i == h:
                return False
        return False
  
    def search(self, x):
        h = self.hash(x)
        t = self.TABLE
        i = h
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i+1) % self.CAP
            if i == h:
                return False
        return False

h = myHash(7)
h.insert(49)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.remove(56))
print(h.search(56))

# ==================================
# how to handle cases when -1 and -2 can be input keys?
# - we can use None for empty
# - we can use DUMMY nodes for deleted items // it will come from library