import cadquery as cq

path = (
    cq.Workplane("XY")
    .moveTo(20, 0)
    .radiusArc(endPoint=(0, 20), radius=-20)
)

poly1 = (
    cq.Workplane("XZ")
    .polyline([(20, 20), (60, 20), (60, 0), (20, 0)])
    .close()
)

poly2 = (
    cq.Workplane("XZ")
    .polyline([(20, 20), (60, 20), (60, 0), (20, 0)])
    .close()
    .rotate((0, 0, -1), (0, 0, 1), 90)
)

# solid.sweep(path, multisection=True)
