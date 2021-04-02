if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    my_list = list(arr)
    
    my_list.sort()
    highest_number = max (my_list)
    
    for i in range (len(my_list)-1, -1, -1):
        if my_list[i] < highest_number:
            break
    print (my_list[i])
