# based on https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

from django import forms

class UploadFileForm(forms.Form):
    # title         = forms.CharField(max_length=50)
    file            = forms.FileField(label='Select a file.')
    upload_datetime = forms.CharField(label='Enter date manually... for now.')
    comment         = forms.CharField(label='Comment.', max_length=100)
