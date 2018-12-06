""" This class creates a LinkedList from scratch that can be used modularly in other files"""

class Node(object):
    """ inherits from Python object class; this creates a node to be used in LinkedList"""
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):
    """ class docstring """
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node, begins as None
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) This is best case because must traverse every
        bucket(b) and then count each node in each bucket in order to get count
        with this method"""
        node_count = 0
        current = self.head
        # Loop through all nodes and count one for each
        while current is not None:
            current = current.next
            node_count += 1
        return node_count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) This is both best and worse case because
        it simply requires you to check for the current node and add
        the new node"""
        # Create new node to hold given item
        new_node = Node(item)
        # Append node after tail, if it exists
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) This is best and worse case for
        same reasons as above"""
        # Create new node to hold given item
        new_node = Node(item)
        # Prepend node before head, if it exists
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) If the found node is the first one
        TODO: Worst case running time: O(n) If you have to traverse all nodes
        because the found node is later in the list or not found"""
        current = self.head
        found_quality = False
        # Loop through all nodes
        while current and found_quality is False:
            # find item where quality(item) is True
            if quality(current.data) is True:
                found_quality = True
                return current.data
            current = current.next

        # Check if node's data satisfies given quality function (quality is a function?)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) same as find()
        TODO: Worst case running time: O(n) Same as find()"""
        # keeping track of current node, last node and if node is found
        current = self.head
        last = None
        found_node = False
        # Loop through all nodes
        while current and found_node is False:
            # find one whose data matches given item
            if current.data == item:
                found_node = True
            else:
                # Update previous node to skip around node with matching data
                last = current
                current = current.next
        # if we got past the end of the list and did not find item
        if current is None:
            raise ValueError('Item not found: {}'.format(item))
        # if we are at the first node, delete by making next node first
        if last is None:
            self.head = current.next # what if current is None
        else:
            last.next = current.next
        # if we are at the last node, delete by making second last, new last
        if current.next is None:
            self.tail = last

    def replace(self, old_data, new_data):
        """ Running time: Best case O(1) same as find; Worst case O(n)
        same as find """
        current = self.head
        found_node = False
        # keep track of current node and if node is found
        while current and found_node is False: # loop through all nodes to find item
            # find node whose data matches item
            if current.data == old_data:
                # no need to get rid of node; replace old data with new data
                current.data = new_data
                found_node = True
            break
        # if we got past the end of the list and did not find old_data
        if current is None:
            raise ValueError('Item not found: {}'.format(old_data))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing replace method
    replace_implemented = True
    if replace_implemented:
        print('\nTesting replace:')
        item = 'A'
        new_data = 'D'
        print('replace({!r}) with ({!r})'.format(item, new_data))
        ll.replace(old_data=item, new_data=new_data)
        print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'D']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
