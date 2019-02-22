
class DoubleLLSentinel(object):
    class LLNode(object):
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.size = 0
        self.sntl = self.LLNode()
        self.sntl.next = self.sntl
        self.sntl.prev = self.sntl

    def __len__(self):
        return self.size

    def __str__(self):
        v = []
        x = self.sntl.next
        while x != self.sntl:
            v.append(str(x.data))
            x = x.next
        return ' '.join(v)

    def search(self, key):
        x = self.sntl.next
        while x != self.sntl and x.data != key:
            x = x.next
        if x == self.sntl:
            x = None
        return x

    def insertStack(self, x):
        node = self.LLNode(x)
        node.next = self.sntl.next
        self.sntl.next.prev = node
        self.sntl.next = node
        node.prev = self.sntl
        self.size += 1

    def insertQueue(self, x):
        node = self.LLNode(x)
        node.prev = self.sntl.prev
        node.next = self.sntl.prev.next
        self.sntl.prev.next = node
        node.next.prev = node
        self.size += 1

    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
