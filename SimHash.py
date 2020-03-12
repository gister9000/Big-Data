import sys
from hashlib import md5

def simhash(text):
    hashlen = 128    
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
    
lines = sys.stdin.read().splitlines()
N = int( lines[0] )
Q = int( lines[ N+1 ] )
texts = lines[ 1 : N+1 ]
queries = lines[ N+2 : N+2+Q ]
simhashes = [ ]

for text in texts:
    simhashes.append(simhash(text.strip()))
    
for query in queries:
    I, K  = query.split(" ")
    queried_simhash = simhashes[int(I)]
    intK = int(K)
    count = -1  # queried text will be checked with itself
    for simhash in simhashes:
        # hamming distance
        h = sum(x1 != x2 for x1, x2 in zip(simhash, queried_simhash))
        if h <= intK:
            count += 1
    print(count)
  
