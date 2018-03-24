from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets
from app.models import Task

class TaskForm(ModelForm):

    class Meta:
        model =  Task
        fields = ('status', )

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
