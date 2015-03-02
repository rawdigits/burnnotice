#!/usr/bin/python

import json
import fnmatch
import sys
import os
import urllib2
import zipfile
import shutil

DATA_DIR = 'data'

token = sys.argv[1]

def destroy_message(ts, channel):
    urllib2.urlopen('https://slack.com/api/chat.delete?token={}&ts={}&channel={}'.format(token, ts, channel))

def delete_history(channel_name, channel_file):
    messages = json.loads(open(channel_file, 'r').read())
    for message in messages:
        destroy_message(message["ts"], channel_hash[channel_name])


if __name__ == "__main__":
    if os.path.isdir(DATA_DIR):
        shutil.rmtree(DATA_DIR)
    os.mkdir(DATA_DIR)

    zip_file = zipfile.ZipFile(sys.argv[2], 'r')
    zip_file.extractall(DATA_DIR)
    zip_file.close()

    channel_hash = {}
    channel_file = open(DATA_DIR + '/channels.json', 'r')
    channel_data = json.loads(channel_file.read())

    for item in channel_data:
        channel_hash[item["name"]] = item["id"]

    for channel_name in channel_hash.keys():
        matches = []
        for root, dirnames, filenames in os.walk('{}/{}'.format(DATA_DIR, channel_name)):
            for filename in fnmatch.filter(filenames, '*.json'):
                matches.append(os.path.join(root, filename))

        print "Deleting everything from {}".format(channel_name)

        for channel_file in matches:
            delete_history(channel_name, channel_file)

    shutil.rmtree(DATA_DIR)
