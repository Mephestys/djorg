from django import forms
from .models import Bookmark, PersonalBookmark

class BookmarkForm(forms.ModelForm):
  class Meta:
    model = Bookmark
    fields = ('url', 'name', 'notes')

class PersonalBookmarkForm(BookmarkForm):
  class Meta:
    model = PersonalBookmark
    fields = BookmarkForm.Meta.fields