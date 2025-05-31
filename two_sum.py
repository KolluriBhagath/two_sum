nums=list(map(int,input().split()))
target=int(input())
lst={}
for i,num in enumerate(nums):
    c=target-num
    if c in lst:
        print([lst[c],i])
    lst[num]=i