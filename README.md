# A minimal Django App
This documents the process for creating and deploying a Django application.

As an example this application generates a QR code base on user input and save the code as a PNG image on disk.

## 1. Setting up the Django environment
* Create a project folder
* Create a virtual environment for the project
  * Run `pipenv shell`
* Install dependencies
  * Run `pipenv install django qrcode pillow`
  * Run `django-admin --version` to confirm
## 2. Create the Django project
* Run `django-admin startproject qr_code_generator .`
* Start the dev server to confirm
  * Run `python manage.py runserver`

## 3. Create the App
* Create a new app
  * Run `python manage.py startapp qr_code_generator_app`
* Register the app in the project
  * Open `settings.py`
  * Add `qr_code_generator_app` to the `INSTALLED_APPS` list
  * Add `STATIC_FILES_DIRS = [BASE_DIR / "static"]` for serving the QR image
* Create the 'static' folder

## 4. Creating the View, Template and URL Routing
* **View**: processes user input (text for the QR code) and generates the QR image using the `qrcode` library.
* **Template**: Provides the HTML form and displays the QR image.
* **URLs**: Maps the browser's request to the view

### View
* Shows a form for the text input
* Generate a QR code from the input and save it as an image in the static folder.
* Pass the image path to the template for display

### Template
Defines the HTML interface.

* Create a templates folder inside app folder
  * Run `mkdir qr_code_generator_app/templates`
  * Run `mkdir qr_code_generator_app/templates/qr_generator`
* Create the template HTML file
  * Create `qr_code_generator_app/templates/qr_generator/qr_form.html`
  * Write app UI logic

### Set URL routing
Connects the view to a URL so the browser knows where to go.

* Create app urls folder
  * Create `qr_code_generator_app/urls.py`
  * Add paths (endpoints) to the views for the app
* Update the project urls
  * Include the app urls in the project urls
  * Also add a path to the static files for serving static files
### Enable static files
* Run `python manage.py collectstatic --noinput`

