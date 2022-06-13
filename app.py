from flask import Flask, request, jsonify
import pickle
# import numpy as np
import pandas as pd

model = pickle.load(open('finalmodel1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "These errors sucks!!!"


@app.route('/predictor', methods=['POST'])
def predictor():
    new = request.get_json()
    marque = new['PC_Marque']
    cpu_marque = new['CPU_Marque']
    cpu_core = new['CPU_Core']
    cpu_generation = new['CPU_Generation']
    cpu_type = new['CPU_Type']
    ram_horloge = new['CPU_Horloge']
    ram_stockage = new['RAM_Stockage']
    ram_type = new['RAM_Type']
    ssd = new['SSD']
    hdd = new['HDD']
    gpu_marque = new['GPU_Marque']
    gpu_type = new['GPU_Type']
    gpu_version = new['GPU_Version']
    gpu_categorie = new['GPU_Categorie']
    gpu_capacité = new['GPU_Capacité']
    ecran_taille = new['ECRAN_Taille']
    ecran_resolution = new['ECRAN_Resolution']
    ecran_type = new['ECRAN_Type']
    etat = new['ETAT']

    options = {
        'PC_Marque': [marque],
        'CPU_Marque': [cpu_marque],
        'CPU_Core': [cpu_core],
        'CPU_Generation': [cpu_generation],
        'CPU_Type': [cpu_type],
        'CPU_Horloge': [ram_horloge],
        'RAM_Stockage': [ram_stockage],
        'RAM_Type': [ram_type],
        'SSD': [ssd],
        'HDD': [hdd],
        'GPU_Marque': [gpu_marque],
        'GPU_Type': [gpu_type],
        'GPU_Version': [gpu_version],
        'GPU_Categorie': [gpu_categorie],
        'GPU_Capacité': [gpu_capacité],
        'ECRAN_Taille': [ecran_taille],
        'ECRAN_Resolution': [ecran_resolution],
        'ECRAN_Type': [ecran_type],
        'ETAT': [etat],

    }

    input_query = pd.DataFrame(data=options)
    result = model.predict(input_query)[0]

    return jsonify(result.round().tolist(), 'DA')


if __name__ == '__main__':
    app.run(debug=True, host="192.168.43.223", port=5111)
