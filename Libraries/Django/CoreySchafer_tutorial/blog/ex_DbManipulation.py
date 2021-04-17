# In order to make a 'stand alone' script in django, we have to use the setup
# method first.
import django
django.setup()

from blog.models import Post  # Importing DB table Post
from django.contrib.auth.models import User  # Importing DB table User


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
# to our Post class, in the models.py module.
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
