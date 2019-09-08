#!/usr/bin/env python

import os
import time
sevenline = []
old = []
new = []
element = []
ele = []
applic = raw_input('name of the poscar: ')
f = open(applic, 'r')   #OPENS THE FILE
i = 0                     #STARTS THE COUNTING
for line in f:            #STARTS A FOR LOOP 
    i = i + 1             #COUNTS THE NUMBER OF LINES
    new.append(line)      #CREATES A NEW FILE OF ALL LINES IN THE POSCAR
    old.append(line)      #CREATES A DUPLICATE FILES OF ALL LINES IN THE POSCAR
    if i==1:              #AN IF STATEMENT THAT TAKES STORES THE FIRST LINE OF THE POSCAR
       line = line.strip()     #STRIPS THE SPACE AT THE END AND BEGINNING OF THE LINE
       firsty = line.split('  ')  #SPLITS THE ELEMENT IN THE LINE and firsty contains the differents elements in the POSCAR 
    if i==6:                       #IF STATEMENT TO STORE THE 6TH LINE
       line = line.strip()             #STRIPS THE SPACE AT THE BEGINNING AND THE END OF THE LINE
       numb = line.split('   ')        #the numb contains the number of each element in the POSCAR
    if i==7:
       line = line.strip()
       sevenline.append(line)
print(firsty)
print(numb)
#create the elements corresponding to each co-ordinate in POSCAR
for k in range(len(firsty)):            
    for j in range(int(numb[k])):
        element.append(firsty[k])
print(element) 
#creates the elements in the POSCAR without duplications
for n in range(len(element)):
    i = 0
    for z in range(len(ele)):
        if element[n]==ele[z]:
           i = i + 1
    if i==0:
       ele.append(element[n])
print(ele)
time.sleep(1.5)
w = '  '
t = ''
#used to check which line to start rearranging the co-ordinates
if 'Selective dynamics'==sevenline[0]:
   y=7
   nk = 8
else:
   y=6
   nk = 7
#creates a new POSCAR with all the elements combined
for p in range(len(ele)):
    a = 0
    for u in range(len(element)):
        if ele[p]==element[u]:
           a = a + 1
           y = y + 1
           d = u + int(nk)
           new[y] = old[d]
    w = w + str(a) + '   '
    t = t + str(ele[p]) + '  ' 
print(w)
new[0] = t + '\n'
new[5] = w + '\n'
time.sleep(1.5)
uu = open('POSCAR', 'w')
for lin in new:
    uu.write("%s" %lin)
uu.close()


