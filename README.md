# 🚗 Car Rental System

Welcome to the Car Rental System! This is a web application built to make renting a car online completely seamless for customers, while giving fleet owners an easy way to manage their business behind the scenes. 

Whether you are a customer looking to book a ride for the weekend, or an admin keeping track of which cars are available and ready to go, this platform handles the heavy lifting.

## 🌟 What it Does
* **For Customers:** You can create an account, browse through available cars (filtering by vehicle type or price), and lock in your rental dates instantly.
* **For Admins:** Instead of dealing with messy spreadsheets, you can use the built-in Django dashboard to add new cars to the fleet, update pricing, or see who currently has a vehicle checked out.

* # Project Information

**Project Title:** Car Rental System

**Developer:** Abdul Samad

**Roll Number:** F23BDOCS1E02208

**Course:** Web Engineering

---

# Features

### User Features

- User Registration
- User Login & Logout
- Customer Profile
- Browse Available Cars
- Search Vehicles
- Book a Vehicle
- Wishlist Management
- Payment Management
- Review & Rating System
- Customer Dashboard
- Responsive User Interface

### Administrator Features

- Manage Vehicles
- Manage Customers
- Approve or Cancel Bookings
- Manage Payments
- Manage Reviews
- Manage Rental Locations
- Vehicle Availability Management
- Django Administration Panel

- # Database Models

The project contains the following database models:

- User
- Customer
- Car
- Booking
- Payment
- Review
- Wishlist
- RentalLocation

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/CarRentalSystem.git
```

Open the project

```bash
cd CarRentalSystem
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the development server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000/
```

---

# Project Structure

```
CarRentalSystem/
│
├── rental/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── CarRentalSystem/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

---

# Key Functionalities

- Secure user authentication
- Vehicle availability management
- Online vehicle booking
- Booking approval system
- Payment record management
- Customer dashboard
- Wishlist functionality
- Vehicle reviews and ratings
- Multi-field search functionality
- Responsive design using Bootstrap

---

# Future Improvements

- Online payment gateway integration
- Email notifications
- Booking invoices
- Advanced search filters
- Vehicle recommendation system
- Booking analytics dashboard

---

# License

This project was developed for educational purposes as part of the **Web Engineering** course.

## 🛠️ Built With
* **Backend:** Django (Python) – handles all the logic, routing, and user accounts.
* **Database:** SQLite – a lightweight, zero-configuration database that keeps setup incredibly simple.
* **Frontend:** HTML, CSS, and JavaScript (with Bootstrap) to keep the design clean and responsive on both desktop and mobile.
