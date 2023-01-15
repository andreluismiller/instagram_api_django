import requests
import json

def getAccess():
    """
    Função para obter as credenciais necessárias ao uso da API
    Retorno:
        dicionário: utilizado globalmente, em todas as funçõoes que fazem chamadas à API
    """
    creds = dict() # Dicionário vazio para guardar as credenciais de autenticação
    creds['access_token'] = 'ACCESS_TOKEN' # access token for use with all api calls
    creds['client_id'] = 'FB_APP_CLIENT_ID' # client id from facebook app IG Graph API Test
    creds['client_secret'] = 'FB_APP_CLIENT_SECRET' # client secret from facebook app
    creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
    creds['graph_version'] = 'v6.0' # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
    creds['debug'] = 'no' # debug mode for api call
    creds['page_id'] = 'FB_PAGE_ID' # users page id
    creds['instagram_account_id'] = 'IG_BUSINESS_ACCOUNT_ID' # users instagram account id
    creds['ig_username'] = 'IG_USERNAME' # ig username

    return creds


def makeApiRequest(url, endpointParams, type) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters
	Returns:
		object: data from the endpoint
	"""

	if type == 'POST' : # post request
		data = requests.post(url, endpointParams)
	else : # get request
		data = requests.get(url, endpointParams)

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	return response # get and return content