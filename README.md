# 🏡 Flask Housing API
Flask Housing API is a simple, session-based RESTful API built using Flask, providing a backend system for managing housing listings and user authentication. It supports basic CRUD operations for housing data and uses session management via Flask-Login.

## ✨ Features
👤User Authentication
- Register new users
- Login and session-based authentication
- Logout functionality

🏠 Housing Management
- Add new house records
- Edit/update existing house data
- Delete house records
- View all available houses

🛠 Tech Stack
- Component	Technology
- Language	Python
- Framework	Flask
- ORM	SQLAlchemy
- Auth Management	Flask-Login
- Database	SQLite (default)

## 🧪 API Endpoints
- Method	Endpoint	Description
- POST	/register	Register a new user
- POST	/login	User login
- GET	/logout	User logout
- GET	/houses	List all houses
- POST	/houses	Add a new house
- PUT	/houses/<id>	Edit a house record
- DELETE	/houses/<id>	Delete a house
  
All protected routes require login via session (Flask-Login).

## 🧩 Optional Enhancements
-JWT-based authentication (alternative to sessions)
- Pagination and filtering
- Upload house images
-Swagger/OpenAPI documentation
