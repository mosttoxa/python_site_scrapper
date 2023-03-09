from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Define a function to wait for an element to appear on the page before interacting with it
def wait_for_element(driver, by, selector):
    for i in range(5):
        try:
            element = driver.find_element(by, selector)
            return element
        except:
            time.sleep(1)
    raise Exception(f"Element {selector} never appeared on the page")

# Define a function to translate text using Google Translate
def translate_text(text):
    # Set up the Chrome driver
    executable_path = 'C:/Users/robot/Desktop/chromedriver_win32/chromedriver.exe'
    service = Service(executable_path)
    driver = webdriver.Chrome(service=service)
    driver.get('https://translate.google.com/?hl=uk&sl=en&tl=hi&op=translate')
    
    # Wait for the input box to appear and enter the text to translate
    input_box = wait_for_element(driver, By.CSS_SELECTOR, 'textarea')
    input_box.send_keys(text)

    # Wait for the translation to appear and retrieve it
    wait_for_element(driver, By.CSS_SELECTOR, 'span[jsname="W297wb"]')
    output_box = driver.find_element(By.CSS_SELECTOR, 'span[jsname="W297wb"]')
    
    translated_text = output_box.text    

    return translated_text

# Set up the Chrome driver
service = Service('C:/Users/robot/Desktop/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigate to the page to scrape
driver.get('https://www.classcentral.com')

# Loop through the elements and translate them
elements = driver.find_elements(By.XPATH, '//*[@id="page-home"]/div[1]/header/div[1]/nav/div[3]/div[2]/span | //*[@id="page-home"]/div[1]/header/div[1]/nav/div[1]/button[2] | //*[@id="page-home"]/div[1]/header/div[1]/nav/div[3]/div[2]/a[1] | //*[@id="page-home"]/div[1]/header/div[1]/nav/div[3]/div[2]/a[2] | //h | //h1 | //h2 | //h3 | //h4 | //h5 | //h6 | //*[@id="page-home"]/div[1]/header/div[1]/nav/div[2]/a | //*[@id="page-home"]/div[1]/main/section[1]/div[2]/div/p/a[1] | //*[@id="page-home"]/div[1]/main/section[1]/div[2]/div/p/a[2] | //*[@id="page-home"]/div[1]/main/section[1]/div[2]/div/p/a[3]/span | //span[@class="padding-right-xxsmall"] | //span[@class="small-down-hidden"] | //strong[@class="margin-left-xsmall fill-space"] | //span[@class="text-1 weight-semi icon-chevron-right-charcoal icon-right-small color-charcoal"] | //span[@class="text-1 weight-semi upper btn-gradient-navy btn-small block color-white margin-bottom-medium"] | //p[@class="head-3 weight-semi max-450 width-centered border-box"] | a[@class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline"] | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[1]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[2]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[3]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[4]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[5]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[6]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/ul/li[7]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[1]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[2]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[3]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[4]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[5]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[6]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/ul/li[7]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[1]/ul/li[1]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[1]/ul/li[2]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[1]/ul/li[3]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[1]/ul/li[4]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[1]/ul/li[5]/a | //p[@class="text-2"] | //*[@id="page-home"]/div[1]/main/section[3]/div/div/a/span | //*[@id="home-stats"]/div/div/div/p[1]/span | //*[@id="home-stats"]/div/div/div/p[2]/span | //p[@class="head-2 weight-semi color-white margin-bottom-xxlarge relative padding-left-xlarge"] | //p[@class="text-1 color-white relative padding-left-xlarge"] | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[1]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[2]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[3]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[4]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[5]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[6]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/ul/li[7]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[1]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[2]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[3]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[4]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[5]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[6]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/ul/li[7]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[1]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[2]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[3]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[4]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[5]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[6]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/ul/li[7]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[2]/ul/li[1]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[2]/ul/li[2]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[2]/ul/li[3]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[2]/ul/li[4]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[2]/ul/li[5]/a | //*[@id="page-home"]/footer/div/div[3]/p/a | //*[@id="page-home"]/footer/div/div[3]/ul/li[1]/a | //*[@id="page-home"]/footer/div/div[3]/ul/li[2]/a | //*[@id="page-home"]/footer/div/div[3]/ul/li[3]/a | //*[@id="page-home"]/footer/div/div[3]/ul/li[4]/a | //*[@id="page-home"]/footer/div/div[1]/div | //*[@id="page-home"]/footer/div/nav/div[1]/div[1]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[2]/a | //*[@id="page-home"]/footer/div/nav/div[1]/div[3]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[1]/a | //*[@id="page-home"]/footer/div/nav/div[2]/div[2]/a | //*[@id="page-home"]/footer/div/div[2]/div[1]/div[2]/a | //*[@id="page-home"]/footer/div/div[2]/div[2]/div/a')

elements_list = []
for element in elements:
    text = element.text.strip()
    if text:
        elements_list.append(text)      

for element in elements:
    original_text = element.text
    if len(original_text) > 0:
        translated_text = translate_text(original_text)        
    else:
        translated_text = original_text
    try:
        # Update the element on the page with the translated text
        driver.execute_script("arguments[0].textContent = arguments[1];", element, translated_text)
    except:
        print(f"Error updating header {element.text}")

# write changes to a new html file
time.sleep(2)
new_html = driver.page_source
with open('new_html.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Close the Chrome driver
driver.quit()