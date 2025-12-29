## 4. 前缀树 Trie

# **使用场景：**
# - 字符串前缀匹配
# - 自动补全
# - 单词搜索

# **时间复杂度：** O(m)，m为字符串长度

# **典型例题：**
# - LeetCode 208. 实现 Trie
# - LeetCode 211. 添加与搜索单词
# - LeetCode 212. 单词搜索 II


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def __str__(self) -> str:
        return f"children={self.children}, is_end={self.is_end}"
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self) -> str:
        return f"Trie <{self.root}>"
    
    def print(self):
        for char in self.root.children:
            print(char)

    
    def insert(self, word):
        node = self.root
        for char in word:
            print(char)
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def main():
    trie = Trie()
    trie.insert("apple")
    trie.print()
    # print(trie.search("apple"))
    # print(trie.search("app"))
    # print(trie.startsWith("app"))
    # trie.insert("app")
    # print(trie.search("app"))

if __name__ == '__main__':
    main()
