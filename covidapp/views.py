from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "1661f2fde0mshbb6c45b45fdd8b9p1b4c21jsn490fd0c42abd",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def hello_world_view(request):
    if request.method == 'POST':
        selected_country = request.POST['selected_country']
        print(selected_country)

    results = int(response['results'])
    my_list = []
    for i in range(0, results):
        my_list.append(response['response'][i]['country'])
        context = {'my_list': my_list}
    return render(request, 'helloworld.html', context)
