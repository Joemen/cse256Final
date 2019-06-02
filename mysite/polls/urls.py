from django.conf.urls import  url
from .views import formview, failview

# The main page is airapp/test. This is the gateway.
# If the user successfully enters two airport codes, okay
# Otherwise, he goes to airapp/fail
# the airapp/get_names is used for autocomplete


urlpatterns = [
    # main view of the app
    url(r'^test/$', formview),
    # this view is activated when the user input-ed codes are not found
    url(r'^fail/$', failview),
]