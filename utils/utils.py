from random import randint


def calculate_distance(src_long, src_lat, dest_lon, dest_lat):
    x = pow(src_long - dest_lon, 2)
    y = pow(src_lat - dest_lat, 2)
    return pow(x + y, 0.5)


def generate_user_ids(id_length=10):
    user_id = ''.join(str(randint(0, 9)) for _ in range(id_length))
    return user_id