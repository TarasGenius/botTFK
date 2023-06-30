from msal import ConfidentialClientApplication
import requests
import json

client_id = 'a715c22b-9292-4f55-b7bd-2c2d54ca2d15'
client_secret = 'lAs8Q~9aWiZzCgNbNHZln0OizbHboW5lmAJlrata'
tenant_id = '0ffa2b50-d82a-4bdc-9e19-dda33d9a2b99'
redirect_uri = "http://localhost:8000"
msal_authority = f'https://login.microsoftonline.com/{tenant_id}'

msal_scope = ['Files.Read', 'Files.Read.All',
              'Files.ReadWrite', 'Files.ReadWrite.All', 'Sites.Read.All', 'Sites.ReadWrite.All']
# msal_scope = ['https://graph.microsoft.com/.default']
user = 'tarasliabuk@tac.lutsk.ua'
password = 'Dontcrybabypls1337'

msal_app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=msal_authority,
)
# result = msal_app.acquire_token_by_username_password(username=user, password=password, scopes=msal_scope)
result = msal_app.acquire_token_silent(
    scopes=msal_scope,
    account=None,
)
if not result:
    result = msal_app.acquire_token_for_client(scopes=msal_scope)
    print(result)
if 'access_token' in result:
    access_token = result['access_token']
else:
    raise Exception('No access token')
print(result)
headers = {
    'Authorization': f'Bearer {access_token}',
}

print(access_token)
responce = requests.get(
    url='https://graph.microsoft.com/v1.0/me/drive/root/children',
    headers=headers
)
print(responce)
print(json.dumps(responce.json(), indent=4))
# # Step 1. get the file name
# for file_id in file_ids:
#     response_file_info = requests.get(
#         GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}',
#         headers=headers,
#         params={'select': 'name'}
#     )
#     file_name = response_file_info.json().get('name')
#
# # Step 2. downloading OneDrive file
# response_file_content = requests.get(GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}/content', headers=headers)
# with open(os.path.join(save_location, file_name), 'wb') as _f:
#     _f.write(response_file_content.content)




