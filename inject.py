from datetime import datetime
import time


def code_inject(lines, start_offset, end_offset, items, indent_inject,input_name):

    identity=[]
    time_arrays=''
    #to write timing data
    #each file is labelled item_linestart.lineend
    for i in range(0,len(items)):
        identity.append(str(items[i])+'_'+str(start_offset[i])+"."+str(end_offset[i]))
        time_arrays=f'delta_time_{str(items[i])}_{str(start_offset[i])}_{str(end_offset[i])} = []\n'+' '*4+time_arrays

    header=f"""from detectRecur import detect_recursion
from fileWriter import writeTime
import sys
sys.setrecursionlimit(10000)
def run({input_name},type_index,size_index):
    from inspect import currentframe, getframeinfo
    from datetime import datetime
    import time
    delta_time = []
    {time_arrays}
    size = [32, 128, 256, 512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096]
    type = ['average','best','worst']
    
"""
    #give all an indent for function encapsule
    for i in range(0,len(lines)):
        lines[i]=' '*4+lines[i]

    # code = "time_up=time_up.append(time.perf_counter())"
    
    # lines[0]=' '*4+lines[0]
    lines[0]=header+lines[0]
    for i in range (len(start_offset)):
        code = "time_up_"+str(start_offset[i])+"_"+str(end_offset[i])+"=time.perf_counter()"
        lines[start_offset[i]]="\n"+' '*4+' '*indent_inject[i]+code+"\n"+lines[start_offset[i]]
        

    # code = "time_down=time_down.append(time.perf_counter())\ndelta_time.append(time_down-time_down)"
    
    for i in range (len(end_offset)):
        # code = "delta_time.append(time.perf_counter()-time_up_"+str(start_offset[i])+"_"+str(end_offset[i])+");"
        code = f"delta_time_{items[i]}_{start_offset[i]}_{end_offset[i]}.append(time.perf_counter()-time_up_"+str(start_offset[i])+"_"+str(end_offset[i])+");"

        # code=code+f"writeTime(str(size[size_index])+'_'+str(delta_time[-1]),str('{identity[i]}'+'_'+type[type_index]))"
        code=code+f"writeTime(str(size[size_index])+'_'+str(delta_time_{items[i]}_{start_offset[i]}_{end_offset[i]}[-1]),str('{identity[i]}'+'_'+type[type_index]))"
        # lines[-1]= lines[-1] + '\n' + ' ' * 4 + f"writeTime(str(size[size_index])+'_'+str(delta_time_{items[i]}_{start_offset[i]}_{end_offset[i]}),str('{identity[i]}'+'_'+type[type_index]))"
        
        if(items[i]=="loop"):
            # print(str(end_offset[i])+" "+str(lines[end_offset[i]]))
            
            lines[end_offset[i]]="\n"+' '*4+' '*indent_inject[i]+code+"\n"+lines[end_offset[i]]
        elif(items[i]!="loop"):
            lines[end_offset[i]]="\n"+lines[end_offset[i]]+' '*4+' '*indent_inject[i]+code+"\n"



    # print("print from inject.py")
    # for i in range(0, len(lines)):
    #     print(lines[i])

    
    # lines.append("x=time_up")
    return lines



# a = time.perf_counter()
# time.sleep(1)
# b = time.perf_counter()
# print(a)
# print(b-a)