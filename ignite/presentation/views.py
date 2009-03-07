from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from ignite.presentation.forms import PresentationForm
from ignite.presentation.models import Presentation

def presentation_detail(request, slug):
    try:
        presentation = Presentation.objects.get(slug=slug)
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
            return HttpResponseRedirect(reverse(presentation_detail, args=(new_presentation.slug,)))
        else:
            pass # Some error
    else:
        form = PresentationForm(instance=presentation)

    return render_to_response(
        'presentation/add.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

