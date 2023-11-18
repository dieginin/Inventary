class Seed:
    def __str__(self):
        return "> " + "\n> ".join(list(self.__dict__.keys()))


class Scrubs(Seed):
    def __init__(
        self,
        colors: dict,
        brands: dict,
        sizes: dict,
    ):
        self.colors = colors
        self.brands = brands
        self.sizes = sizes

    def get_sizes(self):
        return self.sizes.keys()


class Policy(Seed):
    def __init__(
        self,
        data: dict,
    ):
        self.scrubs = Scrubs(**data.get("scrubs", {}))
