def writeInjectedCode(code):
    try:
        fout = open("toCompile.py", "w")        
        fout.seek(0)
        fout.truncate()
        for x in code:
            fout.write(x)
        fout.close()
    except IOError: 
        print("An error occurred.")
    return 0