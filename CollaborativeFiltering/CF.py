import sys
import numpy as np
from scipy import spatial
from decimal import Decimal, ROUND_HALF_UP

score, lines = 0.0, sys.stdin.read().splitlines()
N, M = [int(i) for i in lines[0].split(" ")]
Q, table = int(lines[N+1]), []
for i in range(1, N+1):
    table.append( [int(x) for x in lines[i].replace("X","0").split(" ")])

# for item item prediction
nptable = np.array(table)
print(nptable)
row_means =[]
for i in range(N):
    values = np.array(nptable[i][np.nonzero(nptable[i])])
    row_means.append( np.sum(values) / values.shape )
row_means = np.array(row_means)
normtable = nptable - row_means

# for user user prediction
T_nptable = np.transpose(nptable)
row_means =[]
for i in range(N):
    values = np.array(T_nptable[i][np.nonzero(T_nptable[i])])
    row_means.append( np.sum(values) / values.shape )
row_means = np.array(row_means)
T_normtable = T_nptable - row_means 

def predict_score(t, st, i, j, k):
    sim = np.array([ (1 - spatial.distance.cosine(t[i], t[it])) for it in range(t.shape[0])])
    #sim.sort()
    #print(sim)
    klist = np.argsort(sim)[-k:]
    #print(klist)
    jcol = st[:][j]
    brojnik = np.sum(np.dot(sim[klist], jcol[klist]))
    
    return (brojnik / np.sum(sim[klist])).astype(float)

for i in range(N+2, N+2+Q):
    I, J, T, K = [int(j) for j in lines[i].split(" ")]
    #print(I, J, T, K )
    if T == 1:
        score = predict_score(T_normtable, T_nptable, J-1, I-1, K)
    else:
        score = predict_score(normtable, nptable, I-1, J-1, K)
    print(Decimal(Decimal(score).quantize(Decimal('.001'), rounding=ROUND_HALF_UP)))
    

