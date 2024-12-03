class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # If you want to initialize the list
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

    def print_list(self):
        temp = self.head
        li = ""
        while temp is not None:
            li += str(temp.value) + "-->"
            temp = temp.next
        print(li)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # here we have 3 use cases.
        temp = self.head
        pre = self.head
        if self.length == 0:
            # 1st if there is no node.
            print("Linked List is empty")
            return
        while temp.next:
            # 2nd remove the node.
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            # 3rd after removal, if there is no node.
            self.head = None
            self.tail = None
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return 
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return self.tail

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        print(self.length, index)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev = self.get(index - 1)
        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index - 1)
        current = prev.next
        prev.next = current.next
        current.next = None
        self.length -= 1
        return current
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    
l = LinkedList(4)
l.append(5)
l.append(6)
l.append(9)
l.append(8)
l.append(1)
# l.pop()
# l.pop_first()
l.print_list()
# l.set_value(0, 10)
# l.insert(6, 3)
l.remove(0)
# print(l.get(3).value)
l.reverse()
l.print_list()