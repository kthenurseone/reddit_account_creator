import requests
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os
import random
######SORGU
import requests
import hashlib
import time
from twocaptcha import TwoCaptcha
def lis():
    abcaw = open("settings.txt").read().split("\n")
    url = 'https://kerim.projeman.net/lis.php?value=' + abcaw[2] + "&token=account_creator"
    response = requests.get(url) 
    response = response.text #siteden gelen
    sifre = str(time.time())[0:9]
    sifreleyici = hashlib.sha256()
    sifreleyici.update(sifre.encode("utf-8"))
    hashe = sifreleyici.hexdigest() #bizim şifre

    while hashe != response:
       print("LOADING...")
       time.sleep(1)
       return lis()

lis()
######SORGU 
filem = open("settings.txt").read().split("\n")
ACCOUNT_PASSWORD = filem[0]
BOT_RUN_TIME = filem[1]

def solve(driver):
    solver = TwoCaptcha(filem[3])
    try:
        result = solver.recaptcha(
            sitekey='6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC',
            url='https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2F',
            invisible=1,
            enterprise=0
            )
    finally:
        gcode = result['code']
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
    driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", gcode)
    print("Captcha solved")



for adasd in range(10):
    print("K' The Nurse One Reddit Account Creator BOT //// Telegram: t.me/kthenurseone")
    # time.sleep(0.2)
def create():
    f = open("proxy.txt").read().split("\n")
    random_proxy = random.randint(0, len(f)-1)
    PROXY = f[random_proxy]
    print("Selected proxy:")
    print("Number: ", random_proxy)
    print("Proxy:",PROXY)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2F")
    actions = ActionChains(driver) 

    
    
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    response = requests.request("GET", url, headers=header)
    email = response.text.split("@")[0].replace('["','')
    domain = response.text.split("@")[1].replace('"]','')
    full_mail = str(email) + "@" + str(domain)
    print(full_mail)
    ############################################    SELENIUM PART ############################################
    
    # emailInput = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input[2]")))
    emailInput = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.NAME, "email")))
    emailInput.send_keys(full_mail)
    emailInput.send_keys(Keys.RETURN)  
    userName = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div[2]/div/div/a[1]")))
    userName.click()
    username = userName.text
    print(username)
    password = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div[1]/form/fieldset[2]/input[2]")))
    password.send_keys(ACCOUNT_PASSWORD)
    signUp = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[3]/button")))
    signUp.click() 
    print("All done now solving the captcha")
    # time.sleep(500)
    solve(driver=driver)
    time.sleep(3)
    signUp = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//button[@data-step='username-and-password']"))).click()
    time.sleep(2)
    finish = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Finish']"))).click()
    time.sleep(3)
    # print("Captcha solved")
    # captcha = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]")))
    # captcha.click() 
    # signUp2 = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[3]/button")))
    # signUp2.click() 
    # finish = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div[3]/button")))
    # finish.click()
    
    # time.sleep(100)
    
    ############################################    SELENIUM PART ############################################
    email_check = "https://www.1secmail.com/api/v1/?action=getMessages&login=" + str(email) + "&domain=" + str(domain)
    print(email_check)
    response_email = requests.request("GET", email_check, headers=header)
    while len(response_email.text) < 5:
        response_email = requests.request("GET", email_check, headers=header)
        # print("Waiting for message: " + email + "@" + domain)
        # print(email_check)
        print(email + "@" + domain)
        # print(response_email.text)
        time.sleep(1)
    y = json.loads(response_email.text)
    print(y[0]["id"])
    get_message_url = "https://www.1secmail.com/api/v1/?action=readMessage&login=" + str(email) + "&domain=" + str(domain) + "&id=" + str(y[0]["id"])
    print(get_message_url)
    message = requests.request("GET", get_message_url, headers=header)
    x = json.loads(message.text)
    # print(x["htmlBody"])
    for a in x["htmlBody"].split('"'):
        if a.startswith('https://www.reddit.com/verification/'):
            # print(a)
            driver.get(a)
            print("Email verification done.")
            open("accounts.txt", "a").write("\n" + username + ":" + ACCOUNT_PASSWORD)
            wait = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "/html/body/")))
            time.sleep(2)


    

for abc in range(int(BOT_RUN_TIME)):
    try:
        create()
    except Exception as e:
        print(e)
        pass
    