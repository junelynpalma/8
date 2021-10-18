import schedule
import time
import os
import sys

os.system('node g.js http://bct.ckgroup.ph http.txt 600 GET PHPSESSID:1g6s2thdcoksh05qcpimcgu970')

def job():
    os.system('node g.js http://bct.ckgroup.ph http.txt 600 GET PHPSESSID:1g6s2thdcoksh05qcpimcgu970')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)