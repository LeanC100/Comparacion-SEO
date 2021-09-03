from django.shortcuts import render
import json
import urllib
import requests
from .models import Site

# Create your views here.

def home(request):

    if request.method == "POST":
      if request.POST.get('url1'):
        # sitio 1
        my_url1 = request.POST.get("url1")
        date1 = date_site(my_url1)
        new_site = Site(
                        url=my_url1, 
            speed_index=date1["speed_index"]["displayValue"],
            time_to_interactive=date1["interactive"]["displayValue"]
        )
        new_site.save()

        # sitio 2
        my_url2 = request.POST.get("url2")
        date2 = date_site(my_url2)
        new_site = Site(
            url=my_url1,
            speed_index=date2["speed_index"]["displayValue"],
            time_to_interactive=date2["interactive"]["displayValue"]
        )
        new_site.save()

        context = {
            "date1": date1,
            "date2": date2,
        }
        return render(request, 'home.html', context)

    return render(request, 'home.html')

def date_site(value):

    APIKey = "AIzaSyALIsdCRDWuduGIy071_x5lOFsVgyq3WaE"
    my_url = value
    url_status = True
    
    if my_url is None:
      url_status = True
      my_url = None
      context = {
          "url_status": url_status,
          "my_url": my_url,
      }
    else:

      url_status = False
      url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={my_url}&key={APIKey}"
      # API request
      result = urllib.request.urlopen(url.format(url)).read().decode('UTF-8')
      result_json = json.loads(result)

      context = {
          "my_url": my_url,
          "url_status": url_status,
          "speed_index": result_json["lighthouseResult"]["audits"]["speed-index"],
          "interactive": result_json["lighthouseResult"]["audits"]["interactive"]
      }

    # guarda en la base de datos
    return context
