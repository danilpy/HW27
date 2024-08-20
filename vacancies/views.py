from django.http import HttpResponse, JsonResponse

from vacancies.models import Vacancy


def hello(request):
    return HttpResponse("Hello World!")


def index(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()

        response = []
        for vacancy in vacancies:
            response.append({
                'id': vacancy.id,
                'text': vacancy.text
            })

    return JsonResponse(response, safe=False)
