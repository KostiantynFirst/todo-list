# Todo List

A simple Django web app for managing everyday tasks. Each task can have a deadline and several tags, and you can mark it as done or undo it with one click.

## Features

- **Tasks**: create, update and delete tasks with content, an optional deadline and any number of tags
- **Complete / Undo**: switch a task's status with one button
- **Smart ordering**: tasks that are not done come first, and the newest tasks come first within each group
- **Tags**: create, update and delete tags on a separate page
- **Sidebar navigation** on every page
- Responsive UI built with Bootstrap 5 (Bootswatch "Minty" theme)
- Test data fixture and unit tests

## Tech stack

- Python 3
- Django
- SQLite
- Bootstrap 5, Bootswatch, Bootstrap Icons
- django-crispy-forms + crispy-bootstrap5
- flake8

## Data model

```
Tag                      Task
----                     -----
id                       id
name (unique)            content
                         created_at   (set automatically)
                         deadline     (optional)
                         is_done      (default: False)
                         tags  ── many-to-many ──► Tag
```

A task can have many tags, and a tag can belong to many tasks.

## Pages

| URL | Page |
|---|---|
| `/` | Task list (home page) |
| `/tasks/create/` | Create a task |
| `/tasks/<id>/update/` | Update a task |
| `/tasks/<id>/delete/` | Delete a task |
| `/tasks/<id>/toggle/` | Complete / Undo (POST only) |
| `/tags/` | Tag list |
| `/tags/create/` | Create a tag |
| `/tags/<id>/update/` | Update a tag |
| `/tags/<id>/delete/` | Delete a tag |

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KostiantynFirst/todo-list.git
   cd todo-list
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
4. Create a `.env` file based on `.env.sample` and set your own `SECRET_KEY`:

   ```bash
   copy .env.sample .env        # Windows
   cp .env.sample .env          # macOS / Linux
   ```

5. Apply the migrations:

   ```bash
   python manage.py migrate
   ```

6. Load the test data (optional):

   ```bash
   python manage.py loaddata todo_data
   ```

7. Create a superuser to use the admin panel (optional):

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

   Then open http://127.0.0.1:8000/ in your browser.

## Running tests

```bash
python manage.py test
```

## Code style

```bash
flake8
```

## Project structure

```
todo-list/
├── manage.py
├── requirements.txt
├── todo_list/            # project settings and root URLs
└── todo/                 # main app
    ├── fixtures/         # test data
    ├── migrations/
    ├── templates/
    │   ├── base.html     # layout with sidebar
    │   └── todo/         # task and tag pages
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
