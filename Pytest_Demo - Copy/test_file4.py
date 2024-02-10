import pytest


class Test_PytestDemo4:

    @pytest.mark.sel
    def test_CredenceSiteNumber(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']/p/a"))
        # l=6

        list = []
        for r in range(1, 1 + l):
            number = driver.find_element(By.XPATH,
                                         "//div[@class='quickfinder-description gem-text-output']/p/a[" + str(
                                             r) + "]").text
            # print(number)
            list.append(number)

        if "+91 8237916162" in list:
            assert True
        else:
            assert False

        # list = [num1,num2,num3]

    @pytest.mark.sel
    @pytest.mark.g1
    def test_sum_005(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        driver = webdriver.Firefox()
        driver.get("https://automation.credence.in/login")
        # print(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/h2").text) # CredKart
        driver.find_element(By.ID, "email").send_keys("test@credence.in")
        driver.find_element(By.ID, "password").send_keys("test@123")
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        driver.implicitly_wait(10)
        # Click on "product"
        driver.find_element(By.XPATH, "//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()

        # Click on "Add to Cart"
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # Click on "Continue Shopping"
        driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

        # Click on "Headphones"
        driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()

        # Click on "Add to Cart"
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # Click on "Continue Shopping"
        driver.find_element(By.XPATH, "//a[normalize-space()='Continue Shopping']").click()

        # Click on "Apple iPad Retina"
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()

        # Click on "Add to Cart"
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # Select Quantity for first product
        quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
        quantity1.select_by_index(3)

        # Select Quantity for second product
        Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]")).select_by_index(1)

        # Select Quantity for second product
        Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]")).select_by_index(2)

        ####################################################################################################

        var1 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]").text
        print(var1)

        var2 = driver.find_element(By.XPATH, "//tbody/tr[2]/td[4]").text
        print(var2)

        var3 = driver.find_element(By.XPATH, "//tbody/tr[3]/td[4]").text
        print(var3)

        Product1 = (var1[1:])  # remove $
        product_value1 = float(Product1)  # str to float

        Product2 = (var2[1:])
        product_value2 = float(Product2)

        Product3 = (var3[1:])
        product_value3 = float(Product3)
        # calculate Subtotal
        expected_Subtotal_raw = product_value1 + product_value2 + product_value3

        expected_Subtotal = round(expected_Subtotal_raw, 2)
        print("expected_Subtotal-->" + str(expected_Subtotal))

        # calculate Tax
        expected_tax_raw = expected_Subtotal * 0.13

        expected_tax = round(expected_tax_raw, 2)
        print("expected_Subtotal-->" + str(expected_tax))

        # Total

        Expected_Total = expected_Subtotal + expected_tax

        print("expected_Subtotal-->" + str(Expected_Total))

        # Price--> $9199.96
        # Remove $
        # Price --> 9199.96 -- > str
        # price to float

        var4 = driver.find_element(By.XPATH, "//tbody/tr[4]/td[4]").text

        Actual_value_raw = (var4[1:])  # remove $
        Actual_Value = Actual_value_raw.replace(',', '')
        Actual_Subtotal = float(Actual_Value)  # str to float

        print("Actual_Subtotal-->" + str(Actual_Subtotal))

        if Actual_Subtotal == expected_Subtotal:
            print("TestCase Pass")
            assert True
        else:
            print("TestCase Fail")
            assert False
