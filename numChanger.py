import os

def numFixer(dir,file):
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
    expectedNumber=0
    print("Editing Numbers")

    while(i<(len(line))):
        l=line[i]
        # print(i)
        k=l.rstrip()
        # print("k=",k)
        if(k.isnumeric()):
            expectedNumber+=1
            n=int(k)
            if(n!=(expectedNumber+1)):
                n=expectedNumber+1
                l=str(n)+'\n'


        i+=1
        writeIn.write(l)

    print(i)
    writeIn.close()

if __name__ == '__main__':
    dir='C:\\User\\subManager'
    file='Subfile.srt'
    numFixer(dir,file)
