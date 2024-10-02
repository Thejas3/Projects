class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
#from the class ppt, just changed the variables ie:(head and key)
def search(head, key):
    current = head
    while current:
        if current.value == key:
            return True
        current = current.next
    return False

#based of the code in the class ppt and zybooks
def insert_after_nth_node(head, n, value):
    if n <= 0:
        print("Invalid value of n.")
        return head
    new_node = ListNode(value)
    if n == 1:
        new_node.next = head.next
        head.next = new_node
        return head
    current = head
    count = 1
    while current and count < n:
        current = current.next
        count += 1
    if not current:
        print("List length is less than", n)
        return head
    new_node.next = current.next
    current.next = new_node
    return head

# Creating a linked list that starts from 10 and goes to 50
head = ListNode(10)
current = head
for i in range(20, 60, 10):
    current.next = ListNode(i)
    current = current.next

# Search for a key and these the true and false outputs
print(search(head, 30))  
print(search(head, 35))  

# Insert a node after the nth node
head = insert_after_nth_node(head, 3, 25)  # Inserts 25 after the 3rd node

# Printing the updated linked list
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next