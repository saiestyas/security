#Imports
#-------------------------------------------------------------------------------------------
import requests # http request library
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)	

#Functions
#-------------------------------------------------------------------------------------------

def getDirectories():
 directory_list=[]
 file=open('checkDirectory.txt','r') 	
 
 for directory in file:
 	directory_list.append(directory.rstrip('\n'))

 return directory_list	

#---------------------------------------------------
def getUrls():
 url_list=[]
 file=open('checkUrl.txt','r')

 for url in file:
 	url_list.append(url.rstrip('\n'))

 return url_list	
#---------------------------------------------------

def getStatusCodeDescription(statusCode):
 file=open('httpStatusCodeDescription.txt','r') 	
 line=[]

 for line_comma_lineFeed in file.readlines():
 	line_comma=line_comma_lineFeed.rstrip('\n')
 	line.append(line_comma.split(','))

 for http_code in line:

 	if http_code[0]==statusCode:
 		return http_code[1]
 	else:
 		continue
 
 return "No available description"

#---------------------------------------------------

def joinUrlDirectory(http_protocol):
 urls=getUrls()
 directories=getDirectories()
 finalCheck=[]

 for url in urls:
	for directory in directories:

		if http_protocol=='http' or http_protocol=='both' or http_protocol=='none':
			finalCheck.append('http://'+url+directory)

		if http_protocol=='https' or http_protocol=='both':
			finalCheck.append('https://'+url+directory)

 return finalCheck
#---------------------------------------------------



def httpCodeStatus(check_url,http_protocol):
 firstWriteFlag=True

 for url in check_url:
 	print("Request to "+url)

 	#Make the http/https request and print the result
 	try:
		r = requests.get(url,verify=False)
	except Exception as e: 
		print("Resource not available check the error:\n\n"+str(e)+"\n") 
		writeCSVresult(http_protocol,url,'refused connection',str(e),firstWriteFlag)
		firstWriteFlag=False
		continue
		
	print url+" status "+str(r.status_code)

	if r.status_code>=200 and r.status_code<=308:
		print 'ACCESS  \n'
	else:
		print 'FAILURE \n'
    	
    #Getting the HTTP Code Description
	statusCodeDescription=getStatusCodeDescription(str(r.status_code))

	#Write into a csv file
	writeCSVresult(http_protocol,url,str(r.status_code),statusCodeDescription,firstWriteFlag)
	firstWriteFlag=False

	#Store the obtained data in a dictionary
	status_result = {'url': url, 'statusCode': str(r.status_code)}

 return status_result

#---------------------------------------------------	

def writeCSVresult(http_protocol,url,status,statusCodeDescription,firstWriteFlag):
    file=open('results.csv','a')

    if firstWriteFlag==True:
    	file.write('TRANSFER PROTOCOL;URL;STATUS; STATUS CODE DESCRIPTION\n')
    	file.write(http_protocol+';'+url+';'+status+';'+statusCodeDescription+'\n')
    else:
    	file.write(http_protocol+';'+url+';'+status+';'+statusCodeDescription+'\n')
	
    file.close()
#---------------------------------------------------	


#Main
if __name__ == "__main__":
 os.system("cls")	
 print("Web Directory checker")
 http_protocol=raw_input("Type http https both or none to make the proper check: ")
 print "Starting the process...\n"
 result=httpCodeStatus( joinUrlDirectory( http_protocol.lower() ), http_protocol.upper() )