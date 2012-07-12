from django.shortcuts import render

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
            form.save()
            videos = ModelTest.objects.all()
            return render_to_response('list.html', {'videos': videos})
        else:
            template_dict['form'] = form
    else:
        template_dict['form'] = ModelTestForm()
    return render(request, 'field.html', template_dict)
        
