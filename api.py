from flask import Flask, request, jsonify

#exec model.py
import model

#model.py containing calculate_relevance_for_object_types(radius, object_types, region) function

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    radius = request.args.get('radius')
    object_types = request.args.get('object_types')
    regions = request.args.get('regions')
    return jsonify(model.calculate_relevance_for_object_types(radius, object_types, regions))

if __name__ == '__main__':
    app.run()

#example url request
#127.0.0.1:5000/api?radius=1000&object_types=kiosk,tc,mfc,dk,library,sport&regions=район+Ясенево