from django.shortcuts import render
from rest_framework import viewsets
from .models import MumbaiRoute
from .serializers import MumbaiRouteSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from requests import *

try:
	url="http://127.0.0.1:8000/mumbairoute"
	he = {
			"Authorization": "Token 391a3fead4bcc8d9e3152f28e39497a3e5dcac7c"
	}
	res = get(url, headers=he)
	print(res.status_code)
	if res.status_code == 200:
			data = res.json()
			msg = data["msg"]
			print(msg)
	else:
			print("bad credentials")
except Exception as e:
		print("issue" , e)
def home(request):
    if request.method == "POST":
        route = request.POST.get("route")
        if route == "1":
            res = "Colaba Deport To Khodadad Circle"
            msg = str(res)
        elif route == "2":
            res = "Nariman Point To Chruch Railway Station"
            msg = str(res)
        elif route == "3":
            res = "Colaba To Malabar Hill"
            msg = str(res)
        elif route == "4":
            res = "Bhuleshwar To Malabar Hill"
            msg = str(res)
        elif route == "5":
            res = "Antop Hill To Worli"
            msg = str(res)
        elif route == "6":
            res = "Nariman Point To CSMT"
            msg = str(res)
        elif route == "7":
            res = "Malabar Hill to Fort"
            msg = str(res)
        elif route == "8":
            res = "Tardeo To Colaba"
            msg = str(res)
        elif route == "9":
            res = "Worli To Colaba"
            msg = str(res)
        elif route == "10":
            res = "CSMT To Byculla(E)"
            msg = str(res)
        elif route == "11":
            res = "Sewri To Colaba"
            msg = str(res)
        elif route == "12":
            res = "Sion To Colaba"
            msg = str(res)
        elif route == "13":
            res = "Sion To Chruchgate"
            msg = str(res)
        elif route == "14":
            res = "Worli To Byculla Railway Station"
            msg = str(res)
        elif route == "15":
            res = "Mazgoan To Dharavi"
            msg = str(res)
        elif route == "16":
            res = "Matunga To Girgoan"
            msg = str(res)
        elif route == "17":
            res = "Wadala To Sewri"
            msg = str(res)
        elif route == "18":
            res = "Dadar To Worli"
            msg = str(res)
        elif route == "19":
            res = "Sion To Worli"
            msg = str(res)
        elif route == "20":
            res = "Andheri To Antop Hill"
            msg = str(res)
        elif route == "21":
            res = "Diamond Market(Bandra) To Bandra Railway Station"
            msg =  str(res)
        elif route == "22":
            res = "BKC To Bandra Railway Station"
            msg =  str(res)
        elif route == "23":
            res = "Wadala To Andheri"
            msg =  str(res)
        elif route == "24":
            res = "Goregoan To Sewri"
            msg = str(res)
        elif route == "25":
            res = "Mahim To Borivali"
            msg = str(res)
        elif route == "29":
            res = "Juhu To Dahisar"
            msg = str(res)
        elif route == "30":
            res = "Dahisar To Goregoan"
            msg = str(res)
	
        else:
            msg = "Please enter valid bus number"
        return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")

class MumbaiRouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MumbaiRoute.objects.all()
    serializer_class = MumbaiRouteSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

			