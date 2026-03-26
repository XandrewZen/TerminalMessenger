# **Instructions for Gemini.md**

## **Project Plan: Terminal Messenger App (Python + Kivy + Socket)**

### **Goal**

Build a terminal-themed messenger app for Android using Python and Kivy with socket programming.
We will develop it **part by part, little by little**, starting with **UI**, then **socket communication**, and later optional features like encryption or extra UI tweaks.

---

## **Step-by-Step Plan**

### **Part 1: UI (User Interface)**

* Create **screens first**; no backend yet.
* Screens to implement:

  1. **SplashScreen** – loading animation, app logo
  2. **LoginScreen** – username & password fields, buttons
  3. **RegisterScreen** – username, email, password, confirm password
  4. **OTPScreen** – OTP / security code input, resend option
  5. **ChatScreen** – chat area (empty for now), message input
  6. **ContactsScreen** – list of contacts (empty list)
  7. **ProfileScreen** – display user info, edit option
  8. **SettingsScreen** – theme switch, notifications, logout
* Make **terminal-style theme**: dark background, monospaced font, green/white text.
* **Files to create**:

  * Python screen classes: `screens/*.py`
  * KV layout files: `kv/*.kv`
* Test UI on **PC first**, then **Android** using Kivy.

---

### **Part 2: Socket Programming**

* Implement server-client communication.
* **Server**:

  * `server/server.py` – handle multiple clients
  * `server/utils.py` – helper functions
* **Client**:

  * `client/client.py` – connects to server
  * `client/network.py` – send/receive messages
* Test **basic messaging** first:

  * Can send plain text messages between multiple clients.

---

### **Part 3: Security / Authentication**

* Implement optional features:

  * OTP verification (simulated for testing)
  * Password hashing / encryption
  * Optional message encryption for chat

---

### **Part 4: Extra Features / Improvements**

* Add profile picture upload (optional)
* Add emojis or ASCII art in chat
* Add theme switch (light/terminal dark)
* Expand contacts screen with search/add/delete
* Polish UI and transitions

---

### **General Rules**

1. Work **small part at a time**. Don’t try to do all screens at once.
2. Test **UI first**, then backend sockets.
3. Keep **terminal theme consistent**.
4. Document **each step in Gemini.md**:

   * What you did
   * What works
   * What didn’t work
   * Next step




