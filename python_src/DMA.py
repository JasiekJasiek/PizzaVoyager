import requests

def get_distances(locations: list[str], API_KEY: str) -> list[list[int]]:

    # return [[1, 136000, 289000, 339000], 
    #        [138000, 1, 281000, 338000], 
    #        [290000, 280000, 1, 596000], 
    #        [340000, 336000, 596000, 1]]

    origins_str = "|".join(locations)
    destinations_str = "|".join(locations)

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origins_str}&destinations={destinations_str}&key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    distance_matrix = []

    if data["status"] == "OK":
        for i, origin in enumerate(locations):
            row = []
            for j, destination in enumerate(locations):
                element = data["rows"][i]["elements"][j]
                distance = float(element["distance"]["text"].split()[0]) * 1000 if element["distance"]["text"].split()[1] == 'km' else float(element["distance"]["text"].split()[0])
                row.append(distance)
            distance_matrix.append(row)

    return distance_matrix
