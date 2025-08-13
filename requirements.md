# Project Requirements

## Python Dependencies

- Django>=4.2.0
- mysqlclient>=2.1.0

## System Requirements

- Python 3.8 or higher
- MySQL 5.7 or higher (or compatible database)
- pip package manager

## Installation Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

For MySQL, you'll need to:
1. Install MySQL server
2. Create a database for the application
3. Configure the database connection in Django settings
4. Install the MySQL client library:
   ```bash
   pip install mysqlclient