from django.shortcuts import render
import json
import urllib
import requests


# Create your views here.

def home(request):

    if request.method == "POST":
      if request.POST.get('url1'):
        my_url1 = request.POST.get("url1")
        date1 = date_site(my_url1)
        my_url2 = request.POST.get("url2")
        date2 = date_site(my_url2)
        context = {
            "date1": date1,
            "date2": date2,
        }
        return render(request, 'home.html', context)

    return render(request, 'home.html')

    #response = requests.get(
      #  '
     #   ).json()

   # return render(request, 'home.html',  {'response': response})


def date_site(value):
    #my_url = request.POST.get("url")
    #my_device = request.POST.get("device")
    APIKey = "AIzaSyALIsdCRDWuduGIy071_x5lOFsVgyq3WaE"
    my_url = value
    url_status = True

# https://developers.google.com
#    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={my_url}&key={APIKey}"
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
          "interactive": result_json["lighthouseResult"]["audits"]["interactive"],
          "speed_index": result_json["lighthouseResult"]["audits"]["speed-index"]
      }
    
    return context
