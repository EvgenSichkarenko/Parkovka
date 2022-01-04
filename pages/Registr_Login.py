from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Registration():
	def __init__(self, driver):
		self.driver = driver

	def open(self):
		return self.driver.get("https://staging.parkovki.com.ua/")

	@property
	def registration_btn1(self):
		return self.driver.find_element(By.CSS_SELECTOR, "#root .sc-kfYoZR.cJcgyR")

	@property
	def registration_btn2(self):
		return self.driver.find_element(By.CSS_SELECTOR, ".sc-kfYoZR.fXPAJs")

	@property
	def first_name_input(self):
		first_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='name']")
		first_name.clear()
		return first_name

	@property
	def last_name_input(self):
		last_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='surname']")
		last_name.clear()
		return last_name

	@property
	def number_input(self):
		number = self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
		number.clear()
		return number

	@property
	def number_text(self):
		return self.driver.find_element(By.CSS_SELECTOR, "label[for='phone'] > p.sc-dIvrsQ.kPMqOL").get_attribute("textContent")

	@property
	def email_input(self):
		email = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
		email.clear()
		return email

	@property
	def password_input(self):
		password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
		password.clear()
		return password

	@property
	def condition_checkbox(self):
		return self.driver.find_element(By.CSS_SELECTOR, "input[name='checkbox']")

	@property
	def confirm_button(self):
		return self.driver.find_element(By.XPATH, "//form//button[text()='Підтвердити телефон']")

	def number_attr(self):
		return self.driver.find_element(By.CSS_SELECTOR, "div.sc-dlnjwi.dJXsSm > p.sc-crzoAE.DykGo").get_attribute("textContent")

class Login():
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 5)

	def open(self):
		return self.driver.get('https://staging.parkovki.com.ua/')

	@property
	def Login_btn_1(self):
		return self.driver.find_element(By.CSS_SELECTOR, "#root .sc-kfYoZR.cJcgyR")

	@property
	def Login_btn_2(self):
		return self.driver.find_element(By.CSS_SELECTOR, ".sc-kfYoZR.fwQFNn")

	@property
	def Email_aut(self):
		email_input =  self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
		email_input.clear()
		return email_input

	@property
	def email_text(self):
		email_text = self.driver.find_element(By.CSS_SELECTOR, "label[for='email'] p").get_attribute("textContext")
		return email_text

	@property
	def Password_input(self):
		passwd_inp = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
		passwd_inp.clear()
		return passwd_inp

	@property
	def Login_conform_btn(self):
		btn_log3 = self.driver.find_element(By.CSS_SELECTOR, "div.sc-dlnjwi.dJXsSm button:nth-of-type(1)")
		return btn_log3

	@property
	def asrt(self):
		#actual_result = self.driver.find_element(By.CSS_SELECTOR, "div.sc-bCwfaz.hzzSzX.sc-iwajpm.kydRHc")
		#return self.wait.until(lambda  x: x.find_element(By.CSS_SELECTOR, "div.sc-bCwfaz.hzzSzX.sc-iwajpm.kydRHc"))
		return self.wait.until(EC.presence_of_element_located( "div.sc-bCwfaz.hzzSzX"))
