# -*- coding: utf-8 -*-
#
#  Copyright (C) 2013 by Igor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import wal

from sk1 import _, config, events
from sk1.resources import icons, get_bmp

from .base import CtxPlugin


class PolygonPlugin(CtxPlugin):
    name = 'PolygonPlugin'
    update_flag = False
    num_spin = None

    def __init__(self, app, parent):
        CtxPlugin.__init__(self, app, parent)
        events.connect(events.DOC_CHANGED, self.update)
        events.connect(events.SELECTION_CHANGED, self.update)

    def build(self):
        bmp = get_bmp(self, icons.CTX_POLYGON_NUM,
                      _('Number of polygon angles'))
        self.pack(bmp, padding=2)

        self.num_spin = wal.IntSpin(self, 5, (3, 1000), onchange=self.changes)
        self.pack(self.num_spin, padding=2)

    def changes(self, *_args):
        if self.update_flag:
            return
        val = self.num_spin.get_value()
        if self.insp.is_selection():
            selection = self.app.current_doc.selection
            if self.insp.is_obj_polygon(selection.objs[0]):
                self.app.current_doc.api.set_polygon_corners_num(val)

    def update(self, *args):
        if self.insp.is_selection():
            selection = self.app.current_doc.selection
            if self.insp.is_obj_polygon(selection.objs[0]):
                self.update_flag = True
                self.num_spin.set_value(selection.objs[0].corners_num)
                self.update_flag = False


class PolygonCfgPlugin(CtxPlugin):
    name = 'PolygonCfgPlugin'
    num_spin = None

    def __init__(self, app, parent):
        CtxPlugin.__init__(self, app, parent)
        events.connect(events.CONFIG_MODIFIED, self.config_changed)

    def build(self):
        bmp = get_bmp(self, icons.CTX_POLYGON_CFG,
                      _('Number of angles for newly created polygon'))
        self.pack(bmp, padding=2)

        self.num_spin = wal.IntSpin(self, config.default_polygon_num,
                                    (3, 1000), onchange=self.changes)
        self.pack(self.num_spin, padding=2)

    def changes(self, *_args):
        val = self.num_spin.get_value()
        if not config.default_polygon_num == val:
            config.default_polygon_num = val
        if self.insp.is_selection():
            selection = self.app.current_doc.selection
            if self.insp.is_obj_polygon(selection.objs[0]):
                self.app.current_doc.api.set_polygon_corners_num(val)

    def config_changed(self, *args):
        if args[0][0] == 'default_polygon_num':
            val = self.num_spin.get_value()
            if not config.default_polygon_num == val:
                self.num_spin.set_value(config.default_polygon_num)
