from django.forms import ModelForm
from advocates.models import Session
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.utils import render_crispy_form

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['clientname', 'mobile', 'case_describe', 'track','court','hearing_date','status',]
    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-offset-1 col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.add_input(Submit('submit', 'Submit'))

