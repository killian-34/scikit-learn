import site
easy_install_file = site.getsitepackages()[0]+'/easy-install.pth'
print("Checking for easy-install.pth here: %s"%easy_install_file)
try:
	print('hey')
	lines = []
	f = open(easy_install_file,'r')
	for line in f:
		print('line:',line)
		line = line.strip()
		if not ('.hidden/scikit-learn' in line):
			lines.append(line)
		else:
			print('deleting:', line)
	f.close()
	f = open(easy_install_file,'w')
	for line in lines:
		f.write(line+'\n')
	f.close()

except:
	print('Could not find easy-install.pth file. Locate it on your system and delete the line that looks like \'*.hidden/scikit-learn\'')
	print('Try using the site module and run site.getsitepackages() -- easy-install.pth is usually there.')
