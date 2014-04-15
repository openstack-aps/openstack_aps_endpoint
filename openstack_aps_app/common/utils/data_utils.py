import random
import uuid


def rand_uuid():
    return str(uuid.uuid4())


def rand_uuid_hex():
    return uuid.uuid4().hex


def rand_name(name=''):
    randbits = str(random.randint(1, 0x7fffffff))
    if name:
        return name + '-' + randbits
    else:
        return randbits