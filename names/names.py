import time
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if it's empty
        #if empty put node at root
        
        #sel.value can't be none
        if value < self.value:
        #   if left doesn't exist
            if self.left is None:
        #       create left
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: #value > self.value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #at the start, self will be root
        #compare target against itself
        if  self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
""" for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1) """

print(type(names_1)) #List
#Instantiate BSN with first name
bst = BSTNode(names_1[0])
#2 different loops, not nested
for name_1 in names_1:
    #populate all the names from names_1
    bst.insert(name_1)
for name_2 in names_2:
    #compare it to names_2
    if bst.contains(name_2):
        #if true append it to duplicates
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
