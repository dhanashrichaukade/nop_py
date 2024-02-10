# create Project
# configure interpreter
# Setting -- > Tools --> python integrated tools --> Default test runner--> (select Pytest)
# Install lib selenium, pytest, pytest-xdist, pytest-html
# use below commands in terminal to library:

# pip install selenium
# pip install pytest
# pip install pytes-html
# pip install pytest-xdist

# pytest rules -->
# File name--> prefix--> test_ or suffix --> _test
# Method name should start with --> test_
# setting --> Tools --> Terminal --> shell path should be --> "C:\Windows\system32\cmd.exe"
# To run file or testcases in terminal use command -- > pytest
# pytest -v for more details
# To run specific file --> pytest "file name"
# Group the testcases for run --> @pytest.mark.marker_name
# to run with marker --> pytest -m "marker_name"
# to run with multiple markers --> pytest -m "marker_name1 and marker_name2" / "marker_name1 or marker_name2"
# To generate html report you have to install lib first --> pytest-html
# command for html report -- > pytest -v --html=report.html
# pytest -s -k ? home_work
# parallel run you have to install lib first --> pytest-xdist
# parallel run command -- > pytest -n=4  (n = no. worker processor)




import pytest


class Test_PytestDemo1:

    @pytest.mark.g1
    def test_sum_001(self):
        a = 3
        b = 4
        sum = a + b
        print(sum)
        if sum == 8:
            print("test pass")
            assert True  # Test case Passed
        else:
            print("test fail")
            assert False  # Test Case Fail

    @pytest.mark.g2
    def test_mul_002(self):
        a = 3
        b = 4
        mul = a * b
        print(mul)
        if mul == 12:
            print("test pass")
            assert True  # Test case Passed
        else:
            print("test fail")
            assert False  # Test Case Fail

    def mul_003_test(self):
        a = 3
        b = 4
        mul = a * b
        print(mul)
        if mul == 12:
            print("test pass")
            assert True  # Test case Passed
        else:
            print("test fail")
            assert False  # Test Case Fail

