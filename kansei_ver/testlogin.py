from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
url="https://login.microsoftonline.com/common/oauth2/authorize?response_mode=form_post&response_type=id_token+code&scope=openid&msafed=0&nonce=d50c6e8a-07e5-4f04-bfdd-70789ec57069.637624622347376270&state=https%3A%2F%2Fforms.office.com%2FPages%2FResponsePage.aspx%3Fid%3DgMGpNSuYw0OD_N_OwcUPZJUeY5VBleFMitUvWccOfmBUNEtQWU5XRTQ0MkkwUUJHUFBKOEpZSDBIVC4u%26qrcode%3Dtrue%26sid%3D496c5c91-0843-43fd-b30e-bbf024018827&client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3a%2f%2fforms.office.com%2fauth%2fsignin";

def loginQR(email,stid,stpass,flag):
    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=options)
    driver.get(url)
    #print("ccccccccccccccccc")
    time.sleep(15)
    idBox=driver.find_element_by_id('i0116')
    idBox.send_keys(email)
    login_btn=driver.find_element_by_id("idSIButton9")
    login_btn.click()
    time.sleep(15)
    #driver.save_screenshot("{}screenA.png".format(stid))
    sso_idbox=driver.find_element_by_name('usr_name')
    sso_idbox.send_keys(stid)
    sso_idbox=driver.find_element_by_name('usr_password')
    sso_idbox.send_keys(stpass)
    time.sleep(15)
    sso_login_btn=driver.find_element_by_class_name("btn-sm")
    sso_login_btn.click()
    time.sleep(15)
    #driver.save_screenshot("{}screenB.png".format(stid))
    latelogin_btn=driver.find_element_by_id("idBtn_Back")
    latelogin_btn.click()
    time.sleep(15)
    #driver.save_screenshot("{}screenC.png".format(stid))
    if (flag==1):
        #print("A")
        radio_btn=driver.find_elements_by_name("rb40f9df4ef6c40a48a5f6ae1472c7b5b")
        radio_btn[0].click()
        #driver.save_screenshot("{}screenIN.png".format(stid))
    else:
        #print("b")
        radio_btn=driver.find_elements_by_name("rb40f9df4ef6c40a48a5f6ae1472c7b5b")
        radio_btn[1].click()
        #driver.save_screenshot("{}screenOUT.png".format(stid))
    time.sleep(5)
    last_login_btn=driver.find_element_by_css_selector(".office-form-theme-primary-background.office-form-theme-button.office-form-bottom-button.button-control.light-background-button.__submit-button__")
    #last_login_btn.click()
    time.sleep(5)
    #driver.save_screenshot("{}screenLAST.png".format(stid))
    driver.quit()
    time.sleep(5)
