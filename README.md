# Wave Academy
This is an educational website built with Django.

![waveacademy](https://github.com/user-attachments/assets/65bb44b5-1ef1-442b-92c9-0212f9e5f761)


## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Contact](#contact)

## Requirements
- Python3
- Other dependencies listed in `requirements.txt`

## Installation
1. **Install Python:**

   - Download and install Python 3.7.6 from the official [Python website](https://www.python.org/downloads/).
   - Ensure you tick the option to add Python to PATH during installation.

2. **Install Dependencies:**

   It is best to use the python virtualenv tool to build locally:
   ```sh
   # install virtualenv
   > pip install virtualenv

   # create a virtual environment
   > virtualenv venv

   # activate the virtual environment
   > source venv/bin/activate   # Mac
   > .\venv\Scripts\activate    # Windows

   # clone the repo
   > git clone https://github.com/trevorcj/django-school.git
   > cd django-school

   # install dependencies
   > python -m pip install -r requirements.txt

## Running the Project
1. **Make Migrations:**

   ```sh
   > python manage.py makemigrations
2. **Apply Migrations:**
   
   ```sh
   > python manage.py migrate

3. **Create a superuser:**

   ```sh
   > python manage.py createsuperuser
4. **Run the Development Server:**
   
   ```sh
   > python manage.py runserver

  Open your browser and visit  `http://127.0.0.1:8000/` to view the website.

## Usage
1. **Admin Panel:**

   Access the Django admin panel at  `http://127.0.0.1:8000/admin` using the superuser credentials you created.

## Contact
Any suggestions or feedback on how to improve the project are welcome. Feel free to reach out via:

  - Email: trevorcjustus@gmail.com
