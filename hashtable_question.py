li1 = [1, 2, 3, 5, 4]
li2 = [4, 5, 6, 7]

# find the common in the two list.

# Solution 1
# O(n^2)
def solution1():
    for i in li1:
        for j in li2:
            if i == j:
                print(f"{i} is common")
                break


# Solution 2

# O(n)
def item_in_common(li1, li2):
    di = {}
    for i in li1:
        di[i] = True

    for j in li2:
        if j in di:
            return True, j
    return False


print(item_in_common(li1, li2))
