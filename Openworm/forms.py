from django import forms
from models import Plate

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "id: " + str(obj.id) + " name: "+ obj.name

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    shorttitle = forms.CharField(max_length=20)
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    fps = forms.IntegerField()
    numframes = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    micronsperpixel = forms.IntegerField()
    platekey = MyModelChoiceField(queryset=Plate.objects.all())
    file  = forms.FileField()