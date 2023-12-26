# Reropo Quilt

Since the operation form is very different from PolyQUilt, we divided it into a category called RetopQuilt.
In the future, there are plans to include a retopology mode in Blender, so we plan to integrate it there.

## Quad Patch
It is used from the icon of the PolyQuilt icon.

---

### Basic Operations

- Left mouse button + drag
Draw an edge path by stroke. The number of divisions is calculated by the optional distance. You can also change the number of divisions from the adjustment panel at the bottom left.
 
- Left mouse button + drag with edge selection
Apply a surface that bridges between the selection edge and the stroke. The number of slice divisions is calculated by the optional distance.
You can also change the number of divisions from the adjustment panel at the bottom left.
Also, if you draw a stroke from a vertex, a quad patch will be stretched based on the connecting edge with the selected edge.

### Select operation 
 
- Click or drag on an edge
Make a selection of edges.
 
- Click or drag next to the edge of the selected side
Make additional selections for the sides.
 
- Click or drag at the edge of the selected side
Deselect the edges.
 
- Hold on the edges
Make a selection of edge loops.
 
- Hold at the edge of the selected side
Make a selection of edge circuits.
 
- Click on an empty area
Deselect

### Cooper

Cooper means "barrel maker" and is used to create a topology with a barrel-like sliced shape.

- Left mouse button hold + drag
Slice the tubular topology. The number of slice divisions is calculated by the optional distance. You can also change the number of divisions and offsets from the adjustment panel at the bottom left.

- Left mouse button hold + drag in edge selection state
Bridge the selected edge with the sliced edge. You can also change the offset from the adjustment panel at the bottom left.

### Fill Hole

With the edge circuit selected, fill the hole with a quad with a hold. I don't think it will be a very good result, but please use it when you want to fill it with a quad for the time being.