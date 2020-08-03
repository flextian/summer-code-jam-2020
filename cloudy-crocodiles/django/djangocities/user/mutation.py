#from djangocities.graphql.schema import mutation
from ariadne import MutationType

from djangocities.user.models import CustomUser as User
from djangocities.iam.jwt import encode_auth_token

#
# Mutations
#
mutation = MutationType()

@mutation.field("login")
def resolve_login(_, info, data):
    print('Login')
    print(data)

    username = data['username']
    password = data['password']

    if not username:
        raise Exception('Username missing!')
    if not password:
        raise Exception('Password missing!')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
         
    if user is None or not user.check_password(password):
        raise Exception('No such user or invalid password!')

    # Identity can be any data that is json serializable
    access_token = encode_auth_token(sub=username, id=user.id)
    print(access_token)
    # token = json.dumps({"token": access_token.decode('utf-8')})
    token = access_token.decode('utf-8')
    print(token)
    return {'token': token}
