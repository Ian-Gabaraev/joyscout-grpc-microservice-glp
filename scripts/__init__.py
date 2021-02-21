import yaml

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

try:
    file = open(str(BASE_DIR) + "/env.yml", "r")
    env = yaml.load(file.read(), Loader=yaml.FullLoader)
except FileNotFoundError:
    raise FileNotFoundError(
        "file 'env.ym' expected at %s but could not be found" % BASE_DIR)
