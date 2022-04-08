# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:14:30 2022

@author: daniel pordeus

"""

import scipy.io as sio
import neurokit2 as nk
import os
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

DIRECTORY = "E:\\Doutorado\\Pesquisa\\Covid\\Dados\\"
SAMPLING_RATE_HZ= 256

#for each mat file... do...
feature_vector = pd.DataFrame()
patients = []
for filename in os.listdir(DIRECTORY):
    print(f"Processando arquivo {filename}")
    matlab = sio.loadmat(DIRECTORY + filename)
    #print(matlab["ECGch_2"].T.shape)
    data = matlab["ECGch_2"][:,0]
    try:
        df, info = nk.ecg_process(data, sampling_rate=SAMPLING_RATE_HZ)
        # Visualize
        #df.plot()
        analyze = nk.ecg_analyze(df, sampling_rate=SAMPLING_RATE_HZ)
        #print(analyze)
        #df = pd.concat()
        feature_vector = pd.concat((feature_vector, analyze))
        patients.append(filename)
    except Exception as err:
        print(f"Falha com dados do arquivo {filename}. Erro {err}")

feature_vector["PACIENTE"] = patients
feature_vector.reset_index()
print(feature_vector)

#feature_vector.to_csv("E:\\Doutorado\\Pesquisa\\Covid\\Saida_Covid.csv", index=None)
#Resolvido problema da conversão de locale
feature_vector.to_excel("E:\\Doutorado\\Pesquisa\\Covid\\Saida_Covid.xls", index=None)
