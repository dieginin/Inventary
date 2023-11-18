import json

import pandas as pd

from models import Policy

with open("config/policy.json", "r") as fl:
    policy = Policy(json.load(fl))
data = pd.read_csv("data/data.csv")


def find_colors(brand):
    return policy.scrubs.brands.get(brand)


def find_max_size(color):
    return policy.scrubs.colors.get(color)


def desire_count(lenght, size):
    return policy.scrubs.sizes.get(lenght, {}).get(size)


print(data.info())
