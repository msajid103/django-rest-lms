# Django REST LMS

A comprehensive **Learning Management System (LMS)** built with **Django REST Framework (DRF)**.  
This project provides robust APIs for managing **students, teachers, courses, and departments** in a university environment.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🚀 Features

- ✅ **Student Management** - Comprehensive student profiles, enrollment tracking, and progress monitoring
- ✅ **Teacher Management** - Teacher details, employment types, and department associations
- ✅ **Course Management** - Multi-department and multi-teacher course assignments
- ✅ **Department Management** - Organizational structure management
- ✅ **RESTful APIs** - Full CRUD operations with Django REST Framework
- ✅ **Scalable Architecture** - Modular design for easy extension
- 🔄 **Future Ready** - Prepared for grades, attendance, messaging modules

---

## 📂 Project Structure

```
django_rest_lms/
├── students/                 # Student management app
│   ├── models.py            # Student model definitions
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   └── urls.py              # URL routing
├── teachers/                 # Teacher management app
│   ├── models.py            # Teacher model definitions
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   └── urls.py              # URL routing
├── courses/                  # Course management app
│   ├── models.py            # Course model definitions
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   └── urls.py              # URL routing
├── departments/              # Department management app
│   ├── models.py            # Department model definitions
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   └── urls.py              # URL routing
├── django_rest_lms/          # Core project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── requirements.txt          # Python dependencies
├── manage.py                # Django management script
└── README.md                # Project documentation
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/django-rest-lms.git
   cd django-rest-lms
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   ```bash
   # Apply migrations
   python manage.py makemigrations
   python manage.py migrate
   
   # Create superuser (optional)
   python manage.py createsuperuser
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the API**
   - API Base URL: `http://127.0.0.1:8000/api/v1/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 📡 API Endpoints

### Students
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/students/` | List all students |
| `POST` | `/api/v1/students/` | Create new student |
| `GET` | `/api/v1/students/<id>/` | Get student details |
| `PUT` | `/api/v1/students/<id>/` | Update student |
| `DELETE` | `/api/v1/students/<id>/` | Delete student |

### Teachers
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/teachers/` | List all teachers |
| `POST` | `/api/v1/teachers/` | Create new teacher |
| `GET` | `/api/v1/teachers/<id>/` | Get teacher details |
| `PUT` | `/api/v1/teachers/<id>/` | Update teacher |
| `DELETE` | `/api/v1/teachers/<id>/` | Delete teacher |

### Courses
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/courses/` | List all courses |
| `POST` | `/api/v1/courses/` | Create new course |
| `GET` | `/api/v1/courses/<id>/` | Get course details |
| `PUT` | `/api/v1/courses/<id>/` | Update course |
| `DELETE` | `/api/v1/courses/<id>/` | Delete course |

### Departments
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/departments/` | List all departments |
| `POST` | `/api/v1/departments/` | Create new department |
| `GET` | `/api/v1/departments/<id>/` | Get department details |
| `PUT` | `/api/v1/departments/<id>/` | Update department |
| `DELETE` | `/api/v1/departments/<id>/` | Delete department |

### Example Usage

```bash
# List all students
curl -X GET http://127.0.0.1:8000/api/v1/students/

# Create a new student
curl -X POST http://127.0.0.1:8000/api/v1/students/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Get specific student
curl -X GET http://127.0.0.1:8000/api/v1/students/1/
```

---

## 🛠️ Tech Stack

- **Backend Framework**: Django 4.2+
- **API Framework**: Django REST Framework 3.14+
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Authentication**: DRF Token Authentication / JWT (planned)
- **Documentation**: Auto-generated API docs with DRF
- **Testing**: Django Test Framework
- **Deployment**: Docker / Heroku / AWS (configurable)

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/lms_db
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration

For PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lms_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test students

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📦 Dependencies

Key packages used in this project:

- `Django>=4.2.0` - Web framework
- `djangorestframework>=3.14.0` - REST API framework
- `psycopg2-binary>=2.9.0` - PostgreSQL adapter
- `python-decouple>=3.6` - Environment variable management
- `django-cors-headers>=4.0.0` - CORS handling
- `django-filter>=23.0` - API filtering

---

## 🚢 Deployment

### Using Docker

```bash
# Build the image
docker build -t django-rest-lms .

# Run the container
docker run -p 8000:8000 django-rest-lms
```

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# Stop services
docker-compose down
```

---

## 📌 Roadmap

### ✅ Completed Features
- [x] Basic CRUD operations for all entities
- [x] RESTful API design
- [x] Model relationships and constraints
- [x] Basic authentication setup

### 🔄 In Progress
- [ ] JWT Authentication implementation
- [ ] Role-based access control (Admin, Teacher, Student)
- [ ] API documentation with Swagger/OpenAPI

### ⏳ Planned Features
- [ ] **Grading System** - Assignment submissions and grading
- [ ] **Attendance Tracking** - Class attendance management
- [ ] **Notification System** - Email and in-app notifications
- [ ] **Messaging System** - Student-teacher communication
- [ ] **File Management** - Document and resource sharing
- [ ] **Analytics Dashboard** - Performance metrics and reports
- [ ] **Mobile App** - React Native mobile application
- [ ] **Frontend Integration** - React.js/Next.js web interface

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
   ```bash
   git fork https://github.com/your-username/django-rest-lms.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make your changes**
   - Write clean, documented code
   - Add tests for new features
   - Follow Django and DRF best practices

4. **Test your changes**
   ```bash
   python manage.py test
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add some AmazingFeature"
   ```

6. **Push to your branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Ensure all tests pass

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Django and DRF communities for excellent documentation
- Contributors who help improve this project
- Educational institutions inspiring this LMS design

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/django-rest-lms/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/django-rest-lms/discussions)
- **Email**: your-email@example.com

---

## ⭐ Show Your Support

If this project helps you, please consider giving it a ⭐ on GitHub!

---

**Made with ❤️ using Django & DRF**
