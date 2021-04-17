from django.contrib.auth.models import User  # We import the table User from
        # our database. Since this table was automatically creaded by Django
        # we can reference it by it's schema name.
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Every class that we create here, is a table to our database.
# Every class attribute is our table's columns.

# In order to update our database, we need to run, from the command shell,
# the  makemigrations, system argument, to our manage.py module. Then we use the
# migrate, system argument, in order to pass all of our changes.

# In order to see our ORM object, after  the makemigrations command we can go to
# the xxxx_initial.py file, inside our migrations folder.

# In ordrer to see our SQL code, inside our command shell, we use the following:
#       python manage.py sqlmigrate blog xxxxx
#           where:
#               * blog is the name of our app file
#               *  xxxxx is the numbers of the xxxxx_initial.py that we want to
#                      see the sql statements.


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
