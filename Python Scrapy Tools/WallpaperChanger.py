import ctypes, os, random

#Define your pictures folder.
my_wallpaper = random.choice(os.listdir(f"D:\\Project\\Resimler"))
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"D:\\Project\\Resimler\\{my_wallpaper}" , 0)