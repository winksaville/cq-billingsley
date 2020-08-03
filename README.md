# CadQuery sweep problem

John Billingsley reported a [problem with sweep]( https://groups.google.com/g/cadquery/c/UrPx8CiSdY0/m/rYtuHCR6AgAJ).

This is my attempt to see what's wrong.

After a few steps I got to "how" to do the actual sweep
and searched the cadquery sources and found
Ex024_Sweep_With_Multiple_Sections.py. Looks to be a good
starting point:

Extract the arcSweep example from Ex024 to x2.py:
```
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
```

![](./ss_x2-unchanged-arcSweep-from-Ex024.png)
