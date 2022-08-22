import random
size = [16, 32, 128, 256, 512, 768, 1024, 1536, 2048, 2304, 3072, 3840, 4096, 4096, 7164, 8192, 16384, 20000, 32768, 50000, 100000]

def best_generator():
    for i in range(0,len(size)):
        fout = open("inputs/best/n"+str(size[i])+".txt", "w")
        for j in range(0,size[i]):
            fout.write(str(j)+"\n")
        fout.close()

def worst_generator():
    for i in range(0,len(size)):
        fout = open("inputs/worst/n"+str(size[i])+".txt", "w")
        for j in range(size[i]-1,-1,-1):
            fout.write(str(j)+"\n")
        fout.close()

def random_generator():
    for i in range(0,len(size)):
        fout = open("inputs/average/n"+str(size[i])+".txt", "w")
        for j in range(0,size[i]):
            fout.write(str(random.randint(0,size[i]*3))+"\n")
        fout.close()

def generate_inputs():
    best_generator()
    worst_generator()
    random_generator()

generate_inputs()