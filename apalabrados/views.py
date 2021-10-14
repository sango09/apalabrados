# Django
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
# Forms
from apalabrados.forms import UserInputText

# Models
from apalabrados.models import (Numbers, Texts, Characters)


class InputView(FormView):
    # Input text view
    template_name = 'input.html'
    form_class = UserInputText
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class DataListView(ListView):
    template_name = 'data.html'
    queryset = Numbers.objects.all()
    context_object_name = 'numbers'

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        context['texts'] = Texts.objects.all()
        context['characters'] = Characters.objects.all()
        return context
