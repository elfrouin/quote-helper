#!/usr/bin/env python

import requests
import os

class ImportDisp:
    def __init__(self, name_file):
        self.name_file = name_file

    def load_dispo(self):
        url = "http://jpco-jeunesplants.com/newsletter/DisponibleLaFORET.xlsx"
        resp = requests.get(url)
        output = open(self.name_file, 'wb')
        output.write(resp.content)
        output.close()

class ImportDemand:
    def __init__(self, name_file):
        self.name_file= name_file

    def load_demand(self):
        path_request='../data-test/test.xlsx'
        os.system('cp %s %s' %(path_request, self.name_file))
