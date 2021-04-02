# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

for i in range (int (n/2)):
    string = ".|." * (2 * i +1)
    x =string.center(m, '-')
    print (x)
    
print("WELCOME".center(m, '-'))

for i in reversed(range(int(n/2))):
    string = ".|." * (2 * i +1)
    x =string.center(m, '-')
    print (x)
