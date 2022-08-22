from pathlib import Path
import shutil
import os

def cleaner():
    # print(os.getcwd())

    src_path = os.getcwd()+'\data_for_analysis'
    src_other_path = os.getcwd()+'\conclusion'
    trg_path = os.getcwd()+'\old_data'

    if not os.path.exists(src_path):
        os.makedirs(src_path)  
    else:
        shutil.copytree(src_path, trg_path, dirs_exist_ok = True)  
        shutil.rmtree(src_path)
        os.makedirs(src_path)
        
    if not os.path.exists(src_other_path):
        os.makedirs(src_other_path)
    else:
        shutil.copytree(src_other_path, trg_path, dirs_exist_ok = True)
        shutil.rmtree(src_other_path)
        os.makedirs(src_other_path)

cleaner()