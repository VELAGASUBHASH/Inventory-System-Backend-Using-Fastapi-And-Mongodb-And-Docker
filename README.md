# Inventory System Backend

Backend API for the Inventory Management System built using FastAPI, MongoDB, Motor, Docker, and Cloudinary.

## Live Backend

https://inventory-system-backend-using-fastapi.onrender.com

## Swagger API Docs

https://inventory-system-backend-using-fastapi.onrender.com/docs

---

# Tech Stack

- FastAPI
- MongoDB Atlas
- Motor (Async MongoDB Driver)
- Cloudinary
- Docker
- Render

---

# Features

- Add Product
- Get All Products
- Get Product By ID
- Update Product
- Delete Product
- Search Products
- Filter Products By Category
- Low Stock Alert API
- Product Image Upload
- Async APIs using Motor
- Dockerized Backend
- Render Deployment

---

# Project Structure

```bash
app/
│
├── main.py
├── db.py
│
├── routes/
│   └── product_routes.py
│
├── schemas/
│   └── product_schema.py
│
└── utils/
    ├── helpers.py
    └── cloudinary_config.py
```

---

# Environment Variables

Create `.env` file:

```env
MONGO_URL=your_mongodb_url

CLOUD_NAME=your_cloudinary_name
API_KEY=your_cloudinary_api_key
API_SECRET=your_cloudinary_secret
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/VELAGASUBHASH/Inventory-System-Backend-Using-Fastapi-And-Mongodb-And-Docker.git
```

## Move to Project Folder

```bash
cd Inventory-System-Backend-Using-Fastapi-And-Mongodb-And-Docker
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /add | Add Product |
| GET | /all | Get All Products |
| GET | /search?search=mac | Search Products |
| GET | /low-stock | Low Stock Products |
| GET | /category/{category} | Get Products By Category |
| GET | /{id} | Get Product By ID |
| PUT | /{id} | Update Product |
| DELETE | /{id} | Delete Product |
| POST | /upload-image | Upload Product Image |

---

# Docker Setup

## Build Docker Image

```bash
docker build -t inventory-api .
```

## Run Docker Container

```bash
docker run --env-file .env -p 8000:8000 inventory-api
```

---

# Dockerized API URL

```bash
http://localhost:8000/docs
```

---

# Deployment

Backend deployed on Render.

## Deployment Platform

- Render

## Database

- MongoDB Atlas

## Image Hosting

- Cloudinary

---

# Frontend Repository

https://github.com/VELAGASUBHASH/Inventory-System-Frontend-Using-React

---

# Author

Subhash Velaga
