def knapSack(N,W,wt,val): 
 
    if N == 0 or W == 0: 
        return 0
    if (W<int(wt[N-1])): 
        return knapSack(N-1, W, wt, val) 
    else: 
        return max(val[N-1] + knapSack(N-1,W-wt[N-1], wt, val), knapSack(N-1,W, wt, val)) 
    
N=int(input())
W=int(input())

wt=[]
val=[]

for i in range(N):
    wt.append(int(input()))
    val.append(int(input()))

print(knapSack(N,W,wt,val))