from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_xpath(url, xpath):
    try:
        # Tarayıcıyı başlat
        driver = webdriver.Chrome()
        driver.get(url)

        # Elementlerin tamamen yüklenmesini bekleyin (isteğe bağlı)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

        # Elementleri bul
        elements = driver.find_elements(By.XPATH, xpath)
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
        driver.quit()

# Test etmek için URL ve XPath ifadesini girin
url = "https://x.com/SirSerHooD/followers"
xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]"

test_xpath(url, xpath)
