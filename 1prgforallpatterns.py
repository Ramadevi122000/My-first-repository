#square shape
n=int(input("enter no of rows"))
"""for i in range(1,n+1):
    print("*"*n,end="  ")
    print()"""

#right triangle
"""for i in range(1,n+1):
    print("*"*i,end=" ")
    print()"""

#left triangle
"""for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
    print()"""

###triangle
##for i in range(1,n+1):
##    print(" "*(n-i)+"* "*i)
##    print()
##
###diamond shape
##for i in range(1,n+1):
##    print(" "*(n-i)+"*"*i)
##for i in range(n,0,-1):
##    print(" "*(n-i)+"* "*i)

#diamond modification
for i in range(1,n+1,2):
    print(" "*(n-i)+"*"*i)
for i in range(n-2,0,-2):
    print(" "*(n-i)+"* "*i)

#inverted triangle
"""for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)"""



"""for i in range(1,n+1):
    for j in range(1,i):
        print(j,end=" ")
    print()"""

###arrow
##for i in range(1,n+1):
##    print("*"*i+" "*(n-i))
##for j in range(n-1,0,-1):
##    print("*"*j+" "*(n-j))





    
