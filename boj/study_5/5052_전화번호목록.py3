import sys

class Node():
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie():
    def __init__(self):
        self.head = Node()
    def insert(self, string):
        cur_node = self.head
        for c in string:
            if c not in cur_node.child:
                cur_node.child[c] = Node(c)
            cur_node = cur_node.child[c]
    def check(self, string):
        cur_node = self.head
        for c in string:
            cur_node = cur_node.child[c]
        if cur_node.child:
            return True
        else:
            return False

t = int(sys.stdin.readline())
for _ in range(t):
    retrieve = Trie()
    n = int(sys.stdin.readline())
    phone_book = []
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        retrieve.insert(s)
        phone_book.append(s)
    for phone_num in phone_book:
        if retrieve.check(phone_num):
            print("NO")
            break
    else:
        print("YES")