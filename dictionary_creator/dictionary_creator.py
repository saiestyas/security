#IMPORTS
import itertools
import string
import os
import string

#global# 
alpha_lower='abcdefghijklmnopqrstuvwxyz'
alpha_upper=alpha_lower.upper()
digit_numbers='0123456789'

#--------------------------------------------------------------------------------------------------------#
def printMenu():
 print "List of available dictionary creators:"
 print "1-Letters, Lower case combinations"
 print "2-Letters, Upper case combinations"
 print "3-Letters, Mixed Upper and Lower case combinations"
 print "4-Numbers "
 print "5-Numbers and Lower Case letters"
 print "6-Numbers and Upper Case letters"
 print "7-Numbers, Mixed Upper and lower case letters"


 selection=raw_input("\nSelect an option number: ")
 return selection
#--------------------------------------------------------------------------------------------------------# 


#--------------------------------------------------------------------------------------------------------#
def lowerCaseLetters(size,title):
 file=open(title,'a')

 res = itertools.product(string.lowercase,repeat=int(size)) 
 for i in res: 
 	file.write( format(''.join(i)+'\n') )
 
 file.close()
#--------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------#
def upperCaseLetters(size,title):
 file=open(title,'a')

 res = itertools.product(string.uppercase,repeat=int(size)) 
 for i in res: 
 	file.write( format(''.join(i)+'\n') )
 
 file.close()
#--------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------#
def UpperAndLower(size,title):
 file=open(title,'a')

 res = itertools.product(alpha_lower+alpha_upper,repeat=int(size)) 

 for i in res: 
 	file.write( format(''.join(i)+'\n') )
 
 file.close()
#--------------------------------------------------------------------------------------------------------#

def numbers(size,title):
 file=open(title,'a')

 res = itertools.product(digit_numbers,repeat=int(size)) 
 for i in res:
 	file.write( format(''.join(i)+'\n') )

 file.close()

#--------------------------------------------------------------------------------------------------------#

def numbers_lower(size,title):
 file=open(title,'a')	

 res = itertools.product(digit_numbers+alpha_lower,repeat=int(size)) 
 for i in res:
 	file.write( format(''.join(i)+'\n') )

 file.close()

#--------------------------------------------------------------------------------------------------------#

def numbers_upper(size,title):
 file=open(title,'a')	

 res = itertools.product(digit_numbers+alpha_upper,repeat=int(size)) 
 for i in res:
 	file.write( format(''.join(i)+'\n') )

 file.close()

#--------------------------------------------------------------------------------------------------------#

def numbers_lower_upper(size,title):
 file=open(title,'a')	

 res = itertools.product(digit_numbers+alpha_lower+alpha_upper,repeat=int(size)) 
 for i in res:
 	file.write( format(''.join(i)+'\n') )

 file.close()
#--------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------#
def createDictionary(dictionary_selection):
 size=raw_input("How much characters do you want ? ")

 if dictionary_selection=='1':
 	lowerCaseLetters(size,'LowerCaseLetters.txt')
 if dictionary_selection=='2':
 	upperCaseLetters(size,'upperCaseLetters.txt')
 if dictionary_selection=='3':
 	UpperAndLower(size,'Upper_Lower_CaseLetters.txt')
 if dictionary_selection=='4':
 	numbers(size,'numbers.txt')
 if dictionary_selection=='5':
 	numbers_lower(size,'numbers_lowerCase.txt')		
 if dictionary_selection=='6':
 	numbers_upper(size,'numbers_upperCase.txt')
 if dictionary_selection=='7':
 	numbers_lower_upper(size,'numbers_mixed_letters.txt')	

#--------------------------------------------------------------------------------------------------------#



if __name__ == "__main__":
	#Clean the screen
	os.system("cls")
	selection=printMenu()
	createDictionary(selection)
	print "Dictionary created"


	
