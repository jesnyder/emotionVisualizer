import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from serpapi import GoogleSearch
import re
import requests
import time

from admin import retrieve_list
from admin import retrieve_path
from admin import retrieve_ref


def coregister_wearables():
    """

    """

    print('begin coregister_wearables')


    for study_name in retrieve_ref('study_name'):
        print('study_name = ' + study_name)

        src_path = os.path.join(retrieve_path('source_data'), study_name)
        for folder in os.listdir(src_path):
            src_folder = os.path.join(src_path, folder)

            for file in os.listdir(src_folder):
                src_file = os.path.join(src_folder, file)

                if 'IBI' in file: continue
                elif 'tags' in file: continue
                elif 'info' in file: continue
                elif '.DS_Store' in file: continue

                print('src_file = ' + str(src_file))

                contents = retrieve_list(src_file)
                print('len = ' + str(len(contents)))



    print('completed coregister_wearables')


if __name__ == "__main__":
    main()
