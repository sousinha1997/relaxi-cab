from random import randint


def generate_user_ids(id_length=10):
    user_id = ''.join(str(randint(0, 9)) for _ in range(id_length))
    return user_id