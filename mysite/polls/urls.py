from django.conf.urls import url
from .views import formview

# The main page is airapp/test. This is the gateway.
# If the user successfully enters two airport codes, okay
# Otherwise, he goes to airapp/fail
# the airapp/get_names is used for autocomplete


urlpatterns = [
    # main view of the app
    url(r'^test/$', formview),
]