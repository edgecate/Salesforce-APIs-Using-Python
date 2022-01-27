# Salesforce-APIs-Using-Python
> Access Salesforce GET requests to retrieve customer details, and metadata with Python.

Watch the full YT tutorial, here:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/pT-SrPq4NXk/0.jpg)](http://www.youtube.com/watch?v=pT-SrPq4NXk "How To Access Salesforce APIs using Python")

Accessing SFDC APIs is going to be pretty similar to the Supercoach web scraping video, in that we’re again, trying to create an OAuth2 access token which will give us permission to access Salesforce API GET requests.

If we tried to access those GET requests without a token, we’d basically receive an authorisation error.

In order to generate that token, we need to get our Client Id, Client Secret, and Authorisation URL, which can be done by creating a Connected App in Salesforce. Once you’re logged in, go to:
- Setup > Apps > App Manager > New Connected App
- Give your connected app a name, and contact email
- Tick Enable OAuth Settings
- Provide a callback URL which can be anything – even Localhost
- Select the OAuth scope you’d like to access – for now, select everything
- Click Save and Continue

Note down the:
- Consumer Key which is the Client ID,
- Consumer Secret which is our Client Secret, and
- Callback URL.

Then click:
- Manage
- Edit Policies
- Ensure that Permitted Users is set to All users may self-authorize
- And IP Relaxation is set to Relax IP restrictions.
- Depending on your organisation, you may have to leave it as Enforce IP restrictions, butthen whitelist the IP addresses under Network Access.
- Click Save, and the hard part is done!
- Replace the input variables with your own details

```python
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
```
