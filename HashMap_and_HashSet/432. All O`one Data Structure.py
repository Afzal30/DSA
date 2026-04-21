#https://leetcode.com/problems/all-oone-data-structure/description/
class Node():
    def __init__(self,count):
        self.strval = set()
        self.count = count
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.key_dict = {}
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def inc(self, key: str) -> None:

        if key in self.key_dict:
            node = self.key_dict[key]
            count = node.count
            node.strval.remove(key)

            next_node = node.next

            if next_node==self.tail or next_node.count != count+1:
                new_node = Node(count+1)
                new_node.strval.add(key)
                new_node.prev = node
                node.next = new_node
                next_node.prev = new_node
                new_node.next = next_node
                self.key_dict[key] = new_node

            else:
                next_node.strval.add(key)
                self.key_dict[key] = next_node

            if len(node.strval)==0:
                self.remove(node)

            

        else:
            first_node = self.head.next

            if first_node == self.tail or first_node.count>1:
                new_node = Node(1)
                new_node.strval.add(key)
                new_node.prev = self.head
                new_node.next = first_node
                self.head.next = new_node
                first_node.prev = new_node
                self.key_dict[key] = new_node

            else:
                first_node.strval.add(key)
                self.key_dict[key] = first_node

    def dec(self, key: str) -> None:

        node = self.key_dict[key]
        node.strval.remove(key)
        count = node.count

        if count == 1:
            del self.key_dict[key]

        else:

            prev_node = node.prev

            if prev_node == self.head or prev_node.count != count-1:
                new_node = Node(count-1)
                new_node.strval.add(key)
                new_node.prev = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.prev = new_node
                self.key_dict[key] = new_node



            else:
                prev_node.strval.add(key)
                self.key_dict[key]=prev_node

        if len(node.strval)==0:
            self.remove(node)

        

    def getMaxKey(self) -> str:

        if self.head.next == self.tail:
            return ""

        else:
            for ele  in self.tail.prev.strval:
                return ele
        

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        else:
            for ele in self.head.next.strval:
                return ele

    def remove(self,node):
        nxt = node.next
        previous = node.prev

        previous.next = nxt
        nxt.prev = previous
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
