class Person:
    def __init__(self,name,age,skill):
        self.name=name
        self.age=100-age
        self.skill=self.convert(skill)
    
    # Function to convert skill
    def convert(self,skill):
        if skill == "A" or skill == "a":
            return 1
        elif skill == "B" or skill == "b":
            return 2
        elif skill == "C" or skill == "c":
            return 3
        elif skill == "D" or skill == "d":
            return 4
        elif skill == "E" or skill == "e":
            return 5
        elif skill == "F" or skill == "f":
            return 6

# Functon input person in priority queue
def input(person):
    return (person.age+person.skill,person.name,(100-person.age),person.skill)

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


# Function to insert an element into the tree
def insert(array, newnumber):
    size = len(array)
    if size == 0:
        array.append(newnumber)
    else:
        array.append(newnumber)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, len (array), i)


# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]
    
    temp=num
    array.remove(num)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array) , i)
    return temp



## Test Program ##
p1=Person("Amir",16,"f")
p2=Person("Ali",18,"b")
p3=Person("Javad",20,"f")
p4=Person("Majid",18,"a")
p5=Person("Saman",18,"f")
arr=[]
insert(arr,input(p1))
insert(arr,input(p2))
insert(arr,input(p3))
insert(arr,input(p4))
insert(arr,input(p5))
print("Best Choice:",deleteNode(arr,arr[0]))
print("Best Choice:",deleteNode(arr,arr[0]))
print("Best Choice:",deleteNode(arr,arr[0]))
print("Remaining people on the list:")
for i in arr:
    print(i,end=" ")