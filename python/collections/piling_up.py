# Enter your code here. Read input from STDIN. Print output to STDOUT
ans = []
t = int(input())


for _ in range (t):
    n = int(input())
    s1 = list(map(int, input().split()))
    
    for _ in range(n-1):
        if s1[0] >=s1[len(s1)-1]:
            a = s1[0]
            s1.pop(0)
        elif s1[0] < s1 [len(s1)  -1]:
            a = s1[len(s1)-1]
            s1.pop(len(s1)-1)
        else:
            pass
        
        if len(s1) == 1:
            ans.append("Yes")
            
        if (s1[0] >a or (s1[len(s1)-1] > a)):
            ans.append("No")
            break

print("\n".join(ans))
