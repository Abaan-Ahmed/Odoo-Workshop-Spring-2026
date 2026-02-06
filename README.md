# Odoo Workshop 2026

## Hands-On ERP Development with Odoo 19

### Author

Abaan Ahmed

---

## 📌 Project Overview

This repository contains the complete material for a **hands-on Odoo workshop** designed for educational use.
The project demonstrates how to build a **custom Odoo 19 module** using a modern development setup with **Docker**, and covers both **backend ERP development** and **website integration**.

The workshop is structured to help students understand not only *how* to build an Odoo module, but also *why* Odoo is designed the way it is.

---

## 🎯 Educational Objectives

By completing this workshop, students will:

* Understand what an ERP system is and how it is structured
* Learn why Odoo is widely used in industry
* Understand Odoo’s **modular architecture**
* Build a complete custom Odoo module from scratch
* Learn the difference between **backend UI** and **website UI** in Odoo
* Work with:

  * Python ORM models
  * XML-based backend views
  * Controllers for routing
  * QWeb (HTML templates)
  * CSS styling
* Use Docker for a reproducible development environment

---

## 🧠 Why Odoo?

Odoo is an open-source ERP platform that provides a complete ecosystem for business applications, including:

* Backend administration interface
* Website framework
* ORM and database abstraction
* Modular extensibility
* Security and access control

This makes Odoo an excellent platform for teaching **system-level, full-stack application development** without requiring students to assemble multiple disconnected technologies.

---

## 🛠 Development Environment

This project uses **Docker** to ensure a consistent and reproducible setup.

### Services Used

* **Odoo 19** (Application server)
* **PostgreSQL** (Database)

### Benefits of Using Docker

* No local dependency conflicts
* Same setup for all students
* Easy startup and teardown
* Industry-standard workflow

---

## 📁 Project Structure

```text
Odoo_Workshop_2026/
├── docker-compose.yml        # Defines Odoo and PostgreSQL services
├── odoo.conf                 # Odoo configuration file
├── addons/
│   └── custom/
│       └── workshop_course/  # Custom Odoo module
├── db-data/                  # Persistent PostgreSQL data (ignored by Git)
└── README.md
```

---

## 📦 The Custom Module: `workshop_course`

This workshop revolves around a custom Odoo module called **Workshop Course**, which allows administrators to manage courses and students and exposes a public course listing page.

### Module Structure

```text
workshop_course/
├── __manifest__.py           # Module metadata and dependencies
├── __init__.py
├── models/
│   ├── course.py             # Course model
│   └── student.py            # Student model
├── views/
│   ├── course_views.xml      # Backend course UI
│   ├── student_views.xml     # Backend student UI
│   ├── menus.xml             # Menus and actions
│   └── website_templates.xml # Website HTML templates
├── controllers/
│   └── main.py               # Website routing logic
├── static/
│   └── src/css/
│       └── workshop.css      # Website styling
└── security/
    └── ir.model.access.csv   # Access control rules
```

---

## 📄 Key Files Explained

### `__manifest__.py`

Defines:

* Module name and version
* Dependencies (`base`, `website`)
* Data files to load
* Frontend assets (CSS)

This file is the **entry point** for Odoo when loading the module.

---

### Python Models (`models/`)

Define database tables using Odoo’s ORM:

* No SQL is written manually
* Fields automatically map to database columns
* Relationships (e.g., Many2many) are handled declaratively

---

### Backend Views (`views/`)

Define the backend user interface using XML:

* Form views for data entry
* List views for browsing records
* Menus and actions to navigate the app

> Note: In Odoo 19, `tree` views have been replaced by `list` views.

---

### Website Layer

The module also includes an optional website component:

* Controllers define public URLs (e.g., `/courses`)
* QWeb templates render HTML
* CSS provides styling and visual customization

This layer demonstrates how backend data can be exposed publicly in a controlled manner.

---

## ▶️ How to Run the Project

### 1. Start Docker Desktop

Ensure Docker Desktop is running on your machine.

### 2. Start the Environment

From the project root:

```bash
docker compose up -d
```

### 3. Access Odoo

Open a browser and go to:

```
http://localhost:8069
```

### 4. Install the Module

* Enable Developer Mode
* Go to Apps
* Update Apps List
* Install **Workshop Course**

---

## 🌐 Website Demo Page

Once installed, the public course listing page is available at:

```
http://localhost:8069/courses
```

Students can modify HTML and CSS and immediately see visual changes.

---

## 🎓 Workshop Design

The workshop is designed for **two sessions** (1 hour 15 minutes each):

* **Session 1:**
  Odoo architecture, Docker setup, modules, models, backend UI

* **Session 2:**
  Website integration, HTML/CSS customization, full-stack flow

---

## ✅ Conclusion

This project demonstrates a realistic and educationally effective approach to teaching ERP and full-stack development using Odoo.
It emphasizes modular thinking, clean architecture, and hands-on experimentation.

---

## 📬 Contact

For questions or feedback regarding this workshop material, please feel free to reach out.
