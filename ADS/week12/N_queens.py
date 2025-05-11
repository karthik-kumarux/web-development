def NQueens(k,n,x):
    for i in range(1,n+1):
        if place(k,i,x):
            x[k]=i
            if k==n:
                print_solution(x,n)
            else:
                NQueens(k+1,n,x)

def place(k,i,x):
    for j in range(1,k):
        if x[j]==i or abs(x[j]-i)==abs(j-k):
            return False
    return True

def print_solution(x,n):
    print(x[1:n+1])

def solve_n_queens():
    try:
        n=int(input("Enter the number of queens(n):"))
        if n<1:
            print("please enter a positiv e integer.")
            return
        x=[0]*(n+1)
        print(f"Solution for {n}-Queens problem:")
        NQueens(1,n,x)
    except:
        print("Invalid input please enter an integer")

solve_n_queens()
