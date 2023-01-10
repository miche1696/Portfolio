#second VERSION (with DUPLICATS)
class Classe:
    def __init__(self):
        self.values = []
        self.map = collections.defaultdict(set)
    
    def insert(self,value):
        self.map[value].add(len(self.values))
        self.values.add(value)

        

    def remove(self,value):
        if value not in self.map:
            return
        i = self.map[value].iterator().next()
        val = self.values[-1]
        self.values[-1]=value
        self.values[i] = val
        self.map[val].remove(len(self.values))
        self.map[val].add(i)

        self.values.pop()
        self.map[value].remove(i)

    def get_random(self):
        return random.choice(self.values)


#first VERSION (WITHout DUPLICATES)
class Classe:
    def __init__(self):
        self.values = []
        self.map = {}
    
    def insert(self,value):
        if value in self.map:
            return
        self.values.append(value)
        self.map[value] = len(self.values)

    def remove(self,value):
        if value not in self.map:
            return
        i = self.map[value]
        val = self.values[-1]
        self.values[-1]=value
        self.values[i] = val
        self.map[val]=i

    def get_random(self):
        return random.choice(self.values)
