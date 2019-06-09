# horizons

A python client for the [JPL HORIZONS System](https://ssd.jpl.nasa.gov/?horizons).

This is an ugly telnet and regex fueled API. JPL has a much cleaner [SSD/CNEOS API Service](https://ssd-api.jpl.nasa.gov/) that overlaps with HORIZONS in some places. HORIZONS' orbital element data on "Major Bodies" (i.e. planets, moons, and some others) are not available yet in this other collection of APIs.
