# Enter your code here. Read input from STDIN. Print output to STDOUT
n= input()
room_list = input().split()
room_set = set(room_list)

for ele in list(room_set):
    room_list.remove(ele)
    
captain_room = room_set.difference(set(room_list)).pop()
print(captain_room)
