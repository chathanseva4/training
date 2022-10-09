# minimum number of coins required to make a certain value
# the coins will be provided in a non negeitve intefer array 
# l=list(map(int,input().split()))
# k=int(input())
# l.sort()
# le=len(l)
# c=0
# def run(n,i):
#     if(n%l[i] == 0):
#         c+=n%l[i]
#         return c 
#     else:
#         n=n-((n%i)*l[i])
#         if(i==l-1): return c
#         run(n,i+1)

def coin(coins,s):
    sol=[0]*(s+1)
    for i in range(1,s+1):
        sol[i]=float('inf')
        for c in coin:
            if res=sol[i-c]:
                sol[i]=min(sol[i],res+1)
    if sol[s]!=float('inf'):
        return sol[s]
    else:
        return -1``
print(coin([5,2,1],11))
