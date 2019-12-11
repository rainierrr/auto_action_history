import time
from selenium import webdriver

num = input("学籍番号を入力して下さい：") #学籍番号
pw = input("パスワードを入力して下さい：") #PW
driver = webdriver.Chrome()
driver.implicitly_wait(3) # 要素が見つかるまで10秒待つ設定

#------学籍ポータル-------------------------------
driver.get('https://navi.mars.kanazawa-it.ac.jp/portal/student/')

driver.find_element_by_name("uid").send_keys(num)# 学籍番号入力
driver.find_element_by_name("pw").send_keys(pw) #　PW入力
time.sleep(0.5)

driver.find_element_by_id("StudentLoginBtn").click() #ログインボタンクリック


driver.find_element_by_class_name("crrclmFlow").click() #KITナビのクリック


test = driver.find_element_by_class_name("weekPortfolioBtn") #一週間の行動履歴のボタンをクリック
test.click()
#------一週間の行動履歴-------------------------------

print("今から実験")
time.sleep(10)

driver.switch_to.window(driver.window_handles[-1])

test = driver.find_element_by_xpath('//*[@id="Calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/a/div') #特定の週をクリック（実験用に今は複数取得）
test.click()
#driver.execute_script("document.getElementsByClassName('fc-title')[0].click()")


time.sleep(2)
driver.quit() #ブラウザをすべて閉じる

