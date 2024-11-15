from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Define function to interact with model viewer page
def automate_model_export(start_id, end_id):
    # Set up WebDriver (Chrome in this case)
    driver = webdriver.Chrome()
    champ_id = 1000
    # Navigate to the model viewer page with the current ID
    url = f"https://modelviewer.lol/model-viewer?id={champ_id}"
    driver.get(url)
    time.sleep(6)  # Wait for page to load (adjust as necessary)

    # Locate and click "Watermark" checkbox if it exists
    #watermark_checkbox = driver.find_element(By.ID, "toggle-watermark")
    #watermark_checkbox.click()
    #
    ## Locate and click "Shadows" checkbox if it exists
    #shadows_checkbox = driver.find_element(By.ID, "toggle-shadows")
    #shadows_checkbox.click()
    export_dropdown = driver.find_element(By.ID, "radix-:r11:")
    export_dropdown.click()
    time.sleep(2)
    # Find and click the "Export .png" button
    export_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Export .png')]")
    export_button.click()
    # Pause to ensure the export completes
    time.sleep(6)

    # Close the WebDriver
    driver.quit()

# Run the automation
start_id = 1000  # Starting ID
end_id = 150000    # Ending ID (adjust as needed)

if __name__ == "__main__":
    automate_model_export(start_id, end_id)
