from django import forms
class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=100)
    face_image = forms.FileField()