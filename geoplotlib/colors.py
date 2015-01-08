from random import shuffle
import math


def _convert_color_format(col, alpha):
    return [int(c * 255) for c in col[:3]] + [alpha]


class ColorMap():

    def __init__(self, cmap_name, alpha=255, step=0.2):
        from pylab import get_cmap
        self.cmap = get_cmap(cmap_name)
        self.alpha = alpha
        self.step = step
        self.mapping = {}


    def to_color(self, value):
        value = max(min(value,1),0)
        value = int(value // self.step) * self.step
        if value not in self.mapping:
            self.mapping[value] = _convert_color_format(self.cmap(value), self.alpha)
        return self.mapping[value]


def create_set_cmap(values, cmap_name, alpha=255):
    unique_values = list(set(values))
    shuffle(unique_values)
    from pylab import get_cmap
    cmap = get_cmap(cmap_name)
    d = {}
    for i in range(len(unique_values)):
        d[unique_values[i]] = _convert_color_format(cmap(1.*i/len(unique_values)), alpha)
    return d


def lin_norm(value, maxvalue):
    return value / maxvalue


def log_norm(value, maxvalue):
    return math.log(1+value) / math.log(1+maxvalue)


def colorbrewer(values, alpha=255):
    basecolors = [
        [31, 120, 180],
        [178, 223, 138],
        [51, 160, 44],
        [251, 154, 153],
        [227, 26, 28],
        [253, 191, 111],
        [255, 127, 0],
        [202, 178, 214],
        [106, 61, 154],
        [255, 255, 153],
        [177, 89, 40]
    ]
    unique_values = list(set(values))
    return {k: basecolors[i % len(basecolors)] + [alpha]  for i, k in enumerate(unique_values)}
