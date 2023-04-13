import requests
from django.shortcuts import render

def search(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        response = requests.get(f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album')
        results = response.json()['results']
        return render(request, 'search/results.html', {'results': results})
    else:
        return render(request, 'search/search.html')
