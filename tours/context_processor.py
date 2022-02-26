from tours.data import title, departures


def navbar_context(request):
    return {'title': title,
            'departures': departures}
