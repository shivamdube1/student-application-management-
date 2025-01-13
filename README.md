# Student Applications Management System

This project is a Django-based web application designed to handle student applications. The system allows students to register, log in, submit their application details, and upload required documents. Administrators can review applications, approve or disapprove them, and manage the application process seamlessly.

## Features

1. **User Registration and Login**:
   - Students can create accounts and log in to access the application portal.

2. **Application Submission**:
   - Students can submit details such as:
     - Address
     - CET marks
     - Upload required documents (Aadhar card and CET marksheet).

3. **Admin Dashboard**:
   - Admins can view, sort, approve, or disapprove applications.

4. **Application Status Tracking**:
   - Students can check whether their application has been approved or disapproved.

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS (customizable)
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Authentication**: Django's built-in user authentication

## Installation and Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment tools (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_applications
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Usage

1. **Student Workflow**:
   - Register and log in.
   - Fill out the application form with the required details and upload documents.
   - Submit the application.
   - Check the status on the status page.

2. **Admin Workflow**:
   - Log in as a staff user.
   - Navigate to the admin dashboard.
   - Review applications and approve/disapprove them.

## File Structure

```
student_applications/
|-- applications/               # App handling student applications
|   |-- migrations/             # Database migrations
|   |-- templates/              # HTML templates
|   |-- static/                 # Static files (CSS, JS, etc.)
|   |-- admin.py                # Admin configuration
|   |-- apps.py                 # App configuration
|   |-- forms.py                # Forms for user registration and applications
|   |-- models.py               # Database models
|   |-- urls.py                 # App-specific URLs
|   |-- views.py                # Views for application logic
|
|-- manage.py                   # Django management script
|-- db.sqlite3                  # SQLite database file
|-- requirements.txt            # Python dependencies
|-- README.md                   # Project documentation
```

## Key Files

- **`models.py`**: Defines the `StudentApplication` model with fields for user information, address, CET marks, and uploaded documents.
- **`views.py`**: Contains views for registration, application submission, status tracking, and admin dashboard.
- **`urls.py`**: Maps URLs to the respective views.
- **Templates**: HTML templates for all pages (registration, application form, status page, and admin dashboard).

## Future Enhancements

- Add email notifications for application status changes.
- Implement advanced search and filtering in the admin dashboard.
- Enhance the user interface with modern frontend frameworks (e.g., React or Bootstrap).
- Add support for exporting application data to CSV/Excel.


## Contact

For questions or suggestions, please contact:
- **Name**: [Shivam Dube]
- **Email**: [shivam.suraj.dube@gmail.com]

---
Thank you for using the Student Applications Management System!

