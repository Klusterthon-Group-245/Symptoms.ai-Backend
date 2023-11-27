# Symptoms.ai

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
    - [1. Signup API](#1-signup-api)
    - [2. Login API](#2-login-api)
    - [3. Reset Password API](#3-reset-password-api)
    - [4. GPT-3 Chatbot API](#4-gpt-3-chatbot-api)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Klusterthon-Group-245/Symptoms.ai-Backend.git
   cd Klusterthon-Group-245
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoints

#### 1. **Signup API**

- **Endpoint:** `/signup/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
    }
  ```
- **Response:**
  ```json
  {
    "message": "User created and logged in successfully",
    "data": {
      "id": 1,
      "email": "user@example.com"
    }
  }
  ```

#### 2. **Login API**

- **Endpoint:** `/login/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Login successful",
    "data": {
      "id": 1,
      "email": "user@example.com"
    }
  }
  ```

#### 3. **Reset Password API**

- **Endpoint:** `/reset-password/<int:user_id>/`
- **Method:** `POST`
- **URL Parameters:**
  - `user_id`: ID of the user to reset the password.
- **Request Body:**
  ```json
  {
    "new_password": "new_password123",
    "confirm_password": "new_password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Password reset successfully",
    "data": {
      "id": 1,
      "email": "user@example.com"
    }
  }
  ```

#### 4. **GPT-3 Chatbot API**

- **Endpoint:** `/api/gpt3-api/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user_input": "Describe your symptoms or ask a question"
  }
  ```
- **Response:**
  ```json
  {
    "response": "Chatbot response based on user input"
  }
  ```
