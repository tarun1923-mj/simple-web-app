

# Simple Web App – Flask, MongoDB & Vercel

A full-stack authentication web application built using **Flask** and **MongoDB Atlas**, deployed on **Vercel** using a **serverless architecture**.

Users can register, log in, and access a protected portfolio page.

---

## 🚀 Live Demo

🔗 https://simple-web-app.vercel.app

---

## 📁 Project Structure

simple-web-app/
│
├── api/
│   └── index.py          # Vercel serverless entry point
│
├── templates/
│   ├── index.html
│   └── portfolio.html
│
├── static/
│   └── style.css
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel configuration
├── README.md             # Project documentation
└── .gitignore

---

## ✨ Features

- User Registration & Login
- Password Hashing using Werkzeug
- MongoDB Atlas integration
- Session-based authentication
- Protected routes
- Environment variable security
- Serverless deployment on Vercel

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB Atlas
- **Authentication:** Werkzeug (password hashing)
- **Frontend:** HTML, CSS
- **Deployment:** Vercel (Serverless Functions)
- **Version Control:** Git & GitHub

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/simple-web-app.git
cd simple-web-app

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Environment Variable

export MONGO_URI="your_mongodb_connection_string"

4️⃣ Run the Application

python3 app.py

Open:

http://127.0.0.1:5000


⸻

🌐 Deployment on Vercel

This project is deployed using Vercel serverless functions.

Key Deployment Notes:
	•	api/index.py acts as the serverless handler
	•	vercel.json routes all traffic to the Flask app
	•	MongoDB credentials are stored securely using Vercel Environment Variables

⸻

🔐 Environment Variables

Variable	Description
MONGO_URI	MongoDB Atlas connection string


⸻

🧠 Learning Outcomes
	•	Flask backend development
	•	MongoDB Atlas integration
	•	Secure authentication handling
	•	Serverless deployment on Vercel
	•	GitHub authentication using Personal Access Tokens
	•	Environment-based configuration management

⸻

📌 Author

Tarun MJ
Full Stack Developer

⸻

