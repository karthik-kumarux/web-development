def merge_purge(s1, s2):
    merged = sorted(s1+s2, key = lambda x:(x[0],-x[1]))
    result = []
    max_profit = -1
    for profit, weight in merged:
        if profit > max_profit:
            result.append((profit, weight))
            max_profit = profit
    return result

def trace_back(s,p,w,m,n,x):
    for i in range(n-1,0,-1):
        best_pair_s_i = s[i][-1]
        wp = -1
        best_pair_s_i_minus_1 = None
        for pair in s[i-1]:
            if pair[1]+w[i] <= m and pair[1] > wp:
                wp = pair[1]
                best_pair_s_i_minus_1 = (pair[0]+p[i],pair[1]+w[i])
        if best_pair_s_i_minus_1 is None or best_pair_s_i[0] > best_pair_s_i_minus_1[0]:
            x[i] = 0
        else:
            x[i] = 1
            m -= w[i]
    if s[0] and (0,0) not in s[0]:
        x[0] = 1
    else:
        x[0] = 0

def DKP(p,w,n,m):
    s = [[] for _ in range(n)]
    s[0] = [(0,0)]
    for i in range(1,n):
        s1 = []
        for profit, weight in s[i-1]:
            if weight+w[i] <= m:
                s1.append((profit+p[i], weight+w[i]))
        s[i] = merge_purge(s[i-1],s1)
    px, wx = s[n-1][-1] if s[n-1] else (0,0)
    wp = -1
    best_pair = None
    if n > 1 and s[n-2]:
        for profit, weight in s[n-2]:
            if weight+w[n-1] <= m and weight > wp:
                wp = weight
                best_pair = (profit+p[n-1], weight+w[n-1])
    if best_pair is None or px > best_pair[0]:
        x_n = 0
    else:
        x_n = 1
    x = [0] * n
    x[-1] = x_n
    if n > 1:
        trace_back(s,p,w,m,n,x)
    elif n == 1 and p and w and m >= w[0]:
        x = [1]
    solution_profit = 0
    for i in range(n):
        if x[i] == 1:
            solution_profit += p[i]
    print("solution vector(x):",x)
    print("maximum profit:",solution_profit)

n = int(input("enter number of items:"))
p = list(map(int, input("enter profits of items seperated by space:").split()))
w = list(map(int, input("enter weights of items seperated by space:").split()))
m = int(input("enter maximum capacity of knapsack:"))

if len(p) != n or len(w) != n:
    print("error: profits and weights must have exactly n elements.")
else:
    DKP(p,w,n,m)
