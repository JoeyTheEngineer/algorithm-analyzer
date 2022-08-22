#regex to find input list in code
import re
def find_input(line):
    line=line.strip()
    # if(re.search(r"^[ ]*input[ ]*[=][ ]*[\[]([0-9][,])*[0-9][\]]",line)): #robust but non flexible
    if(re.search(r"^input[ ]*[=][ ]*",line)): #realistic
        
        return True
