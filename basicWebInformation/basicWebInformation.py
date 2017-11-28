#Imports
#-------------------------------------------------------------------------------------------
import requests # http request library
#------------------------Imports------------------------#
import os
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#-----------------------Functions-----------------------#
def printMenu():
 print "\n\nUrl basic requests"
 print "--------------------\n"
 print "Actions"
 print "1-View the server header response:"
 print "2-View the web html source:"
 print "3-View the status code:"
 print "4- View the security html headers:"
 print "5-Get all the url links contained in the url:"
 print "6-EXIT"
 option=raw_input("Select an option number: ")
 return option

def optionInRange(option): 
	try:
		if int(option) not in range(1,7):
			#In case is out of range
			return 0
		else:
			return option	
	except:
			#In case is not an int value
			return 0

def httpRequest():
	url=raw_input("Type the url you want to check: ")
	
	#Cleaning the screen to print the results
	os.system("cls")
	print "\n-----------RESULTS-----------"

	if url.find("http"):
		# if the user doesn't add http or https, asume http
		return requests.get('http://'+url,verify=False)		
	else:
		return requests.get(url,verify=False)

def getLinks(response):
	#use re.findall to get all the links
	links = re.findall('"((http|ftp)s?://.*?)"', response.text)
	file=open('url_results.txt','a')

	for url in links:
		print url
		file.write(str(url)+'\n')

def getHeaders(response):
 	print 'Status Code: '+str(response.status_code)+'\n'
 	for header in response.headers:
 		print header+' : '+response.headers[header]+'\n'

def getHTMLcode(response):
 	print response.text

def getStatusCode(response):
 	print 'Status Code: '+str(response.status_code)+'\n'

def securityHeaders(response):
	allSecurityHeaders=['content-security-policy','x-xss-protection','strict-transport-security','x-frame-options','public-key-pins','x-content-type']
	
	for securityHeader in allSecurityHeaders:
		if securityHeader in response.headers:
			print securityHeader+' : '+response.headers[securityHeader]
			continue
		else:
			print securityHeader+' : Not Found' 

#--------------------------MAIN-------------------------#
if __name__ == "__main__":
 os.system("cls")	
 option = 0

 while option!=6:
 	option=optionInRange(printMenu())	
 	
 	if option == 0:
		print "Bad option"
		continue
 	if option=='6':
		print "\nSuccessfully closed"	
		break	
 	
 	response=httpRequest()

 	if option == '1':
 		getHeaders(response)

 	elif option == '2':
 		getHTMLcode(response)
 
 	elif option == '3':
 		getStatusCode(response)

	elif option == '4':
		securityHeaders(response)

	elif option == '5':
		getLinks(response)	