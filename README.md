
# Flask Healthcare Project

## Introduction

This project is a healthcare management system built with Flask, a lightweight WSGI web application framework in Python. It is designed to manage patients, doctors, and appointments efficiently.

## Key Features

- **Patient Management**: Register and manage patient information.
- **Doctor Management**: Keep track of doctors and their specializations.
- **Appointment Scheduling**: Schedule and manage appointments between patients and doctors.
- **User Authentication**: Secure login for patients.
- **Search Functionality**: Search for patients and doctors.
- **Medical Record Management**: Maintain and access patients' medical records.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.6+
- pip (Python package manager)
- Virtual Environment (recommended)

### Installation

#### Clone the Repository

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

#### Create and Activate Virtual Environment

- For Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### Install Required Packages

```bash
pip install -r requirements.txt
```

#### Environment Variables

Set up the necessary environment variables. Create a `.env` file in the root directory and add the following:

```makefile
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=<your_secret_key>
DATABASE_URL=sqlite:///database.db
```
Replace `<your_secret_key>` with a strong secret key.

#### Database Initialization

Initialize the database with the following commands:

```bash
flask db upgrade
```
Or, if not using migrations:

```bash
flask shell
>>> from app import db
>>> db.create_all()
```

#### Run the Application

```bash
flask run
```
The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

Here are some of the endpoints you can use:

### Patient Endpoints:

- Register: `POST /api/patients`
- Login: `POST /api/patients/login`
- Get all patients: `GET /api/patients`

### Doctor Endpoints:

- Register: `POST /api/doctors`
- Get all doctors: `GET /api/doctors`

### Appointment Endpoints:

- Schedule an appointment: `POST /api/appointments`
- Get appointments for a patient: `GET /api/appointments`
- Update appointment status: `PUT /api/appointments/<appointment_id>/status`

## Running Tests

To run the tests, execute the following command:

```bash
pytest
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
