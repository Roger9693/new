from django.shortcuts import render

def custom_404_page(Request, exception):
    return render(Request, '404.html', status=404)