from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
def crawling(user_id,user_password):
    chromedriver = 'C:\chromedriver_win32\chromedriver.exe'

    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    option.add_argument('headless')
    driver = webdriver.Chrome(chromedriver, options=option)

    driver.get('https://portal.sejong.ac.kr/jsp/login/loginSSL.jsp?rtUrl=blackboard.sejong.ac.kr')

    # 보안프로그램 경고창
    try:
        driver.switch_to_alert().dismiss()  # 경고창 끄기
        driver.switch_to_alert().accept()   # 경고창 확인

    except:
        alert = False

    # 로그인 정보
    user_name = user_id
    password = user_password

    # XPATH
    id_id = '//*[@id="id"]'
    password_id = '//*[@id="password"]'
    login_button = '//*[@id="loginBtn"]'

    # 기다림
    id_tag = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,id_id)))
    password_tag = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,password_id)))
    login_button_tag = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,login_button)))

    # 아이디 패스워드 입력 로그인
    id_tag.clear()
    id_tag.send_keys(user_name)
    password_tag.clear()
    password_tag.send_keys(password)
    login_button_tag.click()

    time.sleep(2)

    scroll = driver.find_element_by_xpath('//*[@id="main-content-inner"]')

    # 스크롤 내리기 (courses load)
    driver.execute_script("arguments[0].scrollBy(0, document.body.scrollHeight)", scroll) # document.body.scrollHeight : 페이지 세로 길이

    time.sleep(2)

    # 코스명 가져오기
    courseList = driver.find_elements_by_css_selector('h4[class="js-course-title-element ellipsis"]')
    
    courselist=[]
    for course in courseList:
        courselist.append(course.text)
    
    



    #linkList = driver.find_element_by_css_selector('div[element-details summary]')

    #time.sleep(3)



    link = driver.find_element_by_css_selector('a[class="course-title ellipsis hide-focus-outline large-10 medium-10 small-12"]')
    '''
    for i in links:
        print(i.get_attribute('id'))
        # selenium 사용시
        link = i.find_element_by_css_selector('li.detail > a').get_attribute('href')
        driver.get('https://map.naver.com' + link)
    '''
    link.click()





    time.sleep(3)

    #브라우저 닫기
    driver.quit()
    
    return courselist