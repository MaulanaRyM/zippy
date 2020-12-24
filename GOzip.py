#python3.8
#codec by Rym

import zipfile
import sys

pathzip = input('Input File Zip : ')
pathpwd = input('Input Wordlist : ')
inc = zipfile.ZipFile(pathzip)
cc = open(pathpwd. 'rb')
cont = 0
for i in cc:
	try:
		cont += 1
		inc.extractall(pwd=i.strip())
	except:
		print('[',str(cont),'] Not Found -> ',i.strip())
	else:
		print('[',str(cont),'] Found -> ',i.decode().strip())
		sys.exit()
print('Password Tidak Ada Dalam Wordlist')