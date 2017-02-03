# Extract data from Untapped API

import requests
import yaml
import pprint
import csv
import convenience
import pprint
import pickle
from datetime import date, datetime, timedelta as td

get_endpoints = ['thepub', 'thepub/local', 'checkin/recent',
                 'beer/trending', 'user/pending', 'notifications',
                 'heartbeat', 'user/checkins', 'venue/checkins',
                 'beer/checkins', 'brewery/checkins', 'brewery/info',
                 'beer/info', 'venue/info', 'checkin/view',
                 'user/info', 'user/badges', 'user/friends',
                 'user/wishlist', 'user/beers', 'checkin/toast',
                 'friend/remove', 'friend/request', 'user/wishlist/add',
                 'user/wishlist/delete', 'search/beer', 'search/brewery']

def get_ids():
    """
    Returns a listing of ids (in string format)
    :return:
    """
    with open("/Users/Miller/GitHub/Blog/Beer/pkl_brewery_ids.pkl","rb") as f:
        data = pickle.load(f)
    return data

def query_brewery_info(ids):
    """
    Intended to extract the highest level, overview.
    :param params:
    :return:
    """

    result = []
    base = 'https://api.untappd.com/v4/brewery/info/'
    creds = convenience.make_credentials()

    # Request - loop to get multiple breweries
    for id in ids:
        url = (base + '{0}?' + creds).format(id)
        print url
        r = requests.get(url) # Make Request

        #  Parse result
        r1 = r.json()

        # Check for Error
        if r1['meta']['code'] != 200:
            print 'Error on API call.  Received error code: ' + r1['status_code'] + ' with explanation of: ' + r1['test']
        else:
            print 'Number of calls remaining in this hour: ' + r.headers['X-Ratelimit-Remaining']
            result.append(r1['response']['brewery'])

    return result

def store_data(data):
    with open("/Users/Miller/GitHub/Blog/Beer/pkl_brewery_data.pkl","wb") as f:
        pickle.dump(data, f)

def parse_data():
    with open("/Users/Miller/GitHub/Blog/Beer/pkl_brewery_data.pkl","rb") as f:
        data = pickle.load(f)

    pprint.pprint(data)

    return




# Primary Run Code
if __name__ == '__main__':
    # First need to run the Get_Brewery_IDs.py script

    # Get IDs and run through API making 1 call per brewery
    # breweries_data = query_brewery_info(get_ids())

    # Store the data in a pickle
    # store_data(breweries_data)

    # Parse the data
    parse_data()


    print 'completed'
