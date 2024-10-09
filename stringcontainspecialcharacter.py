import re

def run(string):
    regex = re.compile('[!@#$%^&*]')

    if (regex.search(string) == None):
         print("Accepted")
    else:
         print("Not Accepted")

string = "Geeks$for$Geeks"
run(string)