import os

#useful function
sign=lambda a:(a>0)-(a<0)
#sOrE indicates start or end value
def timeHandle(times,sighn,sOrE):
    times[sOrE-1]+= sighn*1
    if(times[sOrE-1]<0 or times[sOrE-1]>=60):
        timeHandle(times,sign(times[sOrE-1]),sOrE-1)
    times[sOrE]+=(-sighn)*60

def changeTime(q,t,directory,file,direction):
    q=int(q)
    x=int(t)
    # advance 1 delay 0
    if(direction):
        x=-x

    os.chdir(directory)
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
        # Continue twice (since we are dealing with the following line)
        # when time is updated number and timestamps are rewritten already
        if(c==1):
            c=0
            continue
        k=l.rstrip()
        # print("k=",k)

        #For lines that are numbers
        if(k.isnumeric()):
            # print("in if")
            # i+=4
            n=int(k)
            if(n>=q):
                #time stamps on following line
                l2=line[i+1].rstrip()
                # print(l2)
                startHour=int(l2[0:2])
                startMin=int(l2[3:5])
                startSec=int(l2[6:8])
                # for end times use distance from comma
                commaPos=l2.rfind(',')
                endSec=int(l2[commaPos-2:commaPos])
                endMin=int(l2[commaPos-5:commaPos-3])
                endHour=int(l2[commaPos-8:commaPos-6])
                times=[startHour,startMin,startSec,endHour,endMin,endSec]
                # print(times)

                # add x seconds
                times[2]+=x
                times[5]+=x

                # Seconds may not be 0-60
                if(times[2]<0 or times[2]>=60):
                    timeHandle(times,sign(times[2]),2)

                if (times[5] < 0 or times[5]>=60):
                    timeHandle(times,sign(times[5]),5)

                # print(times)

                # change to strings
                for j,k in enumerate(times):
                    times[j]=str(k)
                    if(k<10):
                        times[j]="0"+times[j]
                    pass
                # print(times)

                l3=times[0]+":"+times[1]+":"+times[2]+l2[8:commaPos-8]
                l3+=times[3]+":"+times[4]+":"+times[5]+l2[commaPos:]
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
    q=6
    x=13
    dir='C:\\Users\\Smaran\\Documents\\Github\\subManager'
    file='SUBTITLE.srt'
    changeTime(q,x,dir,file,1)
