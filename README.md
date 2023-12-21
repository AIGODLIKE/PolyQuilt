# PolyQuilt

> This is a fix version fork from https://github.com/sakana3/PolyQuilt

> Since sakana3 hasn't been updated for a long time, but again this is a very good plugin, I decided to maintain a version myself

> The main tool has been adapted to the blender 4.0 version (and the old
> version is no longer maintained), but other tools have not been tested, if there is any problem, please issue it
---
PolyQuiltis an add-on for Blender 4.0 that supports low-poly modeling. In addition to simple, orthodox, and old-school
face-to-face functions, various functions are assigned to mouse operations such as dragging and long-pressing,
minimizing tool switching and supporting polygon modeling.
It is also compatible with tablets and tablet PCs with digitizers, and can be modeled intuitively while reducing the
amount of operation.

# Features

Various functions are assigned to click, drag, press and hold, and press and hold drag operations. The following
functions are allocated in combination with space, point, and edge elements.
Alt is equivalent to holding. Alt key double-click to lock long press.

|       |                             Click                              |            Drag             |    Hold     |                    Hold Drag                    | 
|:-----:|:--------------------------------------------------------------:|:---------------------------:|:-----------:|:-----------------------------------------------:|
| space |     [Create Vertices]  <br>→ [Facelift]  <br>→ [Loop Cut]      | View Rotation (Provisional) |             |                     [Knife]                     ||
| point |                           [Facelift]                           |         Move (Join)         | Delete/Melt |          [Fan Cut]  <br>Edge Extrusion          |
| edge  |                   Vertex Insertion → Surface                   |           [Move]            | Delete/Melt | Loop Insertion  <br>Edge Extrusion <br>Loop Cut |
| face  |                                                                |           [Move]            |  [removed]  |                                                 |

|   Hold down Shift and press   |        Function         |
|:-----------------------------:|:-----------------------:|
|         Shift + Click         |        AutoQuad         |
|         Shift + Drag          |          Brush          |
| Shift + Middle Button + Drag  |        2ndBrush         |
|       Shift + Hold Drag       | Brush Size/Strength +/- |
|    Shift + Wheel Up/ Down     |     Brush Size +/-      |
| Shift + Ctrl + Wheel Up/ Down |   Brush Strength +/-    |

---

## Move

You can move the view plane by dragging the mouse over a point, line, or face. The vertices of an edge can be combined
by bringing them closer to the vertices of another edge.

## Vertex Creation

Clicking on an empty space creates vertices. Normally, it will be in surface mode as it is, but if you set the geometry
to point mode, you can create points continuously.

## Face Upholstery

Click on an empty area or point to start the surface. Each click adds a point, line, or area. You can click (agree with
double-click) or right-click on the last point you have placed to create a new face.

From the tool menu at the top of the screen, you can choose from points, lines, triangles, squares, and polygons to
create geometry.

Also, if you click at the vertex of the same face, the face will be divided.

## Removal/Melting

Press and hold on a point, line, or face to erase or melt that element. If there are lines or surfaces to share, they
will be melted, otherwise they will be deleted.

## Knife

You can execute the knife by dragging after a long press in space.

## Loop Cuts

You can press and hold on the edge, and then drag to loop the edge.

## Fan cut

After pressing and holding on the dot, you can cut the edges in a fan shape loop by dragging.

## Edge extrusion

Press and hold on a side or point, then drag to extrude the edge.

## Loop Insertion

Insert an edge loop

## Loop Cuts

Cut the side loops

## Extra Setting

This is a special set of settings. For advanced users

### Check PolyQuilt add-on update

You can check for updates to the polyquilt and update it to the latest version. If it doesn't work, please do it the
same way as before.

### Set up a game engine-style keymap

Set up a keymap to change the viewpoint with the right mouse button + drag. The default context menu is opened by
clicking, so you can perform operations like major game engines such as Unity and UE 4 without being affected. Please
note that since the keymap is rewritten, it may conflict with your own custom or other add-ons.

# Feedback

# To be implemented

- [ ] Separation (Rip)
- [ ] LoopCut support for terminal triangles
- [ ] Select
- [x] Hand litopo editing


