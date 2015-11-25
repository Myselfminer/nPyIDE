#!/usr/bin/python
import easygui, os
"""
__version__ = "$Revision: 1.5 $"
__date__ = "$Date: 2004/04/30 16:26:12 $"
"""
os.system("color a")
from PythonCard import model

class MyBackground(model.Background):

    def on_initialize(self, event):
        try:
            import translate
            translate.do(self)
        except ImportError:
            print("Put a translate.py file into the root folder to translate the software. More info at http://nethermc.ddns.net/ide/translate.html")
        a=open("proj.prop","r")
        lines=a.readlines()
        line=[]
        count=0
        for i in lines:
            if count==0:
                pass
            else:
                line.append(i.strip("\n"))
            count=count+1
        self.components.files.items=line
        print(line)
    def on_menuFileNew_select(self, event):
        b=easygui.enterbox("Name:")
        if b.startswith("color "):
            os.system(b)
        else:
            if not b == "ide.py" or "ide.rsrc.py" or "translate.py" :
                new=open(b,"w")
                a=self.components.files.items
                a.append(b)
                self.components.files.items=a
                a=open("proj.prop","w")
                for i in self.components.files.items:
                    a.write("\n")
                    a.write(i)
            else:
                easygui.msgbox("This file is reserved by nPyIDE. Please choose another name! (This may also happen if the filename is weird!)")
    def on_Run_mouseClick(self,event):
        os.system("python "+self.components.files.stringSelection)
    def on_Delete_mouseClick(self,event):
        os.remove(self.components.files.stringSelection)
        a=self.components.files.items
        a.remove(self.components.files.stringSelection)
        self.components.files.items=a
        a=open("proj.prop","w")
        for i in self.components.files.items:
            a.write("\n")
            a.write(i)
    def on_Open_mouseClick(self,event):
        os.system("C:\Python27\Lib\idlelib\idle.bat "+self.components.files.stringSelection)
    def on_Duplicate_mouseClick(self,event):
        os.system("xcopy "+self.components.files.stringSelection+" copy_of_"+self.components.files.stringSelection)
        a=self.components.files.items
        a.append("copy_of_"+self.components.files.stringSelection)
        self.components.files.items=a

if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
