import pytest
from selenium import webdriver
class Test_sum1:


    def test_sum(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is "+ str(sum))

        if sum == 10:
            assert True
        else:
            assert False

    def test_file02(self):
        driver=webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("you are in credence.in")
            assert True
        else:
            print("you are in wrong url")
            assert False


    def test_sub1(self):
        a = 10
        b = 7
        sub = a - b
        print("Sub of a and b is " + str(sub))

        if sub == 3:
            assert True
        else:
            assert False