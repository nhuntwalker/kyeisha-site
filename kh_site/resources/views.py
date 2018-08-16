from django.views.generic import TemplateView
from resources.models import Category, Resource


class ResourceView(TemplateView):
    template_name = 'resources/resource_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['resources_left'] = Resource.objects.order_by('position').all()[::2]
        context['resources_right'] = Resource.objects.order_by('position').all()[1::2]
        return context
