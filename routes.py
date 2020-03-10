from lib.paths import blueprint, url
from blueprints import hello


routes = [
    blueprint(hello.bp)
]
