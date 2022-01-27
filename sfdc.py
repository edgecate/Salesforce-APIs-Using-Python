import requests

# Consumer Key
client_id = 'CONSUMER_KEY_FROM_SFDC'

# Consumer Secret
client_secret = 'CONSUMER_SECRET_FROM_SFDC'

# Callback URL
redirect_uri = 'http://localhost/'

# sfdc_user = your SFDC username
sfdc_user = 'YOUR_SFDC_USERNAME'

# sfdc_pass = your SFDC password
sfdc_pass = 'YOUR_SFDC_PASSWORD'

# Visit https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_oauth_endpoints.htm
auth_url = 'https://login.salesforce.com/services/oauth2/token'

# POST request for access token
response = requests.post(auth_url, data = {
                    'client_id':client_id,
                    'client_secret':client_secret,
                    'grant_type':'password',
                    'username':sfdc_user,
                    'password':sfdc_pass
                    })

# Retrieve token
json_res = response.json()
access_token = json_res['access_token']
auth = {'Authorization':'Bearer ' + access_token}

# In some cases, instance_url may be different from your base URL, so it's best to extract it from response.json()
instance_url = json_res['instance_url']

# GET requests
url = instance_url + '/services/data/v45.0/sobjects/contact/describe'
res = requests.get(url, headers=auth)
r = res.json()
print(r)
