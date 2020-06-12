from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'Signup_Screen'

class SignUpScreen(Screen):
    def add_user(self, f_n, l_n):
        self.f_n = f_n
        self.l_n = l_n

        print("first name is {a}".format(a = f_n))
        print("last name is {a}".format(a = l_n))      
        

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()