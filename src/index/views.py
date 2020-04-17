from django.views.generic import ListView

from tractor.models import Tractor


class IndexView(ListView):
    model = Tractor
    template_name = 'index/index.html'
    context_object_name = 'tractors'
