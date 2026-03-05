# enrollment_system

This is a Coursework Porject for the module Distributed Systems and Cloud Computing at WIUT

It is an enrollment system for students. Users can sign up, log in, and log out of the system. However, only the admin assigns the role of an "instructor" to users. Upon registration all users are defaulted to "student". 

Features: 
- As mentioned login logic.
- Studetns can enroll and unenroll from courses
- Instructors can create, edit, and delete courses
- All can access their profile where their enrolled courses or created courses, their username, and their role is displayed.

Technologies Used:
- Backend: Django, Python
- Database: SQLite for dev and PostgreSQL for prod
- Frontend: Django templates and TailwindCSS
- Containerization: Docker and Docker Compose
- Web server: Nginx, Gunicorn
- CI/CD: GitHub Actions
- Hosting: Eskiz.uz
- SSL: #### to be filled
- Version Control: Git, GitHub

Local Setup Instructions
1. Clone the repository: 
    git clone https://github.com/IslombekMir/enrollment_system 
    cd enrollment_system
2. Make sure Docker and Docker Compose are installed
    docker --version
    docker-compose --version   or   docker compose version
3. Build the Docker containers
    docker compose build
4. Run the project
    docker compose up -d
5. Apply migrations
    docker compose exec web python manage.py migrate
6. Create superuser
    docker compose exec web python manage.py createsuperuser
7. Access the project at 
    http://localhost and the admin panel at http://localhost:8000/admin
8. Stop the project
    docker compose down

Environment Variables
- Copy the example variable file:
    cp .env.example .env
- Then edit .env with your values.

Application Screenshots
![Home](/screenshots/telegram-cloud-photo-size-2-5282917376355668951-y.jpg)
![Profile](/screenshots/telegram-cloud-photo-size-2-5282917376355668954-y.jpg)
![Courses](/screenshots/telegram-cloud-photo-size-2-5282917376355668955-y.jpg)


