import urllib.request,json
from .models import Popular
import app
base_url = None

def configure_request(app):

    global base_url
    base_url = app.config['BASE_URL']

def get_quote(name):

    get_quote_url = base_url.format(name)
    with urllib.request.urlopen(get_quote_url) as url:

        get_quote_url_data = url.read()

        get_quote_response = json.loads(get_quote_url_data)

        quote_results = None

        quote_results = process_quote_results(get_quote_response)

    return quote_results


def process_quote_results(quote_list):

    quote_results = []

    for quote_item in quote_list:

        author = quote_item.get('author')
        quote = quote_item.get('quote')

        quote_object = Popular(author,quote)
        quote_results.append(quote_object)

    return quote_results
