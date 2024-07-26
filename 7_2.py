n=int(input("n="))
a=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i<j :
            a[i][j] = 5
        elif i>j :
            a[i][j] = 10
        else :
            a[i][j] = 20
for row in a :
    print(" ".join([str(elm) for elm in row]))