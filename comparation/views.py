from django.shortcuts import render
import json
import urllib
import requests


# Create your views here.

def home(request):
    #my_url = request.POST.get("url")
    #my_device = request.POST.get("device")
    #APIKey = "AIzaSyALIsdCRDWuduGIy071_x5lOFsVgyq3WaE"

    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://developers.google.com&key=AIzaSyBx49mLr1xROPyOK7gXa_wtulSRkedGPd8"

    # API request
    result = urllib.request.urlopen(url.format(url)).read().decode('UTF-8')
    result_json = json.loads(result)

    print(result_json["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"])
    context = {
        "interactive": result_json["lighthouseResult"]["audits"]["interactive"],
        "speed_index": result_json["lighthouseResult"]["audits"]["speed-index"]
        
    }

    return render(request, 'home.html', context)





    #response = requests.get(
      #  '
     #   ).json()

   # return render(request, 'home.html',  {'response': response})

