from rest_framework import serializers, viewsets
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import Note

class NoteSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
  tags = TagListSerializerField()
  def create(self, validated_data):
    # import pdb; pdb.set_trace()
    user = self.context['request'].user
    note = Note.objects.create(user=user, **validated_data)
    return note

  class Meta:
    model = Note
    fields = ('title', 'content', 'tags')

class NoteViewSet(viewsets.ModelViewSet):
  # Prevent anonymous users from seeing other users notes
  def get_queryset(self):
    user = self.request.user
    return Note.objects.filter(user=user)
  
  serializer_class = NoteSerializer
  queryset = Note.objects.all()