import copy


class Wordplay:
    def __init__(self, words = []):
        self.words = copy.deepcopy(words)
    def add_word(self, n):
        if set([n]).isdisjoint(set(self.words)):
            self.words.append(n)

    def words_with_length(self, n):
        return [t for t in self.words if len(t) == n]

    def only(self, *n):
        return [t for t in self.words if set(t).issubset(set(n))]

    def avoid(self, *n):
        return [t for t in self.words if set(t).isdisjoint(set(n))]

wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.avoid('p', 'r'))