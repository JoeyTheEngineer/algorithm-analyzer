# def writeTime(time,identity):
#     fout = open("data_for_analysis/"+str(identity)+".txt", "a")
#     # fout.seek(0)
#     fout.write(str(time)+'\n')
#     fout.close()
def writeTime(time,identity):
    # identity: item+range+'_'+type
    # write: size+'_'+time
    import os
    route=identity.split("_")
    item=route[0]+"_"+route[1]
    type=route[2]
    path = f'data_for_analysis/{item}/{type}/'

    if not os.path.exists(path):
        os.makedirs(path)

    fout = open(path+'n'+str(time.split('_')[0])+'.txt', "a")
    # fout.seek(0)
    fout.write(str(time.split('_')[1])+'\n')
    fout.close()

def writeConclusion(identity,x,y,conclusion):
    path = f'conclusion/{identity.split("_")[0]}_{identity.split("_")[1]}/'

    import os
    if not os.path.exists(path):
        os.makedirs(path)

    # fout = open(path+str(conclusion)+"_"+str(identity)+'.txt', "a")
    fout = open(f'{path}{identity.split("_")[2]}_{conclusion}.txt', 'w')
    fout.seek(0)
    fout.truncate()
    coordinate=''
    for i in range (0,len(x)):
        coordinate=f'{coordinate}{x[i]}_{y[i]}\n'
    fout.write(f'{coordinate}')
    fout.close()
