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
        print(self.length)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

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
        return temp
                



    

    
l = LinkedList(4)
# l.append(5)
# l.append(6)
# l.append(9)
# l.append(8)
# l.append(7)
l.pop()
l.print_list()
