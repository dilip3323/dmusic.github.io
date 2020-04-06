from django.contrib.auth.models import User
from django import forms
from django.urls import reverse
from .models import Album, Song

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'year', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_name', 'audio_file']

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username', 'email', 'password']

        def get_absolute_url(self):
            return reverse('MyApp:index')