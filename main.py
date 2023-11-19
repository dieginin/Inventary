import json

import pandas as pd

from models import Policy

szs = ["xxs", "xs", "s", "m", "l", "xl", "1x", "2x", "3x", "4x", "5x"]

with open("config/policy.json", "r") as fl:
    policy = Policy(json.load(fl))
df = pd.read_csv("data/data.csv")


def get_missing_style(obj):
    sub = df[df["CODE"] == obj]
    brand = sub["BRAND"].iloc[0]

    missing_colors = {}
    for color in policy.scrubs.colors(brand):
        if color not in sub["COLOR"].unique():
            missing_colors[color] = {
                length: {
                    size: policy.scrubs.desire(length, size)
                    for size in szs
                    if policy.scrubs.desire(length, size)
                }
                for length in policy.scrubs.get_sizes()
            }

    missing_sizes = {}
    for _, r in sub.iterrows():
        length, size, color, count = r["LENGTH"], r["SIZE"], r["COLOR"], r["COUNT"]
        desire = policy.scrubs.desire(length, size)

        if desire > count:
            color_dict = missing_sizes.setdefault(color, {})
            length_dict = color_dict.setdefault(length, {})
            length_dict[size] = desire - count

    return {**missing_colors, **missing_sizes}


# get_missing("7726")
print(get_missing_style("7726"))
