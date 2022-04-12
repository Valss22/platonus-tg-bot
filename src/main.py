import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

token = '5115413693:AAFlHsjG9D64RJkhN5JlUgBnT3bKwZTU4o8'

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://platonus.kgu.kz/"
driver.get(url)

login_button = driver.find_element_by_id("Submit1")
login = driver.find_element_by_id('login_input')
password = driver.find_element_by_id('pass_input')

login.send_keys('Шокоров_Владислав')
password.send_keys('8222')
login_button.click()
time.sleep(1)

# Журнал

driver.find_element_by_xpath('//*[@id="sidebar-nav"]/plt-main-menu/ul/li[3]/a').click()
time.sleep(1)

# Выбор семестра
driver.find_element_by_xpath('//*[@id="s2id_autogen2"]/a/span[2]').click()
time.sleep(1)

# Семестр
driver.find_element_by_xpath('//*[@id="student_register"]/div/div/div/div/div[2]/div/select/option[2]').click()
time.sleep(1)

# Итерирование по боксам с предметами
subjects_marks: list[WebElement] = []

for i in range(1, 20):
    try:
        subjects_marks.append(
            driver.find_element_by_xpath(
                f'//*[@id="student_register"]/div/div/div/div/div[{str(i)}]/div/div')
        )
    except:
        continue


print(subjects_marks[0])
print(len(subjects_marks))
print(*subjects_marks)
