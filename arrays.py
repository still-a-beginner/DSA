#The add function is to push the number, n at the end of list, l. The time complexity is Θ(1).
def add(l, n):
    print('\nAdd function')
    print('Initial list is', l)
    print('Number to be added is', n)
    l.append(n)
    print('The final list is')
    return l

#The remove function is to pop the number from the end of the list, l. The time complexity is Θ(1).
def remove(l):
    print('\nRemove function')
    print('Initial list is', l)
    print('The number to be removed is', l[-1])
    l = l[:-1]
    return l

#The insert function is to push the number, n at a particular index, i in the list, l. The time complexity is Θ(len(l)).
#Use other data structure to insert an element at a particular index.
def insert(l,i,n):
    print('\nInsert function')
    print('Initial list is', l)
    print('Number to be added is', n, 'at an index of', i)
    l1 = l[:i]
    l2 = l[i:]
    l1.append(n)
    l = l1 + l2
    return l

#The delete function is to pop at a particular index, i in the list, l. The time complexity is Θ(len(l)).
#Use other data structure to delete an element at a particular index.
def delete(l,i):
    print('\nDelete function')
    print('Initial list is', l)
    print('Number to be deleted is at an index of', i)
    l1 = l[:i]
    l2 = l[i+1:]
    l = l1 + l2
    return l


n = 8
i = 2

l = [1,2,3,4]
l = add(l,n)
print(l)

l = [1,2,3,4]
l = remove(l)
print(l)

l = [1,2,3,4]
l = insert(l,i,n)
print(l)

l = [1,2,3,4]
l = delete(l,i)
print(l)
