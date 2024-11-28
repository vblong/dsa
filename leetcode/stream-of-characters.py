class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class StreamChecker:

    def __init__(self, words):
        # self.words = words
        self.words = []
        # for w in words:
        #     self.words.append("".join(reversed(w)))
        self.root = TrieNode()
        for w in words:
            self.insert( "".join(reversed(w)) )
        
        self.stream = ""
        self.startIndices = []

    def insert(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.isWord = True

    def search(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current and current.isWord

    def startsWith(self, searchTerm):
        current = self.root
        # print('searching', searchTerm)
        for character in searchTerm:
            if current and current.isWord:
                # print('character', character, 'FOUND')
                return True
            if character not in current.children:
                return False
            current = current.children[character]
        # print('>>>>>>> NOT FOUND')
        return False
    
    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        # print('--------- STREAM', self.stream)
        # self.insert(self.stream)
        # for searchTerm in self.words:
        #     if self.startsWith(searchTerm):
        #         return True
        # return False
        if self.startsWith(self.stream):
            print('at ', letter, '........True')
            return True
        print('at ', letter, 'False')
        return False
        # if letter in self.root.children:
        #     self.startIndices.append(len(self.stream) - 1)
        # for si in self.startIndices:
        #     searchTerm = self.stream[si:]
        #     # print('searching', searchTerm)
        #     if self.search(searchTerm):
        #         # print('XXXXXXXXXXXXXXXX> Found')
        #         return True
        #     # print('----> not found')
        # return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

streamChecker = StreamChecker(["cd", "f", "kl"])
streamChecker.query("a") # return False
streamChecker.query("b") # return False
streamChecker.query("c") # return False
streamChecker.query("d") # return True, because 'cd' is in the wordlist
streamChecker.query("e") # return False
streamChecker.query("f") # return True, because 'f' is in the wordlist
streamChecker.query("g") # return False
streamChecker.query("h") # return False
streamChecker.query("i") # return False
streamChecker.query("j") # return False
streamChecker.query("k") # return False
streamChecker.query("l") # return True, because 'kl' is in the wordlist