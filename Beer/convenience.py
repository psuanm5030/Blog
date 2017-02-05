import unicodedata
import yaml

def make_credentials():
    with open("/Users/Miller/GitHub/Blog/Beer/credentials.yml", 'r') as ymlfile:
        params = yaml.load(ymlfile)

    #https://api.untappd.com/v4/method_name?client_id=CLIENTID&client_secret=CLIENTSECRET
    url = 'client_id=%s&client_secret=%s' % (params['client_ID'],params['client_Secret'])
    return url

def get_credentials():
    with open("/Users/Miller/GitHub/Blog/Beer/credentials.yml", 'r') as ymlfile:
        params = yaml.load(ymlfile)

    return (params['client_ID'],params['client_Secret'])