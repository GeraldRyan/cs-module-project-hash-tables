class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


class LinkedList: # TODO port code into HashTable class
    def __init__(self):
        self.head = None

    def find(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
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

    def insert(self, node): # Corresponds to "put" in HashTable
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
# a = Node(11)
# b = Node(5)
# a.next = b
# head = a
# print(a.value, b.value, a.next.value) # 11, 5, 5

# ll = LinkedList()
# ll.insert(11)
# ll.insert(5)





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
        self.data = [None] * capacity
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

        return self.fnv1(key) % self.get_num_slots()
        

    def put(self, key, value, resize = False):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining. 

        Implement this.
        """
        # Your code 
    


        i = self.hash_index(key)
        if self.data[i] is None:
            self.data[i] = Node(key, value)
        
        else:
            copy = self.data[i]
            self.data[i] = Node(key, value)
            self.data[i].next = copy
        self.count += 1

        if not resize:
            if self.get_load_factor() >.7:
                self.resize(self.get_num_slots() *2)
        





        # found = False

        # for h, element in enumerate(self.data[i]):
        #     if len(element) ==2 and element[0] == key:
        #         self.data[i][h] = (key, value)
        #         found = True
        #         self.count += 1
        #         break
        # if not found:
        #     self.data[i].append((key,value))
        #     self.count += 1


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
        cur = self.data[i]

        if cur is None:
            return None

        # Special Case of deleting head
        if cur.key == key:
            self.data[i] = cur.next
            return cur


        # General Case
        prev = cur
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        cur = self.data[i]
        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next 
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        old_data = self.data
        self.capacity = new_capacity
        self.data = [None] * new_capacity
        self.count = 0
        for i in old_data:
            if i is not None:
                cur_node = i
                while cur_node is not None:
                    self.put(cur_node.key, cur_node.value, True)
                    cur_node = cur_node.next

        
            # General Case
        
        
        # for i in self.data:
        #     if i is None:
        #         print(i)
        #     else:
        #         print(i.key, i.value)
        # print("XXXXXXXX________++++++++++++++++++++++++\n")



if __name__ == "__main__":
    ht = HashTable(8)
    print("initial capacity", ht.get_num_slots())

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
        print(i,": ", ht.get(f"line_{i}").value)

    # Test resizing
    old_capacity = ht.get_num_slots()
    print("Old capacity", old_capacity)

    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()
    print("number of slots", ht.get_num_slots())
    print("number of entries", ht.count)
    print("Load Factor", ht.get_load_factor())


    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}").value)

    print("")
