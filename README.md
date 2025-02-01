# MultiFAQ-Support

MultiFAQ is a web application built with Django that allows you to manage Frequently Asked Questions (FAQs) with multilingual support and caching. This application enables the storage of questions and answers, which can be dynamically translated based on the user's language preference. It also integrates Redis for efficient caching to ensure faster responses.

## Features

- FAQ Management: Store and manage questions and answers.
- Multilingual Support: Automatically translate questions and answers based on the user's language preference (?lang=lang_code).
- WYSIWYG Editor: Use Django CKEditor for rich text formatting in answers.
- Redis Caching: Cache translated questions and answers for faster response times.
- API Integration: Access FAQs via a REST API with language selection.
- Admin Interface: Manage FAQs easily via Django's built-in admin panel.

## Technologies Used

- Django: Backend framework for building the web application.
- Django REST Framework (DRF): For creating REST APIs.
- Google Translate (via googletrans library): For automatic translation of FAQs.
- Redis: Caching mechanism to speed up the response times for frequently accessed translations.
- django-ckeditor: WYSIWYG editor for rich-text answers.
- Docker: For containerizing the application for easier deployment.
  

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bansalmohit123/MultiFAQ-Support.git
    
    cd MultiFAQ-Support
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

## Usage

Running the Development Server

```bash
python manage.py runserver
```

## API Endpoints

- List FAQs (default language: English):

    ```bash
    GET /api/faqs/
    ```

- List FAQs in specific language:

    ```bash
    Method: GET
    Query Parameters:
    lang: Specify the language for translations (e.g., en, hi, bn, es, fr, de, it, pt).
    ```
- Response:
```bash
[
  {
    "id": 1,
    "question": "What is Django?",
    "translated_question": "Django क्या है?",
    "answer": "Django is a Python web framework.",
    "translated_answer": "Django एक पायथन वेब ढांचा है।"
  }
]
```
- Create FAQ
  ```bash
  Endpoint: /api/faqs/create/
  Method: POST
  Request Body:
  {
    "question": "What is Django?",
    "answer": "Django is a Python web framework."
  }
  ```

  - Response:
  ```bash
  {
    "message": "FAQ created successfully!",
    "id": 4
  }
  ```
  

    
# Environment Variables Setup (`.env` File)  

To configure the project, create a `.env` file in the root directory and add the following environment variables:  

```plaintext
# Debug Mode (Set to False in production)
DEBUG=True  

# Django Secret Key (Replace with a secure key in production)
SECRET_KEY='your-secret-key'  

# Database Configuration
DB_NAME=your_database_name  
DB_USER=your_database_user  
DB_PASSWORD=your_database_password  
DB_HOST=your_database_host  
DB_PORT=5432  

# Redis Configuration
REDIS_URL=redis://your_redis_host:6379/1  
```
## Admin Interface

Access the admin interface at [http://localhost:8000/admin](http://localhost:8000/admin) to manage FAQ content.

## Development

### Running Tests

```bash
pytest
```

### Code Quality

We use flake8 for code quality checks:

```bash
flake8 .
```

### Docker Support

1. Build the image:

    ```bash
    docker-compose build
    ```

2. Run the containers:

    ```bash
    docker-compose up
    ```

## Contributing

Fork the repository
