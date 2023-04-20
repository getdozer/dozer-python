from pydozer.auth import AuthClient
from pydozer.api import ApiClient

master_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYWNoZV91c2VyIiwic3ViIjoiYXBpQGRvemVyLmNvbSIsImV4cCI6MTY4MTI4NzcwNDAyNywiYWNjZXNzIjoiQWxsIn0.aD5L6XURIr3hrUp0LzfUQWKHairjK6DDkMlzvnVvzHA'

client = AuthClient(token=master_token, url='0.0.0.0:50051')

restricted_token = client.get_auth_token()

print(f"Token: {restricted_token}")

api = ApiClient("pickup", url='0.0.0.0:50051', token=restricted_token)

count = api.count()

print(f"Count: {count}")
