#!/usr/bin python3

def loadfile():
    fileIn = open("file.txt", "r")
    lines = fileIn.readlines()
    fileIn.close()    
    return lines

if __name__ == '__main__':
    print ("Load file ...\n")    
    lines = loadfile()    
    print (lines)
    print ("\nLoad End\n")
