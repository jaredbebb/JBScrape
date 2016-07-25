import urllib.request
import io
import re
'''will use re library later... currently throws errors when trying to use match function
in write()'''

website = "http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request"
openWeb = urllib.request.urlopen(website)
stringIn = io.TextIOWrapper(openWeb,encoding='utf-8')
readString = stringIn.read()

outputfilelocation = "outputfile.txt"
outputfile = open(outputfilelocation,"w")
outputfile.write(readString)
        
