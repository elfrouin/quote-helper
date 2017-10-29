#!/usr/bin/env python

import requests


class ImportDisp:
    def __init__(self, name_file):
        self.name_file = name_file

    def load_dispo(self):
        url = "http://jpco-jeunesplants.com/newsletter/DisponibleLaFORET.xlsx"
        resp = requests.get(url)
        output = open(self.name_file, 'wb')
        output.write(resp.content)
        output.close()

class ImportRequest:
    def __init__(self, name_file):
        self.name_file= name_file

    def load_request(self):
        path_request='.xls'
