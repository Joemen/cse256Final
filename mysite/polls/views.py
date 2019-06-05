from django.shortcuts import render
from .models import SentimentAnalysisModel, SpamDetectionModel
from django import forms

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
            radio = request.POST.getlist('radio')

            # checkbox = ['1'] Sentiment Analysis

            if len(radio) == 1 and radio[0] == '1':
                sa = SentimentAnalysisModel()
                mylat1, wl, proba = sa.get_code(code1)
                datatype = "Sentiment Analysis"
                ty = "positive"
                if mylat1[0] == 1:
                    result = "Positive"
                else:
                    result = "Negative"
            # checkbox = ['2'] Spam detection
            else:
                sa = SpamDetectionModel()
                mylat1, wl, proba = sa.get_code(code1)
                datatype = "Spam Detection"
                ty = "spam"
                if mylat1[0] == 1:
                    result = "Spam"
                else:
                    result = "Not Spam"

            return render(request, 'polls/out.html', {'ty':ty, 'pred':proba[0][0], 'table':wl, 'distance':result, 'input':code1, 'datatype':datatype})


    else:
        # An unbound form
        form = MyForm()

    # pass variables: form
    return render(request, 'polls/index.html', {'form': form})
