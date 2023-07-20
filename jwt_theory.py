import jwt
import datetime
import time

import config

payload = {
    'my_name': 'Vasyl',
    'password': 'kdfjhgkl;dfjkgdfkluhg;.dfjglkdfgkdfli;ghdfljgkljdfgkl;dfg',

    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=90),
}

encode_jwt = jwt.encode(
    payload=payload,
    key=config.JWT_SECRET,
    algorithm='HS256',
)
time.sleep(3)
decoded = jwt.decode(
    encode_jwt,
    config.JWT_SECRET,
    algorithms=['HS256'],
    # options={
    #     'verify_signature': False,
    # }
)

print(decoded)
