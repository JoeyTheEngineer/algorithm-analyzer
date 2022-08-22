import concurrent.futures
from cleaner import cleaner
from toCompile import run
import time
import sys
import os
import signal, psutil

# print(os.getcwd())


types = ['average','best','worst']
sizes = [32, 128, 256, 512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096, 7164, 8192, 16384, 20000, 32768, 50000, 100000]

def average_run():
    for j in range (0,len(sizes)):
    # 1st loop average-n16
        path=f"inputs/{types[0]}/n{sizes[j]}.txt"
        fin=open(path, "rt")
        sample=fin.read().splitlines()

        # print(f'{type} {size} {sample[-1]}')

        run(sample,0,j)

def best_run():
    for j in range (0,len(sizes)):
    # 1st loop best-n16
        path=f"inputs/{types[1]}/n{sizes[j]}.txt"
        fin=open(path, "rt")
        sample=fin.read().splitlines()
        # print(f'{types[1]} {sizes[j]}')

        # print(f'{type} {size} {sample[-1]}')

        run(sample,1,j)

def worst_run():
    for j in range (0,len(sizes)):
    # 1st loop worst-n16
        path=f"inputs/{types[2]}/n{sizes[j]}.txt"
        fin=open(path, "rt")
        sample=fin.read().splitlines()

        # print(f'{type} {size} {sample[-1]}')

        run(sample,2,j)

# cleaner()
# up=time.perf_counter()
# best_run()
# average_run()
# worst_run()
# print(time.perf_counter()-up)



if __name__ == '__main__':

    def kill_child_processes(parent_pid, sig=signal.SIGTERM):
        try:
            parent = psutil.Process(parent_pid)
        except psutil.NoSuchProcess:
            return
        children = parent.children(recursive=True)
        for process in children:
            process.send_signal(sig)

    cleaner()
    up=time.perf_counter()
    timeout=20
    for i in range (0,2):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # p1=executor.submit(average_run)
            # p2=executor.submit(best_run)
            # p3=executor.submit(worst_run)
            # executor.shutdown(wait=True)
            p1=executor.submit(average_run)
            p2=executor.submit(best_run)
            p3=executor.submit(worst_run)

            try:
                r1 = p1.result(timeout=timeout)
                r2 = p2.result(timeout=timeout)
                r3 = p3.result(timeout=timeout)
            except concurrent.futures._base.TimeoutError:
                print("Timeout")
                executor.shutdown(wait=False, cancel_futures=True) # shutdown if one fails
                kill_child_processes(os.getpid())
                sys.exit(-1)
    print(time.perf_counter()-up)

os.system('cmd /k "python -u visualizer.py"')