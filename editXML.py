try:
    import xml.etree.ElementTree as ET
except:
    print("Errror Install XML Parser")
from codes import*
def AddSoundObject(filepath,name,filename,day,time,message):
    filepath=PATH_TO_PROGRAMS+"/"+filepath
    file=ET.parse(filepath)
    root=file.getroot()
    soundObj=ET.Element("soundObject")
    soundObj.attrib['name']=name
    fileNameobj=ET.Element("filename")
    fileNameobj.text=filename
    dayObj=ET.Element("day")
    dayObj.text=day
    timeObj=ET.Element("time")
    timeObj.text=time
    messageObj=ET.Element("message")
    messageObj.text=message
    soundObj.append(fileNameobj)
    soundObj.append(dayObj)
    soundObj.append(timeObj)
    soundObj.append(messageObj)
    root.append(soundObj)
    file.write(filepath)
def DeleteSoundObject(filepath,name):
    filepath=PATH_TO_PROGRAMS+"/"+filepath
    file=ET.parse(filepath)
    root=file.getroot()
    found=False
    for sObj in root:
        if sObj.attrib['name']==name:
            root.remove(sObj)
            found=True
    file.write(filepath)
    if found:
        return OK_CODE
    return ERROR_CODE
def GetAllSoundObjects(filepath):
    ret=[]
    filepath=PATH_TO_PROGRAMS+"/"+filepath
    file=ET.parse(filepath)
    root=file.getroot()
    for sObj in root:
        strToAdd=sObj.get('name')+' '+sObj.find('filename').text+' '+sObj.find('time').text+' '+sObj.find('day').text+' '+sObj.find('message').text
        ret.append(strToAdd)
    return ret
