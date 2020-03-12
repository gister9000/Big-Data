import sys
from collections import deque
import math

lines = sys.stdin.read().splitlines()
N = int(lines[0])
sizes = list()
x = 1
for i in range(N):
    sizes.append(x)
    x = x*2
    if x > N:
        break
#log2N = math.ceil(math.log(N, 2))
answers = list()
buckets = deque()
time = -1
no_buckets = True
# cheat with normal timestamp?
def answer_query(k):
    global buckets
    global time, N
    
    oldest = True
    estimate = 0
    for i in range(len(buckets)):
        
        if buckets[i][1] >= (time-k):
            #print(buckets[i])
            if oldest is True:
                estimate += math.floor(buckets[i][0] / 2)
                oldest = False
            else:
                estimate += buckets[i][0]
    return estimate

for line in lines[1:]:
    #print(line)
    if line[0] == 'q':
        answers.append(answer_query(int(line.split(" ")[1])))
        #exit()
        continue
    else:
        for i in range(len(line)):
            if no_buckets is True:
                if line[i] == '1':
                    no_buckets = False
                    buckets.append([1,time])
            else:
                if buckets[0][1] == time-N:
                    buckets.popleft()
                
                if line[i] == '1':
                    buckets.append([1, time])
                    for j in sizes:
                    
                        count, ii = 0, list()
                        for k in range(len(buckets)):
                            if buckets[k][0] == j:
                                count += 1
                                ii.append(k)
                        if count > 2:
                            new_elem = [ buckets[ii[0]][0]+buckets[ii[1]][0], buckets[ii[1]][1] ]
                            new_deque, count = deque(), 0
                            
                            for k in range(len(buckets)):
                                if buckets[k][0] == j and count == 0:
                                    count += 1
                                    new_deque.append(new_elem)
                                elif buckets[k][0] == j and count == 1:
                                    count += 1
                                else:
                                    new_deque.append(buckets[k])
                            buckets = new_deque
                        #print(buckets)          
            time = (time+1) #%N 
            
for answer in answers:
    print(answer)
