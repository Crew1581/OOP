class TextHandler:
    def __init__(self):
        self.s = []
    def add_words(self, t):
        self.s += t.split()
    def get_shortest_words(self):
        self.counter = []
        self.lst = []
        for self.i in self.s:
            self.counter.append(len(self.i))
        for self.j in self.s:
            if len(self.j) == min(self.counter):
                self.lst.append(self.j)
        return self.lst

    def get_longest_words(self):
        self.counter = []
        self.lst = []
        for self.i in self.s:
            self.counter.append(len(self.i))
        for self.j in self.s:
            if len(self.j) == max(self.counter):
                self.lst.append(self.j)
        return self.lst

texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())