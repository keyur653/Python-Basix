def mutate_string(string, position, character):
    new_s=s[:int(i)] + c + s[int(i)+1:]
    #method 2
    #l=list(s)
    #l=[int(i)}=c
    #new_s=''.join(l)
    return new_s
if __name__=='__main__':
    s=input()
    i, c=input().split()
    s_new=mutate_string(s, int(i), c)
    print(s_new)


