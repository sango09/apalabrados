"""User input text"""

# Python
import re

# Django
from django import forms

# Models
from apalabrados.models import (
    Numbers,
    Texts,
    Characters
)


class UserInputText(forms.Form):
    input_text = forms.CharField()

    def clean(self):
        # Verifies that the input contains numbers, special characters or plain text.

        data = super().clean()
        user_text = data['input_text'].lower()
        simbols_to_find = re.compile('[@_!#+,¨´$%^&*()<>?/\|}{~:\u00C0-\u00FF]')
        only_numbers = []
        only_special_characters = []

        for text in user_text:
            if text.isnumeric():
                only_numbers.append(int(text))
                user_text = user_text.replace(text, '')
            elif simbols_to_find.search(text) is not None:
                only_special_characters.append({'character': text})
                user_text = user_text.replace(text, '')

        user_text = ' '.join(user_text.split())
        split_characters = [{'text': i, 'initial': i[0], 'final': i[-1]} for i in user_text.split(' ')]
        data = {
            'numbers': only_numbers,
            'special_characters': only_special_characters,
            'texts': split_characters
        }
        return data

    def save(self):
        # Create new rows of  input text
        data = self.cleaned_data
        for number in data.get('numbers'):
            last_number = Numbers.objects.last()
            if last_number:
                accumulate = number + last_number.accumulated
            else:
                accumulate = number
            Numbers(number=number, accumulated=accumulate).save()

        [Texts(**text).save() for text in data.get('texts')]
        [Characters(**character).save() for character in data.get('special_characters')]
