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
# xKIJournalEnglish
# change the contents of the variable below to the desired contents of the journal
xJournalContents = """<cover src="xKIJournalCover*1#0.hsm"><font size=10 face=courier color=000000><margin left=62 right=62 top=62 bottom=48><p align=center>Le KI

<p align=left>Fonctions de base - Le chiffre 3 (�crit en D'ni) appara�t sur le c�t� de tous les appareils... pour symboliser 3 fonctions�?  Il y en a bien plus que �a.  3 fonctions principales�?  En tout cas, le nom est pratique�: KI.

1. L'interface Nexus - le Nexus semble n'�tre qu'un d�codeur pour les donn�es du KI. Les KI permettent aux utilisateurs de proposer ou de refuser l'acc�s d'un Livre � d'autres KI. Je crois qu'on peut les faire fonctionner de la m�me fa�on pour des quartiers.  Le nom des �ges d�finis dans le KI appara�t dans le Nexus. Enfin, �a devrait marcher... 

2. Communication interpersonnelle - bien entendu, il s'agit de la fonction la plus importante�: des communications vocales ou textuelles envoy�es vers les autres utilisateurs de KI. Inter- ou Intra-�ge - �a n'a pas l'air d'avoir d'importance. 

3. Capture d'image, stockage et transfert - Une pression unique sur l'un des boutons permet de r�aliser un clich� et de le stocker dans un r�pertoire appropri� de l'�ge. Les images peuvent �tre envoy�es vers d'autres KI ou charg�es dans certains imageurs (selon les versions). Il semblerait que les serveurs principaux s'occupaient de la coordination de ces fonctions - on risque d'avoir du mal � les faire fonctionner � nouveau. 

4. �l�ments de journal, stockage et transfert - tr�s simple. Permet d'�crire des notes et de les stocker. Un fois de plus, ce sont les serveurs qui permettent les transferts... D'un KI vers un KI ou d'un KI vers un imageur. 

5. Marqueurs - l'appareil permet de r�cup�rer des marqueurs dans un �ge,  � l'emplacement o� se situe l'utilisateur. Les fonctionnalit�s semblent nombreuses, ici - Il faut que j'effectue d'autres recherches.  On peut peut-�tre coupler cette fonctionnalit� et en savoir plus sur le probl�me du GZ... int�ressant.

6. Portes - dans cet �ge, le KI (m�me dans sa version la plus basique) permet d'ouvrir les portes de Niveau 1. Les portes de Niveau 2 et 3 exigent une version sup�rieure. 



Ces appareils sont bien plus polyvalents que je ne l'aurais imagin�. Le ��distributeur�� est capable de fournir au moins cinq versions diff�rentes. Peut-�tre m�me plus. Les fonctionnalit�s varient �norm�ment d'une version � une autre.  Il devait y avoir un syst�me pour contr�ler et surveiller ces appareils... mais o��?

L'imageur int�gr� � la machine est �tonnamment compact et efficace.  Il utilise ce petit syst�me de compression ��matriciel�� (mais le mot ne convient pas)... il faut que je comprenne ce truc.  La projection est vraiment puissante pour un truc qui tient sur le plat de la main. 



Marqueurs 

Finalit�: il s'agissait peut-�tre d'un outil d'entra�nement r�serv� aux Conservateurs. Les marqueurs pouvaient �tre d�finis et les nouvelles recrues ou les rangs inf�rieurs parcouraient la ��piste��.

Interface�: les KI interagissent avec les marqueurs de 3 fa�ons.

��Capture par �quipe�� - une fois tous les marqueurs plac�s, deux �quipes peuvent les ramasser. Le KI enregistre le marqueur � l'�quipe appropri�e. Les marqueurs peuvent dispara�tre apr�s un temps limite ou une fois qu'ils ont tous �t� enregistr�s. Les marqueurs doivent tous se trouver dans le m�me �ge.  Test�: est-il possible de r�initialiser les marqueurs�?

��D�fense�� - une fois de plus, n�cessite deux �quipes. Les marqueurs ne disparaissent qu'apr�s un temps limite pr�d�termin�. Un marqueur ne dispara�t pas apr�s avoir �t� activ�, mais le serveur garde en m�moire l'�quipe qui le ��d�fend��. � la fin du temps d�fini, le serveur comptabilise les marqueurs d�tenus par chaque �quipe. Les marqueurs doivent tous se trouver dans le m�me �ge.

��Capture solo�� - seul un KI peut enregistrer les marqueurs. Les marqueurs contiennent �galement du texte. La s�rie de marqueurs peut �tre envoy�e d'un KI � un autre n'importe o� dans le syst�me. Les marqueurs peuvent �tre plac�s dans n'importe quel �ge. 

Les marqueurs semblent identiques � ceux produits par le Grand Z�ro. En fait, je suis persuad� qu'il s'agit de la m�me technologie. On peut m�me penser que les KI communiquent avec le Z�ro et inscrivent ces marqueurs � l'endroit o� ils sont enregistr�s. Mais cette th�orie pose certains probl�mes... la conservation des marqueurs, etc...



Enregistrement des KI

Un KI peut surveiller un autre KI sur 3 niveaux�:

Intra-�ge�: tout autre KI se trouvant dans le m�me �ge est identifi� et affich�. 

De KI � KI�: tout KI individuel peut-�tre enregistr� et retrouv�. Du coup, quel que soit l'emplacement du KI, les journaux, photos, etc. peuvent �tre transf�r�s. Cette fonction �tait peut-�tre utilis�e lors de certaines missions par �quipe provisoires ou semi-permanentes.  Dans notre cas, �a permettra de fournir une ��liste d'amis��.

Groupes�: Le KI reconna�t �galement les groupes connect�s d'une fa�on ou d'une autre au Nexus. Il semble possible, avec une bonne configuration, de prendre en charge des listes de quartiers gr�ce � cette fonction.
"""
