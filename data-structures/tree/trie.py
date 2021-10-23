class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.is_end = False
        self.counter = 0 # indicates how many times a word is inserted i.e no of times is_end = True
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = Node("")
    
    def insert_word(self, word):
        """Insert a word into the trie"""
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1
    
    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.data, node.counter))
        for child in node.children.values():
            self.dfs(child, prefix + node.data)
    
    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

trie = Trie()
trie.insert_word("Ball")

trie.insert_word("was")
trie.insert_word("word")
trie.insert_word("war")
trie.insert_word("what")
trie.insert_word("what")
trie.insert_word("where")
trie.insert_word("where")
trie.insert_word("whey")
trie.insert_word("wh")

print(trie.query("wh"))


"""
Time complexity
m is the length of the longest word
n is the number of words in the trie
a is the length of the word you're searching for

Create = O(m * n)
Lookup = O(a * n)
Insert = O(a * n)
Delete = O(a * n)
"""