from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import pandas as pd
import time

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver_path = "C:\\Users\\eswanth.kumar\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.ubereats.com/feed?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlNvdXRoJTIwS2Vuc2luZ3RvbiUyMFVuZGVyZ3JvdW5kJTIwTWV0cm8lMjBTdGF0aW9uJTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyNDJjZDhjOWUtODZiYy01YmU4LTZlMGEtMjU2YTEyZjFmMzFmJTIyJTJDJTIycmVmZXJlbmNlVHlwZSUyMiUzQSUyMnViZXJfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E1MS40OTQwODgyJTJDJTIybG9uZ2l0dWRlJTIyJTNBLTAuMTczOTE0OCU3RA%3D%3D"

driver.get(url)

time.sleep(5)

element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/div[5]/li[1]/a[1]/div[1]/div[1]/div[1]")
element.click()
time.sleep(5)

page_source = driver.page_source
# print(page_source)

# print(type(page_source))

with open('page_source.txt', 'w', encoding='utf-8') as file:
    file.write(page_source)
soup = BeautifulSoup(page_source, 'html.parser')

main_tag = soup.find('div', {'data-test': 'feed-desktop'})

data = []
if main_tag:
    # print(main_tag, type(main_tag), len(main_tag))
    for tag in main_tag:
        print(tag)
        store_names = tag.find('h3')
        store_name = store_names.text
        # print(store_name)

        ratings = tag.find('span', class_ = "ag bs bt bu bv bw bx")
        rating =ratings.text
        # print(rating)

        delivery_timing = tag.find('span', class_="bo em bq dw eu er bw bu" )
        delivery_time = delivery_timing.text
        # print(delivery_timing.text)


        data.append({
            'Store Name': store_name,
            'Rating': rating,
            'Delivery Timing': delivery_time
            })
        df = pd.DataFrame(data)
        print(df)

            # Save the DataFrame to an Excel file
        df.to_excel('scraped_data.xlsx', index=False)

        print("Data has been saved to 'scraped_data.xlsx'")
        
else:
    print("Onnum illa")
driver.quit()




