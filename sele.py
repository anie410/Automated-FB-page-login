from selenium import webdriver
usr = input('enter ur username')
passw = input('enter ur password')
chrome_path = r"C:\Users\Ananya Rastogi\Desktop\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.facebook.com/?stype=lo&jlou=AfdJP70i2uxpRQTath9FmX1e-Eavk57vIle9s8TayZZR_7uJQDAW6CdS8jnEIUE3S8JmGsHvEGT53gv_7NDk5WohGd8sC6fvEc8dpBCcyWMvGw&smuh=5707&lh=Ac_LnOFL-VggSVSC")
username=driver.find_element_by_id("email")
username.send_keys(usr)
password=driver.find_element_by_id("pass")
password.send_keys(passw)
login_btn=driver.find_element_by_id("loginbutton")
login_btn.submit()