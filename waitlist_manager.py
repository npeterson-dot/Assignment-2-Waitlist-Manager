# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name, next=None):
        self.name = name
        self.next = next


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current = self.head

        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                return f"Removed {name} from the waitlist"

            current = current.next

        return f"{name} not found"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        current = self.head

        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            print(waitlist.remove(name))

        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo:

The linked list in this program works by storing each customer inside a Node.
Each node contains the customer's name and a reference to the next customer in
the waitlist. The LinkedList class manages these nodes and provides the methods
needed to add customers to the front or end, remove customers by name, and
print the full waitlist. When a customer is added to the front, a new node is
created and connected to the current first node. When someone is added to the
end, the program moves through the list until it reaches the final node and
connects the new customer there. Removing a customer works by moving through
the list until the matching name is found and then changing the connections
between nodes so that customer is removed.

The head plays an important role because it points to the first node in the
linked list. If the head is None, the waitlist is empty. The head also gives
the program a starting point for moving through the rest of the list.

A real engineer could use a custom linked list when working with data that
frequently needs to be added or removed and can change in size. A waitlist is
a good example because customers can constantly enter or leave the list.
Similar structures could also be useful for queues, scheduling systems, or
other applications where the order of data needs to be managed.
'''