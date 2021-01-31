from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


def retrieveTerabytePrices(strBusca):
    #opts = Options()
    #opts.headless = True

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    script = '''
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    '''
    driver = Chrome(desired_capabilities=chrome_options.to_capabilities(), chrome_options=chrome_options, executable_path='C://chromedriver.exe')
    # options.add_argument("--headless")
    driver.execute_script(script)
    dictGPU = {}

    try:
        driver.get('https://www.terabyteshop.com.br/')
        textField = driver.find_element_by_xpath("//input[@id='isearch']")
        for i in strBusca:
            textField.send_keys(i)
            time.sleep(0.3)
        time.sleep(5)
        textField.submit()
        time.sleep(10)
        #driver.find_element_by_xpath("(//button[@aria-label='botão buscar'])[1]")
        time.sleep(2)



        divGPU = driver.find_elements_by_xpath("//div[@id='prodarea']")
        for i in range (len(divGPU)):
            gpuName = driver.find_element_by_xpath("(//div[@class='commerce_columns_item_caption'])[" + str(i+1) + "]//strong").text
            gpuPrice = driver.find_element_by_xpath("(//div[@class='prod-new-price'])[" + str(i+1) + "]/span")

            if gpuPrice.is_displayed:
                gpuPrice = gpuPrice.text
                gpuAvailability = True
            else:
                gpuPrice = None
                gpuAvailability = False
            
            dictGPU[gpuName] = {"price": gpuPrice,
                                 "availability": gpuAvailability}
    finally:

        driver.quit()
    
    return dictGPU

    #//div[@class='sc-fzqARJ eITELq']//div[@class="sc-fznWqX qatGF"]