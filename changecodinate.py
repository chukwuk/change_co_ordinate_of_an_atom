import os
import subprocess
import time
images=[]
imag = []
data_1 = []
data_2 = []
kele = [] 
num_2_change = []
num_4_co = []
cur_dir = os.getcwd() # Dir from where search starts can be replaced with any path

atom_no = raw_input('The atom number to be changed: ')
co_ord = raw_input('The co-ordinate of the atom: ')

if co_ord=='x':
    num_4_co = 0
if co_ord=='y':
    num_4_co = 1

no_atom = int(atom_no) + 1

print(no_atom)
print(num_4_co)

filenames = os.listdir(cur_dir)
for filename in filenames:
    for n in range(10):
        if filename.endswith(str(n)): 
            for n in range(10): 
                if filename.startswith(str(n)):
                    images.append(filename)


images = sorted(images)
for z in range(len(images)):
    os.system('pos2con.pl ' + images[z] + '/POSCAR')
time.sleep(0.5)

#atom_no = raw_input('The atom number to be changed: ')
#co_ord = raw_input('The co-ordinate of the atom: ')

f1 = open(images[0]+'/POSCAR.con', 'r') 
f2 = open(images[len(images)-1]+'/POSCAR.con', 'r')
num_line = 0
for line in f1:
    line = line.strip() 
    kele = line
    num_line+=1
    data_1 = line.split(' ')
#    print (data_1[len(data_1)-1])
#    print (data_1[0])
    if str(no_atom) == data_1[len(data_1)-1]:
        change_line =  num_line
        print(line)
        data_1 = line.split()
        zz = data_1[int(num_4_co)]
for line in f2:
    line = line.strip()
    data_2 = line.split(' ')
    if data_2[len(data_2)-1]== str(no_atom):
        data_2 = line.split()
        yy = data_2[int(num_4_co)]
print (yy)
print (zz)

diff = (float(yy)-float(zz))/float((len(images)-1))
num_add = float(zz)
for i in range(1, len(images)-1):
    num_add += diff
    num_2_change.append(num_add)

for k in range(1, len(images)-1):
  new =[]
  old = [] 
  f3 = open(images[k]+'/POSCAR.con', 'r')
  num_line2 = 0 
  for line in f3:
     new.append(line)
     old.append(line)
     num_line2+=1
     if num_line2==change_line:
       data_3 = line.split()
#       print(data_3[num_4_co])
       data_3[num_4_co] = num_2_change[k-1]
       print(data_3[num_4_co])

#       if '58'==data_3[len(data_3)-1]:
#            print(data_3[0])      
       cod =''
       for i in range(len(data_3)):
         cod += str(data_3[i])
         cod += ' '
       cod += '\n'
       new[change_line-1] = cod
  uu = open(images[k] + '/POSCAR.con', 'w')
  for lin in new:
   uu.write("%s" %lin)
  uu.close()
  time.sleep(0.5)
  os.system('pos2con.pl ' + images[k] + '/POSCAR.con')

#for i in range(len(data_3)):
#    print(data_3[i])

     

#print(cod)
#print(num_2_change)
#print(change_line)
#print(yy)
#print(zz)






#u = ' '
#for h in range(len(images)):
#    u = u  +  images[h] + '/POSCAR.xyz' + ' '
#time.sleep(1.5)
#os.system('cat' + u + '>moviemaker.xyz')
#time.sleep(0.5)
#os.system('ase-gui '+'moviemaker.xyz') 
#print(u)
#print len(images)
#print (images)
#a = [str(00), str(02), str(01), str(06), str(03), str(04), str(05)]
#y = str(0)+a[0]
#print y
#print sorted(a)
