from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse(
        "404: Page not found <br><br> <button onclick="" href = '';"">Go to homepage</button>"
        )