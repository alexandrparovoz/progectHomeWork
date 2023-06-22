# мониторинг буфера обмена

import pyperclip
import time
ad_list = ''
while True:
    s = pyperclip.paste()
    if s != ad_list:
        print(s)
        ad_list = s
    time.sleep(2)
