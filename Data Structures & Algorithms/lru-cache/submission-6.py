class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # hashmap to map keys to nodes

        # Dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Connect left and right
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from wherever it currently is in the linked list
    def remove(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    # Put a node at the right side. The right side means "most recently used."
    def insert(self, node):
        before = self.right.prev
        after = self.right

        before.next = node
        node.prev = before

        node.next = after
        after.prev = node

    def get(self, key):
        # The key does not exist
        if key not in self.cache:
            return -1

        # Find the node
        node = self.cache[key]

        # Remove it from its current position
        self.remove(node)

        # Put it at the right side
        # because we just used it.
        self.insert(node)

        # Return its value
        return node.value

    def put(self, key, value):
        # If the key already exists, remove its old node.
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        # Create a new node
        node = Node(key, value)

        # Put the node in the dictionary
        self.cache[key] = node

        # Put the node at the right side because it is now the most recently used.
        self.insert(node)

        # If we have too many items, remove the least recently used one.
        if len(self.cache) > self.capacity:

            # The node immediately after LEFT is the least recently used node.
            lru = self.left.next

            # Remove it from the linked list
            self.remove(lru)

            # Remove it from the dictionary
            del self.cache[lru.key]