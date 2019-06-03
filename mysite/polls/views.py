from django.shortcuts import render
from .models import SentimentAnalysisModel, SpamDetectionModel
from django import forms
import plotly

class MyForm(forms.Form):

    # A class for a form with two airport codes

    code1 = forms.CharField(max_length=500)


def formview(request):

        # If the form has been submitted...
    if request.method == 'POST':

        # A form bound to the POST data that has fields for user name and user password
        form = MyForm(request.POST)

        # All validation rules pass
        if form.is_valid():

            # first airport code
            code1 = form.cleaned_data['code1']
            checkbox = request.POST.getlist('checkbox')

            # checkbox = ['1'] Sentiment Analysis
            if len(checkbox) == 1 and checkbox[0] == '1':
                sa = SentimentAnalysisModel()
                mylat1, fig = sa.get_code(code1)

                if mylat1[0] == 1:
                    result = "Positive"
                else:
                    result = "Negative"
            # checkbox = ['2'] Spam detection
            else:
                sa = SpamDetectionModel()
                mylat1 = sa.get_code(code1)
                if mylat1[0] == 1:
                    result = "Spam"
                else:
                    result = "Not Spam"

            return render(request, 'polls/out.html', {'distance':result, 'input':code1, 'fig':fig})


    else:
        # An unbound form
        form = MyForm()

    # pass variables: form
    return render(request, 'polls/index.html', {'form': form})
