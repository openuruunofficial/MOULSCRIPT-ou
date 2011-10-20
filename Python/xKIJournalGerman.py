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
xJournalContents = """<cover src="xKIJournalCover*1#0.hsm"><font size=10 face=courier color=000000><margin left=62 right=62 top=62 bottom=48><p align=center>Die KI

<p align=left>Basisfunktionen - D'ni #3 auf der R�ckseite aller Ger�te ... 3 Funktionen? Es gibt mit Sicherheit mehr. Hauptfunktionen? Wie dem auch sei, es ist ein praktischer.

1. Nexus-Oberfl�che - das Nexus scheint nur ein �bersetzer der KI-Daten zu sein. KI erm�glichen es den Benutzern, Zugriff anderer KIs auf ein Buch zu gew�hren oder abzulehnen. Ich denke, wir k�nnen das auch auf Stadtteile ausweiten k�nnen.he Namen von Welten, die in der KI festgelegt werden, erscheinen im Nexus.Oder sollten zumindest...

2. Pers�nliche Kommunikation - Wohl die wichtigste Funktion: Sprach- oder Textnachrichten an andere KI-Benutzer. Inter- oder Intrawelt - ist wohl egal.

3. Bilderfassung, -Speicherung und Transfer - Durch einen einzigen Druck einer Taste wird ein Bild erfasst und im entsprechenden Welt-Verzeichnis gespeichert. Bilder k�nnen sowohl an andere Kis versendet werden, als auch auf Bildger�te geladen werden (je nach Version). Es sieht so aus, als w�rden Hauptserver diese Funktionalit�t koordinieren - k�nnte schwer werden, das wieder in Gang zu setzen.

4. Journaleintr�ge, -Speicherung und -Transfer - recht einfach. Notizen aufschreiben und speichern. Auch hier k�mmert sich der Server um den Transfer. KI-zu-KI oder KI-zu-Bildger�t.

5. Markierungen - die M�glichkeit, in einer der Welten Markierungen des derzeitigen Standorts vorzunehmen oder Informationen dar�ber zu sammeln. Es gibt dabei verschiedene Funktionalit�tsebenen - bedarf weiterer Forschung. Vielleicht w�re diese Funktion eine Hilfe beim GNP-Problem ... interessant.

6. T�ren - In dieser Welt, �ffnete die KI (selbst in ihrer Grundausstattung) T�ren der Stufe 1. T�ren der Stufen 2 und 3 ben�tigen h�here Versionen.


Es gibt viel mehr Varianten dieser Ger�te, als wir zuerst angenommen hatten. Der "Verteiler" ist in der Lage, mindestens f�nf verschiedene Versionen auszugeben, wenn nicht noch mehr. Die Funktionen ariieren zum Teil erheblich. Es muss irgendwo ein System geben, um diese Ger�te zu kontrollieren und aufzusp�ren - aber wo?

Das in diese Einheit integrierte Bildger�t ist �berraschend kompakt und effizient. Verwendet dasselbe "Gitter"-Kompressionssystem, wenn wir es denn momentan so nennen m�chten. Ich muss es knacken ... Sehr gute Projektion f�r etwas, das nicht gr��er ist, als ein Handteller.


Markierungen

Zweck: Vielleicht ein Ausbildungsger�t f�r Erhalter. Markierungen konnten gesetzt werden und Rekruten und/oder niedere R�nge durchlaufen den "Parcours".

Oberfl�che: Kis interagieren mit Markierungen auf drei verschiedene Arten und Weisen.

"Team-Erobern" - nachdem alle Markierungen platziert wurden, werden zwei Mannschaften aufgestellt, die diese Markierungen einsammeln. Die KI ordnet die Markierung dann der entsprechenden Mannschaft zu. Markierungen k�nnen sich entweder nach einer festgesetzten Zeit oder nachdem alle Markierungen registriert wurden, aufl�sen. Markierungen m�ssen sich in derselben Welt befinden.Test: K�nnen Markierungen zur�ckgesetzt werden?

"Halten" - auch hier zwei Mannschaften. Markierungen l�sen sich nur nach einer vorher festgesetzen Zeit auf. Markierungen l�sen sich nach Aktivierung nicht auf, obwohl der Server nachh�lt, welche Mannschaft die Markierung "h�lt". Wenn die Zeit abgelaufen ist, fasst Server zusammen, welche Mannschaft die meisten Markierungen h�lt. Markierungen m�ssen sich in derselben Welt befinden.

"Einzel" - nur eine einzige KI kann Markierungen registrieren. Markierungen enthalten auch Text. Ein KI kann einem anderen KI im gesamten Syste ganze Markierungssets senden. Markierungen k�nnen in jeder Welt gesetzt werden. 

Die Markierungen an sich scheinen identishc mit denen zu sein, die der Gr��e Nullpunkt produziert. Ich bin mir sogar relativ sicher, dass dabei dieselbe Technologie zugrunde liegt, wenn nicht gar der Gro�e Nullpunkt selbst. Es ist m�glich, dass die Kis mit der Null selber kommunizieren und diese Markierungen �berall dort vornehmen, wo sie registriert sind. Probleme dieser Theorie: Erhalter-Markierungen etc. ...


KI-Registrierung

KI zeichnet andere KI auf drei Stufen auf:

Intra-Welt: Jede andere KI innerhalb dieser Welt wird aufgezeichnet und angezeigt.

KI-zu-KI: Jeder einzelne KI kann zur spezifischen Verfolgung aufgezeichnet werden. Dadurch k�nnen - egal wo sich die KI befindet - Journale, Photos etc. gesendet werden und eine Kommunikation ist m�glich. Vielleicht wurde dies f�r tempor�re oder semi-permanente Team-Missionen verwendet. F�r unsere Zwecke - eine "Freundesliste"?

Gruppen: Die KI erkennt auch Gruppen, die in irgendeiner Weise mit dem Nexus verbunden sind. Es scheint m�glich, dass mit dieser Funktion die Stadtteil-Liste unterst�zt werden kann, sofern man es entsprechend konfigurieren kann.
"""
