import os
import platform
from osCommands import*
from codes import*
def getPlatform():
    if platform.system()=='Windows':
        return WindowsCode
    if platform.system()=='Linux':
        return LinuxCode
    return UnknownSystemCode
def GetAllFiles(path):
    if type(path)==str:
        return os.listdir(path)
    ls=[]
    return ls

def GetAllFilesOfFormat(path,format):
    if type(path)==str and type(format)==str:
        format='.'+format
        fullList=GetAllFiles(path)
        retList=[]
        for element in fullList:
            if format in element:
                retList.append(element)
        return retList
    ls=[]
    return ls
def GetAllPrograms():
    return GetAllFilesOfFormat(PATH_TO_PROGRAMS,FORMAT_OF_PROGRAMS)
def WindowsClearScreen():
    os.system('cls')
def LinuxClearScreen():
    os.system('clear')

def ClearScreen():
    platType=getPlatform()
    if platType==WindowsCode:
        WindowsClearScreen()
    elif platType==LinuxCode:
        LinuxClearScreen()
    elif platType==UnknownSystemCode:
        print("Error Unknown Operating System")

def RunHeadlessProgram():
    platType=getPlatform()
    if platType==WindowsCode:
        os.system('start cmd.exe @cmd /k "run.bat"')
    elif platType==LinuxCode:
        os.system("run.sh")
