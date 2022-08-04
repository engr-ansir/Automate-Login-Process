from selenium import webdriver

def get_drvier():
  options = webdriver.ChromeOptions()

  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

driver = get_drvier()
element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
print(element.text)
