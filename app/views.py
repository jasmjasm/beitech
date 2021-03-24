from django.views.generic import TemplateView
from app.models import Customer

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        context.update({"customers": Customer.objects.all().order_by('name')})
        return context
