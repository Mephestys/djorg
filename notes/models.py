from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

class UUIDTaggedNote(GenericUUIDTaggedItemBase, TaggedItemBase):
  class Meta:
    verbose_name = ugettext_lazy("Tag")
    verbose_name_plural = ugettext_lazy("Tags")

class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  tags = TaggableManager(help_text="", through=UUIDTaggedNote, blank=True)

  def __str__(self):
    return "{0} / {1}".format(self.user, self.title)

  ######## Stretch Goals ########
  # Sharing notes between users
  # Hook into bookmarks
  # File attachments