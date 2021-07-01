import itertools
sk = input().split()
s = sk[0]
k = int(sk[1])
for i in range(k + 1):
    output = list(itertools.combinations(sorted(s),i))
    for m in output:
        for n in m:
            print(n,end="")
        print()    
            
        
