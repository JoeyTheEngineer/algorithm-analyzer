from indent import compute_indent
def file_length(fin):
    offset=0
    fin.seek(0)

    for line in fin:
        if(len(line)):
            offset+=len(line)
    # print(offset)       
    return str(offset).strip()

def scope_end_offset(lines,lineno,indent):
    # print(len(lines))
    lineno += 1 #skip 1st line
    for i in range(lineno,len(lines)):
        new_indent=compute_indent(lines[i])
        if new_indent==indent or new_indent<indent:#strictly if indent found
            return i


def readfile(offset):
    fin=open("code.txt", "r")
    fin.seek(offset)
    print(fin.readline())
    # print(fin.readline())
    # print(fin.readline())
    fin.close()


# scope_end_offset(650,0)
# scope_end_offset(open("code.txt", "r"), 360,0)
# readfile(72)
# 
# print (file_length(open("code.txt", "r")))