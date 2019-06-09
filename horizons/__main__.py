from horizons.core import Horizons
import logging


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
horizons_log = logging.getLogger(__name__)
horizons_log.setLevel(logging.DEBUG)
horizons_log.propagate = True


with Horizons() as h:
    major_bodies = h.get_major_bodies()
    print(major_bodies[:4])
