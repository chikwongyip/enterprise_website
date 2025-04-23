# Enterprise Website

This is an enterprise website built with NiceGUI for the frontend, FastAPI for the backend, and MySQL as the database.

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up MySQL database and update `backend/database.py` with your database credentials
4. Run the backend: `cd backend && python main.py`
5. Run the frontend: `cd frontend && python main.py`

## Features

- Frontend:

  - Homepage
  - News display
  - Product list
  - Product details
  - Attachment downloads
  - About us page

- Backend:
  - User login
  - Add, delete, and modify news
  - Add, modify, and delete products
  - Upload product images and attachments

## API Endpoints

- `/api/news`: GET, POST, PUT, DELETE
- `/api/products`: GET, POST, PUT, DELETE
- `/api/products/{product_id}`: GET, PUT, DELETE
