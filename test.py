from os import link
import pandas as pd
import time
import pyautogui
import subprocess
from datetime import datetime
def login(link):

 subprocess.run(["C:\Program Files\Google\Chrome\Application\chrome.exe"])

 time.sleep(10)
 pyautogui.write(link)
 pyautogui.press('enter')






df = pd.read_csv('timings.csv')

while True:
    
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])

       login(m_id)
       time.sleep(10)
       print('signed in')