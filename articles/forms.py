from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data  # dictionary
        print('cleaned_data:', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'the office':
            self.add_error('title', 'this title is taken')
            # raise forms.ValidationError('this title is taken')

        if 'content' in content:
            self.add_error('content', 'This content is taken.')
            raise forms.ValidationError('Not Allowed.')
        return cleaned_data
