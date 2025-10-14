🏍 Motorcycle Shop POS System (Offline Desktop Version)

A Point of Sale (POS) system for motorcycle shops and parts businesses.
It features inventory management, sales processing, user authentication, and reporting — all running offline using Flask (Python) as the backend and React (Vite) as the frontend.

🚀 Features
👤 User Roles

Admin

Manage users (add/edit/remove cashiers)

Manage motorcycle parts inventory

View and generate sales reports

Cashier

Log in securely

Process customer transactions

Print or save receipts

View their sales history

🧱 System Components
🐍 Backend (Flask)

REST API built with Flask

SQLite database (pos.db) — offline storage

Flask-CORS for frontend connection

Flask-Session for user sessions

Secure password hashing

⚛️ Frontend (React + Vite)

Modern, fast, and lightweight UI built with React

TailwindCSS for styling

Axios for connecting to Flask API

Electron-compatible (can run as desktop app)

📁 Folder Structure
POS-web-system/
│
├── back-end/
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── pos.db
│   ├── create_admin.py
│   └── requirements.txt
│
└── front-end/
    ├── src/
    │   ├── components/
    │   │   ├── Login.jsx
    │   │   ├── Register.jsx
    │   │   ├── Dashboard.jsx
    │   │   └── POS.jsx
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── index.css
    ├── public/
    │   └── index.html
    ├── package.json
    ├── vite.config.js
    └── README.md

⚙️ Installation Guide
🐍 Backend Setup (Flask)

Open a terminal in the back-end folder.

Create a virtual environment and activate it:

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the backend:

python app.py


Runs on http://127.0.0.1:5000

⚛️ Frontend Setup (React + Vite)

Open another terminal in the front-end folder.

Install dependencies:

npm install


Start development server:

npm run dev


Opens on http://localhost:5173

🔑 Creating an Admin Account
cd back-end
python create_admin.py


Then input your username, password, and full name.
Your admin is stored in the SQLite database (pos.db).

🧰 Tech Stack
Layer	Technology
Frontend	React (Vite), Tailwind CSS
Backend	Flask (Python)
Database	SQLite
Authentication	Flask-Session, Werkzeug Security
Communication	REST API (JSON)
🧩 API Endpoints (Samples)
Method	Endpoint	Description
POST	/register	Create new user
POST	/login	Authenticate user
GET	/products	Retrieve all products
POST	/sales	Add new sale
GET	/sales	Fetch sales records
💻 Running as an Offline Desktop App

You can make your POS run as a standalone app without needing a browser.

⚙️ Step 1: Convert Flask Backend to Executable (PyInstaller)

Install PyInstaller:

pip install pyinstaller


Inside the back-end folder, run:

pyinstaller --onefile app.py


The executable will be generated in:

dist/app.exe


Run it:

dist/app.exe


Your Flask backend will start in the background.

🖥 Step 2: Wrap React App in Electron

Inside your front-end folder, install Electron:

npm install --save-dev electron


Create a file named electron.js:

const { app, BrowserWindow } = require("electron");
const path = require("path");

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  win.loadURL("http://127.0.0.1:5173"); // or your built frontend URL
}

app.whenReady().then(createWindow);


Add this to your package.json:

"main": "electron.js",
"scripts": {
  "start": "vite",
  "dev": "vite",
  "build": "vite build",
  "electron": "electron ."
}


Run the app with:

npm run electron


✅ The POS will open in its own desktop window while Flask runs in the background!

🏁 Future Features

Barcode scanner integration

Receipt printing

Offline-to-online data sync

Analytics dashboard for admins

👨‍💻 Developers

Project Title: Motorcycle Shop POS System
Developed by: Cleentson Dewey Lenterna, Jase Karl Zerrudo, Krhisha Marie Cavan / The Think Tank Group 
Course: BS Information Technology
Subject: System Integration and Architecture 1 / System Development Final Project
Instructor: Janett M. Claro,MIT
Year: 2025