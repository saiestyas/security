file=open('httpStatusCodeDescription.txt','r') 	
line=[]

for line_comma_lineFeed in file.readlines():
	line_comma=line_comma_lineFeed.rstrip('\n')
	line.append(line_comma.split(','))

for http_code in line:
	print http_code[0]

# for i in clean_line:
#  if i[0]=='100':
#  	print i[1]
#  else:
#  	print "No description"