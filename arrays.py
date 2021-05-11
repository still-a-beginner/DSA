#The add function is to push the number, n at the end of list, l. The time complexity is Θ(1).
def add(l,n):
    print('\nAdd function')
    print('Initial list is',l)
    print('Number to be added is',n)
    l.append(n)
    print('The final list is')
    return l

#The remove function is to pop the number from the end of the list, l. The time complexity is Θ(1).
def remove(l):
    print('\nRemove function')
    print('Initial list is',l)
    print('The number to be removed is',l[-1])
    l = l[:-1]
    return l

#The insert function is to push the number, n at a particular index, i in the list, l. The time complexity is Θ(len(l)).
#Use other data structure to insert an element at a particular index.
def insert(l,i,n):
    print('\nInsert function')
    print('Initial list is',l)
    print('Number to be added is',n, 'at an index of',i)
    l1 = l[:i]
    l2 = l[i:]
    l1.append(n)
    l = l1 + l2
    return l

#The delete function is to pop a number at a particular index, i in the list, l. The time complexity is Θ(len(l)).
#Use other data structure to delete an element at a particular index.
def delete(l,i):
    print('\nDelete function')
    print('Initial list is',l)
    print('Number to be deleted is at an index of',i)
    l1 = l[:i]
    l2 = l[i+1:]
    l = l1 + l2
    return l

#The retrieve function is to get the number at a particular index, i in the list, l. The time complexity is Θ(1).
def retrieve(l,i):
    print('\nRetrieve function')
    print('Initial list is',l)
    print('Number to be retrieved is at an index of',i)
    return l[i]

#The update function is to change a number at a particular index, i in the list, l by the number, n. The time complexity is Θ(1).
def update(l,i,n):
    print('\nUpdate function')
    print('Initial list is',l)
    print('Number to be updated is at an index of',i)
    l[i] = n
    return l
    
#The extreme function is to find the minimum and the maximum number in the list, l. The time complexity is Θ(len(l)).
#Use other data structure to find the extreme of the list.
def extreme(l):
    print('\nExtreme function')
    print('Initial list is',l)
    return {'max':max(l), 'min':min(l)}
    
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

l = [1,2,3,4]
l = retrieve(l,i)
print(l)

l = [1,2,3,4]
l = update(l,i,n)
print(l)

l = [1,2,3,4]
l = extreme(l)
print(l)
