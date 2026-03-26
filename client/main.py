from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import os

# Load KV files
ui_path = os.path.join(os.path.dirname(__file__), "ui")
Builder.load_file(os.path.join(ui_path, "styles.kv"))
Builder.load_file(os.path.join(ui_path, "login.kv"))
Builder.load_file(os.path.join(ui_path, "register.kv"))
Builder.load_file(os.path.join(ui_path, "chat.kv"))
Builder.load_file(os.path.join(ui_path, "inbox.kv"))

# ---Screens---
class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class ChatScreen(Screen):
    chat_with = StringProperty("SYSTEM")

    def send_message(self):
        msg = self.ids.message_input.text
        if msg:
            self.ids.chat_logs.text += f"[b]You:[/b] {msg}\n"
            self.ids.message_input.text = ""
            self.ids.scroller.scroll_y = 0

class InboxScreen(Screen):
    def open_chat(self, username):
        self.manager.get_screen('chat').chat_with = username
        self.manager.current = 'chat'

#-- ScreenManager--
class MessengerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(InboxScreen(name='inbox'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == '__main__':
    MessengerApp().run() #zarif
