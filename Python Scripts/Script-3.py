# ContactKeeper

import heapq
li = []

def isPrefix(a, b):
    l1 = len(a)
    l2 = len(b)

    if l1>l2:
        return False

    s = ""

    for i in range(l1):
        s += b[i]

        if s == a:
            return True
    
    return False

if __name__ == "__main__":
    for _ in range(int(input('Enter number of Contact : '))):
        print('Enter name : ', end = ' ')
        name = input()
        print('Enter number : ', end = ' ')
        num = input()
        li.append((name, num))

    heapq.heapify(li)

    while True:
        print('Select an operation you want : ')
        print('1. Show all the contact details')
        print('2. Show a contact')
        print('3. Show contacts using key word')
        print('4. Add Contact')
        print('5. Delete Contact')
        print('For exit, enter any number except 1, 2, 3, 4, 5')
        print('Enter your choice : ', end = ' ')
        t = int(input())

        if t == 1:
            for i, j in li:
                print(i,' : ', j)
            print('\n')

        elif t == 2:
            print('Enter name : ')
            n = input()
            c = False

            for i, j in li:
                if i == n:
                    c = True
                    print(i, ' : ', j)
                    break

            if not c:
                print('Contact not found !!')
            print('\n')
        
        elif t == 3:
            n = input('Enter key word : ')

            for i, j in li:
                if isPrefix(n, i):
                    print(i, ' : ', j)
            print('\n')
        
        elif t == 4:
            print('Enter name : ', end = ' ')
            name = input()
            print('Enter number : ', end = ' ')
            num = input()
            li.append((name, num))
            heapq.heapify(li)
            print('\n')
        
        elif t == 5:
            n = input('Enter name : ')

            if n not in li:
                print('Contact is not exist')
            li = [(i, j) for i, j in li if i != n]
            print('\n')
        
        else:
            break
