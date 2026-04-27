# 🏠 Home Inventory Tracker

A full-stack web application built using Flask that enables users to efficiently manage and track household inventory.
The application provides secure authentication, an interactive dashboard, and real-time CRUD operations for seamless inventory management.

---

## 🌐 Live Demo

🔗 https://homeinventorytracker-t7if.onrender.com/

---

## 🚀 Features

* 🔐 User Registration & Login (Session-based Authentication)
* 🛡️ Protected Routes using Login Decorators
* 📦 Add, Edit, and Delete Inventory Items (CRUD Operations)
* 🔍 Search Functionality (by name, date, condition, location)
* 📊 Dynamic Dashboard with real-time updates
* 💬 Flash Messages for user feedback
* 🚪 Secure Logout System
* 🎨 Clean and Responsive UI

---

## 🛠️ Tech Stack

**Frontend:**

* HTML
* CSS
* JavaScript

**Backend:**

* Python
* Flask

**Deployment:**

* Render (Cloud Platform)

**Tools:**

* Git & GitHub
* VS Code

---

## 📂 Project Structure

```
HomeInventoryTracker/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── (CSS / JS files)
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/chintadavasudharini/HomeInventoryTracker.git
cd HomeInventoryTracker
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment (Render)

This application is deployed on Render.

### Steps:

1. Push code to GitHub
2. Login to Render
3. Create a new **Web Service**
4. Connect your repository
5. Configure:

   * **Build Command:**

     ```
     pip install -r requirements.txt
     ```
   * **Start Command:**

     ```
     gunicorn app:app
     ```

---

## 🔒 Authentication Flow

* Users must register before logging in
* Session is used to maintain login state
* Protected routes require authentication
* Unauthorized users are redirected to login

---

## ⚠️ Limitations

* ❌ Data is stored in-memory (resets on server restart)
* ❌ Passwords are not encrypted
* ❌ No database integration yet

---

## 🔮 Future Enhancements

* 🗄️ Database integration (MySQL / MongoDB)
* 🔐 Password hashing for security
* 📊 Inventory analytics & reports
* 📱 Mobile responsiveness improvements
* ☁️ AWS deployment version
* 🔔 Email notifications & alerts

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit pull requests.

---

## 👩‍💻 Author

**Chintada Vasudharini**
🔗 GitHub: https://github.com/chintadavasudharini

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub!
