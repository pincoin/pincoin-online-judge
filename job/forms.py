from django import forms

from django.utils.translation import ugettext_lazy as _


class JobSearchForm(forms.Form):
    tech_stack = forms.CharField(
        label=_('Tech stack'),
        help_text=_(''),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Tech stack'),
            'class': 'input',
        }),
    )

    company = forms.CharField(
        label=_('Company title'),
        help_text=_(''),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Company title'),
            'class': 'input',
        }),
    )

    address = forms.CharField(
        label=_('Company address'),
        help_text=_(''),
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': _('Address (District|Province)'),
            'class': 'input',
        }),
    )

    def __init__(self, *args, **kwargs):
        tech_stack = kwargs.pop('tech_stack', '')
        company = kwargs.pop('company', '')
        address = kwargs.pop('address', '')

        super(JobSearchForm, self).__init__(*args, **kwargs)

        self.fields['tech_stack'].initial = tech_stack
        self.fields['company'].initial = company
        self.fields['address'].initial = address
