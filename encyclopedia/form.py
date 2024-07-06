from django import forms


class forms_se(forms.Form):
    form_search = forms.CharField(label="Search", max_length=100)

class forms_np(forms.Form):
    form_title = forms.CharField(label="Title", max_length=100)
    form_description = forms.CharField(widget=forms.Textarea, label="description")