l=list(map(int,input().split()))
n=l.length()
m=l[0]
m_ind=0
w=0

print(w)

last=0
for i in range(1,n):
    if(l[i]<m):
        w+=m-l[i]
        l+=m-l[i]
    else:
        m=l[i]
        m_ind=i
        l=0
if m_ind!=n-1:
    w-=l 
    m=l[n-1]
    for i in range(n-1,m_ind-1,-1):
        if l[i]<m:
            w+=m-l[i]
        else:
            m=l[i]
print(w)



