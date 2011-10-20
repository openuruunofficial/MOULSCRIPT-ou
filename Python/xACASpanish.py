""" *==LICENSE==*

CyanWorlds.com Engine - MMOG client, server and tools
Copyright (C) 2011 Cyan Worlds, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

Additional permissions under GNU GPL version 3 section 7

If you modify this Program, or any covered work, by linking or
combining it with any of RAD Game Tools Bink SDK, Autodesk 3ds Max SDK,
NVIDIA PhysX SDK, Microsoft DirectX SDK, OpenSSL library, Independent
JPEG Group JPEG library, Microsoft Windows Media SDK, or Apple QuickTime SDK
(or a modified version of those libraries),
containing parts covered by the terms of the Bink SDK EULA, 3ds Max EULA,
PhysX SDK EULA, DirectX SDK EULA, OpenSSL and SSLeay licenses, IJG
JPEG Library README, Windows Media SDK EULA, or QuickTime SDK EULA, the
licensors of this Program grant you additional
permission to convey the resulting work. Corresponding Source for a
non-source form of such a combination shall include the source code for
the parts of OpenSSL and IJG JPEG Library used as well as that of the covered
work.

You can contact Cyan Worlds, Inc. by email legal@cyan.com
 or by snail mail at:
      Cyan Worlds, Inc.
      14617 N Newport Hwy
      Mead, WA   99021

 *==LICENSE==* """
"""
This module contains all the strings that need to localized for the ACA
"""

xGlassesName = "Gafas"
xQuitConfirm = "�Est�s seguro de querer salir de Uru?"
#xQuitConfirm = "�Nadie ha visto tu nuevo aspecto! �Seguro que quieres salir?"
xResetConfirm = "�Quieres reiniciar tus cambios?"

xClothesXRef = { # "name in max file": "nombre traducido"
                # Pelo
                "Hair Tint": "Color pelo",
                "Short Hair - Left Part": "Pelo corto - Lado izquierdo",
                "Short Hair - Right Part": "Pelo corto - Lado derecho",
                "Afro": "Afro",
                "Pony Tail": "Cola de caballo",
                "Ponytail": "Cola de caballo",
                "Roman": "Corte a la romana",
                "Bald": "Calvo",
                "Balding": "Con calvicie",
                "Curly": "Rizado",
                "Hard Hat": "Sombrero duro",
                "Golf Cap": "Gorra de golf",
                "Cap": "Gorra",
                "Hat": "Sombrero",
                "Panama Hat": "Sombrero de paja",
                "Knit Hat": "S:Knit Hat",               # NEW #
                "HardHat": "S:Hard Hat",                # NEW #
                # Cara
                "Face": "Cara",
                "Eyes": "Ojos",
                "Glasses": "Gafas",
                # Prenda superior
                "Shirt": "Camisa",
                "Logo": "Logo",
                "Jacket": "Chaqueta",
                "V-Neck": "Cuello de pico",
                "Coat": "Abrigo",
                "Sweater": "Jersey",
                "T-Shirt": "Camiseta",
                "Long Sleeve Shirt": "Camisa de manga larga",
                "Long Sleeve Shirt - Clock": "Camisa de manga larga -Reloj",
                "Long Sleeve Shirt - Tower": "Camisa de manga larga - Torre",
                "Long Sleeve T-Shirt": "Camiseta de manga larga",
                "Long Sleeve T-Shirt - Myst": "Camiseta de manga larga - Myst",
                "Long Sleeve T-Shirt - Riven": "Camiseta de manga larga - Riven",
                "Long Sleeve T-Shirt - Cosmic Osmo": "Camiseta de manga larga - Cosmic Osmo",
                "Leather Jacket": "Cazadora de cuero",
                "Leather Jacket - DRC": "Cazadora de cuero - DRC",
                "Leather Jacket - Clock": "Cazadora de cuero - Reloj",
                "Leather Jacket - Tower": "Cazadora de cuero - Torre",
                "Shearling Coat": "Abrigo de piel de cordero",
                "Dress Shirt": "Camisa de etiqueta",
                "Fleece Pullover": "Jersey de lana",
                "Zipper": "Cierre",
                "zipper": "Cierre",
                "Pullover": "Jersey",
                "Tie Dye T-Shirt": "Camisa de color ajustada",
                "Tie Dye Shirt": "Camisa de color ajustada",
                "Dye 1": "Tinte 1",
                "Dye 2": "Tinte 2",
                "Blouse": "Blusa",
                "Undershirt": "El�stica",
                "Leather": "Cuero",
                "Highland Sweater": "Jersey escoc�s",
                "Turtleneck": "Cuello alto",
                "Short Sleeve T-Shirt": "Camiseta de manga corta",
                "Short Sleeve T-Shirt - Myst": "Camiseta de manga corta - Myst",
                "Short Sleeve T-Shirt - Riven": "Camiseta de manga corta - Riven",
                "Short Sleeve T-Shirt - Cosmic Osmo": "Camiseta de manga corta - Cosmic Osmo",
                "Knit Sweater": "Su�ter de punto",
                "Yeesha Reward": "Premio de Yeesha",
                "Work Shirt": "S:Work Shirt",               # NEW #
                "Polo Shirt": "S:Polo Shirt",               # NEW #
                "Hooded Sweatshirt": "S:Hooded Sweatshirt", # NEW #
                "Sweatshirt": "S:Sweatshirt",               # NEW #
                "Bomber Jacket": "S:Bomber Jacket",         # NEW #
                "Sleeveless Shirt": "S:Sleeveless Shirt",   # NEW #
                "Windbreaker": "S:Windbreaker",             # NEW #
                "Color1": "S:Color 1",                      # NEW #
                "Color2": "S:Color 2",                      # NEW #
                "Field Vest": "S:Field Vest",               # NEW #
                "Vest": "S:Vest",                           # NEW #
                # Manos
                "Hand": "Mano",
                "Hands": "Manos",
                "Nails": "U�as",
                "Glove": "Guante",
                "Gloves": "Guantes",
                "Fingerless Gloves": "Guantes sin dedos",
                "Canvas Gloves": "Guantes tela",
                # Prenda inferior
                "Shorts": "Pantalones cortos",
                "Jeans": "Vaqueros",
                "Pants": "Pantalones",
                "Sailor Pants": "Pantalones de marinero",
                "Khakis": "Chinos",
                "Belt": "Cintur�n",
                "Cargo Pants": "Pantalones de faena",
                "Capris": "Pantalones media ca�a",
                "Cargo Shorts": "Pantalones cortos de faena",
                # Pies
                "Sandal": "Sandalia",
                "Sandals": "Sandalias",
                "Hiking Boots": "Botas de monta�a",
                "Shoe": "Zapato",
                "Shoes": "Zapatos",
                "Laces": "Cordones",
                "Running Shoes": "Zapatillas de deporte",
                "Hiking Shoes": "Zapatos de monta�a",
                "Boot": "Bota",
                "Boots": "Botas",
                "Bare Feet": "S:Bare Feet"                    # NEW #
}

# and now for the control name localization strings:
xAge = "Edad"
xWeight = "Peso"
xSkinColor = "Piel"
xTexture1 = "Textura 1" # Textura 1, 2, y 3 son los deslizadores del componente �tnico
xTexture2 = "Textura 2"
xTexture3 = "Textura 3"
xNoseAngle = "�ng. nariz"
xNoseWidth = "Anch nariz"
xMouth = "Boca"
xChinAngle = "�ng. barb."
xEyebrows = "Cejas"
xNoseLength = "Tam. nariz"
xCheeks = "Mejillas"
xChinWidth = "Anch barb."
