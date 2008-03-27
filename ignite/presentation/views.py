from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.newforms import ModelForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from ignite.presentation.models import Presentation

#
# FORMS
#

class PresentationForm(ModelForm):
    class Meta:
        model = Presentation
        exclude = ('created',)

#
# VIEWS
# 

def presentation_detail(request, presentation_id):
    try:
        presentation = Presentation.objects.get(pk=presentation_id)
    except Presentation.DoesNotExist:
        raise Http404, "Sorry, the presentation you requested was not found."
 
    return render_to_response(
        'presentation/detail.html',
        {'presentation': presentation},
        context_instance=RequestContext(request)
    )
 
def presentation_list(request):

    presentations = Presentation.objects.all()

    if not presentations:
        raise Http404, "No presentations yet, sorry."
    
    return object_list(
        request,
        queryset=presentations,
        template_name='presentation/list.html',
        template_object_name='presentation',
        paginate_by=50,
    )

def presentation_add(request):
    presentation = Presentation()
    if request.method == 'POST':
        form = PresentationForm(data=request.POST, instance=presentation)
        if form.is_valid():
            new_presentation = form.save()
            return HttpResponseRedirect(reverse(presentation_detail, args=(new_presentation.id,)))
        else:
            pass # Some error
    else:
        form = PresentationForm(instance=presentation)

    return render_to_response(
        'presentation/add.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

