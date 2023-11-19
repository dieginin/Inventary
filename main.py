import json

import pandas as pd

from models import Policy

szs = ["xxs", "xs", "s", "m", "l", "xl", "1x", "2x", "3x", "4x", "5x", ""]

with open("config/policy.json", "r") as fl:
    policy = Policy(json.load(fl))
df = pd.read_csv("data/data.csv")


def find_colors(brand):
    return policy.scrubs.brands.get(brand, {})


def find_max_size(color):
    return policy.scrubs.colors.get(color, {})


def desire_count(length, size):
    return policy.scrubs.sizes.get(length, {}).get(size)


def get_missing(obj):
    missing = {}

    sub = df[df["CODE"] == obj]
    brand = sub["BRAND"].iloc[0]
    pol_colors = policy.scrubs.brands.get(brand, {})

    for color in pol_colors:
        if color not in sub["COLOR"].unique():
            color_dict = {}
            for length in policy.scrubs.get_sizes():
                size_dict = {}
                for size in szs[:-1]:
                    desire = desire_count(length, size)
                    if desire:
                        size_dict[size] = desire
                color_dict[length] = size_dict
            missing[color] = color_dict

    return missing


get_missing("7726")
# print(get_missing("7726"))
