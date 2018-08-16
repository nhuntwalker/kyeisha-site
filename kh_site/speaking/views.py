"""Views for handling speaking engagements."""
from django.http import Http404
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from speaking.models import Presentation
from speaking.serializers import PresentationSerializer


class PresentationsList(ListView):
    """View for listing presentations."""

    model = Presentation
    context_object_name = 'presentations'
    template_name = "speaking/speaking.html"
    queryset = Presentation.objects.order_by('order').all()

    def get_context_data(self, **kwargs):
        """Chop the presentations into pairs."""
        context = super().get_context_data(**kwargs)
        presentations = context[self.context_object_name]
        context['presentation_pairs'] = []

        for i in range(0, len(presentations) - 1, 2):
            context['presentation_pairs'].append([presentations[i], presentations[i + 1]])
        if len(presentations) % 2:
            context['orphan'] = presentations.last()
        return context


class PresentationsJSONList(APIView):
    """List all presentations."""

    def get(self, request, format=None):
        """Return all the presentations."""
        serialized = PresentationSerializer(Presentation.objects.all(), many=True)
        return Response(serialized.data)


class PresentationDetail(APIView):
    """Get the details for one presentation."""

    def get_object(self, pk):
        """Get an object or raise a 404."""
        try:
            return Presentation.objects.get(pk=pk)
        except Presentation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Return detail for one object."""
        presentation = self.get_object(pk)
        serialized = PresentationSerializer(presentation)
        return Response(serialized.data)
