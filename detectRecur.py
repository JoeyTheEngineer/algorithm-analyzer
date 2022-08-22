import sys
from inspect import getclosurevars
# import traceback
import re
from indent import compute_indent


def is_recursive(func):
    return getclosurevars(func).globals.get(func.__name__) is func

# def false_recursive():
#     if(1==1):
#         print("not")

# def true_recursive():
#     true_recursive()
# print("working.....\n")

# def detect_recursion(func):
#     try:
#         assert is_recursive(func), 'Must not fail'
#         # print("success")
#         return True
#     except AssertionError:
#         _, _, tb = sys.exc_info()
#         traceback.print_tb(tb) 
#         tb_info = traceback.extract_tb(tb)
#         filename, line, func, text = tb_info[-1]
#         print('An error occurred on line {} in statement {}'.format(line, text))



def scope_end_offset(lines,lineno,indent):
    # print(len(lines))
    lineno += 1 #skip 1st line
    for i in range(lineno,len(lines)):
        new_indent=compute_indent(lines[i])
        if new_indent==indent or new_indent<indent:#strictly if indent found
            return i

def detect_function_call(line):
    if(re.search(r"^[ ]*[^.]+[(][^]*[)][\n]*",line)):
        #must return name without ()
        text = line.split("(")[0].strip()
        if (re.search(r"[=]", text)):
            text=text.split('=')[1].strip()
        return text
    return False


def detect_function_implementation(line):
    if( re.search(r"^[ ]*def[ ][^:]+[:][\n]+",line) ):
        #must return name without def and ()
        return line.split("def ")[1].split("(")[0]
    return False




def compareArrays(defs,def_start,def_end,calls,lineno,indent):
    functions=[]
    functions_lineno=[]
    functions_indent=[]

    candidate = []
    candidate_lineno=[]

    for i in range(len(defs)):
        for j in range(len(calls)):
            if(defs[i]==calls[j]):#if function has both impl and call(s)
                if(lineno[j]>def_start[i] and lineno[j]<def_end[i]):#suitable recursion candidate
                    candidate.append(calls[j])#simply grab name

    for i in range(len(defs)):
        for j in range(len(calls)):
            if(defs[i]==calls[j]):#if function has both impl and utilisation
                if(lineno[j]<def_start[i] or lineno[j]>def_end[i] and calls[j] in candidate):#if call is not in implementation body
                    functions.append(calls[j])
                    functions_lineno.append(lineno[j])
                    functions_indent.append(indent[j])

    return functions,functions_lineno, functions_indent

# print(detect_function_call("        quickSort(arr, low, pi-1)"))
# str=true_recursive
# detect_recursion(str)
# assert not is_recursive(true_recursive), 'See? It fails' # AssertionError: See? It fails