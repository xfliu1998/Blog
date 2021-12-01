class Trie:
    """
    实现一个字符集为小写英文字母的前缀树
    """
    def __init__(self):
        """
        Initialize data structure.
        """
        self.children = [None] * 26
        self.isEnd = False  # 该节点是否是字符串的结尾

    def searchPrefix(self, prefix):
        """
        return None if prefix not in trie else the end of the prefix
        """
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                # 子节点不存在，创建一个新的子节点
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix) is not None


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))     # True
    print(trie.search("app"))       # False
    print(trie.startsWith("app"))   # True
    trie.insert("app")
    print(trie.search("app"))       # True
