from django.shortcuts import render

from forms import WidgetTest

def widget(request):
    
    template_dict = {}

    if request.method == 'POST':
#        import pdb; pdb.set_trace()
        form = WidgetTest(request.POST)
        if form.is_valid():
            template_dict['result'] = form.cleaned_data['youtube_id']
            initial = {'youtube_id': template_dict['result']}
            template_dict['form'] = WidgetTest(initial=initial)
        else: 
            template_dict['form'] = form
    else:
        template_dict['form'] = WidgetTest(initial={'youtube_id': '123'})
    return render(request, 'widget.html', template_dict)
