import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

bst = BSTNode('testing')


# Not quite sure how else to accomplish this at the moment
# OPTIMIZED TO RUN IN 0.172 SECONDS ON MY MACHINE
# for each name in names_1
for name in names_1:
    # add that name to the binary search tree
    bst.insert(name)

# for each name in names 2
for name in names_2:
    # see if that name is already in the bst
    if bst.contains(name):
        # if it is, append it to the duplicates array
        duplicates.append(name)

    # Replace the nested for loops below with your improvements
    # RUNTIME IS 7.6484 SECONDS ON MY MACHINE
    # Current runtime = O(n) + O(n) + O(1) + O(1) == O(n^2)
    # for name_1 in names_1:  # O(n)
    #     for name_2 in names_2:  # O(n)
    #         if name_1 == name_2:  # O(1)
    #             duplicates.append(name_1)  # O(1)?

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
