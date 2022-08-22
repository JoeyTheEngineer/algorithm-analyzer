import sys
from inspect import currentframe, getframeinfo
from indent import compute_indent
from loopStart import detect_loop_start
from scopeEnd import scope_end_offset
from datetime import datetime
from inputFinder import find_input
from indent import compute_indent
from detectRecur import compareArrays, detect_function_call, detect_function_implementation
from writeModifiedCode import writeInjectedCode
from inject import code_inject

frameinfo = getframeinfo(currentframe())

fin = open(sys.argv[1], "rt")
lines = fin.readlines()


lines.append("\n#End of File\n")

# If we need to read line 33, and assign it to some variable
# x = lines[33]
# print(x)
now = datetime.now()
input_name='array_'

function_defs=[]
function_defs_start=[]
function_defs_end=[]

function_calls=[]
function_call_line_numbers=[]
function_call_indents=[]

functions=[]
functions_lineno=[]
functions_indent=[]

items=[]
start_offset=[]
end_offset=[]
indent_inject=[]

# code=[]

# offset=0


for i in range(0,len(lines)):
    indent=compute_indent(lines[i])


    if detect_function_implementation(lines[i]):
        function_defs.append(detect_function_implementation(lines[i]))
        function_defs_start.append(i)
        function_defs_end.append(scope_end_offset(lines,i,indent))
        fin.close

    elif detect_function_call(lines[i]):
        function_calls.append(detect_function_call(lines[i]))
        function_call_line_numbers.append(i)
        function_call_indents.append(indent)
    
    if detect_loop_start(lines[i]):
        items.append("loop")
        start_offset.append(i)
        end_offset.append(scope_end_offset(lines,i,indent))
        indent_inject.append(indent)

    if find_input(lines[i]):
        input_name = input_name+ now.strftime("%H%M%S")
        lines[i]=lines[i].split('=')[0]+'='+str(input_name)+'\n'
        

fin.close()

functions,functions_lineno,functions_indent=compareArrays(function_defs,function_defs_start,function_defs_end, function_calls,function_call_line_numbers, function_call_indents)


# print(start_offset)
# print(end_offset)
# print(item)

# print(function_defs)
# print(function_defs_start)
# print(function_defs_end)

# print(function_calls)
# print(function_call_line_numbers)

# print(functions)
# print(functions_lineno)

items+=functions
start_offset+=functions_lineno
end_offset+=functions_lineno
indent_inject+=functions_indent

# print (items)
# print(start_offset)
# print(end_offset)
# print(indent_inject)

code=code_inject(lines, start_offset, end_offset, items, indent_inject,input_name)

writeInjectedCode(code)

import os
os.system('cmd /k "python -u runner.py"')