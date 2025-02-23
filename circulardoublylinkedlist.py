class Node:
    def __init__(self, data):
        self.data = data  # Store node data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize empty list

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            self.head.next = self.head  # Point to itself (circular)
            self.head.prev = self.head  # Circular doubly link
            return
        
        temp = self.head.prev  # Get last node
        temp.next = new_node  # Link last node to new node
        new_node.prev = temp  # Link new node to last node
        new_node.next = self.head  # Circular link to head
        self.head.prev = new_node  # Link head back to new node

    def insert_at_front(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        
        last = self.head.prev  # Get last node
        new_node.next = self.head  # New node points to old head
        new_node.prev = last  # New node points to last node
        last.next = new_node  # Last node points to new node
        self.head.prev = new_node  # Old head points back to new node
        self.head = new_node  # Update head

    def insert_at_npos(self, pos, data):
        if pos < 1:
            print("Invalid position!")
            return
        
        new_node = Node(data)
        if pos == 1:  # Insert at front
            self.insert_at_front(data)
            return
        
        temp = self.head
        for _ in range(pos - 2):  # Move to position-1
            temp = temp.next
            if temp == self.head:  # Position out of bounds
                print("Position out of range!")
                return
        
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(HEAD)")

    def delete_at_npos(self, pos):
        if not self.head or pos < 1:
            print("Invalid position or empty list!")
            return
        
        temp = self.head
        if pos == 1:  # Delete first node
            self.delete_first()
            return
        
        for _ in range(pos - 1):  # Move to position
            temp = temp.next
            if temp == self.head:
                print("Position out of range!")
                return
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def delete_first(self):
        if not self.head:
            print("List is empty")
            return
        
        if self.head.next == self.head:  # Only one node
            self.head = None
            return
        
        last = self.head.prev  # Get last node
        self.head = self.head.next  # Update head
        self.head.prev = last  # Update previous of new head
        last.next = self.head  # Update next of last node

    def delete_last(self):
        if not self.head:
            print("List is empty")
            return
        
        if self.head.next == self.head:  # Only one node
            self.head = None
            return
        
        last = self.head.prev  # Get last node
        second_last = last.prev  # Get second last node
        second_last.next = self.head  # Update next of second last
        self.head.prev = second_last  # Update previous of head

    def update(self, position, value):
        if not self.head or position < 1:
            print("Invalid position or empty list!")
            return
        
        temp = self.head
        for _ in range(position - 1):
            temp = temp.next
            if temp == self.head:
                print("Position out of range!")
                return
        temp.data = value

sll = CircularDoublyLinkedList()

while True:
    print("\nChoose an operation:")
    print("1. Insert at End")
    print("2. Insert at Front")
    print("3. Insert at N Position")
    print("4. Delete First Node")
    print("5. Delete Last Node")
    print("6. Delete at N Position")
    print("7. Update a Node")
    print("8. Display List")
    print("9. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter value to insert at end: "))
        sll.insert_at_end(data)
    elif choice == 2:
        data = int(input("Enter value to insert at front: "))
        sll.insert_at_front(data)
    elif choice == 3:
        pos = int(input("Enter position to insert: "))
        data = int(input("Enter value: "))
        sll.insert_at_npos(pos, data)
    elif choice == 4:
        sll.delete_first()
    elif choice == 5:
        sll.delete_last()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        sll.delete_at_npos(pos)
    elif choice == 7:
        pos = int(input("Enter position to update: "))
        value = int(input("Enter new value: "))
        sll.update(pos, value)
    elif choice == 8:
        sll.display()
    elif choice == 9:
        break
    else:
        print("Invalid choice, please try again.")
