# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""
import pprint
import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    response_dict= {}
    params= f'url={url}'
    api_url= 'https://opengraph.lewagon.com'
    try:
        response = requests.get(api_url, params= params)
        response.raise_for_status()
        return response.json()
    except:
        return response_dict


# To manually test, please uncomment the following lines and run `python opengraph.py`:
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.github.com"))
