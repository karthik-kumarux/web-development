def knapSackRec(W, val, wt, n, selected_items):
    
    if n == 0 or W == 0:
        return 0, selected_items

   
    if wt[n - 1] > W:
        return knapSackRec(W, val, wt, n - 1, selected_items)

    
    include_val, include_items = knapSackRec(W - wt[n - 1], val, wt, n - 1, selected_items + [n - 1])
    exclude_val, exclude_items = knapSackRec(W, val, wt, n - 1, selected_items)

   
    if include_val + val[n - 1] > exclude_val:
        return include_val + val[n - 1], include_items
    else:
        return exclude_val, exclude_items

def knapSack(W, val, wt):
    n = len(val)
    max_profit, selected_items = knapSackRec(W, val, wt, n, [])
    return max_profit, selected_items

if __name__ == '__main__':
    n = int(input("Enter the number of items: "))
    profit = []
    weight = []
    for i in range(n):
        val = int(input(f"Enter profit for item {i+1}: "))
        wt = int(input(f"Enter weight for item {i+1}: "))
        profit.append(val)
        weight.append(wt)
    W = int(input("Enter the capacity of the knapsack: "))
    
   
    max_profit, selected_items = knapSack(W, profit, weight)
    
   
    print(f"Maximum profit is: {max_profit}, Items included (1-indexed): {', '.join(map(str, [i + 1 for i in selected_items]))}")
