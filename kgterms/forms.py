from django import forms
from .models import ApplicantAgreed


class AgreeToTermsForm(forms.ModelForm):
    i_agree = forms.BooleanField(initial=False)

    class Meta:
        model = ApplicantAgreed

    def __init__(self, *args, **kwargs):
        super(AgreeToTermsForm, self).__init__(*args, **kwargs)
