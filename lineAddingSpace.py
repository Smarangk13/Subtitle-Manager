import os

def addLine(q,dir,file):
    q=int(q)
    os.chdir(dir)
    # print(os.getcwd())

    readFile=file
    writeFile=file

    with open(readFile)as f:
        line=f.readlines()
    # print(line)

    writeIn=open(writeFile,'w')

    #Check what the last lins is
    print(len(line))

    # Add lines in between at position q
    # q=16
    i=0
    n=0

    print("Adding blank lines")

    while(i<(len(line))):
        l=line[i]
        # print(i)
        k=l.rstrip()
        # print("k=",k)
        if(k.isnumeric()):
            # print("in if")
            # i+=4
            n=int(k)
            if(n>q):
                n+=1
                l=str(n)+'\n'

            elif(n==q):
                l=str(q)+'\n[ENTER TIME STAMP HERE]\n[ENTER TEXT HERE]\n\n'
                l+=str(q+1)+'\n'

        i+=1
        writeIn.write(l)

    print(i)
    writeIn.close()

if __name__ == '__main__':
    q=13
    dir='C:\\python_scripts\\subManager'
    file='SUBTITLE FILE.srt'
    addLine(q,dir,file)
