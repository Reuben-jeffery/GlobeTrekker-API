# 🌍 GlobeTrekker API

Welcome to **GlobeTrekker API** — a RESTful web service built with Flask and SQLAlchemy that allows users to explore, manage, and interact with travel destinations across the globe. Perfect for travel apps, destination catalogs, or educational REST API demos.

Tested and debugged using **Postman** for smooth API development and documentation.

---

## ✨ Features

- 🗺️ Create, Read, Update, Delete (CRUD) destinations
- 📦 SQLite database using SQLAlchemy ORM
- 🔎 Filter, search, and sort destinations (planned)
- 📄 JSON-based responses for easy frontend integration
- 🔐 Future upgrades including user authentication and favorites

---

## ⚙️ Tech Stack

| Tech         | Use Case                     |
|--------------|------------------------------|
| Python       | Core programming language    |
| Flask        | Web framework for REST APIs  |
| SQLAlchemy   | ORM for database operations  |
| SQLite       | Lightweight local database   |
| Postman      | API testing and debugging    |

---

## 📂 Folder Structure

```bash
GlobeTrekker-API/
│
├── app.py              # App entry point
├── models.py           # SQLAlchemy database models
├── routes.py           # All route definitions
├── config.py           # App configuration (optional)
├── requirements.txt    # Python dependencies
└── README.md           # This file


🔧 Installation & Setup
Step 1: Clone the Repo

```bash git clone https://github.com/yourusername/GlobeTrekker-API.git ```
```bash cd GlobeTrekker-API ```

Step 2: Create a virtual environment

```bash python3 -m venv api_env ```

Step 3: Install dependencies

bash

```bash pip install -r requirements.txt```

Step 4: Run the app

```bash python app.py ```

Your API will now be running at:

```bash http://localhost:5000 ```

🧪 Testing with 
Open Postman

Create a new collection named GlobeTrekker API

Add requests such as:

GET /destinations

POST /destinations with JSON body

PUT /destinations/<id>

DELETE /destinations/<id>

Set request headers:
You can also import your collection into Postman for quick testing.

bash

Content_Type: application?json

🚀 Future Upgrades
This project is actively being improved and maintained. Here are planned upgrades for future versions of the GlobeTrekker API:

🔐 v1.1 — User Authentication
Add user registration and login

Secure endpoints with JWT (JSON Web Tokens)

Only authenticated users can create/update/delete destinations

⭐ v1.2 — User Favorites / Bookmarked Destinations

Introduce User model and many-to-many relationship with Destination

Add /users/<id>/favorites route

Let users save or unsave destinations they love

🖼️ v1.3 — Destination Images

Add image_url field to store pictures of destinations

Return image URLs in API responses

(Optional) Integrate with Cloudinary or similar for uploads

📄 v1.4 — API Documentation with Swagger

Use Flasgger or Flask-RESTX to auto-generate API docs

Accessible via /docs

Makes API easier to explore and integrate with

🌍 v1.5 — Deploy API Online

Deploy backend to Render, Railway, or Vercel

Make API live so anyone can test it using Postman or browser

🧱 v2.0 — Advanced Backend Improvements

Migrate to PostgreSQL for production-grade DB

Add pagination, rate limiting, and error logging

Set up CI/CD pipeline for automatic deployment

🤝 Contributing

Got an idea or found a bug?

You're welcome to fork the repo and submit a pull request, or open an issue. Let's build this API better together!

📜 License

This project is licensed under the MIT License.

📣 Author

Reuben Jeffery Ofuafo

Builtby CloudKnight 

Connect  with me on [LinkedIn](https://www.linkedin.com/in/yourprofile)






