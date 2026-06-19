# Decode Labs Backend Projects

This repository contains a series of backend development projects built while learning FastAPI, SQLAlchemy, authentication, and API development concepts.

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* bcrypt
* JWT (JSON Web Tokens)
* Pydantic

---

## Project 1: Server Creation

### Goal

Build a stateless web server that serves data using HTTP routes.

### Features

* FastAPI server setup
* GET routes
* POST routes
* JSON responses
* HTTP status codes

### Concepts Learned

* Client-server architecture
* HTTP methods
* Request and response cycle
* Route creation
* JSON formatting
* Status code handling

### Example Routes

* GET /users
* POST /users

---

## Project 2: Database Integration

### Goal

Connect a FastAPI application to a database and perform CRUD operations.

### Features

* SQLite database integration
* SQLAlchemy ORM setup
* Create operation
* Read operation
* Update operation
* Delete operation
* Email uniqueness validation

### Concepts Learned

* Database engines
* Sessions
* ORM models
* Table creation
* CRUD operations
* Pydantic schemas
* Data validation

### Components

* database.py
* models.py
* schemas.py
* main.py

---

## Project 3: Authentication System

### Goal

Secure API endpoints using password hashing and token-based authentication.

### Features

* User registration
* Password hashing with bcrypt
* User login
* JWT token generation
* Protected routes
* Environment variable configuration

### Authentication Flow

1. User registers with name, email, and password.
2. Password is hashed using bcrypt before storage.
3. User logs in using email and password.
4. JWT token is generated after successful authentication.
5. Token is used to access protected routes.

### Security Features

* bcrypt password hashing
* JWT-based authentication
* Environment variables using .env
* Protected API endpoints

### Concepts Learned

* Authentication
* Authorization
* Password hashing
* JWT creation and verification
* Protected routes
* Secret key management

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Decode_labs
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

---

## Repository Structure

```text
Decode_labs
│
├── Project-1-(Server Creation)
│
├── Project-2-(Database Integration)
│
└── Project-3-(Authentication System)
```

---

## Learning Outcomes

Through these projects, the following backend concepts were implemented and practiced:

* REST API Development
* FastAPI Framework
* Request Validation
* Database Integration
* SQLAlchemy ORM
* Authentication and Authorization
* JWT Token Handling
* Password Security
* Environment Variables
* CRUD Operations
* API Design Principles

* => VIVEK KUMAR

```
```
