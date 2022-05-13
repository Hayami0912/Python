#Declaring Table capacity
HTcapacity = 99
HT = [None]*HTcapacity
multFactor = 20

#Read File
fname = '19727415.txt'
f = open (fname)
pFile = f.readlines()
f.close()

#Append item to list
inlists = []
for n in pFile:
    inlists.append(n.split(','))
    
#Hash Function By Profressor Shuman
def Hash (inline, mFactor = 123):
    instring = ''
    for n in range (1, len(inline)):
        instring = instring + str(inline[n])
    Hcode = 0
    for c in instring[:8]:
        Hcode += ord(c)
    # return hash changed by adjusting //value & order of instring
    return ((Hcode//5 * int(inline[3])*mFactor)%HTcapacity)
#iterate transaction codes from list
for i in inlists:
    
    #Insert
    if i[0] == 'I':
        HC = Hash(i,mFactor = multFactor)
        if HT[HC] is None:
            HT[HC] = [i[1:-1]]
            print('Insert: ',[i[1:-1]],'       at index # ',HC)
        else:
            HT[HC].append(i[1:-1])
            print('Insert: ',[i[1:-1]],'       at index # ',HC)
    
    #Find
    if i[0] == 'F':
        HF = Hash(i,mFactor = multFactor)
        for n in range (0, len(HT)):
            if HF == n:
                if HT[n] is None:
                    print('Find: ',i[1:-1],'            not found')
                if HT[n] is not None:
                    for item in (HT[n]):
                        if i[1:-1] == item:
                            print('Find: ',i[1:-1],'    found at index # ',n)
                            
                            
    #Delete
    if i[0] == 'R':
        HC = Hash(i,mFactor = multFactor)
        for n in range (0, len(HT)):
            if HC == n:
                if HT[n] is None:
                    print('Delete: ',i[1:-1],'            not found')
                    
                if HT[n] is not None:
                    for item in (HT[n]):
                        if i[1:-1] == item:
                            print('Delete: ',i[1:-1],'     found at index # ',n,' to be deleted')
                            HT[HC].remove(i[1:-1])
    else:
        pass
     
#Print table and result details
empty = 0
occupied = 0
collision = 0
items = 0
chains = 0
for h in HT:
    if h is None:
        empty +=1
    else:
        occupied +=1
        items += len(h)
        if len(h) >1:
            collision +=1
            chains += len(h)
print('Hash Table size:                      {0:8d}'.format(HTcapacity))
print('# empty HT slots:                     {0:8d}'.format(empty))
print('# occupied HT slots:                  {0:8d}'.format(occupied))
print('# items in table (incl. collisions):  {0:8d}'.format(items))
print('HT load factor                        {0:8.2f}'.format(items/len(HT)))
print('# HT collisions:                      {0:8d}'.format(collision))
print('Average # entires in collision slots: {0:8.2f}'.format(chains/collision))
    
    
        
