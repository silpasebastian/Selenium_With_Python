from time import sleep
from selenium import webdriver
from time import sleep

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options, executable_path=r"D:\Programming\libraries\chromedriver\chromedriver.exe")

driver.get("https://s1.demo.opensourcecms.com/wordpress/")
driver.maximize_window()

sleep(4)

driver.close()