import pandas as pd
from pandas.io.json import json_normalize
import pickle

# with open("/Users/Miller/GitHub/Blog/Beer/pkl_brewery_data.pkl", "rb") as f:
#     data = pickle.load(f)
#
# brew = data[0]
# brew_beers = brew['beer_list']['items']
#
# result = json_normalize(brew_beers)
# result.to_csv('/Users/Miller/GitHub/Blog/Beer/beers.csv')
# print result



def parse_beers():
    """
    Take in the brewery data and parse beers details.  Append and export to csv.
    :param data:
    :return:
    """
    with open("/Users/Miller/GitHub/Blog/Beer/pkl_brewery_data.pkl", "rb") as f:
        data = pickle.load(f)

    appended_data = []
    for brewery in data:
        beers = brewery['beer_list']['items']
        detail = json_normalize(beers)
        appended_data.append(detail)

    master = pd.concat(appended_data, axis=0)
    master.to_csv('/Users/Miller/GitHub/Blog/Beer/beers1.csv',encoding='utf-8')
    print master
    print 'done parsing and printing'
    return

def parse_checkins():
    """
    Take in the brewery data and parse beers details.  Append and export to csv.
    :param data:
    :return:
    """
    with open("/Users/Miller/GitHub/Blog/Beer/pkl_brewery_data.pkl", "rb") as f:
        data = pickle.load(f)

    appended_data = []
    for checkin in data:
        checkins = checkin['checkins']['items']
        detail = json_normalize(checkins)
        appended_data.append(detail)

    master = pd.concat(appended_data, axis=0)
    master.to_csv('/Users/Miller/GitHub/Blog/Beer/checkins.csv',encoding='utf-8')
    return


# Primary Run Code
if __name__ == '__main__':
    # parse_beers()
    parse_checkins()
    print 'completed'