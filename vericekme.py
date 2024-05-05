from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver'ı indir ve tarayıcıyı başlat
service = Service("C:/Users/YunusEmreCoskun/Desktop/python/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(
    "https://www.amazon.com.tr/Apple-AirPods-nesil-MagSafe-Kutusu/product-reviews/B0CHXK8YKT/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
)
time.sleep(10)


def yorumlari_al():
    yorumlar = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".a-size-base.review-text.review-text-content")
        )
    )
    return yorumlar


# İlk sayfadaki yorumları al
ilk_yorumlar = yorumlari_al()
for i, yorum in enumerate(ilk_yorumlar):
    if i != 0:
        print("-" * 100)  # Her yorumun başına 100 karakterlik "-" işareti
    print(yorum.text)  # Yorumları göstermek için yazdır

while True:
    try:
        sonraki_buton = driver.find_element(By.CLASS_NAME, "a-last")
        sonraki_buton_link = sonraki_buton.find_element(By.TAG_NAME, "a").get_attribute(
            "href"
        )
        driver.get(sonraki_buton_link)
        yeni_yorumlar = yorumlari_al()
        if yeni_yorumlar:
            print("" * 100)  # Her sayfa arasına 100 karakterlik "" işareti
            for i, yorum in enumerate(yeni_yorumlar):
                if i != 0:
                    print("-" * 100)  # Her yorumun başına 100 karakterlik "-" işareti
                print(yorum.text)  # Yorumları göstermek için yazdır
        else:
            break
    except:
        break

driver.quit()  # Tarayıcıyı kapat