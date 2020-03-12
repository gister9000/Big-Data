import sys
from decimal import Decimal, ROUND_HALF_UP

lines = sys.stdin.read().splitlines()
n = int(lines[0].split(" ")[0])
e = int(lines[0].split(" ")[1])
boja = dict()
susjedi = dict()
for i in range(n):
    susjedi[str(i)] = list()

for i in range(n):
    boja[str(i)] = lines[i+1]

   
for i in range(n+1,n+e+1):
    x, y = lines[i].split(" ")
    susjedi[str(x)].append(y)
    susjedi[str(y)].append(x)
  
def closestblacknode(node):
    if boja[str(node)] == '1':
        return str(node)+" 0"
    neighbours = susjedi[str(node)]
    seen = set(neighbours)
    for r in range(1,11): # max dist 10
        # when one of the neighbours are black
        blacks = list()
        
        for sused in neighbours:
            if boja[str(sused)] == '1':
                blacks.append(int(sused))
        if not blacks: 
            novisusedi = set()
            for sused in neighbours:
                for susedovsused in susjedi[str(sused)]:
                    if susedovsused not in seen:
                        novisusedi.add(susedovsused)
                        seen.add(susedovsused)
            neighbours = list(novisusedi)
        else:                
            return str(min(blacks))+" "+str(r)
            # return lowest index of blacks and r as distance
    return "-1 -1" # no black node <10 radius

for i in range(n):
    print(closestblacknode(i))
