from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer


# View for the doc rendering, access with /doc
@renderer_classes([TemplateHTMLRenderer])
def show_doc(request):
    template = loader.get_template("doc.html")
    return HttpResponse(template.render({}, request))
