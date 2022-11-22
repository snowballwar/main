# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:32:42 2022

@author: 64497
"""

import numpy as np

class Solution(object):
    def countBits(self, n):
        List = []
        for i in range(n+1):
            if i == 0:
                List.append(0)
            elif (i % 2) == 1:
                List.append(List[int((i-1)/2)] + 1)
            else:
                List.append(List[int(i/2)])
        return List
    
aa = Solution()
aa.countBits(5)
   
# Q19 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head     
        cnt = 0
        while cur is not None:
            cnt = cnt + 1
            cur = cur.next
        
        node_dummy = ListNode(0,head)      
        cur = node_dummy
        for i in range(0,cnt - n):
            cur = cur.next
        cur.next = cur.next.next
        return node_dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

cur = node1
while cur is not None:
    print(cur.val, end = '')
    cur = cur.next
        
n = 2  
cur = node1     
cnt = 0
while cur is not None:
    cnt = cnt + 1
    cur = cur.next

node_dummy = ListNode(0,node1)
if cnt == 1:
    res = None
else: 
    cur = node_dummy
    for i in range(0,cnt - n):
        cur = cur.next
    cur.next = cur.next.next
    res = node_dummy.next
    
# Q701    
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val)
        if self.right:
            self.right.traverseInorder()
        
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
# root = [4,2,7,1,3], val = 5 
node1 = TreeNode(4)
node2 = TreeNode(2)        
node3 = TreeNode(7)   
node4 = TreeNode(1)   
node5 = TreeNode(3)   
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

node1.traverseInorder()


def insertHelper(node, val):
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = insertHelper(node.left, val)
    else:
        node.right = insertHelper(node.right, val)
    return node
        
insertHelper(node1, 5)

root = [4,2,7,1,3]  
def createBST(valueList):
    root = None
    for val in valueList:
        root = insertHelper(root, val)
    return root

createBST(root).traverseInorder()

        
# Binary Tree in Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()

# air invader
def maxPlanes(startHeight, descentRate):
    return

startHeight = [1, 3, 5, 4, 8]
descentRate = [1, 2, 2, 1, 2]

hitTime = np.array(startHeight) / np.array(descentRate)
hitTimeCeil = np.ceil(hitTime)

res = len(startHeight)
for i in range(len(startHeight)):
    if (i+1) > hitTimeCeil[i]:
        res = i
        
# Q206
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def traverse(self):
        cur = self
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
            
        return prev
        

# head = [1,2,3,4,5]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.traverse()


ls = []
cur = node1
cnt = 0
while(cur):
    cnt = cnt + 1
    ls.append(cur.val)
    cur = cur.next
if cnt == 0:
    res = []
else:
    res = ListNode(ls[cnt-1])
    cur = res
    for i in range(cnt-2,-1,-1):
        cur.next = ListNode(ls[i])
        cur = cur.next
        
obj = Solution()
reverseNode = obj.reverseList(node1)
reverseNode.traverse()
        
# Q102 Binary Tree Level Order Traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val)
        if self.right:
            self.right.traverseInorder()
        
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """    
        
node1 = TreeNode(3)
node2 = TreeNode(9)        
node3 = TreeNode(20)   
node4 = TreeNode(15)   
node5 = TreeNode(7)   
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
   
from queue import Queue 
root = node1
myqueue = Queue()    
myqueue.put(root)
res = []

while not myqueue.empty():
    print(myqueue.empty(), end = ' isempty ')
    n = myqueue.qsize()
    temp = []
    for i in range(n):
        current = myqueue.get()
        temp.append(current.val)
        if current.left:
            myqueue.put(current.left)
        if current.right:
            myqueue.put(current.right)
    res.append(temp)
    print(myqueue.empty(), end = '\n')
    
res

# Q160
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
node_a1 = ListNode(4)
node_a2 = ListNode(1)    
    
node_c1 = ListNode(8)   
node_c2 = ListNode(4)   
node_c3 = ListNode(5)   

node_b1 = ListNode(5)   
node_b2 = ListNode(6)   
node_b3 = ListNode(1)   

node_a1.next = node_a2
node_a2.next = node_c1
node_c1.next = node_c2
node_c2.next = node_c3
node_b1.next = node_b2
node_b2.next = node_b3
node_b3.next = node_c1

headA = node_a1
headB = node_b1

# double pointer
cur1 = headA
cur2 = headB
loop1 = 0
loop2 = 0
while (cur1 and cur2):
    if cur1 == cur2:
        res = cur1
        break
    cur1 = cur1.next
    cur2 = cur2.next
    if (cur1 is None) & (loop1 == 0):
        cur1 = headB
        loop1 = 1
    if (cur2 is None) & (loop2 == 0):
        cur2 = headA
        loop2 = 1

if (cur1 is None) and (cur1 is None):
    res = None
    
# hash table
hashtable = dict()
cur1 = headA
while cur1:
    hashtable[cur1] = cur1.val
    cur1 = cur1.next

cur2 = headB    
res = None
while cur2:
    if cur2 in hashtable:
        res = cur2
        break
    cur2 = cur2.next
    
# Q1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
nums = [2,5,5,11]
target = 10

hashtable = dict()

for i,num in enumerate(nums):
    hashtable[num] = i
    
for i,num in enumerate(nums):
    if ((target - num) in hashtable) and (i != hashtable[target-num]):
        res = [i,hashtable[target-num]]
        break
    
# Q142
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
  
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)  

node1.next = node2
node2.next = node3
node3.next = node4
node3.next = node2

hashset = set()
res = None
cur = node1
while cur:
    if cur in hashset:
        res = cur
        break
    hashset.add(cur) 
    cur = cur.next

# Q33
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
nums = [3,1]
target = 1

res = -1    
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        res = mid
        break
    else:
        if nums[left] <= nums[mid]:
            if (target >= nums[left]) and (target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        else:
            if (target > nums[mid]) and (target <= nums[right]):
                left = mid + 1
            else:
                right = mid - 1
                
# Q203
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def traverse(self):
        cur = self
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
#head = [1,2,6,3,4,5,6], val = 6
#head = [7,7,7,7], val = 7
       
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

val = 6
    

# node1 = ListNode(7)
# node2 = ListNode(7)
# node3 = ListNode(7)
# node4 = ListNode(7)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# val = 7

# iterative
dummy_node = ListNode(0,node1)
prev = dummy_node
cur = node1
while cur:
    if cur.val == val:
        prev.next = cur.next
        cur = cur.next
    else:
        prev = cur
        cur = cur.next
    
res = dummy_node.next
# recursive
def removeNode(head, val):
    if head is None:
        return
    elif head.val == val:
        return removeNode(head.next, val)
    else:
        head.next = removeNode(head.next,val)
        return head
    
head = removeNode(node1, val)

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return
        elif head.val == val:
            return self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next,val)
            return head
        
# Q114 Flatten Binary Tree to Linked List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traversePreorder(self):
        print(self.val)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
        
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def traversePreorder(root, myList):
            myList.append(root.val)
            if root.left:
                traversePreorder(root.left, myList)
            if root.right:
                traversePreorder(root.right, myList)   
    
        myList = []
        if root:
            traversePreorder(root, myList)
            cur = root
            for i in range(1,len(myList)):
                cur.left = None
                cur.right = TreeNode(myList[i])
                cur = cur.right
        
node1 = TreeNode(1)
node2 = TreeNode(2)        
node3 = TreeNode(5)   
node4 = TreeNode(3)   
node5 = TreeNode(4)
node6 = TreeNode(6)   

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6 

root = node1    
    
def traversePreorder(root, myList):
    myList.append(root.val)
    if root.left:
        traversePreorder(root.left, myList)
    if root.right:
        traversePreorder(root.right, myList)   

myList = []
if root:
    traversePreorder(root, myList)
    cur = root
    for i in range(1,len(myList)):
        cur.left = None
        cur.right = TreeNode(myList[i])
        cur = cur.right
        
# Q700 Search in a Binary Search Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val)
        if self.right:
            self.right.traverseInorder()
        
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

node1 = TreeNode(4)
node2 = TreeNode(2)        
node3 = TreeNode(7)   
node4 = TreeNode(1)   
node5 = TreeNode(3)   
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

val = 1

# iterative SC: O(1)
cur = node1
res = None
while cur:
    if val == cur.val:
        res = cur
        break
    elif val < cur.val:
        cur = cur.left
    else:
        cur = cur.right

# recursive
def searchBST(root, val):
    if root is None:
        return
    elif val == root.val:
        return root
    elif val < root.val:
        searchBST(root.left, val)
    else:
        searchBST(root.right, val)
        
searchBST(node1, 3)
    
# 98. Validate Binary Search Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.val)
        if self.right:
            self.right.traverseInorder()
        
class Solution(object):
    def traverseInorder(self, root, myList):
        if root.left:
            self.traverseInorder(root.left, myList)
        myList.append(root.val)
        if root.right:
            self.traverseInorder(root.right, myList)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        myList = []    
        self.traverseInorder(root, myList)
        for i in range(1,len(myList)):
            if myList[i-1] >= myList[i]:
                return False
        return True

node1 = TreeNode(5)
node2 = TreeNode(1)        
node3 = TreeNode(4)   
node4 = TreeNode(3)   
node5 = TreeNode(6)   
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5    
    
root = node1    
    
# recursive
# def isValidBST(root):
#     if (root.left == None) and (root.right == None):
#         return True
#     if root.left:
#         if root.left.val >= root.val:
#             return False
#         res = isValidBST(root.left)
#     if root.right:
#         if root.right.val <= root.val:
#             return False
#         res = isValidBST(root.right)
#     return res

myList = []
def traverseInorder(root):
    if root.left:
        traverseInorder(root.left)
    myList.append(root.val)
    if root.right:
        traverseInorder(root.right)
        
traverseInorder(node1)

res = True
for i in range(1,len(myList)):
    if myList[i-1] >= myList[i]:
        res = False
        break
    
# 141. Linked List Cycle
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def traverse(self):
        cur = self
        while cur:
            print(cur.val, end = ' ')
            cur = cur.next
            
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

head = node1

# hashtable
hashtable = set()
res = False
cur = head
while cur:
    if cur not in hashtable:
        hashtable.add(cur)
        cur = cur.next
    else:
        res = True
        break
    
# double pointer
ptr1 = head
ptr2 = head

res = False
while ptr2 and ptr2.next:
    ptr1 = ptr1.next
    ptr2 = ptr2.next.next
    if ptr1 == ptr2:
        res = True
        break
