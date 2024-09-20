from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def kullanici_giris(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(10)

        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Şimdi Değil')]").click()
            time.sleep(5)
        except:
            pass

        try:
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Şimdi Değil')]").click()
            time.sleep(5)
        except:
            pass

    def takipci_al(self, target_username):
        self.driver.get(f"https://www.instagram.com/{target_username}/")
        time.sleep(5)

        takipciler_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
        takipciler_link.click()
        time.sleep(5)

        print("kaydırıyorum")
        
        overflow_div = self.driver.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
        
        while (int(self.driver.execute_script("return arguments[0].scrollTop;", overflow_div)) + int(self.driver.execute_script("return arguments[0].clientHeight;", overflow_div))) != self.driver.execute_script("return arguments[0].scrollHeight;", overflow_div):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", overflow_div)
            print(self.driver.execute_script("return arguments[0].scrollTop;", overflow_div))
            print(self.driver.execute_script("return arguments[0].scrollHeight;", overflow_div))
            time.sleep(4)
        
        print("kaydırdım")
        time.sleep(5)
        
        takipciler = self.driver.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 >div >div").find_elements(By.CSS_SELECTOR, "a")
        
        followerUrls = set()
        for takipci in takipciler:
            followerUrls.add(takipci.get_attribute("href"))
        
        followerUrls = list(followerUrls)  # Set'i listeye dönüştür
        print("Takipçiler: " + str(len(followerUrls)) + " kişi")
        
        for x in followerUrls:
            print(x)
        
        #Excel
        df = pd.DataFrame(followerUrls, columns=["Follower URL"])
        df.to_excel("followers.xlsx", index=False)
        print("Takipçiler Excel dosyasına yazıldı.")

    def cikis(self):
        self.driver.quit()


if __name__ == "__main__":
    username = input("Instagram kullanıcı adınızı girin: ")
    password = input("Instagram şifrenizi girin: ")
    target_username = input("Takipçilerini çekmek istediğiniz hesabın kullanıcı adını girin: ")

    instagram = Instagram(username, password)
    instagram.kullanici_giris()
    instagram.takipci_al(target_username)
    instagram.cikis()
