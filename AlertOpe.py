#ポップアップアラート処理のための例外処理
#納品日が同日の商品の入力など、入力間違いを確認するためのランダムなアラーを処理
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

＃ポップアップアラートが表示された時の処理
try:
	#セーブの段階でアラートが表示されることがあるため例外処理を行う
	save = browser.find_element_by_xpath('xパス')
	save.click()
	Alert(browser).accept()
	print("アラートが表示され、許可しました")
	#ページを遷移させる
	back_page = browser.find_element_by_link_text('aリンクのテキスト')
	back_page.click()
	#ページが読み込まれるまで待機
	wait.until(ec.presence_of_all_elements_located)

#ポップアップアラートが表示されない時の処理
except NoAlertPresentException:
	#ページを遷移させる
	back_page = browser.find_element_by_link_text('aリンクのテキスト')
	back_page.click()
	#ページが読み込まれるまで待機
	wait.until(ec.presence_of_all_elements_located)