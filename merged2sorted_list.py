class ListNode:
    def __init__(self, val=0, next=None):
        # Define a class named ListNode representing a single node in a singly linked list.
        # Initialize the data attribute of the node with the given value.
        self.val = val
        # Initialize the next attribute of the node to point to the next node.
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Define a method named mergeTwoLists to merge two sorted singly linked lists.
        # Initialize a dummy node with value -1.
        # This dummy node serves as the head of the merged list.
        dummy = ListNode(-1)
        # Initialize a pointer 'current' to the dummy node.
        # 'current' will be used to build the merged list.
        current = dummy
        
        # Loop until both list1 and list2 have nodes to merge.
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2.
            if list1.val < list2.val:
                # If the value of the current node in list1 is smaller,
                # attach it to 'current.next'.
                current.next = list1
                # Move the pointer of list1 to its next node.
                list1 = list1.next
            else:
                # If the value of the current node in list2 is smaller or equal,
                # attach it to 'current.next'.
                current.next = list2
                # Move the pointer of list2 to its next node.
                list2 = list2.next
            
            # Move the 'current' pointer to the next node in the merged list.
            current = current.next
        
        # If list1 still has remaining nodes, attach them to the end of the merged list.
        if list1:
            current.next = list1
        # If list2 still has remaining nodes, attach them to the end of the merged list.
        elif list2:
            current.next = list2
        
        # Return the head of the merged list, which is the next node after the dummy node.
        return dummy.next

# Example usage:
# Create some sample linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two lists
s = Solution()
result = s.mergeTwoLists(list1, list2)

# Print the merged list
while result:
    print(result.val, end=" -> ")
    result = result.next
