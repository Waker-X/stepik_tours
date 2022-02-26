def tours_by_departure(tours: dict, departure: str) -> dict:
    tours_departure = {}
    for id, tour in tours.items():
        if tour['departure'] == departure:
            tours_departure[id] = tour
    return tours_departure
