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

import bpy
import math
import mathutils
import bmesh
import bpy_extras
import collections
import copy
from ..utils import pqutil
from ..utils import draw_util
from ..QMesh import *
from ..utils.mouse_event_util import ButtonEventUtil, MBEventType
from .subtool import *
from .subtool_makepoly import *
from .subtool_knife import *
from .subtool_edgeloop_cut import *
from .subtool_move import *
from .subtool_fin_slice import *
from .subtool_polypen import *

class MainToolKnife(MainTool) :
    name = "Knife"

    def __init__(self,op,currentTarget, button) :
        super().__init__(op,currentTarget, button , no_hold = True )        

    def LMBEventCallback(self , event ):
        self.debugStr = str(event.type)

        if event.type == MBEventType.Release :
            self.isExit = True
        elif event.type == MBEventType.Click or event.type == MBEventType.LongClick:
            if self.currentTarget.isVert or self.currentTarget.isEmpty or self.currentTarget.isEdge:
                self.SetSubTool( SubToolMakePoly(self.operator,self.currentTarget , self.buttonType ) )
        elif event.type == MBEventType.Drag or event.type == MBEventType.LongPressDrag:
            self.SetSubTool( SubToolKnife(self.operator,self.currentTarget , self.LMBEvent.PressPos ) )   

    @classmethod
    def DrawHighlight( cls , gizmo , element ) :
        if element is not None and gizmo.bmo is not None :
            return element.DrawFunc( gizmo.bmo.obj , gizmo.preferences.highlight_color , gizmo.preferences , False )
        return None

    def OnDraw( self , context  ) :
        pass

    def OnDraw3D( self , context  ) :
        if self.currentTarget.isNotEmpty :
            color = self.color_highlight()
            self.currentTarget.Draw( self.bmo.obj , color , self.preferences )

    def OnExit( self ) :
        pass

    @classmethod
    def GetCursor(cls) :
        return 'KNIFE'