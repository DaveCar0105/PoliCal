import unittest
from selenium import webdriver


#test acceso Epn (calendario)
class TestAV(unittest.TestCase):
    def testEpn(self):
        #driver = webdriver.Chrome('C:\\drivers\\chromedriver_win32\\chromedriver.exe')
        driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")
        driver.get('https://educacionvirtual.epn.edu.ec')

        titleOfEwbPage=driver.title

        self.assertTrue(titleOfEwbPage == "Google")  #true      
    
if __name__ == "__main__":
    unittest.main()