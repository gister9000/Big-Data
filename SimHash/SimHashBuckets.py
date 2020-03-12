import sys
from hashlib import md5

B = 8 # number of buckets
hashlen = 128 # md5 128 bits
Bsize = 16 # 128 / 8 = 16 bits
  
lines = sys.stdin.read().splitlines()
N = int( lines[0] )
Q = int( lines[ N+1 ] )

texts = lines[ 1 : N+1 ]
queries = lines[ N+2 : N+2+Q ]

simhashes = [ ]
candidates = { }
#print("N: ", N, "\nQ: ", Q)
def simhash(text):
    sh = [0 for i in range(hashlen)] 
    inputs = text.split(" ")
    
    for x in inputs:
        digest = int(md5(x.encode('utf-8')).hexdigest(), 16)
        for i in range(hashlen):
            if digest & (1 << i):
                sh[i] += 1
            else:
                sh[i] -= 1
    
    binary_simhash = ""
    for number in reversed(sh):
        if number >= 0:
            binary_simhash += '1'
        else:
            binary_simhash += '0'
    return binary_simhash
  
  
for text in texts:
    sh = simhash(text.strip())
    simhashes.append(sh)

for n in range(N):
    candidates[n] = set() # to remove duplicates

for b in range(B):
    # start from least important bits
    upper = hashlen - b * Bsize
    lower = upper - Bsize
    buckets = dict()
    for n in range(N):
        current_hash = simhashes[n]
        band = int(current_hash[lower : upper], 2)
        if band not in buckets:
            buckets[band] = { n } # set
        else:
            for item in buckets[band]:
                candidates[n].add(item)
                candidates[item].add(n)
            buckets[band].add(n)
            
#print(candidates) 
for query in queries:
    I, K  = query.split(" ")
    intI = int(I)
    intK = int(K)
    queried_simhash = simhashes[int(I)]
    
    count = 0 
    for i in candidates[intI]:
        # hamming distance
        h = sum(x1 != x2 for x1, x2 in zip(simhashes[i], queried_simhash))
        if h <= intK:
            count += 1
    print(count)
