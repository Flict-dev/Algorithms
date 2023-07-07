states_needed = set(("mt", "wa", "or", "id", "nv", "ut", "ca", "az"))
final_stations = set()
stations = {
    "kone": set(("id", "nv", "ut")),
    "ktwo": set(("wa", "id", "mt", "or")),
    "kthree": set(("or", "nv", "ca")),
    "kfour": set(("nv", "ut")),
    "kfive": set(("ca", "az")),
}

while states_needed:
    best = None
    states_covered = set()
    for station, states in dict(sorted(stations.items(), reverse=True)).items():
        covered = states & states_needed
        if len(covered) > len(states_covered):
            best = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best)
print(final_stations)
