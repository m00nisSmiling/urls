import os
import sys

try:
 aa = sys.argv[1]
 bb = sys.argv[2]
 if aa=='-f': 
  input1 = bb
  file1 = open(f'{input1}').read()
  file2 = file1.splitlines()

  list1 = []

  for i in file2:
   a = f' --new-tab {i}'
   list1.append(a)

  jj = ''.join(list1)

  urls = f"firefox{jj}"

  os.system(f'{urls}')
 else:
  print("ERROR use -f to use file")
except IndexError:
 print("ERROR usage: use -f [file.txt] to extract urls")
