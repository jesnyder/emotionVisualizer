from bs4 import BeautifulSoup
from datetime import datetime
import json
import lxml
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
import pandas as pd
from serpapi import GoogleSearch
import re
import requests
import time


def retrieve_list(name):
    """
    from a path name or a path
    return the list in a csv
    """

    try:
        file_src = retrieve_path(name)
    except:
        file_src = name

    df = pd.read_csv(file_src)

    for name in df.columns:
        df_list = list(df[name])

    return(df_list)


def retrieve_path(name):
    """
    retrieve saved path name
    create folders, if they do not already exist
    """
    src_file = os.path.join('user_provided', 'admin', 'paths.csv')
    df = pd.read_csv(src_file)

    df = df[(df['name'] == name)]
    path = list(df['path'])
    path = path[0]
    path = path.split(' ')


    for i in range(len(path)):

        print('i = ' + str(i))

        if '.' in path[i]: continue

        if i == 0: path_short = os.path.join(path[0])
        else: path_short = os.path.join(path_short, path[i])

        print('path_short = ')
        print(path_short)

        if not os.path.exists(path_short):
            os.makedirs(path_short)

    path = os.path.join(*path)
    return(path)


def retrieve_ref(name):
    """
    retrieve reference value saved in admin file
    """

    df = pd.read_csv(retrieve_path('admin_ref'))
    df = df[(df['name'] == name)]

    value = list(df['value'])
    value = value[0]

    if ' ' in value:
        value = value.split(' ')

    else:
        try:
            value = float(value)
        except:
            value = str(value)

    return(value)
