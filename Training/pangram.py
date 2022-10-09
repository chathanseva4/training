s=input()
st=set()
st.add(' ')
for i in s:
    st.add(i.tolower())
if len(st)==27:
    
    print("YES")
else:
    print("NO") 
#     minor bug resolved
