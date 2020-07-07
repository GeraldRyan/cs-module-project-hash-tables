class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList: # TODO port code into HashTable class
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next 
        return None

    def insert_at_head(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n 
    
    def append(self, value):
        # TODO
        pass

    def insert(self, node): # COrresponds to "put" in HashTable
        # TODO 
        pass

    def delete(self,value):
        cur = self.head

        # Special Case of deleting head
        if cur.value == value:
            self.head = self.head.next
            return cur


        # General Case
        prev = cur
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = Nonedddddd
                return cur
            else:
                prev = prev.next
                cur = cur.next
            return None


# Very simple LinkedList
a = Node(11)
b = Node(5)
a.next = b
head = a
print(a.value, b.value, a.next.value) # 11, 5, 5

ll = LinkedList()
ll.insert(11)
ll.insert(5)





class HashTableEntry:  # Node in Linked List
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.data = [[]] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # return len(self.capacity)
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis
        for k in key:
            hash = hash ^ ord(k)

        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        i = self.fnv1(key) % self.get_num_slots()
        
        return i

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining. 

        Implement this.
        """
        # Your code here

        i = self.hash_index(key)
        found = False
        for h, element in enumerate(self.data[i]):
            if len(element) ==2 and element[0] == key:
                self.data[i][h] = (key, value)
                found = True
                self.count += 1
                break
        if not found:
            self.data[i].append((key,value))
            self.count += 1

        if self.get_load_factor() >.7:
            self.resize(self.capacity *2)

        # self.data[i] = value

        # print(f'key: {key}, value: {value}, i: {i}, data[i]: {self.data[i]}')


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        for index, element in enumerate(self.data[i]):
            if element[0] == key:
                del self.data[i][index]
                self.count -= 1
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        # print(f'Test File>>key: {key} i:{i}, self.data[i]: {self.data[i]}')
        if self.data[i] == None:
            return self.data[i]

        for element in self.data[i]:
            if element[0] == key:
                return element[1]
        # return self.data[i]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # self.capacity = new_capacity
        for i in range(self.capacity, new_capacity): # 8-15
            self.data.append(None) # This is definitely wrong. 

        # For each element in the main list and each element in the linked lists, rehash by using a self.put with the original key values  
        old_data = self.data
        self.data = [[]] * new_capacity
        count = 0
        for i in range(len(old_data)):
            if old_data[i] is not []:
                for index, element in enumerate(old_data[i]):
                    print(f'old_data[i][1] (key): {old_data[i][1]}, old_data[i][2] (value): {old_data[i][2]}')
                    self.put(old_data[i][1], old_data[i][2])
                    count += 1





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(i,": ", ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()
    print("number of slots", ht.get_num_slots())
    print("number of entries", ht.count)
    print("Load Factor", ht.get_load_factor())


    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
