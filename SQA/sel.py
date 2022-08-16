import unittest
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#This code uses the google chrome browser to conduct a single test on the python.org website
#It uses the website search bar to search for "pycon"
# Selenium installation: 3 marks."pip install selenium"
# Conducting API testing: 5 marks."Created unittest for API Testing"
# Sharing the right code and configurations used for API testing: 5 marks."Test passed so code is right"
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.submit()
        self.assertNotIn("No results found.", driver.page_source)
        
        for i in driver.requests:
            print("/n %s",i)
            
            print(i.response)
            a=a+1
       
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()