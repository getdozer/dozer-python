from pydozer.auth import AuthClient

token = ''
client = AuthClient(token=token, url='0.0.0.0:50051')

restricted_token = client.get_auth_token()

print(f"Token: {restricted_token}")
