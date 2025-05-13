from django.db import models
from django.urls import reverse

# import from other app#
# from accounts.models import User
from django.contrib.auth import get_user_model

# getting user model object
# User = get_user_model()


# Create your models here.
class Post(models.Model):
    """
    this is a class to define posts for blog app
    """

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )  # ('Category') -> do category function is down of Post calss we type Category between ''

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    # function for serialzer
    def get_snippet(self):
        return self.content[0:5]  # return 5 char of content

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
