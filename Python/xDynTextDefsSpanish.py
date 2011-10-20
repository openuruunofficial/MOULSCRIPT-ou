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
from PlasmaTypes import *
#   "Text Name": ( font name, font size, color, margin, line spacing, text, justification )
# font color is in format (red,green,blue,alpha) with the values between 0 and 1
# text margin is in format (top,left,bottom,right) with the values being in pixels
# line spacing is in pixels and can be positive or negative
# justification is optional, but can be any of the following: PtJustify.kCenter, PtJustify.kLeftJustify, PtJustify.kRightJustify
xTextObjects = {\
    "Dummy":        ( "Arial", 12, (1,1,1,1), (0,0,0,0), 0, """Este objeto es un texto tonto, �no me ver�s nunca en el juego!""", PtJustify.kCenter ),
    "nb01WelcomeToDni":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """BIENVENIDO A 
D'NI""", PtJustify.kCenter ),






    "nb01GoToGrsn":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """POR FAVOR, CONECTA
CON LA ERA
GAHREESEN PARA
CONSEGUIR TU KI""", PtJustify.kCenter ),





    "nb01GrsnBook":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """EL LIBRO DE LA ERA
GAHREESEN EST�
EL LA SALA DE
CONECCI�N""", PtJustify.kCenter ),





    "grsnRetrieveKI":        ( "Sharper", 24, (0,0,0,1), (0,0,0,0), 10, """POR FAVOR, 
RECUPERA TU
KI""", PtJustify.kCenter ),





    "nb01EaselWelcome":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """
Bienvenido a
BEVIN
Par m�s informaci�n
Ve al 
Aula""", PtJustify.kCenter ),






    "bcoWrinkledNote":        ( "Michelle", 10, (0,0,0,1), (0,0,0,0), 5, """

Dr. Watson -

Tenemos problemas. La casa de Noloben NO est� vac�a.
Hoy me encontr� con alguien all�. Aunque mi D'ni no es
muy bueno habl� un rato con �l. S�, es un D'ni y, tal
y como nos imaginamos, sabe mucho sobre las criaturas.
MUCH�SIMO.

Obviamente necesitamos convocar una reuni�n
CUANTO ANTES.

- Marie""", PtJustify.kLeftJustify ),




"WatsonLetter":        ( "Courier", 10, (0,0,0,1), (0,0,0,0), 0, """

Matthew,

El �ltimo lote de papeles que enviaste fue muy interesantes. Como has hecho un excelente trabajo, tengo otra lista que me gustar�a que dividieras con el equipo. Depender� de ti el c�mo lo hagas. 

1. Me gustar�a tener m�s informaci�n sobe la vida en familia, ceremonias, etc... y cualquier cosa relacionada con los nacimientos, las bodas, los eventos culturales. S� que disponemos de bastante material de referencia al respecto, as� que cualquier informaci�n adicional que consigas ser� muy �til. Creo que hemos recopilado abundante material sobre ciencia y tecnolog�a, y en cambio bastante poco sobre la vida personal de esta gente. 

2. Disponemos de bastante informaci�n sobre los Gremios y estar�a bien hacer una recopilaci�n ordenada de todo ello. 

3. La Ca�da es claramente un tema en el que flaqueamos. No estoy seguro de poder ayudarte con material de investigaci�n, aunque dada la informaci�n que hemos obtenido recientemente, en alg�n momento lo trataremos m�s a fondo. Recomiendo que este trabajo se le asigne a alguien en exclusiva.

4. Contin�a con los Reyes. Una breve sinopsis de todos los reyes ser�a de gran ayuda, siguiendo el procedimiento que empezaste con el �ltimo lote. 

5. Todav�a quedan muchos escritos religiosos por traducir. Van a ser los m�s dif�ciles aunque creo que nos podr�n aportar mucha informaci�n y muy valiosa. 

6. Tenemos un mont�n de diarios de distintas residencias D'ni, y sitios as�... sin contar con las Eras.  

Creo que con esto tendr�s m�s que suficiente. Nuevamente, da las gracias a tu equipo y diles que est�n haciendo un trabajo excelente. 
- Dr. Watson
""", PtJustify.kLeftJustify ),




"JCNote":        ( "Nick", 16, (0,0,0,1), (0,0,0,0), 5, """

Examina esto. S� que el DRC no quiere que lo toquemos, aunque apuesto que a Watson tambi�n le gustar�a saber c�mo se regulan las puertas. No tiene sentido. 

Y no lo pierdas. Me cost� mucho retirarlo de la pared y cuando lo hice, me dio bastante miedo, quiz�s lo m�s extra�o fue que cuando regres� despu�s, la tela de la que tom� esta pieza estaba intacta. 

- Nick
""", PtJustify.kLeftJustify ),






"clftAtrusNote":        ( "Atrus", 16, (0,0,0,1), (0,0,0,0), -5, """


Querid�sima Yeesha,

Anoche tu madre tuvo un sue�o...

Sabemos que algunos futuros no fueron designados
por el autor o por el Hacedor, aunque el sue�o
cuenta que D' ni volver� a desarrollarse alg�n
d�a. Nuevos exploradores de D' ni llegar�n del
desierto, sintiendo la llamada de algo que a�n
no comprenden. 

El sue�o tambi�n habla de un p�jaro del desierto
con poderes para tejer ese nuevo destino de
D' ni. Tememos que tal poder cambie a la gente.

Yeesha, nuestro p�jaro del desierto, tu b�squeda
parece alejarte m�s y m�s de nosotros. Espero
que lo que encuentres te vuelva a acercar a
nosotros. 

-Atrus

""", PtJustify.kLeftJustify ),






"islmNickNote":        ( "Nick", 16, (0,0,.3,1), (0,0,0,0), 1, """

�D�nde demonios est� mi libro? ��Y por qu� se lo tuvo que llevar alguien?!

- Nick 

""", PtJustify.kLeftJustify ),
}
