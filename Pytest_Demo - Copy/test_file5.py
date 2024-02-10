
class Test_PytestDemo4:

    def test_sub_008(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        # Open browser
        driver = webdriver.Firefox()
        driver.maximize_window()
        # Go to Url
        driver.get("https://automation.credence.in/login")

        # Enter email
        # XPATH--> XPATH(XML Path Language) is used language to select elements
        # or attribute from HTML pages
        # XPATH Format --> //tagname[@attribute='value']
        # Email Xpath --> //input[@type='email']
        # To check Xpath in browser console --> $x("Xpath")
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

        # Enter Password
        # CSS--> CSS(Cascading style sheets) is language used to describe
        # presentation of HTML pages.
        # CSS define visual properties of element like front, front size, colour, layout
        # CSS format --> tagname[attribute='value']
        # password css --> input[id='password']
        # To check CSS in browser console --> $$("CSS")
        driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@1234")

        # Click Login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # driver.title == "CredKart" -- > best practice
        # Verify Login status
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed")
        except:
            print("Login TestCase is Failed")

        driver.close()

        # TestCase Studio
        # SelectorHub

    def test_sum_009(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        # 1 Open Browser
        driver = webdriver.Chrome()
        driver.maximize_window()
        # 2 Go to Url
        driver.get("https://automation.credence.in/register")
        # 3 Enter Name
        driver.find_element(By.ID, "name").send_keys("Credence")
        # 5 Enter Email
        driver.find_element(By.ID, "email").send_keys("Credence_tpest@test.com")
        # 6 Enter Password
        driver.find_element(By.NAME, "password").send_keys("Credence@123")
        # 7 Enter Confirm Password
        driver.find_element(By.NAME, "password_confirmation").send_keys("Credence@123")
        # 8 Click Register button
        driver.find_element(By.CLASS_NAME, "btn").click()
        # Verify Registration status # page.title # success message
        # a= driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        # print(a)
        # # if  a == "CredKart" :
        # #     print("Registration TestCase is Passed")
        # # else:
        # #     print("Registration TestCase is Failed")

        try:
            a = driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']").text
            print("Registration TestCase is Passed")
        except:
            print("Registration TestCase is Failed")

    def test_sum_0559(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/windows")
        # time.sleep(4)
        driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']").click()
        # time.sleep(4)
        # To capture all windows in browser
        Select_window = driver.window_handles

        # To switch  specific window by index  (2nd window)
        driver.switch_to.window(Select_window[1])
        print(driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
        # time.sleep(4)
        # (1st window)
        driver.switch_to.window(Select_window[0])
        # time.sleep(4)
        print(driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text)
        # time.sleep(4)
        driver.close()
        # driver.close vs driver.quit()

        # time.sleep(40)





