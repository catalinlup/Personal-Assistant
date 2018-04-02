try:
    from tkinter import*
    from tkinter import filedialog
    #from tkinter import ttk
    from tkinter import messagebox
except:
    print("Error Please Install Tkinter!!")
from osCommands import*
from editXML import*
#s=ttk.Style()
#s.theme_use('clam')

root =Tk()
theMenu=Menu(root)
programsMenu=Menu(theMenu,tearoff=0)
selectMenu=Menu(programsMenu,tearoff=0)
SelectedProgram=StringVar()
SelectedProgram.set(NoneStr)
SelectedProgramLabel=Label(text=SelectedProgram.get())
RunButton=Button(root,text="Run")
AddFrame=Frame(root)
DeleteFrame=Frame(root)
ListFrame=Frame(root)
nameToDelete=Entry(DeleteFrame)
nameToDeleteVar=StringVar()
nameToDeleteLabel=Label(DeleteFrame)
nameToAdd=Entry(AddFrame)
nameToAddLabel=Label(AddFrame)
nameToAddVar=StringVar()
filenameToAdd=Entry(AddFrame)
filenameToAddLabel=Label(AddFrame)
filenameToAddVar=StringVar()
dayToAdd=Entry(AddFrame)
dayToAddLabel=Label(AddFrame)
dayToAddVar=StringVar()
timeToAdd=Entry(AddFrame)
timeToAddLabel=Label(AddFrame)
timeToAddVar=StringVar()
messageToAdd=Text(AddFrame)
messageToAddLabel=Label(AddFrame)
messageToAddVar=StringVar()
AddButton=Button(AddFrame,text="Add")
DeleteButton=Button(DeleteFrame,text="Delete")
#ListBox
elementsInProgram=Listbox(ListFrame)
#end
def onSelect(event):
    w=event.widget
    index=int(w.curselection()[0])
    elm=w.get(index)
    nameToDeleteVar.set(elm.split(' ')[0])
    print(elm)
def InitListMenu():
    filepathStr=SelectedProgram.get()
    if filepathStr==NoneStr:
        return
    elms=GetAllSoundObjects(filepathStr)
    elementsInProgram.delete(0,END)
    for i in range(0,len(elms)):
        elementsInProgram.insert(int(i),str(elms[i]))
    elementsInProgram.grid(row=0,column=0)
    elementsInProgram.config(width=GUI_PROGRAM_WIDTH)
    elementsInProgram.bind("<<ListboxSelect>>",onSelect)
    ListFrame.pack(side=TOP)
def Refresh():
    InitListMenu()
def AddButtonAction(event=None):
    nameAddStr=nameToAddVar.get()
    dayAddStr=dayToAddVar.get()
    timeAddStr=timeToAddVar.get()
    messageAddStr=messageToAdd.get(0.0,END)
    filenameAddStr=filenameToAddVar.get()
    filepathStr=SelectedProgram.get()
    if filepathStr==NoneStr:
        messagebox.showwarning("Warning!","Select a program to write into!")
        return
    if len(nameAddStr)==0 or len(dayAddStr)==0 or len(timeAddStr)==0 or len(filenameAddStr)==0:
        messagebox.showwarning("Warning!","Fill all gaps!")
        return
    AddSoundObject(filepathStr,nameAddStr,filenameAddStr,dayAddStr,timeAddStr,messageAddStr)
    messagebox.showinfo("Info!","Sound Object Successfully Added to "+filepathStr)
    nameToAdd.delete(0,"end")
    filenameToAdd.delete(0,"end")
    dayToAdd.delete(0,"end")
    timeToAdd.delete(0,"end")
    #messageToAdd.delete(0,"end")
    Refresh()

def DeleteButtonAction(event=None):
    nameDelStr=nameToDeleteVar.get()
    filepathStr=SelectedProgram.get()
    if filepathStr==NoneStr:
        messagebox.showwarning("Warning!","Select a program to write into!")
        return
    if len(nameDelStr)==0:
        messagebox.showwarning("Warning!","Specify a name!")
        return
    delCode=DeleteSoundObject(filepathStr,nameDelStr)
    Refresh()
    if delCode==OK_CODE:
        messagebox.showinfo("Info!","Sound Object Successfully Deleted in "+filepathStr)
        nameToDelete.delete(0,"end")
    else:
        messagebox.showwarning("Warining","Could not find "+nameDelStr+" in "+filepathStr)


def InitAddMenu():
    nameToAddLabel.grid(row=0,column=0)
    filenameToAddLabel.grid(row=0,column=1)
    dayToAddLabel.grid(row=0,column=2)
    timeToAddLabel.grid(row=0,column=3)
    messageToAddLabel.grid(row=0,column=4)
    nameToAddLabel.config(text="Name")
    filenameToAddLabel.config(text="Filename")
    dayToAddLabel.config(text="Day")
    timeToAddLabel.config(text="Time")
    messageToAddLabel.config(text="Tweet")
    nameToAdd.grid(row=1,column=0)
    filenameToAdd.grid(row=1,column=1)
    dayToAdd.grid(row=1,column=2)
    timeToAdd.grid(row=1,column=3)
    messageToAdd.grid(row=1,column=4)
    nameToAdd.config(textvariable=nameToAddVar)
    filenameToAdd.config(textvariable=filenameToAddVar)
    dayToAdd.config(textvariable=dayToAddVar)
    timeToAdd.config(textvariable=timeToAddVar)
    #messageToAdd.config(textvariable=messageToAddVar)
    messageToAdd.config(width=30,height=5)
    AddButton.grid(row=1,column=5)
    #AddButton.bind("<Button-1>",AddButtonAction)
    AddButton.config(command=AddButtonAction)
    AddFrame.pack(side=TOP)
def InitDelMenu():
    nameToDelete.grid(row=1,column=0)
    DeleteButton.grid(row=1,column=1)
    nameToDeleteLabel.grid(row=0,column=0);
    nameToDeleteLabel.config(text="Sound Object Name to Delete")
    nameToDelete.config(textvariable=nameToDeleteVar)
    #DeleteButton.bind("<Button-1>",DeleteButtonAction)
    DeleteButton.config(command=DeleteButtonAction)
    DeleteFrame.pack(side=TOP)



def ButtonRun(event=None):
    selPr=SelectedProgram.get()
    if selPr==NoneStr:
        messagebox.showwarning("Warining!","Select A Program To Start")
        return
    dataCom=open(DATA_COM_NAME,"w")
    dataCom.write(selPr)
    dataCom.close()
    RunHeadlessProgram()
    Refresh()
def InitSelectMenu():
    programsList=GetAllPrograms()
    for element in programsList:
        selectMenu.add_radiobutton(label=element,variable=SelectedProgram,command=SetSelectedProgram)
def file_save():
    filename = filedialog.asksaveasfilename(initialdir = PATH_TO_PROGRAMS,title = "Create Program",filetypes = (("program files","*."+FORMAT_OF_PROGRAMS),))
    filename=filename+"."+FORMAT_OF_PROGRAMS
    text2save ='<?xml version="1.0"?>'+'<data>'+'</data>'
    file=open(filename,"w")
    file.write(text2save)
    file.close()
    names=filename.split("/")
    realName=names[len(names)-1]
    selectMenu.add_radiobutton(label=realName,variable=SelectedProgram,command=SetSelectedProgram)
    Refresh()
def SetSelectedProgram():
    SelectedProgramLabel.config(text=SelectedProgram.get())
    SelectedProgramLabel.pack(side=TOP)
    Refresh()


def InitMenu():
    InitSelectMenu()
    programsMenu.add_cascade(label="Select",menu=selectMenu)
    programsMenu.add_command(label="Create",command=file_save)
    theMenu.add_cascade(label="Programs",menu=programsMenu)

def init():
    root.title(GUI_PROGRAM_TITLE)
    root.geometry(GUI_PROGRAM_WSIZE)
    root.resizable(width=False,height=False)
    InitMenu()
    SetSelectedProgram()
    InitAddMenu()
    InitDelMenu()
    root.config(menu=theMenu)
    RunButton.config(width=20,height=3,fg="blue",font="comic 14 bold")
    #RunButton.bind("<Button-1>",ButtonRun)
    RunButton.config(command=ButtonRun)
    RunButton.pack(side=BOTTOM)


def main():
    init()
    root.mainloop()
main()
