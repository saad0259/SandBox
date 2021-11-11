A = [1,3,1,-4,5] #2
B = [1,2,3] #4
C = [-1,-3] #1
D = [0, 44, 23, 1 , 2 , 3 , 6, 3, 4, 99999] #5
E=[2,2,2]
A=E
minimum_positive_integer=0;

# not 2 in A O(n)

for a in A:
    if(len(A)>1):
        if((not (a+1) in A) and a>0):
            if(a<minimum_positive_integer or minimum_positive_integer==0):
                minimum_positive_integer=a
    elif(a==1): 
        minimum_positive_integer=1
            
            

print("Ans : ",minimum_positive_integer+1)