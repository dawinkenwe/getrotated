import win32api as win32
import win32con
import sys
import re
import os
from playsound import playsound
from tkinter import *
from ctypes import *

class Rotator:
    def __init__(self):
        self.oldbg = self.getCurrentBackground()
        self.woo = os.getcwd()+"\sounds\woo.mp3"
        self.newbg = os.getcwd()+"\\images\\rotated.jpg"
        self.monitors = self.getMonitors()
        

    def getMonitors(self):
        monitors = []
        for i in range(10):
            try:
                device = win32.EnumDisplayDevices(None,i)
                if device is None:
                    break
                else:
                    monitors.append(i)
            except Exception as e:
                continue
        return monitors
        

    def rotate(self, undo=False):
        rotation_val=win32con.DMDO_90 if not undo else win32con.DMDO_DEFAULT
        for x in self.monitors:
            try:
                device = win32.EnumDisplayDevices(None,x)
                dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
                if((dm.DisplayOrientation + rotation_val)%2==1):
                    dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
                    dm.DisplayOrientation = rotation_val

                win32.ChangeDisplaySettingsEx(device.DeviceName,dm)
            except Exception as e:
                self.monitors.remove(x)


    def getCurrentBackground(self):
        SPI_GETDESKWALLPAPER = 0x0073
        dll = WinDLL('user32')
        ubuf = create_unicode_buffer(200)
        if dll.SystemParametersInfoW(SPI_GETDESKWALLPAPER,200,ubuf,0):
            return ubuf.value

    def setWallpaperWithCtypes(self,path):
        ustr = create_string_buffer(path.encode('utf-8'))
        ok = windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, ustr, 0)

    def do(self):
        self.setWallpaperWithCtypes(self.newbg)
        self.rotate()
        playsound(self.woo)


    def undo(self):
        self.setWallpaperWithCtypes(self.oldbg)
        self.rotate(True)

class UI:
    def __init__(self):
        self.window = Tk()
        self.butt = Button(self.window, text="Click Me", width=350, height=200)
        self.rotator = Rotator()


    def do(self):
        self.rotator.do()
        self.butt.configure(text="UNDO", command=self.undo)


    def undo(self):
        self.rotator.undo()
        self.butt.configure(text="Click Me", command=self.do)
        

    def setup(self):
        self.window.title("StarFinder Character Creator")
        #width = self.window.winfo_screenwidth() 
        #height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (350, 200))
        self.butt.configure(command=self.do)
        self.butt.pack()


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    ui = UI()
    ui.setup()
    ui.run()
