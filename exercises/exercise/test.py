import pyautogui
import subprocess
import time
import pandas as pd
from datetime import datetime


def sign_in(meetingid, pswd):
    subprocess.call(["/Applications/zoom.us.app"])


sign_in("611142342345", "543523fds")
