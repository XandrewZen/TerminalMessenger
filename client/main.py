from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os
# Load KV files
Builder.load_file(os.path.join(os.path.dirname(__file__), "ui/login.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "ui/register.kv"))
Builder.load_file(os.path.join(os.path.dirname(__file__), "ui/chat.kv"))

# ---Screens---
class LoginScreen(Screen):
    pass
class RegisterScreen(Screen):
    pass
class ChatScreen(Screen):
    pass

#-- ScreenManager--
class MessengerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == '__main__':
    MessengerApp().run() #zarif