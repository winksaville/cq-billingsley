import cadquery as cq

# X axis line length 20.0
path = cq.Workplane("XZ").moveTo(-10, 0).lineTo(10, 0)

# Sweep a polyline 2x6 to circle diameter 1.0 to diameter 2.0 along X axis length 10.0 + 10.0
sketches = (
    cq.Workplane("YZ")
    .workplane(offset=-10.0)
    .polyline([(-3, 1), (3, 1), (3, -1), (-3, -1)])
    .close()
    .workplane(offset=10.0)
    .circle(1.0)
    .workplane(offset=10.0)
    .circle(2.0)
    #.sweep(path, multisection=True)
)
#show_object(sketches)

# Works as expected
result = sketches.sweep(path, multisection=True)
show_object(result)
