from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

with open('albums_scraping_pagin1.csv', 'w') as file:
    file.write('Band; Year; Style; Ratings; Votes \n')

PATH = "/Users/sammas/Desktop/pjatkk/sem2/PAD/LAB7/Selenium/chromedriver"
s = Service(PATH)
chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=s, options=chr_options)

base_url = "https://metalstorm.net/bands/albums.php?a_sortby=&a_where=&a_what=&page="
for page_number in range(1, 773):
    target_url = base_url + str(page_number)
    driver.get(target_url)
    sections = driver.find_elements(By.XPATH,'//div[@class="cbox"]/table[@class="table table-striped"]/tbody/tr')
    with open('albums_scraping_pagin1.csv', 'a') as file:
        for section in sections:
            band = section.find_element(By.XPATH,'./td[3]').text
            year = section.find_element(By.XPATH,'./td[4]').text
            style = section.find_element(By.XPATH,'./td[6]').text
            ratings = section.find_element(By.XPATH,'./td[7]').text
            votes = section.find_element(By.XPATH,'./td[8]').text
            file.write(band + ';' + year + ';' +
                        style + ';' + ratings + ';' + votes + '\n')
