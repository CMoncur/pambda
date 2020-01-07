from pambda.compose import compose, curry, pipe, tap

# cool_pipe = pipe(
#     cmap(lambda x: int(x)),
#     tap(print),
#     cmap(lambda x: x + 1),
#     cfilter(lambda x: x >= 4),
#     lambda x: list(x),
# )









# SCENARIO: I have a list of geofences of any type. I want to select
# only fences with a type of "GEO_CIRCLE_FENCE", a radius greater than 3000,
# and then I want a list of ONLY the name and radius of said fences. Other
# data may be discarded.

# The two filters can clearly be combined into one, but to help illustrate the
# benefit of these utilities I have split them into two filter statements.



cmap = curry(map)
cfilter = curry(filter)

list_of_fences = [] # Imagine that stuff was here










# Some other way
geo_circle_fences = filter(
    lambda geofence: geofence["type"] == "GEO_CIRCLE_FENCE",
    list_of_fences)

big_geo_circle_fences = filter(lambda geofence: geofence["radius"] >= 3000,
                               geo_circle_fences)

minimal_fence_details = map(
    lambda geofence: (geofence["name"], geofence["radius"]),
    big_geo_circle_fences)

big_fence_list = list(minimal_fence_details)












# By means of left-to-right composition
big_fences_pipe = pipe(
    cfilter(lambda geofence: geofence["type"] == "GEO_CIRCLE_FENCE"),
    cfilter(lambda geofence: geofence["radius"] >= 3000),
    cmap(lambda geofence: (geofence["name"], geofence["radius"])),
    lambda x: list(x),
)(list_of_fences)

# It's also worth mentioning that these compositions don't need to have data
# passed to them, they me be constructed into standalone reusable functions.










# By means of right-to-left composition
big_fences_composition = compose(
    lambda x: list(x),
    cmap(lambda geofence: (geofence["name"], geofence["radius"])),
    cfilter(lambda geofence: geofence["radius"] >= 3000),
    cfilter(lambda geofence: geofence["type"] == "GEO_CIRCLE_FENCE")
)(list_of_fences)
