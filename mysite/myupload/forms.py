# based on https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

from django import forms

class UploadFileForm(forms.Form):
    # title         = forms.CharField(max_length=50)
    file            = forms.FileField(
        label    ='Please select a file.',
        required =True
    )
    
    upload_datetime = forms.DateTimeField(
        label    ='Enter date manually... for now.',
        widget   =forms.SelectDateWidget(),
        required =True
    )

    comment         = forms.CharField(
        label      ='Comment.',
        widget     =forms.Textarea,
        max_length =100,
    )
