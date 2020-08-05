from django import forms

class AddTypeForm(forms.Form):
    name = forms.CharField(label = 'Name of the type: ', max_length = 10)
    language = forms.CharField(label = 'Language spoken: ', max_length = 20)

    def clean(self):
        cleaned_data = super(AddTypeForm, self).clean()
        name = cleaned_data.get("name")
        language = cleaned_data.get("language")

        #Check if name is not Sobaka because it's russian word

        error_context = dict()

        if (name == 'Sobaka'):
            error_context['name'] = 'Sobaka is not valid name!'
            raise forms.ValidationError(error_context)
        else:
            return cleaned_data
