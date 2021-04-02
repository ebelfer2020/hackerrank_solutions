if __name__ == '__main__':
    
    n = int(input())
    array = []

    while n!= 0:
        a = input().split()

        if len(a) == 3:
            b = int(a[1])
            c = int(a[2])
        elif len(a) == 2:
            b = int(a[1])

        if a[0] == "insert":
            array.insert(b, c)
        elif a[0] == "print":
            print(array)
        elif a[0] == "remove":
            (array).remove(b)
        elif a[0] == "append":
            (array).append(b)
        elif a[0] == "sort":
            (array).sort()
        elif a[0] == "pop":
            (array).pop()
        elif a[0] == "reverse":
            (array).reverse()
        n -= 1
