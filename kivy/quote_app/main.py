from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from pathlib import Path
from datetime import datetime
from random import randint, choice

no_repeat = ['a']

Builder.load_file('design.kv')

class LoginScreen(Screen):

    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Signup_Screen'

    def login_success(self, u_n, pword):

        self.u_n = u_n
        self.pword = pword

        with open('user.json') as file:
            users = json.load(file)

            if u_n in users:
                if users[u_n]['password'] == pword:
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'Log_In_Success_Screen'
                else:
                    self.ids.login_wrong.text = 'Incorrect Password!'
            else:
                self.ids.login_wrong.text = 'User does not Exist!'      

class LoginSuccesScreen(Screen):
    
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Login_Screen'

    def quote_display(self, mood):

        self.mood = mood
        
        quote_files = glob.glob("*txt")
        available_moods = [Path(f).stem for f in quote_files]
        
        if mood in available_moods:
            with open(f'{mood}.txt', encoding="utf8") as file:
                quotes = file.readlines()
                
                x = choice(quotes)
                y = no_repeat[0]

                while x == no_repeat[0]:
                    print('loop')
                    x = choice(quotes)
                no_repeat.clear()

                no_repeat.append(x)
                self.ids.quote.text = x
                print(x)
        else:
            self.ids.quote.text = "Please enter a different mood"

class SignUpScreen(Screen):

    def add_user(self, u_n, pword):
        self.u_n = u_n
        self.pword = pword

        with open('user.json') as file:
            users = json.load(file)

            users[u_n] = {'username':u_n, 'password':pword, 'time': datetime.now().strftime('%d-%m-%y-%H-%M-%S')}

        with open('user.json', 'w') as file:
            json.dump(users, file)  

        self.manager.transition.direction = 'left'
        self.manager.current = 'Sign_Up_Screen_Success'

    def log_in(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Login_Screen'

class SignUpSuccess(Screen):

    def log_in(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Login_Screen'

class RootWidget(ScreenManager):
    pass

class QuoteGenerator(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    QuoteGenerator().run()