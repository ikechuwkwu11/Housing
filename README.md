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
| Component      | Technology       |
| -------------- | ---------------- |
| Language       | Python           |
| Web Framework  | Flask            |
| ORM            | SQLAlchemy       |
| Authentication | Flask-Login      |
| Database       | SQLite (default) |


## 🧪 API Endpoints
| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| POST   | `/register` | Register a new user |
| POST   | `/login`    | User login          |
| GET    | `/logout`   | User logout         |


## 🏘️ Housing Routes (Login Required)
| Method | Endpoint       | Description             |
| ------ | -------------- | ----------------------- |
| GET    | `/houses`      | Get all houses          |
| POST   | `/houses`      | Add a new house         |
| PUT    | `/houses/<id>` | Edit a specific house   |
| DELETE | `/houses/<id>` | Delete a specific house |

  
All protected routes require login via session (Flask-Login).

## 🧩 Optional Enhancements
-JWT-based authentication (alternative to sessions)
- Pagination and filtering
- Upload house images
-Swagger/OpenAPI documentation
