def end_loop_inject(line, indent):
    inject=' '*indent
    inject+="finject.write(str(get_linenumber())+ ' ')#end_loop"
    line=inject + "\n" + line
    return line