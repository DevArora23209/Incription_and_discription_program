while True :
    aa=input("enter the word ").lower()
    bb=aa.count('')-1

    dd={' ':0+bb,'a':1+bb,'b':2+bb,'c':3+bb,'d':4+bb,'e':5+bb,'f':6+bb,'g':7+bb,
        'h':8+bb,'i':9+bb,'j':10+bb,'k':11+bb,'l':12+bb,'m':13+bb,'n':14+bb,
        'o':15+bb,'p':16+bb,'q':17+bb,'r':18+bb,'s':19+bb,'t':20+bb,'u':21+bb,
        'v':22+bb,'w':23+bb,'x':24+bb,'y':25+bb,'z':26+bb}
    for i in aa:
        vv=dd[i]
        vv=str(vv)
        aa=aa+vv+","
        aa=aa[1:]
    print(aa)
    
