# -*- coding: utf-8 -*-
#
#  Copyright (C) 2013 by Ihor E. Novikov
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

from uc2.uc2const import COLOR_CMYK as CMYK

colors = [
    [CMYK, [0.0, 0.0, 0.0, 1.0], 1.0, 'Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.9], 1.0, '90% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.8], 1.0, '80% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.7], 1.0, '70% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.6], 1.0, '60% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.5], 1.0, '50% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.4], 1.0, '40% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.3], 1.0, '30% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.2], 1.0, '20% Black'],
    [CMYK, [0.0, 0.0, 0.0, 0.1], 1.0, '10% Black'],
    [CMYK, [0.000000, 0.000000, 0.000000, 0.000000], 1.0, 'White'],
    [CMYK, [1.0, 0.000000, 0.0, 0.000000], 1.0, 'Cyan'],
    [CMYK, [0.0, 1.0, 0.000000, 0.000000], 1.0, 'Magenta'],
    [CMYK, [0.000000, 0.000000, 1.0, 0.000000], 1.0, 'Yellow'],
    [CMYK, [0.000000, 1.0, 1.0, 0.000000], 1.0, 'Red'],
    [CMYK, [1.0, 0.0, 1.0, 0.0], 1.0, 'Green'],
    [CMYK, [1.0, 1.0, 0.0, 0.0], 1.0, 'Blue'],
    [CMYK, [0.020000, 0.973000, 0.890000, 0.494000], 1.0, 'Dark Red'],
    [CMYK, [0.757000, 0.000000, 1.000000, 0.251000], 1.0, 'Dark Green'],
    [CMYK, [0.961000, 0.945000, 0.000000, 0.102000], 1.0, 'Dark Blue'],
    [CMYK, [0.792000, 0.208000, 0.396000, 0.212000], 1.0, 'Dark Cyan'],
    [CMYK, [0.565000, 0.957000, 0.020000, 0.063000], 1.0, 'Dark Magenta'],
    [CMYK, [0.314000, 0.133000, 0.976000, 0.404000], 1.0, 'Dark Yellow'],
    [CMYK, [0.741000, 0.447000, 0.486000, 0.463000], 1.0, 'Dark Slate Gray'],
    [CMYK, [0.451000, 0.373000, 0.365000, 0.408000], 1.0, 'Dim Gray'],
    [CMYK, [0.510000, 0.337000, 0.220000, 0.243000], 1.0, 'Slate Gray'],
    [CMYK, [0.490000, 0.325000, 0.192000, 0.212000], 1.0, 'Light Slate Gray'],
    [CMYK, [0.227000, 0.176000, 0.173000, 0.102000], 1.0, 'Gray'],
    [CMYK, [0.169000, 0.125000, 0.125000, 0.047000], 1.0, 'Light Grey'],
    [CMYK, [0.933000, 0.937000, 0.027000, 0.224000], 1.0, 'Midnight Blue'],
    [CMYK, [0.961000, 0.941000, 0.000000, 0.098000], 1.0, 'Navy'],
    [CMYK, [0.580000, 0.373000, 0.008000, 0.012000], 1.0, 'Cornflower Blue'],
    [CMYK, [0.773000, 0.769000, 0.067000, 0.125000], 1.0, 'Dark Slate Blue'],
    [CMYK, [0.627000, 0.596000, 0.020000, 0.031000], 1.0, 'Slate Blue'],
    [CMYK, [0.565000, 0.529000, 0.008000, 0.012000], 1.0, 'Medium Slate Blue'],
    [CMYK, [0.537000, 0.498000, 0.004000, 0.004000], 1.0, 'Light Slate Blue'],
    [CMYK, [0.902000, 0.773000, 0.000000, 0.000000], 1.0, 'Medium Blue'],
    [CMYK, [0.694000, 0.529000, 0.008000, 0.012000], 1.0, 'Royal Blue'],
    [CMYK, [0.843000, 0.667000, 0.000000, 0.000000], 1.0, 'Blue'],
    [CMYK, [0.675000, 0.380000, 0.000000, 0.000000], 1.0, 'Dodger Blue'],
    [CMYK, [0.643000, 0.118000, 0.008000, 0.004000], 1.0, 'Deep Sky Blue'],
    [CMYK, [0.455000, 0.075000, 0.059000, 0.024000], 1.0, 'Sky Blue'],
    [CMYK, [0.459000, 0.102000, 0.020000, 0.012000], 1.0, 'Light Sky Blue'],
    [CMYK, [0.682000, 0.373000, 0.067000, 0.102000], 1.0, 'Steel Blue'],
    [CMYK, [0.325000, 0.169000, 0.063000, 0.039000], 1.0, 'Light Steel Blue'],
    [CMYK, [0.333000, 0.075000, 0.078000, 0.024000], 1.0, 'Light Blue'],
    [CMYK, [0.318000, 0.047000, 0.098000, 0.016000], 1.0, 'Powder Blue'],
    [CMYK, [0.298000, 0.020000, 0.102000, 0.004000], 1.0, 'Pale Turquoise'],
    [CMYK, [0.631000, 0.008000, 0.220000, 0.004000], 1.0, 'Dark Turquoise'],
    [CMYK, [0.576000, 0.012000, 0.243000, 0.008000], 1.0, 'Medium Turquoise'],
    [CMYK, [0.545000, 0.004000, 0.259000, 0.000000], 1.0, 'Turquoise'],
    [CMYK, [0.459000, 0.000000, 0.129000, 0.000000], 1.0, 'Cyan'],
    [CMYK, [0.122000, 0.012000, 0.035000, 0.000000], 1.0, 'Light Cyan'],
    [CMYK, [0.592000, 0.149000, 0.290000, 0.137000], 1.0, 'Cadet Blue'],
    [CMYK, [0.541000, 0.016000, 0.392000, 0.012000], 1.0, 'Medium Aquamarine'],
    [CMYK, [0.365000, 0.000000, 0.247000, 0.000000], 1.0, 'Aquamarine'],
    [CMYK, [0.757000, 0.031000, 0.992000, 0.455000], 1.0, 'Dark Green 2'],
    [CMYK, [0.600000, 0.290000, 0.878000, 0.365000], 1.0, 'Dark Olive Green'],
    [CMYK, [0.455000, 0.082000, 0.490000, 0.059000], 1.0, 'Dark Sea Green'],
    [CMYK, [0.753000, 0.153000, 0.729000, 0.149000], 1.0, 'Sea Green'],
    [CMYK, [0.682000, 0.020000, 0.659000, 0.016000], 1.0, 'Medium Sea Green'],
    [CMYK, [0.694000, 0.043000, 0.337000, 0.031000], 1.0, 'Light Sea Green'],
    [CMYK, [0.373000, 0.000000, 0.486000, 0.000000], 1.0, 'Pale Green'],
    [CMYK, [0.545000, 0.000000, 0.600000, 0.000000], 1.0, 'Spring Green'],
    [CMYK, [0.525000, 0.000000, 0.961000, 0.000000], 1.0, 'Lawn Green'],
    [CMYK, [0.651000, 0.004000, 0.988000, 0.004000], 1.0, 'Green'],
    [CMYK, [0.514000, 0.000000, 0.953000, 0.000000], 1.0, 'Chartreuse'],
    [CMYK, [0.522000, 0.000000, 0.478000, 0.000000], 1.0,
     'Medium Spring Green'],
    [CMYK, [0.369000, 0.000000, 0.906000, 0.000000], 1.0, 'Green Yellow'],
    [CMYK, [0.682000, 0.000000, 0.925000, 0.000000], 1.0, 'Lime Green'],
    [CMYK, [0.463000, 0.008000, 0.902000, 0.004000], 1.0, 'Yellow Green'],
    [CMYK, [0.749000, 0.039000, 0.973000, 0.188000], 1.0, 'Forest Green'],
    [CMYK, [0.553000, 0.137000, 0.953000, 0.208000], 1.0, 'Olive Drab'],
    [CMYK, [0.263000, 0.165000, 0.651000, 0.086000], 1.0, 'Dark Khaki'],
    [CMYK, [0.090000, 0.059000, 0.549000, 0.004000], 1.0, 'Khaki'],
    [CMYK, [0.086000, 0.059000, 0.408000, 0.004000], 1.0, 'Pale Goldenrod'],
    [CMYK, [0.047000, 0.020000, 0.227000, 0.000000], 1.0,
     'Light Goldenrod Yellow'],
    [CMYK, [0.027000, 0.004000, 0.173000, 0.000000], 1.0, 'Light Yellow'],
    [CMYK, [0.047000, 0.000000, 0.941000, 0.000000], 1.0, 'Yellow'],
    [CMYK, [0.020000, 0.102000, 0.929000, 0.020000], 1.0, 'Gold'],
    [CMYK, [0.090000, 0.090000, 0.580000, 0.012000], 1.0, 'Light Goldenrod'],
    [CMYK, [0.086000, 0.310000, 0.925000, 0.094000], 1.0, 'Goldenrod'],
    [CMYK, [0.078000, 0.357000, 0.984000, 0.267000], 1.0, 'Dark Goldenrod'],
    [CMYK, [0.192000, 0.439000, 0.310000, 0.133000], 1.0, 'Rosy Brown'],
    [CMYK, [0.106000, 0.718000, 0.514000, 0.086000], 1.0, 'Indian Red'],
    [CMYK, [0.133000, 0.663000, 0.945000, 0.435000], 1.0, 'Saddle Brown'],
    [CMYK, [0.220000, 0.671000, 0.839000, 0.259000], 1.0, 'Sienna'],
    [CMYK, [0.133000, 0.494000, 0.812000, 0.098000], 1.0, 'Peru'],
    [CMYK, [0.114000, 0.271000, 0.502000, 0.047000], 1.0, 'Burlywood'],
    [CMYK, [0.051000, 0.031000, 0.169000, 0.004000], 1.0, 'Beige'],
    [CMYK, [0.055000, 0.122000, 0.345000, 0.012000], 1.0, 'Wheat'],
    [CMYK, [0.031000, 0.427000, 0.663000, 0.016000], 1.0, 'Sandy Brown'],
    [CMYK, [0.153000, 0.267000, 0.467000, 0.071000], 1.0, 'Tan'],
    [CMYK, [0.055000, 0.627000, 0.925000, 0.114000], 1.0, 'Chocolate'],
    [CMYK, [0.086000, 0.922000, 0.824000, 0.212000], 1.0, 'Firebrick'],
    [CMYK, [0.184000, 0.894000, 0.769000, 0.216000], 1.0, 'Brown'],
    [CMYK, [0.047000, 0.494000, 0.486000, 0.027000], 1.0, 'Dark Salmon'],
    [CMYK, [0.008000, 0.616000, 0.494000, 0.004000], 1.0, 'Salmon'],
    [CMYK, [0.000000, 0.478000, 0.514000, 0.000000], 1.0, 'Light Salmon'],
    [CMYK, [0.008000, 0.412000, 0.988000, 0.012000], 1.0, 'Orange'],
    [CMYK, [0.004000, 0.537000, 0.969000, 0.012000], 1.0, 'Dark Orange'],
    [CMYK, [0.004000, 0.627000, 0.694000, 0.000000], 1.0, 'Coral'],
    [CMYK, [0.027000, 0.604000, 0.388000, 0.020000], 1.0, 'Light Coral'],
    [CMYK, [0.004000, 0.749000, 0.725000, 0.004000], 1.0, 'Tomato'],
    [CMYK, [0.000000, 0.839000, 0.976000, 0.000000], 1.0, 'Orange Red'],
    [CMYK, [0.000000, 0.965000, 0.996000, 0.004000], 1.0, 'Red'],
    [CMYK, [0.024000, 0.671000, 0.067000, 0.008000], 1.0, 'Hot Pink'],
    [CMYK, [0.012000, 0.894000, 0.078000, 0.000000], 1.0, 'Deep Pink'],
    [CMYK, [0.024000, 0.318000, 0.141000, 0.008000], 1.0, 'Pink'],
    [CMYK, [0.016000, 0.373000, 0.157000, 0.004000], 1.0, 'Light Pink'],
    [CMYK, [0.082000, 0.651000, 0.188000, 0.059000], 1.0, 'Pale Violet Red'],
    [CMYK, [0.169000, 0.890000, 0.271000, 0.192000], 1.0, 'Maroon'],
    [CMYK, [0.212000, 0.922000, 0.035000, 0.039000], 1.0, 'Medium Violet Red'],
    [CMYK, [0.196000, 0.890000, 0.020000, 0.024000], 1.0, 'Violet Red'],
    [CMYK, [0.286000, 0.671000, 0.000000, 0.000000], 1.0, 'Magenta'],
    [CMYK, [0.208000, 0.506000, 0.000000, 0.000000], 1.0, 'Violet'],
    [CMYK, [0.188000, 0.420000, 0.016000, 0.016000], 1.0, 'Plum'],
    [CMYK, [0.251000, 0.584000, 0.000000, 0.000000], 1.0, 'Orchid'],
    [CMYK, [0.408000, 0.631000, 0.004000, 0.004000], 1.0, 'Medium Orchid'],
    [CMYK, [0.533000, 0.698000, 0.004000, 0.004000], 1.0, 'Dark Orchid'],
    [CMYK, [0.569000, 0.733000, 0.000000, 0.000000], 1.0, 'Dark Violet'],
    [CMYK, [0.580000, 0.667000, 0.000000, 0.004000], 1.0, 'Blue Violet'],
    [CMYK, [0.537000, 0.651000, 0.000000, 0.000000], 1.0, 'Purple'],
    [CMYK, [0.494000, 0.529000, 0.016000, 0.020000], 1.0, 'Medium Purple'],
    [CMYK, [0.169000, 0.267000, 0.071000, 0.031000], 1.0, 'Thistle'],
    [CMYK, [0.078000, 0.075000, 0.071000, 0.008000], 1.0, 'Snow2'],
    [CMYK, [0.180000, 0.165000, 0.149000, 0.063000], 1.0, 'Snow3'],
    [CMYK, [0.353000, 0.298000, 0.286000, 0.286000], 1.0, 'Snow4'],
    [CMYK, [0.078000, 0.094000, 0.122000, 0.012000], 1.0, 'Seashell2'],
    [CMYK, [0.180000, 0.176000, 0.204000, 0.067000], 1.0, 'Seashell3'],
    [CMYK, [0.349000, 0.318000, 0.325000, 0.286000], 1.0, 'Seashell4'],
    [CMYK, [0.027000, 0.067000, 0.169000, 0.004000], 1.0, 'AntiqueWhite1'],
    [CMYK, [0.078000, 0.114000, 0.208000, 0.016000], 1.0, 'AntiqueWhite2'],
    [CMYK, [0.176000, 0.200000, 0.286000, 0.071000], 1.0, 'AntiqueWhite3'],
    [CMYK, [0.353000, 0.325000, 0.400000, 0.290000], 1.0, 'AntiqueWhite4'],
    [CMYK, [0.075000, 0.169000, 0.298000, 0.016000], 1.0, 'Bisque2'],
    [CMYK, [0.169000, 0.247000, 0.361000, 0.078000], 1.0, 'Bisque3'],
    [CMYK, [0.349000, 0.373000, 0.478000, 0.294000], 1.0, 'Bisque4'],
    [CMYK, [0.071000, 0.220000, 0.333000, 0.020000], 1.0, 'PeachPuff2'],
    [CMYK, [0.161000, 0.298000, 0.396000, 0.082000], 1.0, 'PeachPuff3'],
    [CMYK, [0.345000, 0.408000, 0.514000, 0.298000], 1.0, 'PeachPuff4'],
    [CMYK, [0.075000, 0.180000, 0.412000, 0.020000], 1.0, 'NavajoWhite2'],
    [CMYK, [0.169000, 0.255000, 0.471000, 0.082000], 1.0, 'NavajoWhite3'],
    [CMYK, [0.349000, 0.388000, 0.569000, 0.298000], 1.0, 'NavajoWhite4'],
    [CMYK, [0.082000, 0.063000, 0.306000, 0.008000], 1.0, 'LemonChiffon2'],
    [CMYK, [0.192000, 0.149000, 0.380000, 0.055000], 1.0, 'LemonChiffon3'],
    [CMYK, [0.373000, 0.298000, 0.502000, 0.267000], 1.0, 'LemonChiffon4'],
    [CMYK, [0.075000, 0.071000, 0.224000, 0.008000], 1.0, 'Cornsilk2'],
    [CMYK, [0.184000, 0.157000, 0.306000, 0.063000], 1.0, 'Cornsilk3'],
    [CMYK, [0.361000, 0.302000, 0.420000, 0.278000], 1.0, 'Cornsilk4'],
    [CMYK, [0.075000, 0.055000, 0.137000, 0.004000], 1.0, 'Ivory2'],
    [CMYK, [0.188000, 0.137000, 0.220000, 0.051000], 1.0, 'Ivory3'],
    [CMYK, [0.361000, 0.286000, 0.345000, 0.275000], 1.0, 'Ivory4'],
    [CMYK, [0.129000, 0.047000, 0.137000, 0.008000], 1.0, 'Honeydew2'],
    [CMYK, [0.243000, 0.118000, 0.224000, 0.051000], 1.0, 'Honeydew3'],
    [CMYK, [0.404000, 0.275000, 0.349000, 0.267000], 1.0, 'Honeydew4'],
    [CMYK, [0.082000, 0.125000, 0.078000, 0.012000], 1.0, 'LavenderBlush2'],
    [CMYK, [0.176000, 0.208000, 0.145000, 0.067000], 1.0, 'LavenderBlush3'],
    [CMYK, [0.349000, 0.337000, 0.286000, 0.286000], 1.0, 'LavenderBlush4'],
    [CMYK, [0.075000, 0.180000, 0.141000, 0.016000], 1.0, 'MistyRose2'],
    [CMYK, [0.165000, 0.259000, 0.212000, 0.075000], 1.0, 'MistyRose3'],
    [CMYK, [0.349000, 0.380000, 0.349000, 0.294000], 1.0, 'MistyRose4'],
    [CMYK, [0.129000, 0.051000, 0.067000, 0.008000], 1.0, 'Azure2'],
    [CMYK, [0.239000, 0.125000, 0.149000, 0.051000], 1.0, 'Azure3'],
    [CMYK, [0.400000, 0.278000, 0.290000, 0.271000], 1.0, 'Azure4'],
    [CMYK, [0.541000, 0.498000, 0.004000, 0.004000], 1.0, 'SlateBlue1'],
    [CMYK, [0.569000, 0.529000, 0.008000, 0.012000], 1.0, 'SlateBlue2'],
    [CMYK, [0.631000, 0.604000, 0.020000, 0.031000], 1.0, 'SlateBlue3'],
    [CMYK, [0.776000, 0.773000, 0.067000, 0.122000], 1.0, 'SlateBlue4'],
    [CMYK, [0.651000, 0.475000, 0.004000, 0.004000], 1.0, 'RoyalBlue1'],
    [CMYK, [0.678000, 0.510000, 0.004000, 0.008000], 1.0, 'RoyalBlue2'],
    [CMYK, [0.737000, 0.576000, 0.012000, 0.020000], 1.0, 'RoyalBlue3'],
    [CMYK, [0.867000, 0.737000, 0.063000, 0.149000], 1.0, 'RoyalBlue4'],
    [CMYK, [0.875000, 0.714000, 0.000000, 0.000000], 1.0, 'Blue2'],
    [CMYK, [0.961000, 0.929000, 0.000000, 0.051000], 1.0, 'Blue4'],
    [CMYK, [0.702000, 0.420000, 0.004000, 0.004000], 1.0, 'DodgerBlue2'],
    [CMYK, [0.761000, 0.486000, 0.012000, 0.024000], 1.0, 'DodgerBlue3'],
    [CMYK, [0.882000, 0.643000, 0.094000, 0.184000], 1.0, 'DodgerBlue4'],
    [CMYK, [0.557000, 0.200000, 0.008000, 0.008000], 1.0, 'SteelBlue1'],
    [CMYK, [0.580000, 0.231000, 0.016000, 0.020000], 1.0, 'SteelBlue2'],
    [CMYK, [0.639000, 0.318000, 0.039000, 0.055000], 1.0, 'SteelBlue3'],
    [CMYK, [0.749000, 0.478000, 0.149000, 0.239000], 1.0, 'SteelBlue4'],
    [CMYK, [0.671000, 0.153000, 0.020000, 0.016000], 1.0, 'DeepSkyBlue2'],
    [CMYK, [0.718000, 0.216000, 0.051000, 0.059000], 1.0, 'DeepSkyBlue3'],
    [CMYK, [0.820000, 0.392000, 0.165000, 0.263000], 1.0, 'DeepSkyBlue4'],
    [CMYK, [0.459000, 0.114000, 0.008000, 0.004000], 1.0, 'SkyBlue1'],
    [CMYK, [0.490000, 0.145000, 0.031000, 0.024000], 1.0, 'SkyBlue2'],
    [CMYK, [0.549000, 0.216000, 0.071000, 0.071000], 1.0, 'SkyBlue3'],
    [CMYK, [0.663000, 0.388000, 0.184000, 0.267000], 1.0, 'SkyBlue4'],
    [CMYK, [0.322000, 0.067000, 0.020000, 0.008000], 1.0, 'LightSkyBlue1'],
    [CMYK, [0.369000, 0.094000, 0.047000, 0.020000], 1.0, 'LightSkyBlue2'],
    [CMYK, [0.443000, 0.161000, 0.098000, 0.075000], 1.0, 'LightSkyBlue3'],
    [CMYK, [0.573000, 0.333000, 0.231000, 0.267000], 1.0, 'LightSkyBlue4'],
    [CMYK, [0.251000, 0.090000, 0.012000, 0.004000], 1.0, 'SlateGray1'],
    [CMYK, [0.294000, 0.125000, 0.039000, 0.020000], 1.0, 'SlateGray2'],
    [CMYK, [0.376000, 0.196000, 0.094000, 0.071000], 1.0, 'SlateGray3'],
    [CMYK, [0.518000, 0.361000, 0.227000, 0.267000], 1.0, 'SlateGray4'],
    [CMYK, [0.239000, 0.098000, 0.008000, 0.004000], 1.0, 'LightSteelBlue1'],
    [CMYK, [0.286000, 0.129000, 0.035000, 0.016000], 1.0, 'LightSteelBlue2'],
    [CMYK, [0.373000, 0.208000, 0.090000, 0.071000], 1.0, 'LightSteelBlue3'],
    [CMYK, [0.510000, 0.361000, 0.227000, 0.267000], 1.0, 'LightSteelBlue4'],
    [CMYK, [0.255000, 0.031000, 0.027000, 0.004000], 1.0, 'LightBlue1'],
    [CMYK, [0.310000, 0.055000, 0.067000, 0.016000], 1.0, 'LightBlue2'],
    [CMYK, [0.400000, 0.125000, 0.133000, 0.059000], 1.0, 'LightBlue3'],
    [CMYK, [0.537000, 0.286000, 0.282000, 0.255000], 1.0, 'LightBlue4'],
    [CMYK, [0.184000, 0.043000, 0.078000, 0.008000], 1.0, 'LightCyan2'],
    [CMYK, [0.298000, 0.106000, 0.161000, 0.047000], 1.0, 'LightCyan3'],
    [CMYK, [0.459000, 0.267000, 0.306000, 0.251000], 1.0, 'LightCyan4'],
    [CMYK, [0.227000, 0.004000, 0.055000, 0.000000], 1.0, 'PaleTurquoise1'],
    [CMYK, [0.302000, 0.020000, 0.102000, 0.004000], 1.0, 'PaleTurquoise2'],
    [CMYK, [0.416000, 0.063000, 0.184000, 0.035000], 1.0, 'PaleTurquoise3'],
    [CMYK, [0.553000, 0.239000, 0.322000, 0.231000], 1.0, 'PaleTurquoise4'],
    [CMYK, [0.341000, 0.008000, 0.063000, 0.000000], 1.0, 'CadetBlue1'],
    [CMYK, [0.400000, 0.020000, 0.102000, 0.008000], 1.0, 'CadetBlue2'],
    [CMYK, [0.502000, 0.063000, 0.169000, 0.039000], 1.0, 'CadetBlue3'],
    [CMYK, [0.624000, 0.231000, 0.306000, 0.239000], 1.0, 'CadetBlue4'],
    [CMYK, [0.498000, 0.000000, 0.114000, 0.000000], 1.0, 'Turquoise1'],
    [CMYK, [0.557000, 0.000000, 0.149000, 0.000000], 1.0, 'Turquoise2'],
    [CMYK, [0.655000, 0.016000, 0.212000, 0.012000], 1.0, 'Turquoise3'],
    [CMYK, [0.780000, 0.188000, 0.345000, 0.184000], 1.0, 'Turquoise4'],
    [CMYK, [0.529000, 0.000000, 0.173000, 0.000000], 1.0, 'cyan2'],
    [CMYK, [0.635000, 0.008000, 0.239000, 0.004000], 1.0, 'cyan3'],
    [CMYK, [0.776000, 0.165000, 0.376000, 0.161000], 1.0, 'cyan4'],
    [CMYK, [0.314000, 0.000000, 0.078000, 0.000000], 1.0, 'DarkSlateGray1'],
    [CMYK, [0.384000, 0.008000, 0.122000, 0.004000], 1.0, 'DarkSlateGray2'],
    [CMYK, [0.494000, 0.039000, 0.200000, 0.024000], 1.0, 'DarkSlateGray3'],
    [CMYK, [0.627000, 0.212000, 0.337000, 0.212000], 1.0, 'DarkSlateGray4'],
    [CMYK, [0.431000, 0.000000, 0.298000, 0.000000], 1.0, 'Aquamarine2'],
    [CMYK, [0.682000, 0.184000, 0.514000, 0.184000], 1.0, 'Aquamarine4'],
    [CMYK, [0.235000, 0.000000, 0.310000, 0.000000], 1.0, 'DarkSeaGreen1'],
    [CMYK, [0.298000, 0.008000, 0.361000, 0.000000], 1.0, 'DarkSeaGreen2'],
    [CMYK, [0.412000, 0.043000, 0.455000, 0.024000], 1.0, 'DarkSeaGreen3'],
    [CMYK, [0.557000, 0.220000, 0.573000, 0.224000], 1.0, 'DarkSeaGreen4'],
    [CMYK, [0.463000, 0.000000, 0.451000, 0.000000], 1.0, 'SeaGreen1'],
    [CMYK, [0.518000, 0.000000, 0.510000, 0.000000], 1.0, 'SeaGreen2'],
    [CMYK, [0.616000, 0.000000, 0.600000, 0.000000], 1.0, 'SeaGreen3'],
    [CMYK, [0.357000, 0.000000, 0.475000, 0.000000], 1.0, 'PaleGreen1'],
    [CMYK, [0.412000, 0.000000, 0.518000, 0.000000], 1.0, 'PaleGreen2'],
    [CMYK, [0.518000, 0.012000, 0.616000, 0.008000], 1.0, 'PaleGreen3'],
    [CMYK, [0.651000, 0.180000, 0.729000, 0.184000], 1.0, 'PaleGreen4'],
    [CMYK, [0.592000, 0.000000, 0.639000, 0.000000], 1.0, 'SpringGreen2'],
    [CMYK, [0.678000, 0.000000, 0.722000, 0.000000], 1.0, 'SpringGreen3'],
    [CMYK, [0.804000, 0.125000, 0.843000, 0.122000], 1.0, 'SpringGreen4'],
    [CMYK, [0.663000, 0.000000, 0.973000, 0.000000], 1.0, 'Green2'],
    [CMYK, [0.706000, 0.000000, 0.976000, 0.000000], 1.0, 'Green3'],
    [CMYK, [0.757000, 0.000000, 1.000000, 0.169000], 1.0, 'Green4'],
    [CMYK, [0.545000, 0.000000, 0.980000, 0.000000], 1.0, 'Chartreuse2'],
    [CMYK, [0.604000, 0.000000, 0.965000, 0.000000], 1.0, 'Chartreuse3'],
    [CMYK, [0.655000, 0.039000, 0.988000, 0.216000], 1.0, 'Chartreuse4'],
    [CMYK, [0.294000, 0.000000, 0.867000, 0.000000], 1.0, 'OliveDrab1'],
    [CMYK, [0.357000, 0.000000, 0.878000, 0.000000], 1.0, 'OliveDrab2'],
    [CMYK, [0.549000, 0.141000, 0.957000, 0.239000], 1.0, 'OliveDrab4'],
    [CMYK, [0.247000, 0.000000, 0.686000, 0.000000], 1.0, 'DarkOliveGreen1'],
    [CMYK, [0.310000, 0.000000, 0.702000, 0.000000], 1.0, 'DarkOliveGreen2'],
    [CMYK, [0.420000, 0.024000, 0.753000, 0.012000], 1.0, 'DarkOliveGreen3'],
    [CMYK, [0.545000, 0.188000, 0.843000, 0.220000], 1.0, 'DarkOliveGreen4'],
    [CMYK, [0.043000, 0.024000, 0.553000, 0.000000], 1.0, 'Khaki1'],
    [CMYK, [0.098000, 0.055000, 0.576000, 0.004000], 1.0, 'Khaki2'],
    [CMYK, [0.208000, 0.137000, 0.627000, 0.051000], 1.0, 'Khaki3'],
    [CMYK, [0.384000, 0.298000, 0.718000, 0.259000], 1.0, 'Khaki4'],
    [CMYK, [0.024000, 0.059000, 0.561000, 0.000000], 1.0, 'LightGoldenrod1'],
    [CMYK, [0.090000, 0.094000, 0.580000, 0.012000], 1.0, 'LightGoldenrod2'],
    [CMYK, [0.192000, 0.173000, 0.631000, 0.071000], 1.0, 'LightGoldenrod3'],
    [CMYK, [0.373000, 0.318000, 0.725000, 0.278000], 1.0, 'LightGoldenrod4'],
    [CMYK, [0.078000, 0.055000, 0.212000, 0.004000], 1.0, 'LightYellow2'],
    [CMYK, [0.192000, 0.133000, 0.302000, 0.047000], 1.0, 'LightYellow3'],
    [CMYK, [0.373000, 0.290000, 0.431000, 0.263000], 1.0, 'LightYellow4'],
    [CMYK, [0.125000, 0.004000, 0.937000, 0.000000], 1.0, 'Yellow2'],
    [CMYK, [0.243000, 0.047000, 0.969000, 0.035000], 1.0, 'Yellow3'],
    [CMYK, [0.275000, 0.098000, 0.976000, 0.376000], 1.0, 'Yellow4'],
    [CMYK, [0.071000, 0.141000, 0.945000, 0.039000], 1.0, 'Gold2'],
    [CMYK, [0.082000, 0.165000, 0.961000, 0.180000], 1.0, 'Gold3'],
    [CMYK, [0.165000, 0.224000, 0.973000, 0.459000], 1.0, 'Gold4'],
    [CMYK, [0.012000, 0.247000, 0.906000, 0.004000], 1.0, 'Goldenrod1'],
    [CMYK, [0.047000, 0.275000, 0.922000, 0.047000], 1.0, 'Goldenrod2'],
    [CMYK, [0.129000, 0.325000, 0.945000, 0.125000], 1.0, 'Goldenrod3'],
    [CMYK, [0.196000, 0.369000, 0.969000, 0.439000], 1.0, 'Goldenrod4'],
    [CMYK, [0.008000, 0.294000, 0.945000, 0.008000], 1.0, 'DarkGoldenrod1'],
    [CMYK, [0.043000, 0.322000, 0.961000, 0.047000], 1.0, 'DarkGoldenrod2'],
    [CMYK, [0.094000, 0.353000, 0.965000, 0.145000], 1.0, 'DarkGoldenrod3'],
    [CMYK, [0.137000, 0.384000, 0.980000, 0.475000], 1.0, 'DarkGoldenrod4'],
    [CMYK, [0.024000, 0.314000, 0.196000, 0.008000], 1.0, 'RosyBrown1'],
    [CMYK, [0.059000, 0.353000, 0.216000, 0.024000], 1.0, 'RosyBrown2'],
    [CMYK, [0.141000, 0.420000, 0.282000, 0.086000], 1.0, 'RosyBrown3'],
    [CMYK, [0.337000, 0.518000, 0.404000, 0.302000], 1.0, 'RosyBrown4'],
    [CMYK, [0.004000, 0.722000, 0.506000, 0.004000], 1.0, 'IndianRed1'],
    [CMYK, [0.024000, 0.729000, 0.510000, 0.020000], 1.0, 'IndianRed2'],
    [CMYK, [0.098000, 0.753000, 0.549000, 0.082000], 1.0, 'IndianRed3'],
    [CMYK, [0.306000, 0.804000, 0.643000, 0.310000], 1.0, 'IndianRed4'],
    [CMYK, [0.004000, 0.604000, 0.757000, 0.004000], 1.0, 'Sienna1'],
    [CMYK, [0.031000, 0.616000, 0.757000, 0.020000], 1.0, 'Sienna2'],
    [CMYK, [0.114000, 0.647000, 0.792000, 0.090000], 1.0, 'Sienna3'],
    [CMYK, [0.294000, 0.702000, 0.867000, 0.325000], 1.0, 'Sienna4'],
    [CMYK, [0.027000, 0.192000, 0.447000, 0.004000], 1.0, 'Burlywood1'],
    [CMYK, [0.067000, 0.235000, 0.467000, 0.020000], 1.0, 'Burlywood2'],
    [CMYK, [0.161000, 0.306000, 0.525000, 0.086000], 1.0, 'Burlywood3'],
    [CMYK, [0.345000, 0.424000, 0.624000, 0.302000], 1.0, 'Burlywood4'],
    [CMYK, [0.024000, 0.090000, 0.333000, 0.004000], 1.0, 'Wheat1'],
    [CMYK, [0.078000, 0.141000, 0.361000, 0.016000], 1.0, 'Wheat2'],
    [CMYK, [0.173000, 0.227000, 0.424000, 0.078000], 1.0, 'Wheat3'],
    [CMYK, [0.349000, 0.365000, 0.525000, 0.294000], 1.0, 'Wheat4'],
    [CMYK, [0.008000, 0.435000, 0.745000, 0.004000], 1.0, 'Tan1'],
    [CMYK, [0.051000, 0.451000, 0.769000, 0.027000], 1.0, 'Tan2'],
    [CMYK, [0.290000, 0.565000, 0.859000, 0.345000], 1.0, 'Tan4'],
    [CMYK, [0.004000, 0.612000, 0.910000, 0.004000], 1.0, 'Chocolate1'],
    [CMYK, [0.031000, 0.620000, 0.925000, 0.020000], 1.0, 'Chocolate2'],
    [CMYK, [0.063000, 0.631000, 0.925000, 0.129000], 1.0, 'Chocolate3'],
    [CMYK, [0.000000, 0.925000, 0.851000, 0.000000], 1.0, 'Firebrick1'],
    [CMYK, [0.012000, 0.914000, 0.820000, 0.016000], 1.0, 'Firebrick2'],
    [CMYK, [0.078000, 0.922000, 0.839000, 0.071000], 1.0, 'Firebrick3'],
    [CMYK, [0.239000, 0.945000, 0.863000, 0.322000], 1.0, 'Firebrick4'],
    [CMYK, [0.000000, 0.878000, 0.737000, 0.000000], 1.0, 'Brown1'],
    [CMYK, [0.012000, 0.875000, 0.725000, 0.012000], 1.0, 'Brown2'],
    [CMYK, [0.086000, 0.882000, 0.741000, 0.078000], 1.0, 'Brown3'],
    [CMYK, [0.271000, 0.914000, 0.804000, 0.314000], 1.0, 'Brown4'],
    [CMYK, [0.008000, 0.573000, 0.573000, 0.004000], 1.0, 'Salmon1'],
    [CMYK, [0.035000, 0.588000, 0.592000, 0.024000], 1.0, 'Salmon2'],
    [CMYK, [0.114000, 0.624000, 0.635000, 0.090000], 1.0, 'Salmon3'],
    [CMYK, [0.322000, 0.686000, 0.710000, 0.310000], 1.0, 'Salmon4'],
    [CMYK, [0.035000, 0.502000, 0.533000, 0.020000], 1.0, 'LightSalmon2'],
    [CMYK, [0.125000, 0.537000, 0.588000, 0.090000], 1.0, 'LightSalmon3'],
    [CMYK, [0.329000, 0.620000, 0.671000, 0.310000], 1.0, 'LightSalmon4'],
    [CMYK, [0.020000, 0.416000, 0.965000, 0.055000], 1.0, 'Orange2'],
    [CMYK, [0.078000, 0.447000, 0.980000, 0.145000], 1.0, 'Orange3'],
    [CMYK, [0.078000, 0.467000, 0.988000, 0.502000], 1.0, 'Orange4'],
    [CMYK, [0.000000, 0.600000, 0.965000, 0.004000], 1.0, 'DarkOrange1'],
    [CMYK, [0.016000, 0.604000, 0.957000, 0.024000], 1.0, 'DarkOrange2'],
    [CMYK, [0.020000, 0.616000, 0.996000, 0.165000], 1.0, 'DarkOrange3'],
    [CMYK, [0.004000, 0.627000, 1.000000, 0.518000], 1.0, 'DarkOrange4'],
    [CMYK, [0.004000, 0.690000, 0.651000, 0.004000], 1.0, 'Coral1'],
    [CMYK, [0.024000, 0.690000, 0.643000, 0.016000], 1.0, 'Coral2'],
    [CMYK, [0.102000, 0.714000, 0.682000, 0.086000], 1.0, 'Coral3'],
    [CMYK, [0.302000, 0.773000, 0.761000, 0.314000], 1.0, 'Coral4'],
    [CMYK, [0.024000, 0.745000, 0.714000, 0.016000], 1.0, 'Tomato2'],
    [CMYK, [0.098000, 0.765000, 0.741000, 0.082000], 1.0, 'Tomato3'],
    [CMYK, [0.282000, 0.804000, 0.827000, 0.322000], 1.0, 'Tomato4'],
    [CMYK, [0.000000, 0.831000, 0.976000, 0.016000], 1.0, 'OrangeRed2'],
    [CMYK, [0.020000, 0.835000, 0.973000, 0.118000], 1.0, 'OrangeRed3'],
    [CMYK, [0.055000, 0.855000, 0.976000, 0.443000], 1.0, 'OrangeRed4'],
    [CMYK, [0.000000, 0.965000, 1.000000, 0.020000], 1.0, 'Red2'],
    [CMYK, [0.016000, 0.941000, 0.933000, 0.082000], 1.0, 'Red3'],
    [CMYK, [0.039000, 0.953000, 0.898000, 0.408000], 1.0, 'Red4'],
    [CMYK, [0.039000, 0.925000, 0.067000, 0.012000], 1.0, 'DeepPink2'],
    [CMYK, [0.106000, 0.937000, 0.094000, 0.075000], 1.0, 'DeepPink3'],
    [CMYK, [0.231000, 0.965000, 0.165000, 0.337000], 1.0, 'DeepPink4'],
    [CMYK, [0.027000, 0.659000, 0.075000, 0.008000], 1.0, 'HotPink1'],
    [CMYK, [0.063000, 0.667000, 0.094000, 0.024000], 1.0, 'HotPink2'],
    [CMYK, [0.141000, 0.702000, 0.141000, 0.078000], 1.0, 'HotPink3'],
    [CMYK, [0.357000, 0.816000, 0.247000, 0.267000], 1.0, 'HotPink4'],
    [CMYK, [0.012000, 0.376000, 0.129000, 0.004000], 1.0, 'Pink1'],
    [CMYK, [0.055000, 0.412000, 0.153000, 0.024000], 1.0, 'Pink2'],
    [CMYK, [0.137000, 0.475000, 0.220000, 0.090000], 1.0, 'Pink3'],
    [CMYK, [0.329000, 0.569000, 0.337000, 0.302000], 1.0, 'Pink4'],
    [CMYK, [0.012000, 0.420000, 0.180000, 0.004000], 1.0, 'LightPink1'],
    [CMYK, [0.047000, 0.451000, 0.200000, 0.024000], 1.0, 'LightPink2'],
    [CMYK, [0.133000, 0.502000, 0.267000, 0.090000], 1.0, 'LightPink3'],
    [CMYK, [0.329000, 0.584000, 0.400000, 0.306000], 1.0, 'LightPink4'],
    [CMYK, [0.012000, 0.600000, 0.149000, 0.004000], 1.0, 'PaleVioletRed1'],
    [CMYK, [0.039000, 0.624000, 0.161000, 0.024000], 1.0, 'PaleVioletRed2'],
    [CMYK, [0.118000, 0.667000, 0.216000, 0.094000], 1.0, 'PaleVioletRed3'],
    [CMYK, [0.318000, 0.737000, 0.325000, 0.310000], 1.0, 'PaleVioletRed4'],
    [CMYK, [0.059000, 0.800000, 0.000000, 0.000000], 1.0, 'Maroon1'],
    [CMYK, [0.114000, 0.827000, 0.004000, 0.004000], 1.0, 'Maroon2'],
    [CMYK, [0.204000, 0.871000, 0.024000, 0.031000], 1.0, 'Maroon3'],
    [CMYK, [0.384000, 0.945000, 0.145000, 0.224000], 1.0, 'Maroon4'],
    [CMYK, [0.008000, 0.843000, 0.110000, 0.004000], 1.0, 'VioletRed1'],
    [CMYK, [0.035000, 0.851000, 0.106000, 0.020000], 1.0, 'VioletRed2'],
    [CMYK, [0.110000, 0.878000, 0.141000, 0.086000], 1.0, 'VioletRed3'],
    [CMYK, [0.298000, 0.925000, 0.255000, 0.310000], 1.0, 'VioletRed4'],
    [CMYK, [0.318000, 0.702000, 0.000000, 0.000000], 1.0, 'Magenta2'],
    [CMYK, [0.380000, 0.757000, 0.000000, 0.000000], 1.0, 'Magenta3'],
    [CMYK, [0.545000, 0.937000, 0.008000, 0.031000], 1.0, 'Magenta4'],
    [CMYK, [0.169000, 0.498000, 0.000000, 0.000000], 1.0, 'Orchid1'],
    [CMYK, [0.212000, 0.537000, 0.000000, 0.000000], 1.0, 'Orchid2'],
    [CMYK, [0.286000, 0.612000, 0.008000, 0.008000], 1.0, 'Orchid3'],
    [CMYK, [0.478000, 0.753000, 0.086000, 0.125000], 1.0, 'Orchid4'],
    [CMYK, [0.110000, 0.314000, 0.000000, 0.000000], 1.0, 'Plum1'],
    [CMYK, [0.149000, 0.369000, 0.004000, 0.004000], 1.0, 'Plum2'],
    [CMYK, [0.227000, 0.451000, 0.035000, 0.031000], 1.0, 'Plum3'],
    [CMYK, [0.424000, 0.580000, 0.149000, 0.192000], 1.0, 'Plum4'],
    [CMYK, [0.322000, 0.533000, 0.000000, 0.000000], 1.0, 'MediumOrchid1'],
    [CMYK, [0.349000, 0.573000, 0.000000, 0.000000], 1.0, 'MediumOrchid2'],
    [CMYK, [0.420000, 0.643000, 0.004000, 0.008000], 1.0, 'MediumOrchid3'],
    [CMYK, [0.584000, 0.812000, 0.051000, 0.086000], 1.0, 'MediumOrchid4'],
    [CMYK, [0.451000, 0.592000, 0.000000, 0.000000], 1.0, 'DarkOrchid1'],
    [CMYK, [0.475000, 0.627000, 0.000000, 0.000000], 1.0, 'DarkOrchid2'],
    [CMYK, [0.529000, 0.694000, 0.000000, 0.004000], 1.0, 'DarkOrchid3'],
    [CMYK, [0.675000, 0.886000, 0.027000, 0.059000], 1.0, 'DarkOrchid4'],
    [CMYK, [0.541000, 0.608000, 0.000000, 0.004000], 1.0, 'Purple1'],
    [CMYK, [0.561000, 0.643000, 0.004000, 0.004000], 1.0, 'Purple2'],
    [CMYK, [0.624000, 0.718000, 0.004000, 0.004000], 1.0, 'Purple3'],
    [CMYK, [0.761000, 0.910000, 0.027000, 0.051000], 1.0, 'Purple4'],
    [CMYK, [0.427000, 0.451000, 0.004000, 0.004000], 1.0, 'MediumPurple1'],
    [CMYK, [0.459000, 0.490000, 0.008000, 0.012000], 1.0, 'MediumPurple2'],
    [CMYK, [0.529000, 0.561000, 0.020000, 0.031000], 1.0, 'MediumPurple3'],
    [CMYK, [0.675000, 0.718000, 0.082000, 0.141000], 1.0, 'MediumPurple4'],
    [CMYK, [0.063000, 0.149000, 0.024000, 0.000000], 1.0, 'Thistle1'],
    [CMYK, [0.106000, 0.200000, 0.035000, 0.004000], 1.0, 'Thistle2'],
    [CMYK, [0.196000, 0.294000, 0.090000, 0.047000], 1.0, 'Thistle3'],
    [CMYK, [0.384000, 0.435000, 0.231000, 0.239000], 1.0, 'Thistle4'],
    [CMYK, [0.016000, 0.024000, 0.031000, 0.000000], 1.0, 'Snow'],
    [CMYK, [0.047000, 0.027000, 0.020000, 0.000000], 1.0, 'Ghost White'],
    [CMYK, [0.043000, 0.031000, 0.031000, 0.004000], 1.0, 'White Smoke'],
    [CMYK, [0.137000, 0.102000, 0.102000, 0.027000], 1.0, 'Gainsboro'],
    [CMYK, [0.016000, 0.020000, 0.078000, 0.000000], 1.0, 'Floral White'],
    [CMYK, [0.027000, 0.035000, 0.118000, 0.004000], 1.0, 'Old Lace'],
    [CMYK, [0.043000, 0.059000, 0.110000, 0.004000], 1.0, 'Linen'],
    [CMYK, [0.039000, 0.075000, 0.184000, 0.004000], 1.0, 'Antique White'],
    [CMYK, [0.027000, 0.063000, 0.204000, 0.004000], 1.0, 'Papaya Whip'],
    [CMYK, [0.024000, 0.078000, 0.235000, 0.004000], 1.0, 'Blanched Almond'],
    [CMYK, [0.031000, 0.114000, 0.271000, 0.004000], 1.0, 'Bisque'],
    [CMYK, [0.027000, 0.161000, 0.314000, 0.004000], 1.0, 'Peach Puff'],
    [CMYK, [0.031000, 0.129000, 0.384000, 0.004000], 1.0, 'Navajo White'],
    [CMYK, [0.031000, 0.106000, 0.345000, 0.004000], 1.0, 'Moccasin'],
    [CMYK, [0.024000, 0.024000, 0.176000, 0.000000], 1.0, 'Cornsilk'],
    [CMYK, [0.016000, 0.004000, 0.090000, 0.000000], 1.0, 'Ivory'],
    [CMYK, [0.031000, 0.020000, 0.259000, 0.000000], 1.0, 'Lemon Chiffon'],
    [CMYK, [0.024000, 0.039000, 0.086000, 0.004000], 1.0, 'Seashell'],
    [CMYK, [0.067000, 0.008000, 0.090000, 0.000000], 1.0, 'Honeydew'],
    [CMYK, [0.039000, 0.008000, 0.035000, 0.000000], 1.0, 'Mint Cream'],
    [CMYK, [0.063000, 0.008000, 0.020000, 0.000000], 1.0, 'Azure'],
    [CMYK, [0.078000, 0.027000, 0.024000, 0.004000], 1.0, 'Alice Blue'],
    [CMYK, [0.133000, 0.094000, 0.031000, 0.004000], 1.0, 'Lavender'],
    [CMYK, [0.035000, 0.071000, 0.047000, 0.004000], 1.0, 'Lavender Blush'],
    [CMYK, [0.031000, 0.125000, 0.122000, 0.004000], 1.0, 'Misty Rose'],
]
