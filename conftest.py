import os
import shutil
import tempfile
from selenium import webdriver
import pytest

@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome(executable_path=r"C:\Users\Samiksha\Downloads\chromedriver\chromedriver.exe")
    request.cls.driver.get("https://www.saucedemo.com/")
    yield
    request.cls.driver.quit()


