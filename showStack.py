import os
filepath = 'stack' 
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       line = fp.readline()
       if  "<" not in line:
           continue
       line = line.split("<")[1].split("+")[0]
       os.system("c++filt "+line)
       cnt += 1
