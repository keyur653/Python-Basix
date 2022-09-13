def splitandjoin(line):
    split_line=line.split(" ")
    joined="-".join(split_line)
    return joined
if __name__ =='__main__':
    line=input()
    result=splitandjoin(line)
    print(result)
