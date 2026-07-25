# cook your dish here
for _ in range(int(input())):
    ddsa,dtoc,ddm=map(int,input().split())
    sdsa,stoc,sdm=map(int,input().split())
    if ddsa+dtoc+ddm==sdsa+stoc+sdm:
        if ddsa==sdsa:
            if dtoc==stoc:
                print("TIE")
            else :
                if dtoc>stoc:
                    print("Dragon")
                else:
                    print("sloth")
        else :
            if ddsa>sdsa:
                print("dragon")
            else:
                print("sloth")
    elif ddsa+dtoc+ddm>sdsa+stoc+sdm:
        print("dragon")
    else:
        print("sloth")
            