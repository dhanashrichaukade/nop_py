import pytest


class Test_PytestDemo2:
    @pytest.mark.g2
    def test_sub_003(self):
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

    @pytest.mark.g1
    def test_sum_005(self):
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


# pytest -v -m g1 -p no:warnings