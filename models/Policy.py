class Seed:
    def __str__(self):
        return "> " + "\n> ".join(list(self.__dict__.keys()))


class Scrubs(Seed):
    def __init__(
        self,
        colors: dict,
        sizes: dict,
    ):
        self._colors = colors
        self._sizes = sizes

    def get_sizes(self):
        return self._sizes.keys()

    def colors(self, brand):
        return self._colors.get(brand, {})

    def desire(self, length, size):
        return self._sizes.get(length, {}).get(size, {})


class Policy(Seed):
    def __init__(
        self,
        data: dict,
    ):
        self.scrubs = Scrubs(**data.get("scrubs", {}))
