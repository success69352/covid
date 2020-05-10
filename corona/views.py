from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect,requires_csrf_token
# Create your views here.
def home(request):
	return render(request,'cov_template.html.j2')
def covid(request):
	import requests
	import ast
	url = "https://api.covid19india.org/state_district_wise.json"

	payload = {}
	headers= {}

	response = requests.request("GET", url, headers=headers, data = payload)
	Total_cases = response.text.encode('utf8')
	if(Total_cases):
		dict_str = Total_cases.decode("UTF-8")
		global sorted_dicts 
		sorted_dicts = ()
		'''if request.method == "POST":
			if "button_id" in request.POST:
				button_id = request.POST["button_id"]
				return HttpResponse("success") # if everything is OK
			else:
				return HttpResponse(button_id)'''
		#return HttpResponse(request.method)
		state = request.POST
		lists = list(state)
		state_list = lists[0]
		data = ast.literal_eval(dict_str)
		#split = state.split("crsfmiddleware")
		# = list(split)
		#dictionary = dict(data)
		#return render(request,'result.html.j2',{'datas': data,'st':state_list})
		#state = request.POST.get('button_id')
		state_details = data[state_list]["districtData"]
		#mydict = dict(state_details)
		for s in sorted(state_details.items(), key=lambda x_y: x_y[1]['active'], reverse=False):
			sorted_dicts = (s) + sorted_dicts

		length = sorted_dicts.__len__()
		length /= 2
		mylength = int(length) 

		#state_values = data[state_list]["districtData"].values()
		#mydict = dict((y, x) for x, y in sorted_dicts)
		#return HttpResponse(mylength)
		return render(request,'result.html.j2',{'sd': sorted_dicts,'len': mylength,'range': range(mylength)})
		
		#for i in tn:
		#	return HttpResponse(i)
		#length = tn.__len__()
		#cbe = tn["districtData"]["Coimbatore"]
		
		#return HttpResponse(cbe.)
		#for i in tn.keys():
			#return HttpResponse(i,"\n")
		    #return HttpResponse(i,"\n","active:" ,tn[i]["active"],"confirmed: ",tn[i]["confirmed"],"deceased:" ,tn[i]["deceased"])
		
	else:
		return HttpResponse("Oops ! Something got wrong with the server")


