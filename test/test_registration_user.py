import unittest
from base_page.base_page import Application
from pages.Registr_Login import Registration

class Registr_Login(unittest.TestCase):

	def test_regisrt_user(self):
		app = Application()
		app.registr_user()
		app.quit()

	def test_login_user(self):
		app = Application()
		app.login_user()
		app.quit()

	def test_invalid_register(self):
		app = Application()
		app.registr_invalid()
		app.quit()

	def test_login_inv_user(self):
		app = Application()
		app.login_invalid_user()
		app.quit()