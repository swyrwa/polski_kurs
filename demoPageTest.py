from selenium import webdriver
from selenium.webdriver.common.by import By
from ChromeOptions import ChromeOptions


driver = webdriver.Chrome(r"D:\Users\SWyrwa\Documents\zzz_moje\17.CDV\polski_kurs\drivers\chromedriver.exe", options=ChromeOptions().options)
driver.get("file:///D:/Users/SWyrwa/Downloads/Test.html")
driver.maximize_window()
# driver.find_element_by_id("fname")
driver.find_element(By.ID, "fname")
driver.find_element(By.LINK_TEXT, "Visit W3Schools.com!")
driver.find_element(By.PARTIAL_LINK_TEXT, "Visit W3School")
print(driver.find_element(By.CSS_SELECTOR, "th:first-child").text)
print(driver.find_element(By.XPATH, "//th[text()='Month']"))
print(driver.find_element(By.XPATH,"//input[text()='Male]"))
driver.close()