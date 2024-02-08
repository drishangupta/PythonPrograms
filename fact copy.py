# Node Class
class Node:
    def __init__(self, n):
        self.data = n
        self.prev = None
 
# Function to perform desired operation
def Multiply(head, i):
    temp = head
    prevPtr = head
    carry = 0
    # Perform operation until temp becomes None
    while temp is not None:
        prod = temp.data * i + carry
        temp.data = prod % 10 # Stores the last digit
        carry = prod // 10
        prevPtr = temp # Change Links
        temp = temp.prev # Moving temp to the next node
    # If carry is greater than 0, create new nodes to store remaining digits
    while carry != 0:
        prevPtr.prev = Node(carry % 10)
        carry = carry // 10
        prevPtr = prevPtr.prev
 
# Using recursion to print the linked list's data in reverse
def print_list(head):
    if head is None:
        return
    print_list(head.prev)
    print(head.data, end="") # Print linked list in reverse order
 
# Driver code
def main():
    n = 100
    head = Node(1) # Create a node and initialize it by 1
    for i in range(2, n+1):
        Multiply(head, i) # Run a loop from 2 to n and multiply with head's i
    print("Factorial of", n, "is : ")
    print_list(head) # Print the linked list
    print()
 
main()