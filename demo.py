# a = '[][{]}'
a = '[{}[{{}]}(())]'
# a = '[{}[{{}}](())]'

def is_check(s: str):
    if "[" == s:
        return True
    elif "{" == s:
        return True
    if "(" == s:
        return True
    return False

def check_para(s: str) -> bool:
    li = []
    index = []
    for i, v in enumerate(s):
        # print(v)
        if is_check(v):
            li.append(v)
            index.append(i)
        else:
            if  "]" == v and "[" in li:
                li.pop()
                index.pop()
            if "}" == v and "{" in li:
                li.pop()
                index.pop()
            if v == ")" and "(" in li:
                li.pop()
                index.pop()
    print(li, index)
    # if li:
    #     print("this is not valid")
    #     print(f"On {li['index']}")
    #     return False
    # print("Valid")
    # return True


check_para(a)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self):
        temp = self.head
        s = ""
        while temp:
            s += str(temp.value) + "-->"
            temp = temp.next
        print(s)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def append_first(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.head
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return
        curr = self.head
        prev = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        self.tail = prev
        prev.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
            print("Linked list is empty")
        return True





l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append_first(0)
l.append_first(-1)
l.append(4)
l.print_list()
l.pop()
l.pop()
l.pop()
l.pop()
l.pop()
l.pop()

l.print_list()


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_list(self):
        temp = self.top
        s = ""
        while temp:
            s += str(temp.value) + "-->"
            temp = temp.next
        print(s)

    def add(self, value):
        new_node = Node(value)
        temp = self.top
        self.top = new_node
        new_node.next = temp
        self.height += 1
    
    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1


s = Stack(1)
s.add(2)
s.add(3)
s.pop()
s.print_list()