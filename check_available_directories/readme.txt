Description
-----------
The script's purpose is to verify if the Server configuration is working
as expected just allowing access to the desired directories
from a specific scenario. 

E.g  Regular web visitor musn't have access to the cgi-bin directory

Developed with Python 2.7

How to use it
-------------

Steps:
	1-Modify the checkURL.txt with the urls/ip to check
	2-Modify the checkDirectory.txt adding the structure of your website
		E.g For example in a drupal 7.0 server you can check the default website structure adding
		    directories like /includes, /modules, /profiles, /scripts, /themes
	3-Run the script and visualize the results

checkURL.txt and checkDirectory.txt files have test values, check it to see how to fill those files.


Output results
--------------

The results are visualized in two ways:
	1-Teminal output
	2-CSV file 

The results show the http/https status code of the diferent performed requests.

