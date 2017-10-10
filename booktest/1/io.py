import os
import shutil

##f = open(r'C:\Python27_13\tqvv\qiye.txt')
##print f.read()
##f.closed
with open(r'C:\Python27_13\tqvv\qiye3.txt','w') as fr :

    print fr.write('dfasfddsad\nafa\n'
                   'fasfsadf\n'
                   'fasdasdf\n')
   # print fr.read()
#with open(r'C:\Python27_13\tqvv\qiye.txt', 'r') as fr2:
   # for eachline in fr2.readlines(223132):
       ## print eachline

pwd = os.getcwd()
#print pwd
print os.listdir(pwd)
print os.path.split('C:\Python27_13\tqvv\qiye3.txt')
txt = os.stat('1.txt')
print txt
