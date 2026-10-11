class TrieNode:
    def __init__(self, val = ''):
        self.val = val
        self.neighbors = {}
class PrefixTree:

    def __init__(self):
        self.god_father = TrieNode()

    def insert(self, word: str) -> None:
        tmp = self.god_father
        for i in range(len(word)):
            if word[i] not in tmp.neighbors:
                node = TrieNode(word[i])
                tmp.neighbors[word[i]] = node
                tmp = node
            else:
                tmp = tmp.neighbors[word[i]]
        end_node = TrieNode("/")
        tmp.neighbors["/"] = end_node



    def search(self, word: str) -> bool:

        tmp = self.god_father
        for i in range(len(word)):
            if word[i] in tmp.neighbors:
                tmp = tmp.neighbors[word[i]]
            else:
                return False
        end_character = "/"
        if end_character in tmp.neighbors:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.god_father
        for i in range(len(prefix)):
            if prefix[i] in tmp.neighbors:
                tmp = tmp.neighbors[prefix[i]]
            else:
                return False
        return True
        
        