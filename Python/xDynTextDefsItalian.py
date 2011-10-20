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
    "nb01WelcomeToDni":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """BENVENUTO A
D'NI""", PtJustify.kCenter ),






    "nb01GoToGrsn":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """COLLEGATI ALL'ETA' 
GAHREESEN 
PER RITIRARE 
IL TUO KI""", PtJustify.kCenter ),





    "nb01GrsnBook":        ( "Sharper", 22, (0,0,0,1), (0,0,0,0), 5, """IL LIBRO DELL'ETA' 
GAHREESEN SI TROVA 
NELLA STANZA DI
COLLEGAMENTO""", PtJustify.kCenter ),





    "grsnRetrieveKI":        ( "Sharper", 24, (0,0,0,1), (0,0,0,0), 10, """RITIRA IL 
TUO KI, 
PER FAVORE""", PtJustify.kCenter ),





    "nb01EaselWelcome":        ( "Sharper", 28, (0,0,0,1), (0,0,0,0), 5, """
Benvenuto a
BEVIN
Per informazioni
presentati
in aula""", PtJustify.kCenter ),






    "bcoWrinkledNote":        ( "Michelle", 10, (0,0,0,1), (0,0,0,0), 5, """

Dr. Watson -

Grossi problemi. La casa su Noloben NON � vuota.
Oggi ho incontrato qualcuno. Il mio D'Ni non � granch�,
ma ho parlato con lui per un po'. S�, � un D'Ni e,
come pensavamo, sa molte cose sulle creature.
MOLTISSIME cose.

Ovviamente dobbiamo vederci subito.

- Marie""", PtJustify.kLeftJustify ),




"WatsonLetter":        ( "Courier", 10, (0,0,0,1), (0,0,0,0), 0, """

Matthew,

L'ultima serie di documenti che hai mandato era molto interessante. Siccome hai fatto un ottimo lavoro, ho un'altra lista di lavori che vorrei che tu condividessi con la squadra. Come organizzarti � affar tuo.


1. Vorrei pi� informazioni sulla vita familiare: cerimonie, ecc... Qualsiasi cosa riguardi nascite, matrimoni, eventi culturali. So che abbiamo parecchio materiale originale su questo, quindi qualsiasi cosa trovi � la benvenuta. Finora abbiamo raccolto molto sulla scienza e la tecnologia, ma non abbastanza sulla vita privata di questa gente.

2. Abbiamo molte informazioni sulle Gilde, ma raccoglierle tutte in un'area dedicata sarebbe bello.

3. L'Autunno � ovviamente un'area su cui dobbiamo lavorare parecchio. Non sono certo di poterti aiutare con materiale di ricerca, ma viste le informazioni pi� recenti che stiamo raccogliendo, prima o poi dovremo occuparcene a fondo. Ti consiglio di assegnare qualcuno all'Autunno a tempo pieno.

4. Vai avanti con i Re. Un breve riassunto su tutti i Re sarebbe utile, seguendo la traccia che hai avviato con l'ultima serie.

5. Ci sono ancora degli scritti religiosi da tradurre. Sono i pi� difficili, ma credo che ci potranno fornire molte informazioni utili.

6. Abbiamo una montagna di diari provenienti da residenze D'Ni, ecc. Per non parlare delle Et�.

Credo che per ora sia pi� che abbastanza. Di nuovo, grazie a te e alla tua squadra, fai loro i complimenti per l'ottimo lavoro.
 
- Dr. Watson
""", PtJustify.kLeftJustify ),




"JCNote":        ( "Nick", 16, (0,0,0,1), (0,0,0,0), 0, """

Dai un'occhiata a questo. So che il DRC non vuole che li tocchiamo, ma scommetto che anche Watson vorr� sapere come fanno questi cosi a registrarsi con le porte. Non ha senso.

E non perderlo. Sono a malapena riuscito a staccarlo dal muro e, quando l'ho fatto, sono morto di paura. Forse la cosa pi� strana � che quando sono tornato, pi� tardi, il tessuto che avevo strappato era di nuovo intatto.

- Nick
""", PtJustify.kLeftJustify ),






"clftAtrusNote":        ( "Atrus", 16, (0,0,0,1), (0,0,0,0), -5, """


Yeesha,

La scorsa notte tua madre ha avuto un sogno...

Il sogno racconta che D 'ni crescer� nuovamente
un giorno. Nuovi seguaci di D 'ni
ritorneranno dal deserto, chiamati verso
qualcosa che non comprendono.

Ma il sogno racconta anche di un uccello del 
deserto con il potere di tessere questo
nuovo futuro D 'ni... 

Noi temiamo tale potere, poich� cambia le persone.

Yeesha, oh uccello del deserto, la tua
ricerca sembra condurti sempre pi� lontano
da noi. Spero che ci� che troverai ti
avviciner� nuovamente.

-Atrus
""", PtJustify.kLeftJustify ),






"islmNickNote":        ( "Nick", 16, (0,0,.3,1), (0,0,0,0), 1, """

Dove diavolo � il mio libro? Ma soprattutto, perch� qualcuno l'ha preso?

- Nick 

""", PtJustify.kLeftJustify ),
}