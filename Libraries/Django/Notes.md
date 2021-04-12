# Creating a Django Project.
 1. __Create a virtual environment__, with pipenv module, inside our project's
 folder and install the django module.
    ```shell
    C:\DjangoProject> pipenv install django
    ````
2. After verifying our installation with the _python -m django --version_ command, we are
ready to start our project by typing:
    ```shell
    C:\DjangoProject> django-admin startproject <Project's name>
    ```
3. To run the server for our website, we browse to our project's root folder and
we type the following command:
    ```shell
    C:\DjangoProject> python manage.py runserver
    ```

+ ## Creating a Super-User for our Project
___
For the creation of a super-user, in order to be able to connect in the admin page
of our project, we must run the following commands.

- <a id="db"></a>First we run the command _makemigrations_, this allows
django to initialise the default database that will allow us to create the
super-user. This command also detects any changes we make to our own databases.
    ```shell
    C:\DjangoProject> python manage.py makemigrations
    ```
- Secondly we run the _migrate_ command, in order to apply any changes we have
made to our databases.
    ```shell
    C:\DjangoProject> python manage.py migrate
    ```

- Finally we execute the _createsuperuser_ command in order to create our super-
user.
    ```shell
    C:\DjangoProject> python manage.py createsuperuser
    ```
# Creating an App inside our website.
1. We browse to our project's root file and type the command:
    ```shell
    C:\DjangoProject> python manage.py startapp <App's name>
    ```
2. In our App's folder inside the views.py file, we create the view that our
website will have when we browse to those pages. For example:
    ```python
    # <App's Name>/views.py
    from djagno.shortcuts import render
    from django.http import HttpResponse


    def home(request):
        return HttpResponse("<h1>Blog Home</h1>")

    def about(request):
        return HttpResponse("<h1>About</h1>")

    ```
3. We create a urls.py file inside our App's folder. In this file we map the url's
patterns that we want our App to correspond to. We import the views module from
our folder and we declare our patterns.
    ```python
    # <App's Name>/urls.py
    from django.urls import path
    from "<App's Name>" import views


    urlpatterns = [
        path("", views.home, name="blog-home"),  # Since we want this to be
                                                 # our home page, we leave the
                                                 # argument empty.
        path("about", views.about, name="blog-about"),
    ]

    ```
4. After we created and filled the App's urls.py file, we browse to our project's
root folder and inside the corresponding urls.py file we map the routes to our
<App's Name> url's.
    ```python
    # DjangoProject/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("blog/", include("blog.urls")),
    ]

    ```
5. Finally, in order for django to use our App, we copy the App's configuration
from the _App's Name/apps.py_ file
    ```python
    # <App's Name>/apps.py
    from django.apps import AppConfig


    class BlogConfig(AppConfig):
        name = 'blog'

    ```
    <a id="apps"></a>and we add it to the INSTALLED_APPS list in the _DjangoProject/settings.py_
    ```python
    # DjangoProject/settings.py
    ...
        INSTALLED_APPS = [
        'blog.apps.BlogConfig',  # User defined app
        'users.apps.UsersConfig',  # User defined app
        'crispy_forms',  # User defined app
        # ----------------------------------------------------------------------
        'django.contrib.admin',  # Default app
        'django.contrib.auth',  # Default app
        'django.contrib.contenttypes',  # Default app
        'django.contrib.sessions',  # Default app
        'django.contrib.messages',  # Default app
        'django.contrib.staticfiles',  # Default app
    ]
    ...

    ```

# Using Templates
Templates are used to present complex HTML to our site. For maintainability reasons
we don't pass our HTML code directly to our views, instead we save them in our
_templates_ folder. The convention for this folder is:

>```shell
>C:\DjangoProject\App's Name> mkdir templates
>
>C:\DjangoProject\App's Name\templates> mkdir <App's Name>
>
>C:\DjangoProject\App's Name\templates\App's Name>
>```

Inside this folder, we can now save our .html, files. We follow a similar approach
for our custom .css, .js files using the _static_ folder.

>```shell
>C:\DjangoProject\App's Name> mkdir static
>
>C:\DjangoProject\App's Name\static> mkdir <App's Name>
>
>C:\DjangoProject\App's Name\static\App's Name>
>```

+ ## Rendering a Template
___
In order for Django to render our template, i.e. <App's Name>/home.html, we browse
to our _<App's Name>/views.py_ file and we import the _render_ method from the
_django.shortcuts_ module.
```python
# <App's Name>/views.py
    from djagno.shortcuts import render


    def home(request):
        return render(request, 'blog/home.html')

    def about(request):
        return render(request, 'blog/about.html')

```
+ ### Rendering with "dummy" Data.
___
For our app to render the template with data, we use a third argument to our
 _render_ method.

```python
# <App's Name>/views.py
    from djagno.shortcuts import render


    dummy_data = [
        {
            'author': 'Author One',
            'title': "<App's Name> Post 1",
            'content': 'First post content',
            'date': '21st November 2020'
        },
        {
            'author': 'Author Two',
            'title': "<App's Name> Post 2",
            'content': 'Second post content',
            'date': '22nd November 2020'
        }
    ]

    def home(request):
        context = {
            'posts': dummy_data
        }
        return render(request, 'blog/home.html', context)

    def about(request):
        return render(request, 'blog/about.html')

```
Now for our template to have access to those data, we pass them with a codeblock.
In this case we will use a _for loop_. For code inside our .html files, with
django, we use the **"{% %}"** block and in order to access variables the **"{{ }}"**.

```html
<!-- <App's Name>/templates/<App's Name>/home.html -->
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
    </head>

    <body>
        {% for post in posts %}
            <h1>{{ post.title }}</h1>
            <p>
                By {{ post.author }} on {{ post.date_posted }}
            </p>
            <p>
                {{ post. content }}
            </p>
        {% endfor %}
    </body>
</html>
```
**Note: In django, we always 'end' our statements and loops. i.e.:**

```html
<!-- <App's Name>/templates/<App's Name>/home.html -->
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% if title %}
        <title>Django - {{ title }}</title>
        {% else %}
            <title>Django - Default</title>
        {% endif %}
    </head>

    <body>
        {% for post in posts %}
            <h1>{{ post.tile }}</h1>
            <p>
                By {{ post.author }} on {{ post.date_posted }}
            </p>
            <p>
                {{ post. content }}
            </p>
        {% endfor %}
    </body>
</html>
```

+ ### Creating and expanding a Base Template
___
As long as we have templates with similar appearance, it is easier and more maintainable
for us to have a "Base Template" that is used by all other templates of our app
and then be customized accordingly. To do so, we define the codeblock that our
child templates are permitted to override.

```html
<!-- <App's Name>/templates/<App's Name>/base.html -->
    <!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% if title %}
            <title>Django - {{ title }}</title>
        {% else %}
            <title>Django - Default</title>
        {% endif %}
    </head>

    <body>
        {% block content %}

        {% endblock %}
    </body>
</html>
```
After creating our "Base Template", we expand it to our other templates and we
begin to customize it as we wish. i.e.:

```html
<!-- <App's Name>/templates/<App's Name>/home.html -->
{% extends "<App's Name>/base.html" %}  <!-- "Importing" our base template -->

{% block content %}  <!-- The override to our base's template codeblock -->
        {% for post in posts %}
            <h1>{{ post.tile }}</h1>
            <p>
                By {{ post.author }} on {{ post.date_posted }}
            </p>
            <p>
                {{ post. content }}
            </p>
    {% endfor %}
{% endblock content %}

```
```html
<!-- <App's Name>/templates/<App's Name>/about.html -->
{% extends "<App's Name>/base.html" %}  <!-- "Importing" our base template -->

{% block content %}  <!-- The override to our base's template codeblock -->
    <h1>About page</h1>
{% endblock content %}

```
+ ### Adding Relative Paths to Base Template
___
For us to have flexibility in our App we can pass django style urls to our html
and not absolute paths. This allows us to dynamically change the reference of
different HTML objects.

```html
.....
<header class="site-header">
    <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
            <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>  <!-- Dynamically refers to our <App's Name >/urls.py -->
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle"
                aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                    <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>  <!-- Dynamically refers to our <App's Name>/urls.py -->
                    <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>  <!-- Dynamically refers to our <App's Name  >/urls.py -->
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                    {% if user.is_authenticated %}
                        <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>  <!-- Dynamically refers to our <App's Nam>/urls.py -->
                        <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>  <!-- Dynamically refers to our <App's Name >/urls.py -->
                    {% else %}
                        <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>  <!-- Dynamically refers to our <App's Nam>/urls.py -->
                        <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>  <!-- Dynamically refers to our <App's Name >/urls.py -->
                    {% endif %}
                </div>
            </div>
        </div>
    </nav>
</header>
.....
```
+ ### Loading CSS to our Base Template
___
When we want to include a custom .css file to our .html file, we first have to
reference it, by using a django codeblock. After the reference we can load it
inside our file.
```html
{% load static %} <!-- Referencing our <App's Name>/static folder-->

<!DOCTYPE html>
<html lang="en">

    <head>
        .....

       <!-- Loading <App's Name>/main.css file -->
       <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

        {% if title %}
        <title>Django Blog- {{ title }}</title>
        {% else %}
        <title>Django Blog- Default</title>
        {% endif %}
    </head>

    <body>
        .....
```
# Create Data Bases
Django, by default, has it's own Object Relational Mapper(ORM). That means that
any table we want to create, we can do so, by creating a class -called model-
inside our _<App's Name>/models.py_ file.
+ Every class that we create here, is a table to our database.
+ Every class attribute is our table's columns.
```python
# <App's Name>/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # We import the table User from
        # our database. Since this table was automatically creaded by Django
        # we can reference it by it's schema name.


class Post(models.Model):

        title = models.CharField(max_length=100)
        content = models.TextField()
        # For arguments in our date attribute, among others, we can use the following:
        #       * auto_now=True , this gives us the time for every time the Post
        #               class is updated.
        #       * auto_now_add=True, this gives us the time the post Class is created.
        #       * default=timezone.now, this gives us the time the post Class is
        #               created but also allows us to change the time if we wish so.
        date_posted = models.DateTimeField(default=timezone.now)
        # We use the on_delete argument, so as to specify what happens when our user
        # gets deleted. By passing the CASCADE value, we have every post the deleted
        # user made, deleted as well.
        author = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
                return self.title
```
To be able to create and view our database we must follow the [procedure](#db)
that we described earlier. This allows the migration of all our data to our
Project's database. After that, we can inspect our object by viewing the
_<App's Name>/migrations/####_initial.py_ file. In case we want to view the exact
SQL code that created our object, we execute the _sqlimigrate_ command:
```shell
C:\DjangoProject> python manage.py sqlmigrate <App's Name> <####>
```
+ ## Querying the Data Base
___
There are two ways to make queries to our database. The first is through our terminal
by executing the _shell_ command and then importing our models:
```shell
D:\DjangoProject> python manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from <Apps Name>.models import Post
>>> from django.contrib.auth.models import User
```
The second is by creating a "standalone" module inside our <App's Name> folder:
```python
# <App's Name>/db_queries_example.py

# In order to make a 'stand alone' script in django, we have to use the setup
# method first.
import django
django.setup()

from blog.models import Post  # Importing DB table Post
from django.contrib.auth.models import User  # Importing DB table User
```
In both cases, we can perform our queries, i.e.:
```python
# <App's Name>/db_queries_example.py
.....

# Viewing all our users
print(User.objects.all())

# Filtering our users using a field
print(User.objects.filter(username='UserTest'))

# Taking information from a specific user entry.
user = User.objects.filter(username='gbxxi').first()

print(user.id)  # Printing our users id.
print(user.pk)  # Printing our users Primary Key

# Finding a user by it's id.
user1 = User.objects.get(id=1)
print(user1)

# Checking to see if we have any posts.
print(Post.objects.all())

# Since we have none, we can create one as an example.
post_1 = Post(
    title= 'First db Post.',
    content= f'This is a post made by the {__name__} module',
    author= user1
)

# In order for our post to be saved in our database, we must explicitly save it
# with the .save() method.
post_1.save()
print(Post.objects.all())

# In order to make our Post object more discripted, we must make a __str__ method
# to our Post class, in the <App's Name>/models.py module.

# NOTE: Every time we run this script, an new post_1 will be created. But it's
# going to be distinct because of the .time attribute of our class.

# Creating a second post. In this case we will use the user id.
post_2 = Post(
    title= 'Second db Post.',
    content= 'This is a post made with author_id',
    author_id=user1.id
)
post_2.save()

# Parsing through the fields of our Post object.
parse = Post.objects.first()
print(parse.content)
print(parse.title)
print(parse.date_posted)
print(parse.author)

print(parse.author.email)

# Retrieving all the posts by a specific user.
print(user1.post_set.all())

# Creating a post from a specific user.
# With this method of creating, there is no need to use the .save() method.
user1.post_set.create(
    title= 'Immediate post',
    content= 'This is an immediate post created with the .post_set.create method'
    )

```
Finally, for our website in order to have access to our data we must import them
in the respective _<App's Name>/views.py_,
```python
# <App's Name>/views.py

from django.shortcuts import render
from blog.models import Post  # Importing this module in order to query our database
                              # and pass the values that we want, to be rendered.

# Rendering our templates.
def home(request):
    context = {
        'posts': Post.objects.all()  # Quering from our database.
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

```
and for the admin site to also have access, we register them in the _<App's Name>
/admin.py_ file.
```python
# <App's Name>/admin.py

from django.contrib import admin
from <Apps Name>.models import Post  # Importing our model.

admin.site.register(Post)  # Registering our model to our admin site.

```
# Create User Registration Forms
As a first approach we create our registration forms as a new app. In this example
we will use a ready form from django that we will adjust later on. So after we
add our app inside our [INSTALLED_APPS](#apps) list in our _<Project's name>/settings.py_
we browse to our _<App's Name>/views.py_ and create our registration form.
```python
# <App's Name>/views.py

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    return render(request, "<App's Name>/register.html", {'form': form})

```
Continuing, we now can create our _<App's Name>/register.html_ with the same way
as we did in our [previous example](#Using-Templates).
```html
<!-- <App's Name>/templates/<App's Name>/register.html -->
{% extends "blog/base.html %}
{% block content %}
    <div class="content-section">
        <for method="post">
        {% csrf_token %}
        <fieldset class="form-group">
             <legend class="border-bottom mb-4">
                 Join today
             </legend>
             {{ form }}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">
                Sign Up
            </button>
        </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Already Have an Account <a class="ml-2" href="#">
                    Sing In
                </a>
            </small>
        </div>
    </div>
{% endblock content %}

```
Moving along, since we have only one view -so far- in this app, we can import it
directly to our _<Project's Name>/urls.py_ module.
```python
# <Project's Name>/urls.py
from django.contrib import admin
from django.urls import include, path
from users import views as user_views  # Altenative way of importing our urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),  # Since we want our blog app to be our
                                     # default page, we leave the stirng blank.
    path('register/', user_views.register, name='register')
]

```
Now that the first steps are concluded, we can manipulate our form as we wish.
We begin by adding a user validation that will also show us a message if the
validation is successful. In order to do that we browse back to our _<App's Name>/views.py_
module.
```python
#<App's Name>/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Importing flash message. It is an easy way
                                     # to sent one time alerts to a template.


Creating our form.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()  # Saving our user, from our form object, to our database.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})  # If our valid-
                                # ation is unsuccessful we render again the page
                                # with empty the fields that do not validate.

```
For the flash-messages to be shown we must add them to a template. In this example
we will add them to our _base.html_.
```html
<!-- templates/<App's Name>/base.html -->

{% load static %}

<!DOCTYPE html>
<html lang="en">

    <head>
        .....
    </head>
    <body>
        .....
        <main role="main" class="container">
            <div class="row">
                <div class="col-md-8">
                    {% if messages %}
                        {% for message in messages %}  <!-- Passing our messages
                                                        to our template -->
                        <div class="alert alert-{{ message.tags }}">  <!--
                            Bootstrap and Django, use the same message tags
                            so we can easily pass the .tags variable to our alert
                            css class. -->
                             {{ message }}
                        </div>
                        {% endfor %}
                    {% endif %}
                    {% block content %}
                    {% endblock %}
                </div>
                .....
            </div>
        </main>
    </body>
</html>

```
+ ## Customising our form
___
To be able to customise our form, we first create - inside our <App's Name>- folder
a module named _forms.py_, and we start creating a new form that inherits from
django form class.
```python
# <App's Name>/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adds the email field to our form.
                                # (or any other additional fiels that we want)

    class Meta:  # In this class, we specify the model that we want our form to
                # interact with. So, whenever this form validates it's creating
                # a new user.
                # This class gives us a namespace for configurations and keeps
                # them in one place.
        model = User
        fields = [  # These are the fields - and their order- that are going to
                    # be shown in our form.
            'username',
            'email',
            'password1',
            'password2'
        ]

```
After that, we are able to use our custom form just by importing it to our
_<App's Name>/views.py_ module.
```python
# <App's Name>/veiws.py

from django.shortcuts import render, redirect
from django.contrib import messages  # Importing flash message. It is an easy way
                                     # to sent one time alerts to a template.
from users.forms import UserRegisterForm  # Our custom form.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Saving our user to our database.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})  # If our valid-
                                # ation is unsuccessful we render again the page
                                # with empty the fields that do not validate.

```
+ ## Adding Styling to our Form with Crispy-forms
___
To be able to add .css styling to our form, we can easily use a tool named crispy-
forms. To do so, first we install it to our environment.
```shell
C:\DjangoProject> pipenv install django-crispy-forms

```
then we add it to our [INSTALLED_APPS](#apps) list in our
 _<Project's name>/settings.py_ . Because crispy-forms defaults to "bootstrap2"
 inside our _<Project's name>/settings.py_ we set it to "bootstrap4" to the very
 bottom of the file.
 ```python
 # <Project's name>/settings.py

 """
Django settings for CoreySchafer_tutorial project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yxtmgmx5^u($d7wr$75s9p@0r6f@%9%i%g#*iyrcun8ulz2)j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',

    # --------------------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
.....

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

 ```
Continuing, in order to be render we load crispy-forms to our template, in this
example <App's Name>/register.html .
```html
<!-- templates/<App's Name>/register.html -->

{% extends "blog/base.html" %}
{% load crispy_forms_tags %}

{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
            <legend class="border-bottom mb-4">
                Join Today
            </legend>
            {{ form|crispy  }}  <!-- using the crispy filter -->
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">
                Sing Up
            </button>
        </div>
        </form>
        <div class="border-to pt-3">
            <small class="text-muted">
                Already Have An Account?
                <a class="ml-2" href="{% url 'login' %}">
                    Sing In
                </a>
            </small>
        </div>
    </div>
{% endblock content %}

```
# Creating an Login and Logout System
In this example, we are going to use the django default login and logout views.
So as a first step we import the url's to our _<Project's Name>/urls.py_ module.

```python
# <Project's Name>/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views  # Login and Logout views
from django.urls import include, path
from users import views as user_views  # Altenative way of importing our urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Since we want our blog app to be our default page, we leave the stirng blank.
    path("", include("blog.urls")),
    path('register/', user_views.register, name='register'),
    path(
        'login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
]

```
As we see, we specify the argument template_name to search for our .html files.
We have to do that, because as a default django will search for those files in
the _registration/login.html_ or _registration/logout.html_ path.<br>
So after we have our url's specified, we browse to our templates folder and we
create our login.html & logout.html files.
```html
<!-- templates/<App's Name>/login.html -->
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}

{% block content %}
    <div class="content-section">
         <form method="POST">
             {% csrf_token %}
             <fieldset class="form-group">
                <legend class="border-bottom mb-4">
                    Log In
                </legend>
                {{ form|crispy  }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">
                    Log In
                </button>
            </div>
         </form>
         <div class="border-to pt-3">
              <small class="text-muted">
                  Need An Account?
                  <a class="ml-2" href="{% url 'register' %}">
                      Sing Up Now
                  </a>
              </small>
         </div>
    </div>
{% endblock %}

```
```html
<!-- templates/<App's Name>/logout.html -->

{% extends "blog/base.html" %}

{% block content %}
    <h2>You have been logged out</h2>
    <div class="border-to pt-3">
        <small class="text-muted">
            <a href="{% url 'login' %}">
                Log In Again?
            </a>
        </small>
    </div>
{% endblock content %}

```
At this point if we try to open in our browser our login page, it will have some
functionality but, it will try -by default- to redirect us to **accounts/profile**.
So as to make the redirection to work as we wish we go to our _<Project's Name>/settings.py_
file and we add the url that we want to be redirected, inside the LOGIN_REDIRECT_URL
variable.
```python
# <Project's Name>/settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yxtmgmx5^u($d7wr$75s9p@0r6f@%9%i%g#*iyrcun8ulz2)j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',

    # --------------------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
.....

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'

```
## Creating a Profile
___
To create a profile for our users, we first create a view inside our _<App's Name>.views.py_
file.

```python
# <App's Name>/views.py

from django.shortcuts import render, redirect
from django.contrib import messages  # Importing flash message. It is an easy way
                                     # to sent one time alerts to a template.
from users.forms import UserRegisterForm


# Redirecting to the login page, after user creation
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Saving our user to our database.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
            print()
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def profile(request):
    return render(request, 'users/profile.html')

```
Then we go to our templates folder and create our _profile.htm_ file, then we
import it's url to our <Project's Name>/urls.py file and after that we pass our
profile to our base.html file to be shown.
```html
<!-- templates/<App's Name>/profile.html -->

{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <h1>{{ user.username }}</h1>
{% endblock %}

```
```python
# <Project's Name>/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views  # Login and Logout views
from django.urls import include, path
from users import views as user_views  # Altenative way of importing our urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Since we want our blog app to be our default page, we leave the stirng blank.
    path("", include("blog.urls")),
    path('register/', user_views.register, name='register'),
    path(
        'login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),

    path('profile/', user.views.profile, name='profile')
]

```
```html
<!-- templates/<App's Name>/base.html -->
{% load static %}

<!DOCTYPE html>
<html lang="en">

    <head>
        .....
    </head>
    <body>
        .....
        <div class="navbar-nav">
            {% if user.is_authenticated %}
                <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
                <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
            {% else %}
                <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
                <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
            {% endif %}
        </div>
        .....
    </body>
</html>

```
Now in order to restrict access to our profile page only for users who are logged
in, we browse back to our _<App's Name>/view.py_ file and we import the django.contrib.auth.decorators
module. Now by doing so if someone tries to view the profile without being logged in by
default will be redirected to accounts/login/?next=/profile/ url. So we will also
have to declare to django our login route. To declare so, we do by passing a
LOGIN_URL variable to our _<Project's Name>/settings.py_
```python
# <App's Name>/views.py

from django.shortcuts import render, redirect
from django.contrib import messages  # Importing flash message. It is an easy way
                                     # to sent one time alerts to a template.
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm


# Redirecting to the login page, after user creation
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Saving our user to our database.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
            print()
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

```
```python
# <Project's Name>/settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yxtmgmx5^u($d7wr$75s9p@0r6f@%9%i%g#*iyrcun8ulz2)j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',

    # --------------------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
.....

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'

LOGIN_URL = 'login'

```
## Adding a Profile Picture
___

To be able to add a profile picture, we must first extend our User model. To do
so, we go to our <App's Name>/models.py file and create a _Profile_ model that
has "one to one relationship" with the _User_ model. "One to one relationship"
means that one User is associated with one profile and vice versa.

```python
# <App's Name>/models.py

from django.db import models
from django.contrib.auth.models import User  # Importing our default User model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

```
_Note: For django database to be able to use pictures we must install the Pillow package._<br>

After those steps we execute the previously mentioned [procedure](#db) in order
to update our database. Moving on we register our models to our _<App's Name>/admin.py_
module.
```python
# <App's Name>/admin.py

from django.contrib import admin
from users.models import Profile

admin.site.register(Profile)

```
With our actions so far our users profile pictures will be saved in a profile_pic
inside our projects root folder. Since we do not want to clutter our root folder
with different non App's folders containing pictures, videos etc. we can adjust
our <Project's Name > settings by adding a MEDIA_ROOT and a MEDIA_PATH variable.
```python
# <Project's Name>/settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yxtmgmx5^u($d7wr$75s9p@0r6f@%9%i%g#*iyrcun8ulz2)j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',

    # --------------------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
.....

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = PurePath(BASE_DIR).joinpath('media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'

LOGIN_URL = 'login'

```
Having completed these steps, now we must adjust our _profiles.html_ template
to be able to show our users profile pictures.
```html
<!-- <App's Name>/templates/<App's name>/profile.html -->

{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
<div class="content-section">
    <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
        <h2 class="account-heading">{{ user.username }}</h2>
        <p class="text-secondary">{{ user.email }}</p>
        </div>
    </div>
    <!-- FORM HERE -->
</div>
{% endblock %}

```
And finally we go to Django documentation and we see how to deploy static files.
So per documentation we browse to our <Project's name>/urls.py file.
```python
# <Project's Name>/urls.py

rom django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views  # Altenative way of importing our urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Since we want our blog app to be our default page, we leave the stirng blank.
    path("", include("blog.urls")),
    path('register/', user_views.register, name='register'),
    path(
        'login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path('profile/', user_views.profile, name='profile')

]

# ------------------------------Adding Static Files-----------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
## Creating a Profile for each New User Automatically.
___
To be able with each new register user to have a profile automatically created
we must first create in our <App's Name> folder a signals.py file, tight this
automation and after that we must import those signals to our <App's name>/apps.py file.
```python
# <App's Name>/signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile


# Creating our profile.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Save a profile each time a user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

```
```python
# <App's Name>/apps.py

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

```
## Updating User Profile and Profile Picture.
In order to be able to update our user info and our profile picture, we must first
create the required forms to do so. So we browse to our _<App's Name>/forms.py_
file and after we import the necessary models we create them.
```python
# <App's Name>/forms.py

# We create a custom form by inheriting from the django.form class.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adds the email field to our form.

    class Meta:  # In this class, we specify the model that we want our form to
        # interact with. So, whenever this form validates it's creating
        # a new user.
        # This class gives us a namespace for configurations and keeps
        # them in one place.
        model = User
        fields = [  # These are the fields - and their order- that are going to
                    # be shown in our form.
            'username',
            'email',
            'password1',
            'password2'
        ]


# User info, update.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Profile picture, update.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

```
After we have those forms created, we browse to our _<App's Name>/views.py_ file
we import them and we create instances of those in our _profile_ method.
```python
# <App's Name>/views.py

from django.contrib import messages  # Importing flash message. It is an easy way
                                     # to sent one time alerts to a template.

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


# Redirecting to the login page, after user creation
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Saving our user to our database.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        update_UserForm = UserUpdateForm(request.POST, instance=request.user)
        update_ProfileForm = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if update_UserForm.is_valid() and update_ProfileForm.is_valid():
            update_UserForm.save()
            update_ProfileForm.save()

            messages.success(request, 'The Account has been Updated')
            return redirect('profile')
    else:
        update_UserForm = UserUpdateForm(instance=request.user)
        update_ProfileForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update_UserForm': update_UserForm,
        'update_ProfileForm': update_ProfileForm
    }

    return render(request, 'users/profile.html', context)

```
The next step is to pass our forms to our template. So in our profile.html template
we do just that.
```html
<!-- <App's Name>/templates/<App's Name>/profile.html -->

{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}

<div class="content-section">
    <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
            <h2 class="account-heading">{{ user.username }}</h2>
            <p class="text-secondary">{{ user.email }}</p>
        </div>
    </div>
    <!-- We add the enctype attribute in order to be able to upload pictures -->
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">
                Profile Info
            </legend>
            {{ update_UserForm|crispy  }}  <!-- Our inserted forms -->
            {{ update_ProfileForm|crispy  }}  <!-- Our inserted forms -->
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">
                Update
            </button>
        </div>
    </form>
</div>
{% endblock %}

```
Finally in order to resize our pictures after any update, we are going to override
the _save_ method of our model.
```python
# <App's Name>/models.py

from django.db import models
from django.contrib.auth.models import User  # Importing our default User model
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pics/default.jpeg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} Profile"

```
# Create, Update, and Delete Posts
For ease, in order to have the functionality of making CrUD operations to our posts
we can have **class based views**. We can import those views in our _<App's Name>/views.py_
file.
```python
# <App's Name>/views.py

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import \
    Post  # Importing this module in order to query our database
          # and pass the values that we want, to be rendered.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


def about(request):
    return render(request, 'blog/about.html')

```
+ Our first _class view_, which is a ListView, since it replaces our home function
needs to specify some attributes in order to work properly. By default the class
ListView will search for a template with the naming convention:


    > <'app'>/<'model'>_<'view-type'>.html,

    <br>then will try to replace it's context with the name _object_ -instead the post we
    have already specified- and finally since we want our blog-posts to be shown
    from the newest to the oldest, we must specify the ordering.
    ```python
    # <App's Name>/views.py
    .....

    class PostListView(ListView):
        model = Post
        template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
        context_object_name = 'posts'
        ordering = ['-date_posted']
    .....

    ```
+ The _LoginRequiredMixin_ and _UserPassesTestMixin_ are there to ensure that a
user is logged in and only if owns that instance of those classes is able to
manipulate them. The _form_valid_ method is to pass to our classes the current
author, which in this case is the current user.

+ Now in order to have our created instances to be properly redirected, we go
to our Post model and we add the _get_absolute_url_ method. We use the reverse
method, because we want a string of the full url that we want to be redirected
so we will let the _view_ to do the redirect for us.
    ```python
    # <App's Name>/models.py

    from django.contrib.auth.models import User
    from django.db import models
    from django.urls import reverse
    from django.utils import timezone


    class Post(models.Model):

            title = models.CharField(max_length=100)
            content = models.TextField()
            # For arguments in our date attribute, among others, we can use the following:
            #       * auto_now=True , this gives us the time for every time the Post
            #               class is updated.
            #       * auto_now_add=True, this gives us the time the post Class is created.
            #       * default=timezone.now, this gives us the time the post Class is
            #               created but also allows us to change the time if we wish so.
            date_posted = models.DateTimeField(default=timezone.now)
            # We use the on_delete argument, so as to specify what happens when our user
            # gets deleted. By passing the CASCADE value, we have every post the deleted
            # user made, deleted as well.
            author = models.ForeignKey(User, on_delete=models.CASCADE)

            def get_absolute_url(self):
                    return reverse("post-detail", kwargs={"pk": self.pk})

            def __str__(self):
                    return self.title
    ```
+ We add the _success_url_ in our delete view, so we can be redirected to our
home-page when our deletion is successful.

After these steps are finished we go to our urls module and we import our views.
```python
# <App's Name>/urls.py

from django.urls import path

from blog import views
from blog.views import (PostCreateView, PostDetailView, PostListView, PostDeleteView,
                        PostUpdateView)

urlpatterns = [
    # Since we want it to be the blog homepage we leave the string, blank.
    path("", PostListView.as_view(), name="blog-home"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about", views.about, name="blog-about"),
]

```
# Pagination
In order to paginate our posts, at first, we can easily go to our class-based
list-view and add the attribute _paginate_by_.
```python
# <App's Name>/views.py

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import \
    Post  # Importing this module in order to query our database
          # and pass the values that we want, to be rendered.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7  # Number of posts per page.
.....

```
After that we can go to our _home.html_ template in order to create a way for the
user to be able to browse throughout our pages.
```html
<!-- <App's Name>/templates/<App's Name>/home.html -->

{% extends "blog/base.html" %}

{% block content %}
    {% for post in posts %}
        <article class="media content-section">
            <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
            <div class="media-body">
                <div class="article-metadata">
                    <a class="mr-2" href="{% url 'user-post' post.author.username %}">{{ post.author }}</a>
                    <!-- <small class="text-muted">{{ post.date_posted }}</small>
                    This renders our unformmated date -->
                    <small class="text-muted">{{ post.date_posted|date:"d-F o" }}</small>
                </div>
                <h2><a class="article-title" href="{% url 'post-detail' post.id %}">
                    {{ post.title }}
                </a></h2>
                <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
    {% endfor %}

    {% if is_paginated %}  <!-- Checking if our home page is paginated -->
        {% if page_obj.has_previous %} <!-- Creating a link to the first and the
        previous pages if those exist -->
            <a class="btn btn-outline-info mb-4" href="?page=1">
                First
            </a>
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">
                Previous
            </a>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}  <!-- Creating a loop so
        whenever we are on a page with adjustend pages, those to be shown -->
            {% if page_obj.number == num %}
                <a class="btn btn-info mb-4" href="?page={{ num }}">
                    {{ num }}
                </a>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                <a class="btn btn-outline-info mb-4" href="?page={{ num }}">
                    {{ num }}
                </a>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %} <!-- Creating a link to the last and the next
        pages if those exist -->
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">
                Next
            </a>
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">
                Last
            </a>

        {% endif %}
    {% endif %}

{% endblock content %}

```
## Creating Pagination per User Posts.
___
To be able to create a view that shows a specific user's posts, we first go to
our _<App's Name>/views.py_ and create a new class-bases list-view, where we add
a filter, provided by the _get_queryset_ method,
```python
# <App's Name>/views.py

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User  # Importing our User model.
from django.shortcuts import render, get_object_or_404  # importing a user filter
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.models import \
    Post  # Importing this module in order to query our database
          # and pass the values that we want, to be rendered.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7  # Number of posts per page.


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # Our view's .html file(to be created)
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        # Filters if a user indeed exists and returns a 404 page if it does not.
        # The 'kwargs' attribute, is the query parameters.
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Post.objects.filter(author=user).order_by('-date_posted')
.....

```
Continuing, we import our _UserPostListView_ into our urls.
```python
# <App's Name>/urls.py

from django.urls import path

from blog import views
from blog.views import (PostCreateView, PostDetailView, PostListView, PostDeleteView,
                        PostUpdateView, UserPostListView)

urlpatterns = [
    # Since we want it to be the blog homepage we leave the string, blank.
    path("", PostListView.as_view(), name="blog-home"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-post"),  # Our view
    path("about", views.about, name="blog-about"),
]

```
Finally we create our template. **Note:** we must also add our _{{ post.author.username }}_
variable to our _home.html_ and _profile.html_ templates, since -so far- we have
not mentioned sub-templates.
```html
<!-- <App's Name>/templates/<App's Name>/user_posts.html -->

{% extends "blog/base.html" %}

{% block content %}
    <h1 class="mb-3">Posts by {{ view.kwarg.username }} ({{ page_obj.paginator.count }})</h1>  <!-- Our users title -->
    {% for post in posts %}
        <article class="media content-section">
            <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
            <div class="media-body">
                <div class="article-metadata">
                    <a class="mr-2" href="{% url 'user-post' post.author.username %}">{{ post.author }}</a>
                    <!-- <small class="text-muted">{{ post.date_posted }}</small>
                    This renders our unformmated date -->
                    <small class="text-muted">{{ post.date_posted|date:"d-F o" }}</small>
                </div>
                <h2><a class="article-title" href="{% url 'post-detail' post.id %}">
                    {{ post.title }}
                </a></h2>
                <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
    {% endfor %}

    {% if is_paginated %}
        {% if page_obj.has_previous %}
            <a class="btn btn-outline-info mb-4" href="?page=1">
                First
            </a>
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">
                Previous
            </a>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
                <a class="btn btn-info mb-4" href="?page={{ num }}">
                    {{ num }}
                </a>
            {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                <a class="btn btn-outline-info mb-4" href="?page={{ num }}">
                    {{ num }}
                </a>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">
                Next
            </a>
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">
                Last
            </a>

        {% endif %}
    {% endif %}

{% endblock content %}

```
## Email and Password Reset
___
In django is build-in the ability to send a password-reset email with tokens.
All we have to do is similar to our login-logout system. First we import the
class based views inside our url's.
```python
# <Project's Name>/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views  # Altenative way of importing our urls

urlpatterns = [
.....
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',  # Inside the '<>' are the
                                                     # parameters we want to
                                                     # recieve to our url
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
.....
]
.....

```
After that we create the corresponding .html files inside our templates folder.
Then, as we want to use our .gmail to send our emails we save our email and password
to our .env folder (or the activate file).<br>
And finally we pass the following to our <Project's Name>/settings.py file.
```python
# <Project's Name>/settings.py

from pathlib import Path, PurePath
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

.....
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',

    # --------------------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
.....

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = PurePath(BASE_DIR).joinpath('media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')  # Retrieving our Environmental variables
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')

```
