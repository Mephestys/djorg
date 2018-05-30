from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return "{0} / {1}".format(self.user, self.title)

  ######## Stretch Goals ########
  # Sharing notes between users
  # Hook into bookmarks
  # File attachments