1. Django Framework: All the files in the project are built using the Django framework. This includes the use of Django's built-in functions, classes, and methods.

2. Django Settings: The settings.py file contains all the configuration of the Django project. These settings are used across all the other files in the project.

3. Django URL Dispatcher: The urls.py files in the project and app directories use Django's URL dispatcher. This is used to route different URLs to their respective views.

4. Django Models: The models.py file contains the data schema for the application. This schema is used in views.py, serializers.py, and admin.py files.

5. Django Views: The views.py file contains the business logic of the application. These views are used in the urls.py file to route URLs.

6. Django Serializers: The serializers.py file contains the serializers for the models. These serializers are used in the views.py file.

7. Django Admin: The admin.py file uses the models to create an admin interface.

8. Django Apps: The apps.py file contains the configuration of the app. This configuration is used in the settings.py file.

9. PostgreSQL: The PostgreSQL database is used in the settings.py file for database configuration. The models.py file also uses this for defining the data schema.

10. RPC Commands: The views.py file contains the RPC commands for the API. These commands are used in the urls.py file for routing.

11. Django Tests: The tests.py file contains the tests for the app. These tests use the models, views, and serializers.

12. WSGI: The wsgi.py file contains the WSGI application. This is used by Django's development server and any WSGI-compatible web server.

13. Django Package for APIs: The views.py and serializers.py files use this package for creating the API.

14. __init__.py: These files are used to mark directories on disk as Python package directories. They are present in every directory of the Django project.