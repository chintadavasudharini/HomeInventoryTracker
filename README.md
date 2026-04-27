# 🏠 Home Inventory Tracker
Python Flask Render License

A production-ready Flask web application that enables users to securely manage and track household inventory through an intuitive, interactive dashboard.

🔗 **Live Demo**: [https://homeinventorytracker-t7if.onrender.com/](https://homeinventorytracker-t7if.onrender.com/)

🔗 **Source Code**: [https://github.com/chintadavasudharini/HomeInventoryTracker](https://github.com/chintadavasudharini/HomeInventoryTracker)

## ✨ Overview
Home Inventory Tracker is designed to solve a common real-world problem: organizing and maintaining household items efficiently. It provides authenticated user access, structured inventory management, and a responsive interface for seamless interaction.

This project demonstrates full-stack development fundamentals, including authentication, session management, CRUD operations, and deployment.

## 🚀 Key Features

### 🔐 Authentication & Security
*   Session-based user authentication
*   Protected routes using decorators
*   Controlled access to user-specific data

### 📦 Inventory Management
*   Create, update, and delete items
*   Structured data handling (name, condition, date, location)
*   Real-time dashboard updates

### 🔍 Search & Filtering
*   Multi-field search (name, date, condition, location)
*   Dynamic filtering for better usability

### 💬 User Experience
*   Flash messaging system for feedback
*   Clean and responsive UI
*   Inline editing for faster interactions

### ☁️ Deployment
*   Fully deployed on Render
*   Production-ready configuration using Gunicorn

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python, Flask |
| **Deployment** | Render |
| **Versioning** | Git, GitHub |

## 📂 Project Structure
```text
HomeInventoryTracker/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies
│
├── templates/             # HTML templates (Jinja2)
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/                # Static assets (CSS/JS)
│
└── README.md
```

## ⚙️ Getting Started

### Prerequisites
*   Python 3.x
*   pip

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/chintadavasudharini/HomeInventoryTracker.git
    cd HomeInventoryTracker
    ```

2.  **Create virtual environment**:
    ```bash
    python -m venv venv
    ```

3.  **Activate**:
    *   **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    *   **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application**:
    ```bash
    python app.py
    ```

6.  **Open in browser**:
    `http://127.0.0.1:5000/`

## 🌐 Deployment (Render)
This application is deployed using Render with the following configuration:

*   **Build Command**: `pip install -r requirements.txt`
*   **Start Command**: `gunicorn app:app`

## 🧠 Design Decisions
*   **Session-based Authentication**: Lightweight and suitable for small-to-medium scale apps.
*   **In-Memory Storage**: Chosen for simplicity and rapid prototyping (no DB dependency).
*   **Modular Route Design**: Clear separation of concerns using Flask routing.
*   **Jinja2 Templating**: Enables dynamic rendering of inventory data.

## ⚠️ Current Limitations
*   Data is stored in-memory (not persistent)
*   Passwords are not hashed
*   No database integration
*   Limited scalability in current architecture

## 🔮 Future Enhancements

### 🔐 Security
*   Password hashing using `werkzeug.security`
*   CSRF protection
*   Role-based access control (Admin/User)

### 🗄️ Data Layer
*   Integration with MySQL / MongoDB
*   Persistent storage
*   ORM integration (SQLAlchemy)

### 📊 Features
*   Inventory analytics dashboard
*   Export to PDF/CSV
*   Item categorization & tagging

### ☁️ Cloud & DevOps
*   AWS deployment (EC2 / S3 / RDS)
*   Docker containerization
*   CI/CD pipeline integration

### 📱 UX Improvements
*   Fully responsive mobile design
*   Improved UI/UX with modern frameworks

## 🤝 Contributing
Contributions are welcome.
1.  Fork the repository
2.  Create a feature branch
3.  Commit your changes
4.  Submit a pull request

## 📜 License
This project is licensed under the MIT License.

## 👩‍💻 Author
**Chintada Vasudharini**
🔗 **GitHub**: [https://github.com/chintadavasudharini](https://github.com/chintadavasudharini)

## ⭐ Acknowledgment
If you found this project useful, consider giving it a ⭐ — it helps others discover it.
