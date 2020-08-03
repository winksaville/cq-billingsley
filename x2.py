import cadquery as cq

# Switch to an arc for the path : line l=5.0 then half circle r=4.0 then line l=5.0
path = (
    cq.Workplane("XZ")
    .moveTo(-5, 4)
    .lineTo(0, 4)
    .threePointArc((4, 0), (0, -4))
    .lineTo(-5, -4)
)

# Placement of different shapes should follow the path
# cylinder r=1.5 along first line
# then sweep allong arc from r=1.5 to r=1.0
# then cylinder r=1.0 along last line
arcSweep = (
    cq.Workplane("YZ")
    .workplane(offset=-5)
    .moveTo(0, 4)
    .circle(1.5)
    .workplane(offset=5)
    .circle(1.5)
    .moveTo(0, -8)
    .circle(1.0)
    .workplane(offset=-5)
    .circle(1.0)
    .sweep(path, multisection=True)
)

