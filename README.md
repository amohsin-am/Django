🍕 User Management System (Django Project)

📌 Project Title
**User Management System**

---

📝 Description
This project is a **Django-based User Management System** that provides a complete platform for handling user data.  
It supports user authentication, profile creation, product management, and admin functionalities.  
The system is designed with scalability in mind and makes use of Django’s built-in features, along with additional packages.

---

⚙️ Installation / Setup Instructions

1️⃣ Prerequisites
Before running this project, ensure you have the following installed:
- **Python 3.9+**
- **Django**
- **MySQL** (with a locally deployed database and credentials)
- **pip** (Python package manager)

2️⃣ Required Packages
Install the necessary dependencies by running:

```bash
pip install -r requirements.txt

3️⃣ Database Setup
Configure your MySQL database in settings.py with correct credentials.

Run migrations:

4️⃣ Create Superuser (Admin)
 - Configure your MySQL database in settings.py with correct credentials.
 - Run migrations:
     python manage.py migrate

5️⃣ Run the Server
 - python manage.py runserver

🚀 Usage

The system provides the following pages and functionalities:

🏠 Home Page – Welcome page with navigation.

📞 Contact Page – Contact form and details.

📝 User Form Page – Add user information (name, age, city, hobbies, favorite food).

📋 User Info List Page – View all user entries.

✏️ User Update Page – Update existing user information.

❌ User Delete – Remove a user entry.

🛒 Products Page – Display products (only available products are listed).

🔑 Login / Logout – Secure authentication system.

🛠 Admin Panel – Full-featured Django admin panel for adding/editing users and products.

🌟 Features

✅ User Authentication (Login, Register, Logout)

✅ User Profile Management

✅ Admin panel with user/product management

✅ CRUD operations on user data

✅ Product availability management

✅ Secure CSRF protection enabled

✅ Media support (upload images like Welcome.png)

👨‍💻 Contribution

This project is a collaborative learning effort. Contributions from:

  - Abhay Barthwal
  - GitHub
  - Google
  - ChatGPT
  - Gemini

📄 License

This project is open-source and available under the MIT License.
