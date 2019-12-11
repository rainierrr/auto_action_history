import time
from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
import datetime


#--------------------------------------------------------------------------------------------

#num = input("学籍番号を入力して下さい：") #学籍番号
#pw = input("パスワードを入力して下さい：") #PW
#year = input("自動入力したい週の西暦を入力して下さい：") #学籍番号
#pw = input("自動入力したい週の月を入力して下さい：") #PW
#pw = input("自動入力したい週の日曜日の日付を入力して下さい：") #PW
#pw = input("自動入力は入力済みですか(入力済みではない場合は1、入力済みの場合は0)：") #PW
num = "1916320" #学籍番号
pw = "h110714" #PW
sleep_start = 6 #睡眠時間の最小の値（整数）
sleep_end = 7 #睡眠時間の最大の値（整数）
year = 2019
month = 12
date = 15
entered = 0 # 入力済みか否か 入力済みは0
driver = webdriver.Chrome()
#driver = webdriver.Chrome("chromedriver")


#------------------------------------------------------------------------------------------

def save():
    driver.find_elements_by_class_name("btnBlueExec")[0].click() #登録確認ボタンクリック
    time.sleep(0.5)
    driver.find_elements_by_class_name("btnBlueExec")[0].click() #登録ボタンクリック
    time.sleep(0.5)
    driver.find_elements_by_class_name("btnBlueExec")[0].click() #戻るボタンクリック
    time.sleep(0.5)
    driver.find_elements_by_class_name("btnBlueExec")[2].click() #閉じるボタンクリック
def find_name(name,connent):
    driver.find_element_by_name(name).clear() #もともとの内容を消す
    driver.find_element_by_name(name).send_keys(connent)

def time_select(name):
    if "EXERCISE" in name:
        Select(driver.find_element_by_name(name)).select_by_value("0")  #運動時間
    elif "SLEEP" in name:
        Select(driver.find_element_by_name(name)).select_by_value(str(random.randint(sleep_start,sleep_end))) #睡眠時間
def meel_check(str_time):
    meel_time_name = ["BREAKFAST", "LUNCH", "DINNER"]
    for i in meel_time_name:
        if not driver.find_element_by_name(i + "." + str_time).is_selected(): #チェック入ってない場合のみチェックボックスをクリックする
            driver.find_element_by_name(i + "." + str_time).click()


def close_browse(i):
    time.sleep(i)
    driver.quit()

def get_first_day_of_month(date=None):
    '''指定された日付の月の最初の日を返す'''
    if not date:
        date = datetime.date.today()
    return date.replace(day=1)

def get_last_day_of_prev_month(date=None):
    #指定された日付の前月の最終日を取得する
    if not date:
        date = datetime.date.today()
    first_date = get_first_day_of_month(date)
    return first_date - datetime.timedelta(days=1)

def last_month_weekday(target_date):
    last_weekday = (get_last_day_of_prev_month(target_date)).weekday()
    return last_weekday == 5

def input_connent(target_date):
    sunday_plan = ""
    monday_plan = "NW勉強会 17:00~19:00"
    tuesday_plan = ""
    wednesday_plan = "セキプロ 19:00~21:00"
    thursday_plan = ""
    fryday_plan = "IoAプロジェクト17:00~19:00"
    saturday_plan = ""
    test = "勉強内容\n勉強内容2"
    goal2 = "水曜日までに部屋の片付けをする"
    goal3 = "NWのBGPについて７時間以上勉強する"
    for i in range(7):
        find_name("PRIORITY2", goal2) #目標2の入力
        find_name("PRIORITY3", goal3) #目標3の入力
        Select(driver.find_element_by_name("ACHIEVEMENT2")).select_by_value("4") #目標2の評価
        Select(driver.find_element_by_name("ACHIEVEMENT3")).select_by_value("4") #目標3の評価
        if i == 0:
            str_year = target_date.strftime("%Y")
            str_month = target_date.strftime("%m")
            str_date = target_date.strftime("%d")
        else:
            target_date = target_date + datetime.timedelta(days=1)
            str_year = target_date.strftime("%Y")
            str_month = target_date.strftime("%m")
            str_date = target_date.strftime("%d")
        str_time = str_year + "/"+ str_month + "/" + str_date
        meel_check(str_time)
        time_select("SLEEP_TIME." + str_time)
        time_select("EXERCISE_TIME." + str_time)
        weekday = target_date.weekday()
        if weekday == 6: #日曜日
            find_name("ACTIVITY_CONTENT." + str_time, sunday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯
        elif weekday == 0: #月曜日
            find_name("ABSENCE_LATE." + str_time, "遅刻欠席なし") #欠席・遅刻科目・理由
            find_name("ACTIVITY_CONTENT." + str_time, monday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯
        elif weekday == 1: #火曜日
            find_name("ABSENCE_LATE." + str_time, "遅刻欠席なし") #欠席・遅刻科目・理由
            find_name("ACTIVITY_CONTENT." + str_time, tuesday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯
        elif weekday == 2: #水曜日
            find_name("ABSENCE_LATE." + str_time, "遅刻欠席なし") #欠席・遅刻科目・理由
            find_name("ACTIVITY_CONTENT." + str_time, wednesday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯
        elif weekday == 3: #木曜日
            find_name("ABSENCE_LATE." + str_time, "遅刻欠席なし") #欠席・遅刻科目・理由
            find_name("ACTIVITY_CONTENT." + str_time, thursday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯
        elif weekday == 4: #金曜日
            find_name("ABSENCE_LATE." + str_time, "遅刻欠席なし") #欠席・遅刻科目・理由
            find_name("ACTIVITY_CONTENT." + str_time, fryday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯
        else: #土曜日
            find_name("ACTIVITY_CONTENT." + str_time, saturday_plan) #部活動・利用施設・アルバイトなどの内容・時間帯

        find_name("HOMEWORK_TIME." + str_time, test) #予習・復習・課題・所要時間（分）

def get_nth_week(target_date): #第何週か返す
    return (target_date.day - 1) // 7 + 1









driver.implicitly_wait(5) # 要素が見つかるまで3秒待つ設定

#------学籍ポータル-------------------------------
driver.get('https://navi.mars.kanazawa-it.ac.jp/portal/student/')

driver.find_element_by_name("uid").send_keys(num)# 学籍番号入力
driver.find_element_by_name("pw").send_keys(pw) #　PW入力
time.sleep(0.8)

driver.find_element_by_id("StudentLoginBtn").click() #ログインボタンクリック


driver.find_element_by_class_name("crrclmFlow").click() #KITナビのクリック


test = driver.find_element_by_class_name("weekPortfolioBtn") #一週間の行動履歴のボタンをクリック
test.click()

#------一週間の行動履歴-------------------------------
driver.switch_to.window(driver.window_handles[-1]) #操作する新しいタブに選択
start_time = datetime.date(year, month, date)
diff_month = (datetime.datetime.now()).month - month
if diff_month == 0:
    pass
elif diff_month < 0:
    for i in range(abs(diff_month)):
        driver.find_element_by_xpath("//*[@id='Calendar']/div[1]/div[1]/div/button[2]").click()
else:
    for i in range(abs(diff_month)):
        driver.find_element_by_xpath("//*[@id='Calendar']/div[1]/div[1]/div/button[1]").click()
time.sleep(2)
week_count = get_nth_week(start_time) #第何周か
if last_month_weekday(start_time):
    driver.find_elements_by_class_name("fc-title")[(week_count - 1) * 2].click()#曜日選択
else:
    driver.find_elements_by_class_name("fc-title")[((week_count - 1) * 2) + 2].click()#曜日選択

if entered == 0:
    driver.find_elements_by_class_name("btnBlueExec")[0].click()#編集ボタンクリック

input_connent(start_time)

time.sleep(1000)
#save()
close_browse(1)
