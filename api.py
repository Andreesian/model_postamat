from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import json
import csv

#exec model.py
import model

#model.py containing calculate_relevance_for_object_types(radius, object_types, region) function

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api', methods=['GET'])
def api():
    radius = request.args.get('radius')
    model_c = request.args.get('model')
    area = request.args.get('area')
    object_types = request.args.get('object_types')
    regions = []
    if area == 'rayon':
        rayons = request.args.get('rayons')
        regions = rayons
        reg_type = 1
    elif area == 'okruga':
        okrugas = request.args.get('okrugas')
        regions = okrugas
        reg_type = 2
    if model_c == '1':
        result = model.calculate_relevance_for_object_types(radius, object_types, reg_type, regions)
    elif model_c == '2':
        partners = request.args.get('partners')
        result = model.calculate_relevance_for_object_types_and_partnership(radius, object_types, reg_type, regions, partners)
    elif model_c == '3':
        partners = request.args.get('partners')
        result = model.calculate_relevance_for_object_types_and_competition(radius, object_types, reg_type, regions, partners)
    
    return jsonify(result)

@app.route('/exportcsv', methods=['GET'])
def apii():
    radius = request.args.get('radius')
    model_c = request.args.get('model')
    area = request.args.get('area')
    object_types = request.args.get('object_types')
    export_type = request.args.get('export_type')
    regions = []
    if area == 'rayon':
        rayons = request.args.get('rayons')
        regions = rayons
        reg_type = 1
    elif area == 'okruga':
        okrugas = request.args.get('okrugas')
        regions = okrugas
        reg_type = 2
    if model_c == '1':
        result = model.calculate_relevance_for_object_types(radius, object_types, reg_type, regions)
    elif model_c == '2':
        partners = request.args.get('partners')
        result = model.calculate_relevance_for_object_types_and_partnership(radius, object_types, reg_type, regions, partners)
    elif model_c == '3':
        partners = request.args.get('partners')
        result = model.calculate_relevance_for_object_types_and_competition(radius, object_types, reg_type, regions, partners)
    export_to_csv(result, 'export.csv')
    return send_file("export.csv", as_attachment=True)

#function to convert json to csv
def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['type', 'coords', 'relevance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in data:
            for i in data[d]:
                writer.writerow({'type': i[1], 'coords': i[0], 'relevance': i[2]})
    #open file as binary and return it

if __name__ == '__main__':
    app.run(app.run(host="0.0.0.0", port="5000"))

#example url request
#127.0.0.1:5000/api?radius=1000&model=1&object_types=kiosk,tc,mfc,dk,library,sport&area=rayon&rayons=район+Ясенево,район+Кунцево