import math

def radius_formula(lat1, lon1, lat2, lon2, n):
    R = 6371
    dLat = deg2rad(lat2-lat1)
    dLon = deg2rad(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d <= float(n) / 1000

def deg2rad(deg):
    return deg * (math.pi/180)

import json

def calculate_relevance(radius, x, y):
    relevance = 0
    with open('full_house_final.json', 'r', encoding='utf-8') as f:
        data_houses = json.load(f)
    for i in range(len(data_houses)):
        if radius_formula(x, y, data_houses[i]['lat'], data_houses[i]['lon'], radius):
            relevance += data_houses[i]['population']
    return relevance

def calculate_relevance_for_object_types(radius, object_types, regions):
    with open('full_house_final.json', 'r', encoding='utf-8') as f:
        data_population = json.load(f)
    filtered_data_population = []
    region = regions
    for i in range(len(data_population)):
        if data_population[i]['region'] == region:
            filtered_data_population.append(data_population[i])
    final_list = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    if 'kiosk' in object_types:
        with open('pechat_produkcii.json', 'r', encoding='utf-8') as f:
            data_kiosk = json.load(f)
        for i in range(len(data_kiosk)):
            final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
    if 'tc' in object_types:
        with open('coord_torg_objects.json', 'r', encoding='utf-8') as f:
            data_tc = json.load(f)
        for i in range(len(data_tc)):
            final_list['tc'].append([data_tc[i], 'tc'])
    if 'mfc' in object_types:
        with open('coord_gos_uslugi.json', 'r', encoding='utf-8') as f:
            data_mfc = json.load(f)
        for i in range(len(data_mfc)):
            final_list['mfc'].append([data_mfc[i], 'mfc'])
    if 'dk' in object_types:
        with open('coord_dom_culture.json', 'r', encoding='utf-8') as f:
            data_dk = json.load(f)
        for i in range(len(data_dk)):
            final_list['dk'].append([data_dk[i], 'dk'])
    if 'library' in object_types:
        with open('coord_biblioteki.json', 'r', encoding='utf-8') as f:
            data_library = json.load(f)
        for i in range(len(data_library)):
            final_list['library'].append([data_library[i], 'library'])
    if 'sport' in object_types:
        with open('coord_sport_objects.json', 'r', encoding='utf-8') as f:
            data_sport = json.load(f)
        for i in range(len(data_sport)):
            final_list['sport'].append([data_sport[i], 'sport'])
    relevance_data = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    for obj_type in final_list:
        for obj in final_list[obj_type]:
            relevance = 0
            for house in filtered_data_population:
                if radius_formula(obj[0][1], obj[0][0], house['lat'], house['lon'], radius):
                    relevance += house['population']
            if relevance != 0:
                relevance_data[obj_type].append([obj[0], obj[1], relevance])
    return relevance_data

#print(calculate_relevance_for_object_types(400, ['kiosk', 'tc', 'mfc', 'dk', 'library', 'sport'], ['район Ясенево', 'район Кунцево']))