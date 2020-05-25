import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def loadFile(filename,rate):
    path='music\\'
    path=path+filename
    y,sr=librosa.load(path,sr=rate)
    return y,sr

def music2note(data,rate):
    data=np.transpose(data)
    data=data/data.max()
    data[data<0.75]=0

    unit_rate=rate/(data.shape[1]-1)
    Note=[]

    for i in data:
        note=[]
        for j in range(len(i)):
            if i[j]>0 and len(note)==0:
                note.append(librosa.hz_to_note((j+1)*unit_rate))
        if len(note)!=0:
            Note.append(note[0])

    return  Note

def getNoteAndNum(data):
    data.append('#')
    N=data[0]
    count=1
    Count=[]
    Note=[]
    for i in range(1,len(data)):
        if N==data[i]:
            count=count+1
        if N!=data[i]:
            Count.append(count)
            Note.append(data[i-1])
            count=1
            N=data[i]
    return Note,Count

def Normlize(data,num):
    Data=[]
    Num=[]
    for i in range(len(data)):
        num[i]=num[i]//10
        if num[i]>=1:
            Data.append(data[i])
            Num.append(num[i])
    return Data,Num

def saveFile(filename,data,num=None):
    if num!=None:
        output = open(filename,'w+')
        for i in range(len(data)):
            output.write(data[i])
            output.write(' ')
            output.write(str(num[i]))
            output.write('\n')
        output.close()
    elif num==None:
        output = open(filename,'w+')
        for i in range(len(data)):
            output.write(data[i])
            output.write(' ')
            output.write('\n')
        output.close()

def note2note(data):
    Data=[]
    noteDic={'C5':'1','D5':'2','E5':'3','F5':'4','G5':'5','A5':'6','B5':'7',
             'C4':'(1)','D4':'(2)','E4':'(3)','F4':'(4)','G4':'(5)','A4':'(6)','B4':'(7)',
             'C6':'[1]','D6':'[2]','E6':'[3]','F6':'[4]','G6':'[5]','A6':'[6]','B6':'[7]'}
    for x in data:
        if x not in noteDic.keys():
            Data.append('#')
        else:
            Data.append(noteDic[x])
    return Data

def singleNote(filename,sr):
    y,rate=loadFile(filename,sr)
    Time=librosa.get_duration(y,sr=rate)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music2note(D,rate/2)
    Data=note2note(data)
    return data,Data

def mergeNote(filename,sr):
    y,rate=loadFile(filename,sr)
    Time=librosa.get_duration(y,sr=rate)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music2note(D,rate/2)
    data,num=getNoteAndNum(data)
    data,num=Normlize(data,num)
    Data=note2note(data)
    return data,Data,num

def plib(data):
    plt.figure()
    librosa.display.specshow(data,sr=44100,x_axis='time',y_axis='log')
    plt.show()
    
if __name__=='__main__':
    y,rate=loadFile('mer1.wav',44100)
    Time=librosa.get_duration(y,sr=rate)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music2note(D,rate/2)
    data,num=getNoteAndNum(data)
    data,num=Normlize(data,num)
    Data=note2note(data)

    output = open('mer1.txt', 'w+')
    for i in range(len(data)):
        output.write(Data[i])
        output.write('  ')
        output.write(data[i])
        output.write('  ')
        output.write(str(num[i]))
        output.write('\n')
    output.close()

    # data,Data,num=mergeNote('happy.wav',44100,0,10)
    # saveFile('1.txt',data,num)
    # data1,Data1,num1=mergeNote('happy.wav',44100,0,5)
    # saveFile('2.txt',data1,num1)
    # data2,Data2,num2=mergeNote('happy.wav',44100,5,5)
    # saveFile('3.txt',data2,num2)
