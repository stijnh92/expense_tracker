from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import discogs

# Create your views here.


def home(request):
    try:
        name = 'Stijn Houben'

        releases = discogs.releases()
        total_expense = discogs.get_total_expense(releases)

        values = {
            'name': name,
            'total_expense': total_expense,
            'count': len(releases),
            'releases': releases
        }
    except:
        raise Http404("Error parsing name")
    return render(request, 'expense_tracker/home.html', values)


@api_view(['GET'])
def get_releases(request):
    return Response(discogs.releases())
