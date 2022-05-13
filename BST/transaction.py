def parenthesize(T, p):
    """ Print a parenthesized representation of a subtree of T rooted at p. """
    if p is not None:
        print (p.element, end = '')
        if not T.is_leaf(p):
            first_time = True
            for c in (T.left(p), T.right(p)):
                if first_time:
                    sep = ' ('
                else:
                    sep = ', '
                print (sep, end = '')
                first_time = False
                parenthesize(T, c)
            print(')', end = '')

transactions= []
fname = '19622700.txt'
f = open (fname)
pFile = f.readlines()
for items in pFile:
    item = items.split(',')

    if len(item) == 1:
        item[0] = item[0][:-1]
        if item[0] == '':
            pass
        else:
            transactions.append(item)
        
    if len(item) == 2:
        item[1] = item[1][:-1]
        item[1] = item[1].strip(' ')
        transactions.append(item)

    else:
        pass
print(transactions)

BST2 = BinarySearchTree()
for t in transactions:
    if t[0] == "I":
        print('insert: ', t[1])
        if BST2.size == 0:
            BST2.add_root(t[1])
        else:
            BST2.insert(t[1])
        
    elif t[0] == "R":
        print('delete: ', t[1])
        BST2.delete(t[1])
        
    elif t[0] == "D":
        print('parenthesize: ') 
        parenthesize(BST2, BST2.root)
        print('\nLength: ',len(BST2))
    
    elif t[0] == "E":
        print('Reset Tree')
        print('-------------------------------------------------------------')
        BST2 = BinarySearchTree()
    
    else:
        pass
