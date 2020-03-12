import sys
from decimal import Decimal, ROUND_HALF_UP

lines = sys.stdin.read().splitlines()
n = int(lines[0].split(" ")[0])
beta = float(lines[0].split(" ")[1])
degree = {}
count = 0
with open("M","w") as f:
    for line in lines[ 1 : n+1 ]:
        f.write(line+"\n")
        degree[str(count)] = len(line.split(" "))
        count += 1
q = int(lines[n+1])

with open("R","w") as r:
    rank = {}
    default = 1/n
    for j in range(n):
        rank[str(j)] = default
    for i in range(101):
        ss = ""
        for j in range(n):
            ss += str(Decimal(Decimal(rank[str(j)]).quantize(Decimal('.0000000001'), rounding=ROUND_HALF_UP)))+" "
        r.write(ss + "\n")
        rank_next = {}
        for j in range(n):
            rank_next[str(j)] = 0
        with open("M","r") as f:
            for j in range(n): 
                strj = str(j)       
                line = f.readline()[:-1]
                dest = line.split(" ")
                for d in dest:
                    rank_next[d] += (beta * rank[strj] / degree[strj]) 
                S = sum(rank_next.values())
                for k in range(n):
                    rank_next[str(k)] += (1-S)/n
        for j in range(n):
            strj = str(j) 
            rank[strj] = rank_next[strj]
    

for i in range(n+2, n+2+q):
    node, it = lines[i].split(" ")
    with open("R","r") as r:
        for j in range(int(it)):
            r.readline()
        print(r.readline()[:-1].split(" ")[int(node)])
