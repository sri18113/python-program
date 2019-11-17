import os
import shutil
import glob

def fileCombineNoNumber(sourcePath , destFile):
    txtfiles = []
    for file in glob.glob(sourcePath):
        txtfiles.append(file)
    with open(destFile, 'wb') as wfd:
        for f in txtfiles:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
def fileCombineNumber(txtFiles , destFile):
    with open(destFile, 'wb') as wfd:
        for f in txtFiles:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)


def main():
     #fileCombineNoNumber("D:\\MiniConda\\ForPyAlgoTrade\\Data\\temp\\*.txt","D:\\MiniConda\\ForPyAlgoTrade\\Data\\temp\\temp3.abc")
     txtfiles = []
     for fileNumber in range(1, 3):
         txtfiles.append('D:\\MiniConda\\ForPyAlgoTrade\\Data\\temp\\temp'+str(fileNumber)+'.txt')
     print(txtfiles)
     fileCombineNumber(txtfiles, "D:\\MiniConda\\ForPyAlgoTrade\\Data\\temp\\temp3.abca")

main()