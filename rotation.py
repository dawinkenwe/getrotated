import win32api as win32
import win32con
import sys
import re
import os


print (os.getcwd())

# arg 1 is for which desktop I believe.
def setWallpaperWithCtypes(path):
    cs = ctypes.c_buffer(path)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 0)

def rotate(x):
    rotation_val=win32con.DMDO_90
    device = win32.EnumDisplayDevices(None,x)
    dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
    if((dm.DisplayOrientation + rotation_val)%2==1):
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
    dm.DisplayOrientation = rotation_val

    win32.ChangeDisplaySettingsEx(device.DeviceName,dm)
    
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

if __name__ == "__main__":
    run()
