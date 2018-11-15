
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

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
        TODO: Running time: O(???) Why and under what conditions?"""
        node_count = 0
        current = self.head
        # Loop through all nodes and count one for each
        while current is not None:
            current = current.next
            node_count += 1
        return node_count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
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
        TODO: Running time: O(???) Why and under what conditions?"""
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
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        current = self.head
        found_quality = False
        # Loop through all nodes
        while current and found_quality is False:
            # find item where quality(item) is True
            if quality(current.data) is True:
                found_quality = True
                return current.data
            else:
                current = current.next

        # Check if node's data satisfies given quality function (quality is a function?)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
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
