from selenium import webdriver
import time
import random
import string
import datetime


# RANDOM USER ID GENERATOR

def id_generator(size=8, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# RANDOM DOB GENERATOR

def dob_generator(size=8, chars=string.digits):
    start_date = datetime.date(1960, 1, 1)
    end_date = datetime.date(2000, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_date_string = str(random_date)
    random_day = random_date_string[slice(8, 10)]
    random_month = random_date_string[slice(5,7)]
    random_year = random_date_string[slice(0,4)]
    

    return random_day + '/' + random_month + '/' + random_year

# RANDOM PHONE NUMBER GENERATOR

def number_generator(size=8, chars=string.digits):
    num_prefix = random.randint(3, 7)
    return '08' + str(num_prefix) + ''.join(random.choice(chars) for _ in range(size))



def autom():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    web = webdriver.Chrome(chrome_options=chrome_options)
    web.get('https://365digital-liveassistance.com/')

    time.sleep(1)

    UserID = id_generator()
    user = web.find_element_by_xpath('//*[@id="C2__USER_NAME"]')
    user.send_keys(UserID)

    time.sleep(1)

    dateofbirth = dob_generator()
    date = web.find_element_by_xpath('//*[@id="dob"]')
    date.send_keys(dateofbirth)


    PhoneNumber = '0850850856'
    phone = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div[2]/div/div/div/div[3]/div[1]/div[4]/div[6]/div[2]/div/div/input')
    phone.send_keys(PhoneNumber)

    time.sleep(1)

    Submit = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div[2]/div/div/div/div[3]/div[1]/div[4]/div[7]/div[2]/div/button')
    Submit.click()

    time.sleep(2)

    p1 = random.randint(1, 9)
    digitone = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/fieldset/div[3]/input')
    digitone.send_keys(p1)

    time.sleep(0.5)

    p2 = random.randint(1, 9)
    digittwo = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/fieldset/div[4]/input')
    digittwo.send_keys(p2)

    time.sleep(0.5)

    p3 = random.randint(1, 9)
    digitthree = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/fieldset/div[7]/input')
    digitthree.send_keys(p3)

    time.sleep(0.5)

    Submit1 = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[4]/div[1]/div[3]/div[2]/div/button/span')
    Submit1.click()

    time.sleep(2)

    p4 = random.randint(1, 9)
    digitfour = web.find_element_by_xpath('/html/body/form[1]/div[3]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/fieldset/div[2]/input')
    digitfour.send_keys(p4)

    time.sleep(0.5)

    p5 = random.randint(1, 9)
    digitfive = web.find_element_by_xpath('//*[@id="pass4"]')
    digitfive.send_keys(p5)

    time.sleep(0.5)

    p6 = random.randint(1, 9)
    digitsix = web.find_element_by_xpath('//*[@id="pass5"]')
    digitsix.send_keys(p6)

    time.sleep(0.5)

    Submit2 = web.find_element_by_xpath('//*[@id="C2__C1__C1__Authentication-PINPage-Continue"]')
    Submit2.click()

    time.sleep(2)

    web.close()


for i in range(10):
    autom()