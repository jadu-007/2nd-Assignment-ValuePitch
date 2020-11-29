import requests
from bs4 import BeautifulSoup
import time
import csv
with open('python_assignment.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    
    spamwriter.writerow(["Diary No.",
                         "Case No.",
                         "Present/Last Listed On",
                         "Status/Stage",
                         "Category",
                         "Act",
                         "Petitioner(s)",
                         "Respondent(s)",
                         "Pet. Advocate(s)",
                         "Resp. Advocate(s)",
                         "U/Section"])
    

for year in range(2020,2000,-1):
    for diary_number in range(1,100):
        with requests.session() as s:

            captcha_url="https://main.sci.gov.in/php/captcha_num.php"
            headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
            }
            r=s.get(captcha_url,headers=headers)
            captcha = BeautifulSoup(r.content , 'html.parser').text.strip()
            print("Captcha is "+captcha)


            form_data={
                "d_no": diary_number,
                "d_yr": year,
                "ansCaptcha": str(captcha)
                }
            headers={
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "32",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "main.sci.gov.in",
            "Origin": "https://main.sci.gov.in",
            "Referer": "https://main.sci.gov.in/case-status",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        }

            try:
                url="https://main.sci.gov.in/php/case_status/case_status_process.php"
                r=s.post(url,headers=headers,data=form_data)
                soup = BeautifulSoup(r.content, 'html.parser')
                tds = soup.find('table').findAll("td")
                td=[]
                for i in range(1,21,2):
                    td.append(tds[i].text)
                with open('python_assignment.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile)
                    spamwriter.writerow(td)
                time.sleep(2)
                print("\nDiary Number "+str(diary_number)+"\nYear "+str(year)+"\nDone")
                s.close()
                time.sleep(2)
            except:
                continue
    
