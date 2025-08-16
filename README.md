# lead_managment

Step-by-Step Installation
Step 1: Clone the repository

Open your terminal or command prompt and run:

git clone https://github.com/prabeshkhatiwada29/lead_managment.git
cd lead_managment

Step 2: Create a virtual environment (optional but recommended)
python -m venv lead_env


Activate the environment:

Linux/Mac:

source lead_env/bin/activate

Step 3: Install dependencies
pip install -r requirements.txt


This will install all Python packages needed for the project.

Step 4: Database Setup

Run Django migrations to set up the database:

python manage.py makemigrations
python manage.py migrate

Step 5: Create a superuser (Admin)
python manage.py createsuperuser


Follow the prompts to set username, email, and password.

Step 6: Run the development server
python manage.py runserver


The app will be accessible at:

http://127.0.0.1:8000/
