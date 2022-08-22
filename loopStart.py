import re

def detect_loop_start(str):
    if(re.search(r"^[ ]*for[ ][^:]+[:][\n]+",str) or re.search(r"^[ ]*while[ ][^:]+[:][\n]+",str) or re.search(r"^[ ]*while[(][^:]*[)][:][\n]+",str)):
        return True
    else:
        return False
