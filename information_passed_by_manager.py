# manager id --> 0
# team leader id --> tl

# sample input
# 7
# 1
# 4
# 5 3 8
# 1 2 2
# 4 6 3
# 3 1 4

n =  int(input())
tl = int(input())

no_of_meetings = int(input())

meetings =  [list(map(int, input().split())) for i in range(no_of_meetings)]

#  returns third item
def getTime(arr):
    return arr[2]

meetings = sorted(meetings, key=getTime)  # sorting by third item

info_known_members = [0, tl]  # at time 0

for meet in meetings:
    # print("meet at time ==> ", meet[2])
    meet.pop()
    for member in meet:
        # print(member, member in info_known_members)
        if member in info_known_members:
            meet.remove(member)
            info_known_members += meet
            break

info_known_members = list(set(info_known_members))

print(sorted(info_known_members))
