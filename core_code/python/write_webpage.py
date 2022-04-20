import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import shutil
import re
import requests
import time

from admin import retrieve_list
from admin import retrieve_path
from admin import retrieve_ref


def write_webpage():
    """
    write html
    """

    write_html()
    copy_html()


def copy_html():
    """
    copy html
    """

    src_html = retrieve_path('index')
    dst_html = retrieve_path('docs_index')
    shutil.copy(src_html, dst_html)


def write_html():
    """
    write html
    """

    index_html = retrieve_path('index')

    f = open(index_html, 'w+')

    f.write('hello')
    f.close()
