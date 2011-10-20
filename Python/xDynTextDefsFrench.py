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
    "Bidon":        ( "Arial", 12, (1,1,1,1), (0,0,0,0), 0, """Ceci est un objet texte bidon, ne devrait pas appara�tre dans le jeu�!""", PtJustify.kCenter ),
    "nb01WelcomeToDni":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """BIENVENUE �
D'NI""", PtJustify.kCenter ),






    "nb01GoToGrsn":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """RENDEZ-VOUS DANS
L'�GE GAHREESEN
POUR R�CUP�RER
VOTRE KI""", PtJustify.kCenter ),





    "nb01GrsnBook":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """LE LIVRE DE LIAISON DE
L'�GE GAHREESEN
SE TROUVE DANS LA
SALLE DE LIAISON""", PtJustify.kCenter ),





    "grsnRetrieveKI":        ( "Sharper", 24, (0,0,0,1), (0,0,0,0), 10, """VEUILLEZ
R�CUP�RER VOTRE
KI""", PtJustify.kCenter ),





    "nb01EaselWelcome":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """
Bienvenue �
BEVIN
Pour plus d'infos,
rendez-vous dans la
salle de classe""", PtJustify.kCenter ),






    "bcoWrinkledNote":        ( "Michelle", 10, (0,0,0,1), (0,0,0,0), 5, """

Dr. Watson -

Gros soucis. La maison de Noloben n'est PAS vide.
J'y ai rencontr� quelqu'un aujourd'hui. Je ne parle pas
tr�s bien le D'ni, mais j'ai r�ussi � communiquer avec
lui un petit moment. Oui, c'est un D'ni et comme nous
nous en doutions, il sait beaucoup de choses sur les
cr�atures. BEAUCOUP de choses.

Nous devons organiser une r�union d�s que possible.

- Marie""", PtJustify.kLeftJustify ),




"WatsonLetter":        ( "Courier", 10, (0,0,0,1), (0,0,0,0), 0, """

Matthew,

Les derniers documents que vous m'avez envoy�s �taient tr�s int�ressants. Puisque vous avez fait un excellent travail, j'ai une petite liste de t�ches � r�partir pour l'�quipe. Organisez �a comme bon vous semble. 

1. J'aimerais plus d'infos sur les coutumes de la vie en famille�: les c�r�monies, etc... Tout ce qui se rapporte � la naissance, au mariage et aux �v�nements culturels. Je sais que nous disposons de nombreux documents � �tudier, donc r�cup�rez tout ce que vous pouvez. Je pense que nous avons trop ax� nos recherches sur les sciences et la technologie et pas assez sur la vie quotidienne de ce peuple.

2. Nous avons beaucoup d'infos sur les Guildes, mais il serait bon d'organiser un peu tout �a.

3. Nous avons de nombreuses lacunes sur la Chute. Je ne suis pas s�r de pouvoir vous aider � ce propos, mais �tant donn�es nos derni�res infos, je crois qu'il va falloir creuser ce sujet. Je vous recommande de mettre une personne � plein temps sur la Chute.

4. Continuez aussi � travailler sur les Rois. Un r�sum� de tous les rois serait vraiment le bienvenu.

5. Nous avons encore des documents religieux � faire traduire. �a risque d'�tre difficile, mais je crois que �a peut nous apporter de pr�cieuses informations.

6. Nous avons encore un stock de journaux r�cup�r�s dans diverses r�sidences D'ni, etc... sans m�me parler des �ges.  

Je crois que �a suffira pour l'instant. Merci encore � votre �quipe. Dites-leur qu'ils font un excellent boulot. 
 
- Dr. Watson
""", PtJustify.kLeftJustify ),




"JCNote":        ( "Nick", 16, (0,0,0,1), (0,0,0,0), 5, """

�coutez �a. Je sais que le CRD ne veut pas qu'on y touche, mais je suis s�r que Watson serait ravi de voir le rapport avec les portes. C'est totalement illogique. 

Mais il ne faut pas le perdre. J'ai eu beaucoup de mal � l'enlever du mur, ce qui n'est pas rassurant. Mais le plus �trange, c'est que quand je suis revenu plus tard, l'�toffe �tait r�apparue, intacte.

- Nick
""", PtJustify.kLeftJustify ),






"clftAtrusNote":        ( "Atrus", 18, (0,0,0,1), (0,0,0,0), -5, """

Yeesha ch�rie,

La nuit derni�re, ta m�re a fait un r�ve...

Le r�ve annonce que D 'ni rena�tra un jour. Les
nouveaux explorateurs de D 'ni afflueront dans
le d�sert, comme irr�sistiblement attir�s par
quelque chose qu'ils ne comprennent pas.

Le r�ve parle aussi d'un oiseau du d�sert, au
pouvoir capable d'inventer l'avenir de D 'ni.
Nous craignons ce genre de pouvoir - il peut
changer les gens.

Yeesha, notre oiseau du d�sert, ta qu�te semble
t'�loigner toujours plus. J'esp�re que ce que tu
trouveras te rapprochera de nous.

-Atrus

""", PtJustify.kLeftJustify ),






"islmNickNote":        ( "Nick", 16, (0,0,.3,1), (0,0,0,0), 1, """

O� est pass� mon Livre�? Pourquoi quelqu'un l'a-t-il pris�!

- Nick 

""", PtJustify.kLeftJustify ),
}