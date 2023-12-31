# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import bpy
import math
import mathutils
import bmesh
import copy
import bpy_extras
import collections
from ..utils import pqutil
from ..utils import draw_util
from ..QMesh import *
from .subtool import SubToolEx
from ..utils.dpi import *

C_HAND_NOISE = 3 # pixel, consider as noise
C_CHANGE = 3 # count of change, consider as noise


class SubToolBrushSize(SubToolEx) :
    name = "BrushSizeTool"

    def __init__(self, event , root ) :
        super().__init__(root)
        self.preMousePos = self.startMousePos
        self.start_radius = display.dot( self.preferences.brush_size )
        self.radius = self.start_radius
        self.strength = self.preferences.brush_strength
        self.start_strength = self.strength
        self.PressPrevPos = mathutils.Vector( (event.mouse_prev_x , event.mouse_prev_y) )

        self.mode = None
        self.changeCount = 0
    def AttemptChangeMode(self,mode:str):
        if self.mode is None: # first time, skip
            self.mode = mode
            return True
        elif self.mode != mode:
            self.changeCount += 1
            if self.changeCount > C_CHANGE:
                self.mode = mode
                self.changeCount = 0
                return True
            return False
        else:
            self.changeCount = 0
            return True

    def OnUpdate( self , context , event ) :
        if event.type == 'MOUSEMOVE':
            vec = self.mouse_pos - self.preMousePos
            self.preMousePos = self.mouse_pos

            if vec.length < C_HAND_NOISE: # consider as noise, else will cause brush size change
                return 'RUNNING_MODAL'

            nrm = vec.normalized()
            ang = math.radians(45) # angle

            if nrm.x > ang or nrm.x < -ang :
                if self.AttemptChangeMode('radius'):
                    self.radius = self.radius + vec.x
                    self.radius = min( max( 50 , self.radius ) , 500 )
                    self.preferences.brush_size = display.dot_to_mm( self.radius )

            if nrm.y > ang or nrm.y < -ang :
                if self.AttemptChangeMode('strength'):
                    self.strength = self.strength + vec.y / self.radius
                    self.strength = min( max( 0 , self.strength ) , 1 )
                    self.preferences.brush_strength = self.strength

        elif event.type == self.rootTool.buttonType :
            if event.value == 'RELEASE' :
                x = int(self.PressPrevPos.x)
                y = int(self.PressPrevPos.y)
                bpy.context.window.cursor_warp(x, y)
                return 'FINISHED'

        return 'RUNNING_MODAL'

    def OnDraw( self , context  ) :
        draw_util.draw_circle2D( self.startMousePos , self.radius * self.strength , color = (1,0.25,0.25,0.5), fill = False , subdivide = 64 , dpi= False )
        draw_util.draw_circle2D( self.startMousePos , self.radius , color = (1,1,1,1), fill = False , subdivide = 64 , dpi= False )
        draw_util.DrawFont( "Strenght = " + '{:.0f}'.format(self.strength * 100) , 10 , self.startMousePos , (0,0) )
        draw_util.DrawFont( "Radius = " + '{:.0f}'.format(self.radius ) , 10 , self.startMousePos , (0,-8) )

    def OnDraw3D( self , context  ) :
        pass

    def resetMouse(self, context, event):
        context.window.cursor_warp(context.region.x + context.region.width / 2 - 0.5*(event.mouse_x - event.mouse_prev_x), \
            context.region.y + context.region.height / 2 - 0.5*(event.mouse_y - event.mouse_prev_y))

    @classmethod
    def GetCursor(cls) :
        return 'NONE'
