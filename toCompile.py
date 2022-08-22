from detectRecur import detect_recursion
from fileWriter import writeTime
import sys
sys.setrecursionlimit(10000)
def run(array_220148,type_index,size_index):
    from inspect import currentframe, getframeinfo
    from datetime import datetime
    import time
    delta_time = []
    delta_time_loop_4_7 = []
    delta_time_loop_1_8 = []
    
    size = [32, 128, 256, 512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096, 7164, 8192, 16384, 20000, 32768, 50000, 100000]
    type = ['average','best','worst']
    
    def insertionSort(array):

        time_up_1_8=time.perf_counter()
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1      

            # time_up_4_7=time.perf_counter()
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1

            # delta_time_loop_4_7.append(time.perf_counter()-time_up_4_7);writeTime(str(size[size_index])+'_'+str(delta_time_loop_4_7[-1]),str('loop_4.7'+'_'+type[type_index]))
            array[j + 1] = key

        delta_time_loop_1_8.append(time.perf_counter()-time_up_1_8);writeTime(str(size[size_index])+'_'+str(delta_time_loop_1_8[-1]),str('loop_1.8'+'_'+type[type_index]))
    
    
    input =array_220148
    insertionSort(input)
    
#End of File
