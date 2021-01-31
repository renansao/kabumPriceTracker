from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

def retrieveKabumPrices(strBusca):
    #opts = Options()
    #opts.headless = True
    driver = Chrome(executable_path='C://chromedriver.exe')
    dictGPU = {}

    try:
        driver.get('https://www.kabum.com.br/')
        textField = driver.find_element_by_xpath("//input[@class='sprocura']")
        textField.send_keys(strBusca)
        textField.send_keys(Keys.ENTER)
        time.sleep(2)

        selectBox = driver.find_element_by_xpath("(//select[@class='sc-fzpkJw sc-fznMnq jRnSvz'])[1]")
        optionValue = driver.find_element_by_xpath("(//option[@value='100'])[1]")

        selectBox.click()
        time.sleep(1)
        optionValue.click()
        time.sleep(1)
        timesDisabled = 0


        while (True):

            try:
                driver.find_element_by_xpath("(//div[contains(text(), 'Próxima') and @disabled])[1]")
                timesDisabled+= 1
            except:
                pass

            if (timesDisabled == 2):
                break

            time.sleep(2)

            divGPU = driver.find_elements_by_xpath("//div[@class='sc-fzqARJ eITELq']")
            for i in range (len(divGPU)):
                gpuName = (driver.find_element_by_xpath("//div[@class='sc-fzqARJ eITELq'][" + str(i+1) + "]//a[@class='sc-fzoLsD gnrNhT item-nome']").text).replace("'", "").replace('"', "")
                gpuPrice = driver.find_element_by_xpath("//div[@class='sc-fzqARJ eITELq'][" + str(i+1) + "]//div[@class='sc-fznWqX qatGF']").text
                gpuAvailabilityTag = driver.find_element_by_xpath("//div[@class='sc-fzqARJ eITELq'][" + str(i+1) + "]//img[@alt='tag de disponibilidade do produto']")
                if str(gpuAvailabilityTag.get_property("src")).endswith("indisponivel.gif"):
                    gpuAvailability = False
                else:
                    gpuAvailability = True

                dictGPU[gpuName] = {"price": gpuPrice,
                                    "availability": gpuAvailability}
            driver.find_element_by_xpath("(//div[contains(text(), 'Próxima')])[1]").click()
        
    finally:

        driver.quit()
    
    print(dictGPU)
    return dictGPU

    #//div[@class='sc-fzqARJ eITELq']//div[@class="sc-fznWqX qatGF"]