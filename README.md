Perfect! Let’s make a **clean, professional `README.md`** for your messenger project with the **full folder structure, screens, KV files, and class names**, suitable for GitHub. I’ll make it **better structured than before**, so anyone can understand your project at a glance.

---

# **README.md – Terminal Messenger App**

```markdown
# Terminal Messenger App (Python + Kivy + Socket)

## Overview
A **terminal-themed messenger app** built with **Python and Kivy**, designed for **Android**.  
This is a **learning project** to practice **UI design, socket programming, and security/authentication**.  
The app is developed **part by part**, starting with the UI, then sockets, and later extra features.

---

## Features
- Terminal-style chat UI (dark background, monospaced font)
- User login and registration
- OTP / security code verification
- Real-time chat using Python sockets
- Contacts list management
- Profile display and editing
- Theme selection (dark / light)
- Android-ready via Kivy

---

## Project Structure

```

MessengerApp/
│
├─ main.py                  # Entry point of the app
├─ app.kv                   # Main KV file (optional for multiple KV files)
├─ README.md                # Project overview (this file)
├─ requirements.txt         # Dependencies: Kivy, socket, etc.
│
├─ server/
│   ├─ server.py            # Socket server
│   ├─ server_config.py     # Server settings (IP, port, max clients)
│   └─ utils.py             # Server helper functions
│
├─ client/
│   ├─ client.py            # Socket client
│   ├─ network.py           # Network handling
│   ├─ security.py          # Encryption / authentication helpers
│   └─ utils.py             # Client helper functions
│
├─ screens/                 # Kivy screens
│   ├─ **init**.py
│   ├─ splash_screen.py
│   ├─ login_screen.py
│   ├─ register_screen.py
│   ├─ otp_screen.py
│   ├─ chat_screen.py
│   ├─ contacts_screen.py
│   ├─ profile_screen.py
│   └─ settings_screen.py
│
├─ kv/                      # KV layout files for screens
│   ├─ splash_screen.kv
│   ├─ login_screen.kv
│   ├─ register_screen.kv
│   ├─ otp_screen.kv
│   ├─ chat_screen.kv
│   ├─ contacts_screen.kv
│   ├─ profile_screen.kv
│   └─ settings_screen.kv
│
├─ assets/
│   ├─ icons/
│   ├─ fonts/
│   └─ themes/
│       ├─ terminal_dark.kv
│       └─ terminal_light.kv
│
└─ tests/
├─ test_network.py
├─ test_security.py
└─ test_ui.py

````

---

## Screen Classes & KV Files

| Screen           | Python Class             | KV File                 | Description                                      |
|-----------------|------------------------|------------------------|--------------------------------------------------|
| Splash Screen    | `SplashScreen`         | `splash_screen.kv`     | Loading animation, app logo                     |
| Login Screen     | `LoginScreen`          | `login_screen.kv`      | Username & password input, login/register buttons |
| Register Screen  | `RegisterScreen`       | `register_screen.kv`   | Username, email, password, confirm password     |
| OTP Screen       | `OTPScreen`            | `otp_screen.kv`        | Security code / OTP input, resend button        |
| Chat Screen      | `ChatScreen`           | `chat_screen.kv`       | Main chat area, message input, send button      |
| Contacts Screen  | `ContactsScreen`       | `contacts_screen.kv`   | Friend list, add/search contacts                |
| Profile Screen   | `ProfileScreen`        | `profile_screen.kv`    | Display/edit user profile                        |
| Settings Screen  | `SettingsScreen`       | `settings_screen.kv`   | Theme selection, notifications, logout          |

---

## Server & Client Classes

**Server:**
- `ChatServer` – handles multiple client connections  
- `ClientHandler` – handles individual client  

**Client:**
- `ChatClient` – connects to server  
- `MessageManager` – formats and sends/receives messages  
- `SecurityManager` – encrypt/decrypt messages  




