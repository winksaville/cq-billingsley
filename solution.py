import cadquery as cq

print("hi")

poly1 = [(-3, 1), (3, 1), (3, -1), (-3, -1)]
poly2 = [(-1, 3), (1, 3), (1, -3), (-1, -3)]

# Not sure how to "translate2d" natively in cadquery
def translate2d(poly, t):
    X = 0
    Y = 1
    return [(loc[X] + t[X], loc[Y] + t[Y]) for loc in poly]

# The path that we'll sweep
path = (
    cq.Workplane("XZ")
    .moveTo(0, 4)
    .radiusArc(endPoint=(4, 0), radius=4)
)
#show_object(path)

# Plane1 has poly1
p1 = cq.Workplane("YZ").polyline(translate2d(poly1, (0, 4))).close()
#show_object(p1)

# Plane2 has circle or poly1 or poly2
p2 = cq.Workplane("XY").moveTo(4, 0).circle(0.5)
#p2 = cq.Workplane("XY").polyline(translate2d(poly1, (4, 0))).close()
#p2 = cq.Workplane("XY").polyline(translate2d(poly2, (4, 0))).close()
#show_object(p2)

# Put both planes on the stack
c = p1.add(p2)
# BUG: len(c.ctx.pendingWires) should equal 2 at this point, but it equals 1
print(f"len(c.ctx.pendingWires)={len(c.ctx.pendingWires)}")
#show_object(c)

# This does NOT work, but I believe it should
#result = c.sweep(path, multisection=True)

# Looking at pendingWires and _addPendingWire() I discovered that
# each() adds appends wires to pendingWires. I used that fact to
# make this work.

# Clear pendingWires, otherwise the result is 3, although not a fatal error.
c.ctx.pendingWires = []

def look(shape):
    print(f"type(shape)={type(shape)}")
    return shape
r = c.each(look)
print(f"len(r.ctx.pendingWires)={len(r.ctx.pendingWires)}")
#show_object(r)

# sweep out the multisection's that are on the stack 
result = r.sweep(path, multisection=True)

show_object(result)
