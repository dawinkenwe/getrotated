import win32api as win32
import win32con
import sys
import re
import os
from playsound import playsound
from tkinter import *
from ctypes import *

# arg 1 is for which desktop I believe.
def setWallpaperWithCtypes(path):
    ustr = create_string_buffer(path.encode('utf-8'))
    ok = windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, ustr, 0)

def rotate(x):
    rotation_val=win32con.DMDO_90
    device = win32.EnumDisplayDevices(None,x)
    dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
    if((dm.DisplayOrientation + rotation_val)%2==1):
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
    dm.DisplayOrientation = rotation_val

    win32.ChangeDisplaySettingsEx(device.DeviceName,dm)

def playWoo():
    playsound(os.getcwd()+"\sounds\woo.mp3")
    
def run():
    displays = []
    for i in range(10):
        try:
            device = win32.EnumDisplayDevices(None,i)
            if device is None:
                break
            else:
                displays.append(i)
                print(device.DeviceName)
                print(vars(device))
        except Exception as e:
            break
    print("ok")
    print(displays)
    displays = [ x for x in range(10) if win32.EnumDisplayDevices(None,x) is not None ]
    print(displays)

def getCurrentBackground():
    SPI_GETDESKWALLPAPER = 0x0073
    dll = WinDLL('user32')
    ubuf = create_unicode_buffer(200)
    if dll.SystemParametersInfoW(SPI_GETDESKWALLPAPER,200,ubuf,0):
        print(ubuf.value)

def undo():
    setWallpaperWithCtypes(r"C:\Users\dwink\AppData\Local\Microsoft\Windows\Themes\RoamedThemeFiles\DesktopBackground\1000 gates painting.jpg")
    rotate()

def setwall():
    setWallpaperWithCtypes(os.getcwd()+"\\images\\rotated.jpg")

def doGUI():
    window = Tk()
    window.title("StarFinder Character Creator")
    window.geometry('350x200')
    btn = Button(window, text="Click Me", command=playWoo)
    btn.grid(column=1, row=0)
    window.mainloop()

if __name__ == "__main__":
    # Rotate the screen
    # Set the desktop background to be get rotated
    # Play the woooo
    #getCurrentBackground()

    #doGUI()
    setwall()
    undo()
