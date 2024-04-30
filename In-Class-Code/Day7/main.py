import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message):
    sender_email = ""
    app_password = ""
    recipient_email = ""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print("Email sent successfully!")
    

cookies = json.load(open('cookies.json', 'r'))
courses = json.load(open('courses.json', 'r'))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://portal.psut.edu.jo/')

for cookie in cookies:
    if 'sameSite' in cookie:
        cookie['sameSite'] = 'Strict'
    driver.add_cookie(cookie)
    
driver.get('https://portal.psut.edu.jo:5050/StudentServices/StudentRegistration.aspx')
time.sleep(2)

# Accept Button
try:
    driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[2]/td[2]/div[2]/a').click()
    time.sleep(2)
except NoSuchElementException:
    pass

# Search Button
driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[2]/td[2]/div/div[3]/div[3]/a').click()
time.sleep(5)


curr_page = 1
while True:
    if len(courses) == 0:
        print('All courses found!')
        break

    time.sleep(2)
    table = driver.find_element(By.XPATH, '/html/body/form/div[3]/table/tbody/tr[2]/td[2]/div/div[3]/div/table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    
    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        course_id = cells[0].text
        course_name = cells[1].text
        course_section = cells[3].text
        if course_id in courses.keys():
            if course_section == courses[course_id]:
                if cells[-1].text == 'Add Course':
                    print(f'Found {course_name}!')
                    cells[-1].click()
                    del courses[cells[0].text]
                    send_email(f'{course_name} Found!', f'Course {course_id} section {course_section} found!')
                    
    paging_row = table.find_elements(By.CLASS_NAME, 'paging')[0]
    pages = paging_row.find_elements(By.TAG_NAME, 'a')
    if curr_page >= len(pages) + 1:
        curr_page = 0
    for page in pages:
        if page.text == str(curr_page + 1):
            page.click()
            curr_page += 1
            break