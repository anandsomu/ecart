from django.http import JsonResponse


def health_check(request):
    return JsonResponse({'status': 'I am OK.'})
