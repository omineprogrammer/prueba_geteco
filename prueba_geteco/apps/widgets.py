from django import forms


class CustomSelect(forms.Select):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'form-select'}
        super().__init__(*args, **kwargs)


class CustomTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'form-control'}
        super().__init__(*args, **kwargs)


class CustomTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {
            'class': 'form-control',
            'style': 'height: 124px'
        }
        super().__init__(*args, **kwargs)

