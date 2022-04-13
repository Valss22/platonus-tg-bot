import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

# Авторизация в Платонусе
from src.enums import SubjectBoxKeys, UserDataKeys


def start_webdriver(
        user_data: dict[UserDataKeys, str]
) -> list[dict[SubjectBoxKeys, str]]:
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    url = "https://platonus.kgu.kz/"
    driver.get(url)

    login_button = driver.find_element_by_id("Submit1")
    login = driver.find_element_by_id('login_input')
    password = driver.find_element_by_id('pass_input')

    login.send_keys(user_data[UserDataKeys.LOGIN])
    password.send_keys(user_data[UserDataKeys.PASSWORD])
    login_button.click()
    time.sleep(1)

    # Журнал
    driver.find_element_by_xpath(
        '//*[@id="sidebar-nav"]/'
        'plt-main-menu/ul/li[3]/a'
    ).click()

    # Выбор семестра
    driver.find_element_by_xpath(
        '//*[@id="s2id_autogen2"]'
        '/a/span[2]'
    ).click()

    # Семестр
    driver.find_element_by_xpath(
        f'//*[@id="student_register"]/div/div/div/'
        f'div/div[2]/div/select/option[{user_data[UserDataKeys.PERIOD]}]'
    ).click()

    subjects_marks: list[WebElement] = []
    # Итерирование по боксам с предметами
    for i in range(1, 20):
        try:
            subjects_marks.append(
                driver.find_element_by_xpath(
                    f'//*[@id="student_register"]/div/'
                    f'div/div/div/div[{str(i)}]/div/div'
                )
            )
        except:
            continue

    del subjects_marks[:2]

    subject_boxes: list[dict[SubjectBoxKeys, str]] = []

    for elements in subjects_marks:
        subject_box: dict[SubjectBoxKeys, str] = {}

        text: str = elements.text
        text_list = text.split('\n')

        j = 0
        for i in text_list:
            text_list[j] = text_list[j].replace(',', '.')
            if '%' in i:
                text_list.remove(i)
            j += 1

        subject_box[SubjectBoxKeys.SUBJECT] = text_list[0]
        subject_box[SubjectBoxKeys.TEACHER] = text_list[1]
        subject_box[SubjectBoxKeys.AVERAGE_MARK] = text_list[2]
        subject_box[SubjectBoxKeys.BC_1] = text_list[4]
        subject_box[SubjectBoxKeys.BC_2] = text_list[6]
        subject_box[SubjectBoxKeys.RATING] = text_list[8]
        subject_box[SubjectBoxKeys.EXAM] = text_list[10]

        subject_boxes.append(subject_box)

    return subject_boxes

# start_webdriver({
#     UserDataKeys.LOGIN: 'Шокоров_Владислав',
#     UserDataKeys.PASSWORD: '8222',
#     UserDataKeys.PERIOD: '1'
# })
