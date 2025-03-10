import psutil
import os
os.system("pkill -9 chrome")  # Forcefully kill all Chrome processes
def kill_chrome():
    for process in psutil.process_iter(attrs=["pid", "name"]):
        if "chrome" in process.info["name"].lower():
            try:
                p = psutil.Process(process.info["pid"])
                p.terminate()  # Terminate gracefully
            except psutil.NoSuchProcess:
                pass  # Process already closed

kill_chrome()

#requiredlib = [selenium,time]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
#import tempfile
#import uuid

'''
os.environ["MOZ_LOG"] = "debug"  # Enable verbose logging
# Initialize WebDriver
options = Options()
service = Service(excecutable_path="/usr/local/bin/geckodriver")
options.binary_location = '/usr/bin/firefox'
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, service=service)
'''
# Chrome Options
options = Options()
options.add_argument("--headless=new")  # Use new headless mode
options.add_argument("window-size=1920x1080")  # Ensure full viewport
options.add_argument("--disable-gpu")  # Fix rendering issues in headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
#temp_dir = f"/tmp/chrome-user-data-{uuid.uuid4()}"
#options.add_argument(f"--user-data-dir={temp_dir}")

# Bypass detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--enable-javascript")
options.add_argument("--disable-web-security")
service = Service("/usr/local/bin/chromedriver")  # Path to ChromeDriver
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=IsolateOrigins,site-per-process")
options.add_argument("--disable-extensions")

# Initialize WebDriver
driver = webdriver.Chrome(options=options,service=service) 
driver.get("https://accounts.seedloaf.com/sign-in")
#driver.maximize_window()

# Wait for page to fully load
WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

usernamesec = os.getenv("USERNAME")
passwordsec = os.getenv("PASSWORD")

try:
    # Wait for the username field to be visible
    username = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "identifier-field"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", username)
    driver.execute_script("arguments[0].click();", username)
    username.send_keys(usernamesec)
    username.send_keys(Keys.RETURN)
    
    # Optional: Wait to observe behavior (debugging)
    time.sleep(5)
    print("entered username")
except Exception as e:
    print(f"Error occurred(username): {e}")
#---------------------------
try:
    # Wait for the password field to be visible
    password = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password-field"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", password)
    driver.execute_script("arguments[0].click();", password)
    password.send_keys(passwordsec)
    password.send_keys(Keys.RETURN)
    # Optional: Wait to observe behavior (debugging)
    time.sleep(8)
    print("entered password")
except Exception as e:
    print(f"Error occurred(password): {e}")
#---------------------------
try:
    # Wait for the start button to be visible
    wait = WebDriverWait(driver, 30)
    # Ensure the button is visible
    #startworld = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'btn-primary')]")))
    startworld = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    
    # Now ensure it’s clickable
    startworld = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
    driver.execute_script("arguments[0].scrollIntoView(true);", startworld)
    driver.execute_script("arguments[0].click();", startworld)
    print("Clicked start")
    time.sleep(2)

except Exception as e:
    print(f"Error occurred(start): {e}")

#---------------------------
try:
    # Wait for the alert div to appear
    alert_div = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='alert']/div[2]"))
    )
    
    # Extract the text
    alert_text = alert_div.text
    print(f"{alert_text}")

except Exception as e:
    print(f"Error while fetching alert text: {e}")

#---------------------------
# Handle alert if present
try:
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    alert.accept()  # Accept the alert
except Exception:
    print("No alert found.")
    
# Check browser logs to see if any errors are happening
for entry in driver.get_log('browser'):
    print(entry)

driver.quit()
