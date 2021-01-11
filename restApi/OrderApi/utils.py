from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
"""
Description :
this function renders a html template to a pdf using xhtml2pdf which is a python library.

parameters : 
template_src : thss first parameter which is the source template that we are going to render
context_dict: it's a dictionary which contains the params that we are going to put in our pdf 

what the function Returns :
 the function returns a HttpResponse(template converted, content_type='application/pdf') 
 
"""

def render_to_pdf(template_src, context_dict={}):

    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
