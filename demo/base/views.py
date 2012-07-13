from django.shortcuts import render, render_to_response

from forms import WidgetTest, ModelTestForm
from models import ModelTest

def field(request):

    template_dict = {}

    if request.method == 'POST':
        form = WidgetTest(request.POST)
        if form.is_valid():
            template_dict['result'] = form.cleaned_data['youtube_id']
            initial = {'youtube_id': template_dict['result']}
            template_dict['form'] = WidgetTest(initial=initial)
        else:
            template_dict['form'] = form
    else:
        template_dict['form'] = WidgetTest(initial={'youtube_id': '123'})
    return render(request, 'field.html', template_dict)

def model(request):

    template_dict = {}

    if request.method == 'POST':
        form = ModelTestForm(request.POST)
        if form.is_valid():
            m = form.save()
            return render_to_response('single.html', {'video': m})
        else:
            template_dict['form'] = form
    else:
        template_dict['form'] = ModelTestForm()
    return render(request, 'field.html', template_dict)


def videos(request):
    return render_to_response('list.html', {'videos': ModelTest.objects.all()})

def late(request):
    return render_to_response('late.html')

def more(request):
    return render_to_response('more.html', {'videos': ModelTest.objects.all()})
