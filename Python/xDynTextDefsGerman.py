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
    "Dummy":        ( "Arial", 12, (1,1,1,1), (0,0,0,0), 0, """This is a dummy text object, you should never see me in game!""", PtJustify.kCenter ),
    "nb01WelcomeToDni":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """WILLKOMMEN
IN D'NI""", PtJustify.kCenter ),






    "nb01GoToGrsn":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """BITTE HOLEN SIE
SICH IHRE KI IN
DER WELT
GAHREESEN""", PtJustify.kCenter ),





    "nb01GrsnBook":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 0, """DAS BUCH F�R
GAHREESEN
BEFINDET SICH
IM RAUM DER
VERBINDUNGEN""", PtJustify.kCenter ),





    "grsnRetrieveKI":        ( "Sharper", 24, (0,0,0,1), (0,0,0,0), 10, """BITTE
HOLEN SIE SICH
IHRE KI""", PtJustify.kCenter ),





    "nb01EaselWelcome":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """
Willkommen in
BEVIN
Weitere Informationen
erhalten Sie
im Unterrichtsraum""", PtJustify.kCenter ),






    "bcoWrinkledNote":        ( "Michelle", 10, (0,0,0,1), (0,0,0,0), 5, """

Dr. Watson -

Es gibt Probleme. Das Haus in Noloben ist NICHT leer.
Ich habe heute dort jemanden angetroffen. Mein D'ni
ist nicht besonders, aber ich habe mich eine Weile
mit ihm unterhalten. Er sagt er sei ein D'ni und wie
wir bereits angenommen haben, wei� er eine Menge
�ber diese Kreaturen.
WIRKLICH EINE GANZE Menge.

Wir sollten umgehend ein Meeting einberufen.

- Marie""", PtJustify.kLeftJustify ),




"WatsonLetter":        ( "Courier", 10, (0,0,0,1), (0,0,0,0), 0, """

Matthew,

Der letzte Satz Unterlagen, den du geschickt hast, war sehr interessant. Ich habe noch eine weitere Liste, von der ich m�chte, dass du sie an das Team weiter gibst. Wie du sie genau aufteilst, ist deine Sache. 

1. Ich m�chte mehr Informationen �ber das Familienleben: Zeremonien, etc... Einfach alles, was mit Geburt, Heirat, kulturellen Ereignissen zusammenh�ngt. Ich wei�, dass wir einige Quellen haben, daher w�re deine Hilfe sehr wertvoll f�r mich. �ber Wissenschaft und Technologie haben wir ja schon einiges zusammengetragen, aber ich finde, dass wir noch nicht genug �ber das Leben dieses Volkes wissen.

2. Wir haben einiges an Informationen �ber die Gilden gesammelt. Eine ordentliche Aufstellung an einem Ort w�re sehr praktisch.

3. Der Fall ist etwas, �ber das wir nur sehr wenig wissen. Ich wei� nicht, ob du mir da weiterhelfen kannst, aber nach den Nachrichten der letzten Zeit, sollten wir uns das mal n�her ansehen. Ich w�rde empfehlen, jemanden ausschlie�lich auf den Fall anzusetzen.

4. Macht mit den K�nigen weiter. Ein kurzer Abriss zu allen K�nigen entsprechend denen im letzten Satz w�re hilfreich.

5. Wir haben immer noch religi�se Schriften, die �bersetzt werden m�ssen. Das wird nicht einfach werden, aber ich bin sicher, dass wir darin sehr wertvolle Informationen finden werden.

6. Wir haben einen ganzen Stapel Tageb�cher aus den verschiedenen D'ni-Unterk�nften, etc. - von Welten gar nicht zu reden ...  

Ich glaube, das ist mehr als genug. Noch mal vielen Dank - auch an dein Team, das gro�artige Arbeit macht. 
- Dr. Watson
""", PtJustify.kLeftJustify ),




"JCNote":        ( "Nick", 16, (0,0,0,1), (0,0,0,0), 0, """

Sieh dir das mal an. Ich wei�, dass der DRC nicht, will, dass wir die Dinger anfassen, aber ich wette, Watson will auch wissen, wie die mit den T�ren in Verbindung stehen. Es macht einfach keinen Sinn. 

Und verlier es nicht. Ich habe es kaum von der Wand bekommen und als ich es endlich geschafft hatte, war es ganz sch�n unheimlich. Aber etwas ist noch seltsamer: Als ich sp�ter zur�ckkam, war das Tuch, von dem ich dieses St�ck habe, wieder intakt.

- Nick
""", PtJustify.kLeftJustify ),






"clftAtrusNote":        ( "Atrus", 16, (0,0,0,1), (0,0,0,0), -5, """


Yeesha,

in der letzten Nacht hatte deine Mutter einen Traum.

Der Traum k�ndete davon, dass D'ni eines Tages
wieder auferstehen wird. Sucher der D'ni werden von
der W�ste her kommen werden - gerufen von etwas, was
sie nicht verstehen.

Der Traum handelte auch von einem W�stenvogel mit
der Macht, diese neue Zukunfts D'nis zu weben.

Wir f�rchten eine solche Macht - sie ver�ndert die 
Menschen.

Yeesha, du bist unser W�stenvogel. Auf deiner Suche
scheinst du dich mehr und mehr von uns zu entfernen.
Ich hoffe, dass das, was du finden wirst, dich uns 
wieder n�her bringt.

-Atrus
""", PtJustify.kLeftJustify ),






"islmNickNote":        ( "Nick", 16, (0,0,.3,1), (0,0,0,0), 1, """

Wo zur H�lle ist mein Buch? Wer hat �berhaupt etwas da dran zu suchen?!

- Nick 

""", PtJustify.kLeftJustify ),
}
