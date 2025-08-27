# BAC

## Introduction

BAC is a full-stack Python application designed to provide interactive dashboards for educational use, allowing users to interact with data and visualizations through a modern web interface.

---

## ✨ Features

- **Dashboard & Visualization**

  - Interactive dashboard for users to view and manage data.
  - Dynamic charts and statistics (customizable in `dashboard.py`).

- **User Authentication**

  - Secure login system for users.
  - User management and session handling.

- **Forms & Data Entry**

  - Custom forms for user input using Flask-WTF (`flaskforms.py`).
  - Validation and error handling.

- **Responsive Frontend**
  - Modern, mobile-friendly UI using HTML, CSS, and JavaScript.
  - Organized templates for easy navigation and usability.

---

## 🛠️ Tech Stack

- **Backend**

  - **Python 3.x**
  - **Flask**: Lightweight web framework for routing, request handling, and session management.
  - **WTForms**: For building and validating web forms.
  - **(Optional) SQLAlchemy**: For database models if needed.

- **Frontend**

  - **HTML5**: Structure of web pages.
  - **CSS3**: Styling and responsive design (custom stylesheets in `static/`).
  - **JavaScript**: Client-side interactivity (custom scripts in `static/`).

- **Templates**
  - **Jinja2**: Flask’s templating engine for dynamic HTML rendering.

## 📝 Project Structure

```
BAC/
  flaskforms.py      # Web forms
  models.py          # Database models
  routes/            # Route handlers
    dashboard.py     # Dashboard logic
    index.py         # Main page logic
  static/            # CSS, JS, images
  templates/         # HTML templates
    dashboard.html   # Dashboard page
    index.html       # Home page
    login.html       # Login page
app.py               # Application entry point
```

---

## How to Run

Follow these steps to set up and run the BAC project:

1. **Install Python**  
   Make sure Python 3.x is installed on your system.

2. **Install dependencies**  
   Open a terminal in the project directory and run:

   ```powershell
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install Flask and Flask-WTF manually:

   ```powershell
   pip install flask flask-wtf
   ```

3. **Run the application**  
   In the project directory, execute:

   ```powershell
   python app.py
   ```

4. **Access the web app**  
   Open your browser and go to:

   ```
   http://localhost:5000
   ```

---
