from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from meteoserver.api.forms import WeatherForm, FIELD_MAP


@method_decorator(csrf_exempt, name="dispatch")
class LogView(View):
    def post(self, request, *args, **kwargs):
        good_keys = {FIELD_MAP[k]: v for k, v in request.POST.items() if k in FIELD_MAP}
        form = WeatherForm(data=good_keys)
        if form.is_valid():
            form.save()
            return HttpResponse(content=b"Success", content_type="text/plain", status=201)
        print(request.POST)
        return HttpResponse(content=b"Wrong request", content_type="text/plain", status=400)
