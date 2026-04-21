#https://leetcode.com/problems/lru-cache/description/
class Node:
    def __init__(self,key=0, val=0, prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left_most = Node(0,0)
        self.right_most = Node(0,0)

        self.left_most.next = self.right_most
        self.right_most.prev = self.left_most

        self.left_most.prev = None
        self.right_most.next = None

    def insert(self,node):
        previous = self.right_most.prev
        
        previous.next = node
        node.prev = previous

        node.next = self.right_most
        self.right_most.prev = node

    def remove(self,node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
            
        node = Node(key,value)
        self.cache[key]=node
        self.insert(node)

        if len(self.cache)>self.capacity:
            lru_node = self.left_most.next
            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
