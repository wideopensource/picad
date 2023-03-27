# PiCad

## Installation

pip install picad

## Usage

This example finds small breaks in the board outline and joins them at their midpoint.

```
from picad import Layout

def fix_edge_cuts(layout:Layout, max_distance:float=1.0):
    points = sum([x.end_points for x in board_layout.get_all_lines(layer_name="Edge.Cuts")], ())

    for p in points:
        closest_p = min([x for x in points if 0 != p.distance_from(x)], key=lambda a: p.distance_from(a))
        
        if closest_p.distance_from(p) < max_distance:
            p.lerp(closest_p, 0.5)
            closest_p.move_to(p)
```
