from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_xpath(url, xpath):
    try:
    
        browser = webdriver.Chrome()
        browser.get(url)

        
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

        elements = browser.find_elements(By.XPATH, xpath)
        if not elements:
            print(f"No elements found for XPath: {xpath}")
        else:
            print(f"Found {len(elements)} elements for XPath: {xpath}")
            for i, element in enumerate(elements):
                print(f"Element {i+1}: {element.text}")

    except NoSuchElementException as e:
        print(f"Error finding elements for XPath: {xpath}\n{str(e)}")
    except TimeoutException as e:
        print(f"Timeout while waiting for elements for XPath: {xpath}\n{str(e)}")
    finally:
        # Tarayıcıyı kapat
        browser.quit()


url = "URL" #change here
xpath = "XPATH" #change here too

test_xpath(url, xpath)
