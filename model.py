import math
#:)
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

def calculate_relevance_for_object_types(radius, object_types, reg_type, regions):
    filtered_data_population = []
    regions = regions.split(',')
    if reg_type == 1:
        for i in range(len(data_population)):
            for region in regions:
                if data_population[i]['region'] == region:
                    filtered_data_population.append(data_population[i])
    elif reg_type == 2:
        for i in range(len(data_population)):
            for region in regions:
                if data_population[i]['region'] == region:
                    filtered_data_population.append(data_population[i])
    final_list = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    if 'kiosk' in object_types:
        with open('pechat_regional.json', 'r', encoding='utf-8') as f:
            data_kiosk = json.load(f)
        for i in range(len(data_kiosk)):
            for region in regions:
                if data_kiosk[i][1] == region:
                    final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
            #final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
    if 'tc' in object_types:
        with open('tc_regional.json', 'r', encoding='utf-8') as f:
            data_tc = json.load(f)
        for i in range(len(data_tc)):
            for region in regions:
                if data_tc[i][1] == region:
                    final_list['tc'].append([data_tc[i], 'tc'])
    if 'mfc' in object_types:
        with open('mfc_regional.json', 'r', encoding='utf-8') as f:
            data_mfc = json.load(f)
        for i in range(len(data_mfc)):
            for region in regions:
                if data_mfc[i][1] == region:
                    final_list['mfc'].append([data_mfc[i], 'mfc'])
    if 'dk' in object_types:
        with open('dk_regional.json', 'r', encoding='utf-8') as f:
            data_dk = json.load(f)
        for i in range(len(data_dk)):
            for region in regions:
                if data_dk[i][1] == region:
                    final_list['dk'].append([data_dk[i], 'dk'])
    if 'library' in object_types:
        with open('libraries_regional.json', 'r', encoding='utf-8') as f:
            data_library = json.load(f)
        for i in range(len(data_library)):
            for region in regions:
                if data_library[i][1] == region:
                    final_list['library'].append([data_library[i], 'library'])
    if 'sport' in object_types:
        with open('sport_regional.json', 'r', encoding='utf-8') as f:
            data_sport = json.load(f)
        for i in range(len(data_sport)):
            for region in regions:
                if data_sport[i][1] == region:
                    final_list['sport'].append([data_sport[i], 'sport'])
    relevance_data = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    #print(final_list)
    for obj_type in final_list:
        for obj in final_list[obj_type]:
            relevance = 0
            for house in filtered_data_population:
                if radius_formula(obj[0][0][0], obj[0][0][1], house['lat'], house['lon'], radius):
                    relevance += house['population']
            if relevance != 0:
                #print(obj)
                relevance_data[obj_type].append([[obj[0][0][1], obj[0][0][0]], obj[1], relevance])
    return relevance_data

def calculate_relevance_for_object_types_and_partnership(radius, object_types, reg_type, regions, partners):
    filtered_data_population = []
    filtered_data_partners = []
    regions = regions.split(',')
    partners = partners.split(',')
    if reg_type == 1:
        for i in range(len(data_population)):
            for region in regions:
                if data_population[i]['region'] == region:
                    filtered_data_population.append(data_population[i])
        for i in range(len(data_partners['postamats'])):
            for region in regions:
                for partner in partners:
                    if data_partners['postamats'][i][2] == region and data_partners['postamats'][i][0] == partner:
                        filtered_data_partners.append(data_partners['postamats'][i])
    elif reg_type == 2:
        for i in range(len(data_population)):
            for region in regions:
                if data_population[i]['region'] == region:
                    filtered_data_population.append(data_population[i])
        for i in range(len(data_partners['postamats'])):
            for region in regions:
                for partner in partners:
                    if data_partners['postamats'][i][2] == region and data_partners['postamats'][i][0] == partner:
                        filtered_data_partners.append(data_partners['postamats'][i])
    final_list = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    if 'kiosk' in object_types:
        with open('pechat_regional.json', 'r', encoding='utf-8') as f:
            data_kiosk = json.load(f)
        for i in range(len(data_kiosk)):
            for region in regions:
                if data_kiosk[i][1] == region:
                    final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
            #final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
    if 'tc' in object_types:
        with open('tc_regional.json', 'r', encoding='utf-8') as f:
            data_tc = json.load(f)
        for i in range(len(data_tc)):
            for region in regions:
                if data_tc[i][1] == region:
                    final_list['tc'].append([data_tc[i], 'tc'])
    if 'mfc' in object_types:
        with open('mfc_regional.json', 'r', encoding='utf-8') as f:
            data_mfc = json.load(f)
        for i in range(len(data_mfc)):
            for region in regions:
                if data_mfc[i][1] == region:
                    final_list['mfc'].append([data_mfc[i], 'mfc'])
    if 'dk' in object_types:
        with open('dk_regional.json', 'r', encoding='utf-8') as f:
            data_dk = json.load(f)
        for i in range(len(data_dk)):
            for region in regions:
                if data_dk[i][1] == region:
                    final_list['dk'].append([data_dk[i], 'dk'])
    if 'library' in object_types:
        with open('libraries_regional.json', 'r', encoding='utf-8') as f:
            data_library = json.load(f)
        for i in range(len(data_library)):
            for region in regions:
                if data_library[i][1] == region:
                    final_list['library'].append([data_library[i], 'library'])
    if 'sport' in object_types:
        with open('sport_regional.json', 'r', encoding='utf-8') as f:
            data_sport = json.load(f)
        for i in range(len(data_sport)):
            for region in regions:
                if data_sport[i][1] == region:
                    final_list['sport'].append([data_sport[i], 'sport'])
    relevance_data = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    for obj_type in final_list:
        for obj in final_list[obj_type]:
            relevance = 0
            for house in filtered_data_population:
                if radius_formula(obj[0][0][0], obj[0][0][1], house['lat'], house['lon'], radius):
                    relevance += house['population']
            for partner in filtered_data_partners:
                if radius_formula(obj[0][0][0], obj[0][0][1], partner[1][0], partner[1][1], 200):
                    relevance *= 1.5
            if relevance != 0:
                relevance_data[obj_type].append([[obj[0][0][1], obj[0][0][0]], obj[1], relevance])
    return relevance_data

def calculate_relevance_for_object_types_and_competition(radius, object_types, reg_type, regions, partners):
    filtered_data_population = []
    filtered_data_partners = []
    regions = regions.split(',')
    partners = partners.split(',')
    if reg_type == 1:
        for i in range(len(data_population)):
            for region in regions:
                if data_population[i]['region'] == region:
                    filtered_data_population.append(data_population[i])
        for i in range(len(data_partners['postamats'])):
            for region in regions:
                for partner in partners:
                    if data_partners['postamats'][i][2] == region and data_partners['postamats'][i][0] == partner:
                        filtered_data_partners.append(data_partners['postamats'][i])
    final_list = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    if 'kiosk' in object_types:
        with open('pechat_regional.json', 'r', encoding='utf-8') as f:
            data_kiosk = json.load(f)
        for i in range(len(data_kiosk)):
            for region in regions:
                if data_kiosk[i][1] == region:
                    final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
            #final_list['kiosk'].append([data_kiosk[i], 'kiosk'])
    if 'tc' in object_types:
        with open('tc_regional.json', 'r', encoding='utf-8') as f:
            data_tc = json.load(f)
        for i in range(len(data_tc)):
            for region in regions:
                if data_tc[i][1] == region:
                    final_list['tc'].append([data_tc[i], 'tc'])
    if 'mfc' in object_types:
        with open('mfc_regional.json', 'r', encoding='utf-8') as f:
            data_mfc = json.load(f)
        for i in range(len(data_mfc)):
            for region in regions:
                if data_mfc[i][1] == region:
                    final_list['mfc'].append([data_mfc[i], 'mfc'])
    if 'dk' in object_types:
        with open('dk_regional.json', 'r', encoding='utf-8') as f:
            data_dk = json.load(f)
        for i in range(len(data_dk)):
            for region in regions:
                if data_dk[i][1] == region:
                    final_list['dk'].append([data_dk[i], 'dk'])
    if 'library' in object_types:
        with open('libraries_regional.json', 'r', encoding='utf-8') as f:
            data_library = json.load(f)
        for i in range(len(data_library)):
            for region in regions:
                if data_library[i][1] == region:
                    final_list['library'].append([data_library[i], 'library'])
    if 'sport' in object_types:
        with open('sport_regional.json', 'r', encoding='utf-8') as f:
            data_sport = json.load(f)
        for i in range(len(data_sport)):
            for region in regions:
                if data_sport[i][1] == region:
                    final_list['sport'].append([data_sport[i], 'sport'])
    relevance_data = {'kiosk': [], 'tc': [], 'mfc': [], 'dk': [], 'library': [], 'sport': []}
    for obj_type in final_list:
        for obj in final_list[obj_type]:
            relevance = 0
            for house in filtered_data_population:
                if radius_formula(obj[0][0][0], obj[0][0][1], house['lat'], house['lon'], radius):
                    relevance += house['population']
            for partner in filtered_data_partners:
                if radius_formula(obj[0][0][0], obj[0][0][1], partner[1][0], partner[1][1], 200):
                    relevance /= 1.5
            if relevance != 0:
                relevance_data[obj_type].append([[obj[0][0][1], obj[0][0][0]], obj[1], relevance])
    return relevance_data

with open('full_house_final.json', 'r', encoding='utf-8') as f:
        data_population = json.load(f)

with open('postamats_regional.json', 'r', encoding='utf-8') as f:
        data_partners = json.load(f)

#print(calculate_relevance_for_object_types(400, ['kiosk', 'tc', 'mfc', 'dk', 'library', 'sport'], 1, 'район Ясенево,район Кунцево'))