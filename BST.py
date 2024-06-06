class BinaryTree:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
    
    # Inorder traversal of binary tree    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value,end=" ")
        if self.right:
            self.right.inorder()
    
    # Function to delete node from tree       
    def deleteNode(self,root,key):
        if root is None:
            return root
        
        if key < root.value:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the roots key then it lies in the right subtree
        elif key > root.value:
            root.right = self.deleteNode(root.right, key)
        # If key is same as roots key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children : Get the inorder successor
            root.value =minimum(root.right)

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.value)

        return root

# Function to find minimum value 
def minimum(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current.value

# Function find maximum value
def maximum(node):
    current = node
    while(current.right is not None):
        current = current.right
    return current.value

# Function to insert node in tree
def insert(root, data):
    if root is None:
        return BinaryTree(data)
    else:
        if root.value < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

# Function to find next successor in tree
def Next_Successor(node):
        if node.right is not None:
            return minimum(node.right)
        y = node.value
        while y is not None and node == y.right:
            node = y
            y = y.value
        return y

# Function to find previous successor in tree
def Previous_Successor(node):
        if node.left is not None:
            return maximum(node.left)
        y = node.value
        while y is not None and node == y.left:
            node = y
            y = y.value
        return y

# Function inorder traversal of tree
def Inorder(root, arr = []):
    if root:
        Inorder(root.left, arr)
        arr.append(root.value)
        Inorder(root.right, arr)

# Function to sort two arrays by merge sort
def merge_sorted_arr(arr1, arr2):
    arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while i < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr

# Function to convert array to BST
def arr_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = BinaryTree(arr[mid])
    root.left = arr_to_bst(arr[:mid])
    root.right = arr_to_bst(arr[mid + 1:])
    return root

# Function to build maxheap
def maxheap(root,tree):
    if root:
        max=maximum(root)
        insert(tree,max)
        root.deleteNode(root,max)
    return tree

# Function to heapify the tree
def heapify(arr, size, i):
    # Find the largest among root  left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < size and arr[i] < arr[l]:
        largest = l

    if r < size and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


## Test Program ##    
r = BinaryTree(50)
insert(r, 30)
insert(r, 70)
insert(r, 80)

r2=BinaryTree(40)
insert(r2,60)
insert(r2,20)

print("Minimum value in BST is", minimum(r))
print("Maximum value in BST is", maximum(r))
print("Next Suc in BST is", Next_Successor(r))
print("Per Suc in BST is",Previous_Successor(r))
print(BinaryTree.inorder(r))
r.deleteNode(r,70)
print(BinaryTree.inorder(r2))

arr1 = []
Inorder(r, arr1)
arr2 = []
Inorder(r2, arr2)
arr = merge_sorted_arr(arr1, arr2)
root = arr_to_bst(arr)
print('Following is Inorder traversal of the merged tree:')
print(BinaryTree.inorder(root))





        