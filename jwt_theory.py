import jwt
import datetime
import time

payload = {
    'my_name': 'Vasyl',
    'password': 'kdfjhgkl;dfjkgdfkluhg;.dfjglkdfgkdfli;ghdfljgkljdfgkl;dfg',

    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=90),
}

encode_jwt = jwt.encode(
    payload=payload,
    key='secret',
    algorithm='HS256',
)
time.sleep(3)
decoded = jwt.decode(
    encode_jwt,
    'secret',
    algorithms=['HS256'],
    # options={
    #     'verify_signature': False,
    # }
)

print(decoded)
