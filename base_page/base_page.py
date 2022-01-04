from selenium import webdriver
from pages.Registr_Login import Registration, Login

class Application:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.registration = Registration(self.driver)
		self.login = Login(self.driver)

	def quit(self):
		return self.driver.quit()

	def registr_user(self):
		self.registration.open()
		self.registration.registration_btn1.click()
		self.registration.registration_btn2.click()
		self.registration.first_name_input.send_keys('Петро')
		self.registration.last_name_input.send_keys('Міляков')
		self.registration.number_input.send_keys('+380982545256')
		self.registration.email_input.send_keys('peter@getnada.com')
		self.registration.password_input.send_keys('Qwer1234')
		self.registration.condition_checkbox.click()
		self.registration.confirm_button.click()

	def login_user(self):
		self.login.open()
		self.login.Login_btn_1.click()
		self.login.Login_btn_2.click()
		self.login.Email_aut.send_keys("sichkarenko96@gmail.com")
		self.login.Password_input.send_keys("123Qwe123")
		self.login.Login_conform_btn.click()
		self.login.asrt.click()

	def registr_invalid(self):
		self.registration.open()
		self.registration.registration_btn1.click()
		self.registration.registration_btn2.click()
		self.registration.first_name_input.send_keys('qwer')
		self.registration.last_name_input.send_keys('Міляков')
		self.registration.number_input.send_keys()
		self.registration.email_input.send_keys('peter@getnada.com')
		self.registration.password_input.send_keys('Qwer1234')
		self.registration.condition_checkbox.click()
		self.registration.confirm_button.click()
		assert "Обов'язкове поле" == self.registration.number_text

	def login_invalid_user(self):
		self.login.open()
		self.login.Login_btn_1.click()
		self.login.Login_btn_2.click()
		self.login.Email_aut.send_keys("sichkarenko966@gmail.com")
		self.login.Password_input.send_keys("123Qwe123")
		self.login.Login_conform_btn.click()
		#assert "Неправильний логин або пароль" in self.login.email_text