from horizons import Horizons, BodyResult
import json
import logging


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
horizons_log = logging.getLogger(__name__)
horizons_log.setLevel(logging.INFO)
horizons_log.propagate = True


def get_major_bodies():
    major_bodies = None
    with Horizons() as h:
        major_bodies = h.get_major_bodies()
    major_bodies_as_dicts = list(map(lambda b: b.__dict__, major_bodies))
    with open('bodies.json', 'w+') as f:
        f.write(json.dumps(major_bodies_as_dicts, indent=2))

def get_planet_vectors():
    planet_ids = [
        '199',
        '299',
        '399',
        '499',
        '599',
        '699',
        '799',
        '899',
    ]
    vector_map = {}
    with Horizons() as h:
        for planet_id in planet_ids:
            planet_vectors = h.get_vectors(planet_id)
            vector_map[planet_id] = planet_vectors.__dict__
    with open('vectors.json', 'w+') as f:
        f.write(json.dumps(vector_map, indent=2))

get_planet_vectors()
