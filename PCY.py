
import sys
import itertools

"""
​N je ukupan broj košara u datoteci
s ​je prag podrške zapisan kao omjer (vrijednost mi je 0 - 1)
b​ je broj pretinaca na raspolaganju funkciji sažimanja
"""
lines = sys.stdin.read().splitlines()
N = int(lines[0].strip())
s = float(lines[1].strip())
b = int(lines[2].strip())

prag = s * N
A, P = 0, 0

kosare = {}
brojac = {}
for i in range(3, N+3):
 kosare[str(i)] = lines[i].replace("\n","").split(" ") 
#kosare[str(i)] = [int(x) for x in lines[i].replace("\n","").split(" ")] 

for k in kosare.keys():  
 for item in kosare[k]:
   if item in brojac.keys():
     brojac[item] += 1
   else:
     brojac[item] = 0

freq_items = {}
for k in kosare.keys():  
 for item in kosare[k]:
   if brojac[item] >= prag:
     freq_items[item] = brojac[item]

m = len(freq_items)
A = int(m*(m-1)/2)
print(A)
pretinci = [0 for i in range(b)]
br = len(brojac)
# drugi prolaz, sazimanje u pretince
for k in kosare.keys():
 for i,j in itertools.combinations(kosare[k], 2):
   if i in freq_items and j in freq_items:
     pretinci[(int(i) * br + int(j)) % b] += 1    

parovi = {}
# treci prolaz, brojanje parova
for k in kosare.keys():
 for i,j in itertools.combinations(kosare[k], 2):
   if i in freq_items and j in freq_items:
     index = (int(i) * len(brojac) + int(j)) % b
     if pretinci[index] >= prag:
       key = i + "," + j
       if key in parovi.keys():
         parovi[key] += 1
       else:
         parovi[key] = 1
print(len(parovi))
for item in sorted(list(parovi.values()),reverse=True):
  print(item)
