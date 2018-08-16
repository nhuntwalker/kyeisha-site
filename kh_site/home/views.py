"""Some base-level views to be used."""
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class ContactView(TemplateView):
    """View for the contact page."""

    template_name = "base/contact.html"

    def get_context_data(self, **kwargs):
        """Add the Google API key to the context."""
        context = super().get_context_data(**kwargs)
        context['GOOGLE_KEY'] = settings.GOOGLE_KEY
        return context


def handler404(request):
    """Handle a 404 with a custom template."""
    response = render(request, 'base/404.html', context={})
    response.status_code = 404
    return response


def handler500(request):
    """Handle a 500 with a custom template."""
    response = render(request, 'base/500.html', context={})
    response.status_code = 500
    return response
