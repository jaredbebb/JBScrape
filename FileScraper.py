import re

"""
Only return links that have pages with relevant search terms. 
Scrape webpages for links.
Print links to file. 
Feed links back into program.
"""
#search terms are terms that the client wants to search for
ahref = "<a href=\"https://\S*\""

#startsite is the site that the scraper begins
#startsite = input("What site do you want to start the crawler on:")
#print("You want to start on:", startsite)

irs = input("Enter the file name: ")
try:
    thisFile = open(irs)
except:
    print("that file is not in the current directory:", irs)

#How relevent is the page to your search?
def pageRel(search):
    #rscore is the relevent score, how many "hits" the keyword had in the document
    linenumber = 0
    i = 0
    for line in thisFile:
        line = line.rstrip()
        linenumber = linenumber + 1
        i = i
        if re.search(search, line):
            i = i + 1
            print("The matching line is at:", linenumber,re.search(search, line),"i =", i)
    print("releventscore is :",i)


pageRel(ahref)


		

