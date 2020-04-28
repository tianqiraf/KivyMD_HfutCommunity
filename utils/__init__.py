from kivy.app import App
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest

import os
import json
import time

app = App.get_running_app()

def is_json(data):
    try:
        json.loads(data)
    except:
        return False
    return True

def write_oldata(fpath, data):
    with open(fpath, 'w') as f:
        f.write(data)

def on_success(req, oldata, endpoint):
    # got new data, update the schedule
    ndata = None
    with open(req.file_path, 'rb') as f:
        ndata = f.read().decode('utf-8')
    if ndata == oldata:
        return

    if not is_json(ndata):
        write_oldata(req.file_path, oldata)
        return
    # check which endpoint got a response
    scr = {'schedule':'screenschedule',
        "tracks": 'screentalks',
        'sponsors': 'screensponsor',
        'about': 'screenabout',
        'venue': 'screenvenue',
        'community': 'screencommunity'}[endpoint]
    getattr(app, scr).on_enter(onsuccess=True)


def _check_data(req, oldata):
    ndata = None
    with open(req.file_path, 'rb') as f:
        ndata = f.read().decode('utf-8')
    if ndata == oldata:
        return
    # data is invalid in file
    # overwrite file with old data

    write_oldata(req.file_path, oldata)

def on_failure(req, oldata, endpoint):
    _check_data(req, oldata)


def on_error(req, oldata, endpoint):
    _check_data(req, oldata)

def fetch_remote_data(dt):
    '''Fetch remote data from the endpoint
    '''
    endpoint, filepath, oldata = fetch_remote_data._args
    req = UrlRequest(
        #FIXME: initial url should be abstracted out too.
        'http://conference.pydelhi.org/api/' + endpoint + '.json',
        file_path=filepath,
        on_success=lambda req ,r2:on_success(req, oldata, endpoint),
        on_error=lambda req ,r2:on_error(req, oldata, endpoint),
        on_failure=lambda req ,r2:on_failure(req, oldata, endpoint),
        timeout=15)

trigger_fetch_remote_data = Clock.create_trigger(fetch_remote_data, 9)
'''Trigger fetching of data only once every 9 seconds
'''

def get_json(endpoint):
    filepath = './data/json/' + endpoint + '.json'
    # use old data to check if anything in the data has been updated.
    oldata = None
    with open(filepath, 'rb') as f:
        oldata = f.read().decode('utf-8')
    jsondata = json.loads(oldata)

    return jsondata
