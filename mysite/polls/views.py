from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Airport
from django import forms


class MyForm(forms.Form):

    # A class for a form with two airport codes

    code1 = forms.CharField(max_length=50)
    code2 = forms.CharField(max_length=50)


def formview(request):

        # If the form has been submitted...
    if request.method == 'POST':

        # A form bound to the POST data that has fields for user name and user password
        form = MyForm(request.POST)

        # All validation rules pass
        if form.is_valid():

            # first airport code
            code1 = form.cleaned_data['code1']
            # second airport code
            code2 = form.cleaned_data['code2']

            #mydist = Airport.objects.get()
            #mylat1 = Airport.get_code(Airport)
            #mylat1 = Airport.objects.get(code=code1)
            #mylat2 = Airport.objects.get(code=code2)

            #mydist = code1 + " " + code2
            #mydist = 3.14
            a = Airport()
            mylat1 = a.get_code(code1)

            return render(request, 'polls/out.html', {'distance':mylat1})

            """
            # if not, go to "fail" page
            else:
                # Redirect to fail page after POST
                return HttpResponseRedirect('/polls/fail/')
            """

    else:
        # An unbound form
        form = MyForm()

    # pass variables: form
    return render(request, 'polls/index.html', {'form': form})


def failview(request):
    # A view to send user to the fail page if he enters the wrong airport codes'''

    return render(request, 'airapp/fail.html')