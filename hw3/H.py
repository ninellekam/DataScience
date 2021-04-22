from collections import deque
import time


class Node:
    def __init__(self, char, is_end):
        self.char = char
        self.children = [None] * 123
        self.is_end = is_end


class TrieIterator:

    def __init__(self, root=None):
        queue = deque()
        queue.append(root)
        self.index = -1
        words = []
        while queue:
            node = queue.pop()
            if node.is_end:
                words.append(node.data)
            [queue.appendleft(node) for node in node.children if node is not None]
        self.n = len(words)
        self.words = words

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.n:
            return self.words[self.index]
        raise StopIteration


class Trie:

    def __init__(self):
        self.wordCount = 0
        self.root = Node("", False)

    def add(self, word):
        node = self.root
        n = len(word)
        k = 0
        for i in range(n):
            if node.children[ord(word[i])] is not None:
                node = node.children[ord(word[i])]
                k = i + 1
            else:
                break

        if k != n or node.is_end is False:
            for i in range(k, n):
                new_node = Node(word[i], False)
                node.children[ord(word[i])] = new_node
                node = new_node

            node.data = word
            node.is_end = True
            self.wordCount += 1

    def pop(self, word):
        node = self.root
        n = len(word)
        k = 0
        for i in range(n):
            if node.children[ord(word[i])] is not None:
                node = node.children[ord(word[i])]
                k = i

        if k != n - 1 or node.is_end is False:
            raise KeyError(word)

        node.is_end = False
        self.wordCount -= 1

    def __len__(self):
        return self.wordCount

    def __contains__(self, item):
        node = self.root
        n = len(item)
        for i in range(n):
            f = False
            if node.children[ord(item[i])] is not None:
                node = node.children[ord(item[i])]
            else:
                return False
        return node.is_end

    def starts_with(self, word):
        node = self.root
        n = len(word)
        for i in range(n):
            f = False
            for child in node.children:
                if child is not None and word[i] == child.char:
                    node = child
                    f = True
                    break
            if not f:
                return TrieIterator()
        return TrieIterator(node)

    def __iter__(self):
        self.iterTree = TrieIterator(self.root)
        return self.iterTree

    def __next__(self):
        return next(self.iterTree)
