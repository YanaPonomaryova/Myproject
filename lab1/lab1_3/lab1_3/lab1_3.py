N = int(input("Enter a number (1<N<9): "))

for i in range(N):
 
    for j in range(i):
        print(" ", end="")
    
    for k in range(N, i, -1):
        print(k, end="")
    
    print()
