from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("username/phone : ")
#ID = input()
ID = "7378400435"
print("password : ")
#PASSWORD = input()
PASSWORD = "gohome@003"

print("url of product : ")
URL = "https://www.flipkart.com/samsung-galaxy-a51-prism-crush-black-128-gb/p/itm38c2ee53cb67b"

print("chrome driver location : ")
#DRIVER_PATH = input()
driver = webdriver.Chrome()
driver.get(URL)

def login():
    try:
        time.sleep(10)
        print("Logging In..")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._3Ep39l"))
            )
            print('Login Button Clickable')
        except:
            print('Login Button Not Clickable')
        login.click()
    except:
        print('login Failed. Retrying.')
        time.sleep(0.5)	
        login()
       
def login_submit():
    try:
        if 'Enter Password' in driver.page_source:
            print('Trying Usual method of Login.')
            email = driver.find_element_by_css_selector("._2zrpKA._1dBPDZ")
            passd = driver.find_element_by_css_selector("._2zrpKA._3v41xv._1dBPDZ")
            email.clear()
            passd.clear()
            email.send_keys(ID)
            passd.send_keys(PASSWORD)
            try:
                form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._2AkmmA._1LctnI._7UHT_c"))
                )
                print('Submit Button Clickable')
            except:
                print('Submit Button Not Clickable')
            form.click()     
        else:
            print('Trying Alternate method of Login.')
            email = driver.find_element_by_css_selector("._2zrpKA")
            email.clear()
            email.send_keys(ID)
            loginnext = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
                        )
            loginnext.click()
            loginpassword = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jUwFiZ"))
                        )
            loginpassword.click()
            time.sleep(0.5)
            passd = driver.find_elements_by_css_selector("._2zrpKA")[1]
            passd.clear()
            passd.send_keys(PASSWORD)
            form = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
                        )
            form.click()
        print("Logged In Successfully")
    except:
        if ('Login &amp; Signup' not in driver.page_source and 'Login & Signup' not in driver.page_source):
            print('Logged in Manually.')
        else:
            print('login_submit Failed. Please login manually.')
            time.sleep(1)
            login_submit()
            
def retry_check():
    try:
        if 'RETRY' in driver.page_source:
            print("retrying..")
            try:
                driver.find_element(By.XPATH, '//button[text()="RETRY"]').click()
                print('Retry Clicked')
            except:
                print('Retry Not Clickable')
        else:
            print('Retry button not found ')
    except:
        print('Retry Manually.')
        

def addtocart():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                #driver.refresh()
                time.sleep(0.2)
                print("Adding to cart")
                driver.find_element(By.XPATH, '//button[text()="ADD TO CART"]').click()
                print('Cart Button Clickable: ' + time.ctime())
                addr_sal_avl = False
                print('Cart Button Clickable')
            except:
                addr_sal_avl = True
                print('Cart Button Not Clickable')
        print('Cart Button Clicked Successfully')
        
    except:
        print('Cannot add to cart. Retrying.')
        
def run_script():
    login()
    time.sleep(10)
    login_submit()
    time.sleep(10)
    addtocart()
  
if __name__ == "__main__":
   run_script()


