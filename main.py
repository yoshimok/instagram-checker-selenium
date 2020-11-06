from selenium import webdriver
import chromedriver_binary
from time import sleep
import settings # environments

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

heart_passive = "M34.6 6.1c5.7 0 10.4 5.2 10.4 11.5 0 6.8-5.9 11-11.5 16S25 41.3 24 41.9c-1.1-.7-4.7-4-9.5-8.3-5.7-5-11.5-9.2-11.5-16C3 11.3 7.7 6.1 13.4 6.1c4.2 0 6.5 2 8.1 4.3 1.9 2.6 2.2 3.9 2.5 3.9.3 0 .6-1.3 2.5-3.9 1.6-2.3 3.9-4.3 8.1-4.3m0-3c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5.6 0 1.1-.2 1.6-.5 1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z"
heart_active = "M34.6 3.1c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5s1.1-.2 1.6-.5c1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z"

# 環境変数の取得
# load_dotenv(verbose=True)
# 
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

print('connectiong to remote browser...')
driver = webdriver.Chrome(options=options)

user_name = settings.USN
user_pass = settings.PWD

# instagramにアクセス
driver.get('https://www.instagram.com/')
sleep(1)

# ユーザー情報を入力
driver.find_element_by_name("username").send_keys(user_name)
driver.find_element_by_name("password").send_keys(user_pass)

# instagramにログイン
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(5)

# 山下七海さんのアカウントページへ飛ぶ
driver.get('https://www.instagram.com/aishite773/')
sleep(1)

# 投稿内容をクリック
driver.find_element_by_xpath("//img[@style='object-fit: cover;']").find_element_by_xpath("..").find_element_by_xpath("..").click()
sleep(2)

for i in range(10):  # 投稿件数を決める

  while True:
    sleep(2)
    try:
      driver.find_element_by_xpath("//button/div[@class='    coreSpriteRightChevron  ']").click()
    except:
      break
  
  sleep(1)
  try:
    section = driver.find_elements_by_xpath("//section[1]/span/button/div/span//*[name()='svg']//*[name()='path'][@d='%s']" % heart_active)
    if (len(section) < 1 ): print("いいね")
  except:
    break
  sleep(1)
  driver.find_element_by_xpath("//a[contains(text(), '次へ')]").click()  

# ブラウザを終了 お疲れselenium!!
driver.quit()
