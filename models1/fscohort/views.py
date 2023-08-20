from django.http import HttpResponse


def fscohort(request):
    return HttpResponse('''
    <h2>
    welcome to fscohort
    </h2>
    ''')
def goodbye(request):
    return HttpResponse('''
    <h2>
    thank you see you later.goodbye...
    </h2>
    ''')
