A = [1,3,1,-4,5] #2
B = [1,2,3] #4
C = [-1,-3] #1
D = [0,2,4,8] #5
E=[123]
A=E

min=0
if(A!=[]):
    max=max(A)
else:
    max=0
# not 2 in A O(n)

for a in range(1,max+1):
    if(not a in A):
        min=a-1
        break
    if(min==0 and a==max):
        min=a
        break

print(min+1)
