if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    l = list(arr)
    l.sort()
    l.reverse()
    maxi = l[0]
    
    for i in l:
        if maxi>i:
            print(i)
            break
         
    