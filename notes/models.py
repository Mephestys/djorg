from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

class UUIDTaggedNote(GenericUUIDTaggedItemBase, TaggedItemBase):
  class Meta:
    verbose_name = _("Tag")
    verbose_name_plural = _("Tags")

class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  tags = TaggableManager(through=UUIDTaggedNote)

  def __str__(self):
    return self.title

  ######## Stretch Goals ########
  # Sharing notes between users
  # Hook into bookmarks
  # File attachments