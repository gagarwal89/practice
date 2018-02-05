from node import Node

class LinkedList(object):
    """LinkedList implementation using Node"""
    def __init__(self):
        self.head = None
    
    def print(self):
        temp = self.head
        while temp is not None:
            print str(temp.data) + "->"
            temp = temp.next

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        
        temp.next = new_node
        return

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
        return

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos < 0:
            raise Exception("Invalid position specified")

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        i = 0
        temp = self.head
        while i < pos-1:
            if temp is None:
                raise Exception("Invalid position specified")

            temp = temp.next
            i = i+1

        new_node.next = temp.next
        temp.next = new_node
        return

    def delete_at_start(self):
        if self.head is None:
            raise Exception("No elements in linked list")
        
        tmp = self.head.data
        self.head = self.head.next
        return tmp 

    def delete_at_end(self):
        if self.head is None:
            raise Exception("No elements in linked list")

        if self.head.next is None:
            tmp = self.head.data
            self.head = None
            return tmp

        prev = self.head
        temp = prev.next
        while temp.next is not None:
            prev = prev.next
            temp = temp.next

        tmp = temp.data
        prev.next = None
        return tmp

    def delete_at_pos(self, pos):
        if self.head is None:
            raise Exception("No elements in linked list")

        if pos < 0:
            raise Exception("Invalid position specified")

        if pos == 0:
            temp = self.head.next
            tmp = self.head.data
            self.head = temp
            return tmp

        prev = self.head
        temp = prev.next
        i = 0
        while i < pos-1:
            if temp is None:
                raise Exception("Invalid position specified")
            prev = prev.next
            temp = temp.next
            i = i+1

        if temp is None:
            raise Exception("Invalid position specified")

        tmp = temp.data
        prev.next = temp.next
        return tmp

    def mth_to_last(self, m):
        """FAKE"""
        if self.head is None:
            raise Exception("No elements in linked list")

        if m < 0:
            raise Exception("Invalid position specified")

        temp = self.head
        fwd = temp
        i = 0
        while i < m:
            if fwd is None:
                raise Exception("Not enough elements")
            fwd = fwd.next
            i += 1

        while fwd.next is not None:
            fwd = fwd.next
            temp = temp.next

        return temp

    def has_cycle(self):
        if self.head is None:
            return False

        slow = self.head
        if slow.next is None:
            return False


        fast = slow.next
        while fast is not None and fast.next is not None:
            if fast.next is slow or fast.next.next is slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False