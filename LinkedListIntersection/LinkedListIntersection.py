'''
Cracking the coding interview
Chapter 2 - Linked List pg 95
Linked List - Intersection
----------------------------------------
Question:Given 2 singly linked list, detirmine if the 2 lists intersect
Return the intersected node
Example: 
input: 
output: 
Constraits or Questions you need to ask:

Solution notes:
Using 2 pointers to iterate through the linked list 
When you reach the end of one of the list with the pointers
You assign the pointer to the head of the other list

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    #Intersection method with Time O(n) and Space O(1)
    def getIntersectionNode(self, list2):
        p1 = self.head
        p2 = list2.head

        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = list2.head
            if p2:
                p2 = p2.next
            else:
                p2 = self.head

        return p1

list1 = LinkedList()
list2 = LinkedList()

list1.append(4)
list1.append(1)
list1.append(8)
list1.append(4)
list1.append(5)

list2.append(5)
list2.append(0)
list2.append(1)
list2.append(8)
list2.append(4)
list2.append(5)

print(list1.getIntersectionNode(list2))