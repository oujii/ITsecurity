import pyautogui
import subprocess
import time
import pandas as pd
from datetime import datetime


def sign_in(meetingid, pswd):

    subprocess.call(["/usr/bin/open", "-a", "zoom.us.app"])
    time.sleep(10)
    


sign_in("611142342345", "543523fds")
