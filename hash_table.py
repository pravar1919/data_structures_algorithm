class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        # for letter in key:
        #     '''
        #     Create our own logic.
        #     like my_hash = hash(key) % len(self.data).
        #     % operator gives the remainder.
        #     '''
        #     my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        my_hash = hash(key) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] # while storing in a particular index we again wrap up in a list.
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        value = self.data_map[index] 
        if value is not None:
            for i in value:
                if i[0] == key:
                    return i[1]
        return None
    
    def keys(self):
        all_keys = []
        for index_i, value_i in enumerate(self.data_map):
            if self.data_map[index_i]:
                for index_j, value_j in enumerate(self.data_map[index_i]):
                    all_keys.append(value_j[0])
        return all_keys

    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")
    


h = HashTable()

h.set_item("bolts", 100)
h.set_item("washer", 50)
h.set_item("pravar", 33)
h.set_item("pravar", "alwar")
h.set_item("lumber", 70)

h.print_table()

print(h.get_item('bolts'))
print(h.get_item('www'))
print(h.get_item('pravar'))
print(h.get_item('washer'))
 
print(h.keys())
