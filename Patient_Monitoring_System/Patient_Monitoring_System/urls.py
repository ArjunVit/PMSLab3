from django.urls import re_path
import PMS.views

urlpatterns = [
    re_path(r'^$', PMS.views.display_data, name='display_data'),
]

