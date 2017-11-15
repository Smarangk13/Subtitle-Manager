import os

def advance(q,t,dir,file):
    q=int(q)
    x=int(t)
    os.chdir(dir)
    # print(os.getcwd())

    readFile=file
    writeFile=file

    with open(readFile)as f:
        line=f.readlines()
    # print(line)

    writeIn=open(writeFile,'w')

    # Increment time past a line q by x
    i=0
    n=0
    c=0
    for i,l in enumerate(line):
        # print(l)
        # k=l[0:n-2]
        # Continue twice
        if(c==1):
            c=0
            continue
        k=l.rstrip()
        # print("k=",k)
        if(k.isnumeric()):
            # print("in if")
            # i+=4
            n=int(k)
            if(n>=q):
                # print(k)
                l2=line[i+1].rstrip()
                # print(l2)
                startMin=int(l2[3:5])
                startSec=int(l2[6:8])
                endMin=int(l2[20:22])
                endSec=int(l2[23:25])
                times=[startMin,startSec,endMin,endSec]
                # print(times)

                # add x seconds
                times[1]-=x
                times[3]-=x
                if(times[1]<0):
                    times[0]-= 1
                    times[1]=60+times[1]

                if (times[3] < 0):
                    times[2]-= 1
                    times[3]=60+times[3]

                # print(times)

                # change to strings
                for j,k in enumerate(times):
                    times[j]=str(k)
                    if(k<10):
                        times[j]="0"+times[j]
                    pass
                # print(times)

                l3=l2[0:3]+times[0]+":"+times[1]+l2[8:20]+times[2]+":"+times[3]+l2[25:]
                # print(l3)
                writeIn.write(l)
                l=l3+'\n'
                writeIn.write(l)
                c=1
                continue

        writeIn.write(l)


    # print(i)
    writeIn.close()

if __name__ == '__main__':
    q=13
    x=3
    dir='C:\\python_scripts\\subManager'
    file='SUBTITLE FILE.srt'
    advance(q,x,dir,file)
