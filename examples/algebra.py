from build123d import *
from build123d.algebra import Rot, Pos

try:
    from ocp_vscode import show_object, show
except:
    ...

# %%

b = Box(1, 2, 3)
c = Cylinder(0.1, 4)
d = b - [c @ (Plane.XZ * Pos(y=1)), c @ (Plane.XZ * Pos(y=-1)), c @ Plane.YZ]

show(d, transparent=True)

# %%
