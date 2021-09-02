from django.shortcuts import render
import json
import urllib
import requests


# Create your views here.

def home(request):
    #my_url = request.POST.get("url")
    #my_device = request.POST.get("device")
    APIKey = "AIzaSyALIsdCRDWuduGIy071_x5lOFsVgyq3WaE"
    my_url = request.POST.get("url")
    value = True

# https://developers.google.com
#    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={my_url}&key={APIKey}"
    if len(my_url)== 0:
      value = True
      context = {
          "value": value,
          "my_url": my_url,
      }
    else:
      value=False
      url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://developers.google.com&key={APIKey}"
      # API request
      result = urllib.request.urlopen(url.format(url)).read().decode('UTF-8')
      result_json = json.loads(result)

      context = {
          "my_url": my_url,
          "value": value,
          "interactive": result_json["lighthouseResult"]["audits"]["interactive"],
          "speed_index": result_json["lighthouseResult"]["audits"]["speed-index"]
      }
      
    return render(request, 'home.html', context)





    #response = requests.get(
      #  '
     #   ).json()

   # return render(request, 'home.html',  {'response': response})

