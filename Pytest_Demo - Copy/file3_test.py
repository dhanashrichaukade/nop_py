import pytest


class Test_PytestDemo3:
    @pytest.mark.xfail
    def test_sub_007(self):
        a = 6
        b = 4
        sub = a - b
        print(sub)
        if sub == 2:
            print("test pass")
            assert True  # Test case Passed
        else:
            print("test fail")
            assert False  # Test Case Fail

    @pytest.mark.skip
    def test_sum_008(self):
        a = 7
        b = 4
        sum = a + b
        print(sum)
        if sum == 11:
            print("test pass")
            assert True  # Test case Passed
        else:
            print("test fail")
            assert False  # Test Case Fail

