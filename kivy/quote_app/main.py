from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'Signup_Screen'

class SignUpScreen(Screen):
    def add_user(self, u_n, pword):
        self.u_n = u_n
        self.pword = pword

        with open('user.json') as file:
            users = json.load(file)

            users[u_n] = {'username':u_n, 'password':pword, 'time': datetime.now().strftime('%d-%m-%y-%H-%M-%S')}

        with open('user.json', 'w') as file:
            json.dump(users, file)        

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()