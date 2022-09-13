if __name__== '__main__':
    print("Enter the no of commands :")
    N = int(input())
    list=[2,3,5,7]
    print(list)
    print("Start entering the commands:")
    for _ in range(N):
        str1=input().split()
        if str1[0] == 'append':
            list.append(int(str1[1]))
            print(list)
        elif str1[0] == 'print':
            print(list)
        elif str1[0] == 'sort':
            list.sort()
            print(list)
        elif str1[0] == 'reverse':
            list.reverse()
            print(list)
        elif str1[0] == 'pop':
            list.pop()
            print(list)
        elif str1[0] == 'insert':
            list.insert(int(str1[1]), int(str1[2]))
            print(list)
        elif str1[0] == 'remove':
            list.remove(int(str1[1]))
            print(list)
        
            
        
