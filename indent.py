def compute_indent(line):
    indent=0
    for character in line:
        if(character != " "):
            break
        else:
            indent = indent + 1
    return indent
