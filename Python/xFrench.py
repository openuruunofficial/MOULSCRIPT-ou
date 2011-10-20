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
from Plasma import *
from PlasmaVaultConstants import *

#============================
#--- vault folder node names
xFolderIDToFolderName = {    PtVaultStandardNodes.kUserDefinedNode:"D�fini par l'utilisateur",\
                            PtVaultStandardNodes.kInboxFolder:"Bo�te de r�ception",\
                            PtVaultStandardNodes.kBuddyListFolder:"Amis", \
                            PtVaultStandardNodes.kIgnoreListFolder:"Liste � ignorer",\
                            PtVaultStandardNodes.kPeopleIKnowAboutFolder:"R�cents",\
                            PtVaultStandardNodes.kChronicleFolder:"Chronique",\
                            PtVaultStandardNodes.kAvatarOutfitFolder:"Armoire",\
                            PtVaultStandardNodes.kAgeTypeJournalFolder:"Journaux d'�ges",\
                            PtVaultStandardNodes.kSubAgesFolder:"Sous-�ges",\
                            PtVaultStandardNodes.kHoodMembersFolder:"Voisins",\
                            PtVaultStandardNodes.kAllPlayersFolder:"Tous les joueurs",\
                            PtVaultStandardNodes.kAgeMembersFolder:"Joueurs de l'�ge",\
                            PtVaultStandardNodes.kAgeJournalsFolder:"Dossiers des journaux d'�ges",\
                            PtVaultStandardNodes.kCanVisitFolder:"Visiteurs potentiels",\
                            PtVaultStandardNodes.kAgeOwnersFolder:"Propri�taires",\
                            PtVaultStandardNodes.kPublicAgesFolder:"Quartiers publics",\
                            PtVaultStandardNodes.kAgesIOwnFolder:"�ges poss�d�s",\
                            PtVaultStandardNodes.kAgesICanVisitFolder:"�ges visitables",\
                            PtVaultStandardNodes.kAvatarClosetFolder:"Armoire � avatar",\
                        }

#============================
#--- player status name
xMayorOfNeighborhood = "Maire"
xMemberOfNeighborhood = "Membre"

#--- neighborhood status strings
xNeighborhoodPrivate = "priv�"
xNeighborhoodPublic = "public"

#--- date and time display Formats (as described by time.strftime python standard module)
xDateTimeFormat = "%d/%m/%y  %H:%M"
xDateFormat = "%d/%m/%y"

# --- Imager Text Message Format
xImagerMessage = "De�: %s\nObjet�: %s\n\n%s"

# --- Hood welcome message
xHoodWelcome = "Bienvenue � %s. Pour plus d'informations, rendez-vous dans la salle de classe"

# --- Bookshelf deletion messages
xDeleteNeighborhoodBook = "�tes-vous s�r(e) de vouloir supprimer ce Livre et ainsi perdre votre inscription dans ce quartier ?"
xDeleteBook = "�tes-vous s�r(e) de vouloir supprimer ce Livre et ainsi annuler votre progression dans cet �ge ?"

# --- Age name localization stuff
xNeighborhood = "Quartier"
xTranslatedAgeNames = {
    # City link-in points
    "Ferry Terminal": "Terminal de ferry",
    "Tokotah Alley": "All�e Tokotah",
    "Palace Alcove": "Alc�ve du palais",
    "Library Courtyard": "Cour de la biblioth�que",
    "Concert Hall Foyer": "Hall de la salle de concert",
    # Age names
    "Eder Kemo": "Eder Kemo",
    "Eder Gira": "Eder Gira",
    "Gahreesen": "Gahreesen",
    "Kadish": "Kadish",
    "Nexus": "Nexus",
    "Neighborhood": "Quartier",
    "Relto": "Relto",
    "Teledahn": "Teledahn",
    # Great Zero link-in points
    "Great Zero Observation": "Grand Z�ro observation",
    "Great Zero": "Great Zero",
}
xPossesive = "de"

def LocalizeAgeName(displayName):
    "Returns a localized version of the age display name you give it"
    localizedName = displayName
    if localizedName == "D'ni-Rudenna":
        # if the poles are not in a certain state, we can't call this age its normal name
        try:
            sdl = xPsnlVaultSDL()
            if sdl["TeledahnPoleState"][0] > 5 or sdl["KadishPoleState"][0] > 5 or sdl["GardenPoleState"][0] > 5 or sdl["GarrisonPoleState"][0] > 5:
                localizedName = "D'ni-Rudenna"
            else:
                localizedName = "???"
        except:
            localizedName = "???" # default to unknown if we can't access the SDL for some reason
    elif localizedName == "Ae'gura":
        localizedName = "D'ni-Ae'gura"
    elif localizedName == "GreatZero":
        localizedName = "D'ni-Rezeero"
    elif not localizedName.startswith("D'ni"):
        # D'ni names are not localized, so if they don't start with D'ni, then they will be localized
        # check if this is a neighborhood name
        if localizedName[len(localizedName)-12:] == "Neighborhood":
            # chop off the neighborhood part and tack on the localized version of that word
            localizedName = localizedName[:len(localizedName)-12] + xNeighborhood
            return localizedName
        # we are either a possesive name or a city link, check for city link first
        try:
            localizedName = xTranslatedAgeNames[localizedName]
            return localizedName
        except:
            # ok, we're actually a possesive or something we have no translation for, check possesive
            pass
        apostropheLoc = localizedName.rfind("'")
        if apostropheLoc == -1:
            localizedName = "F:"+localizedName
            return localizedName
        if apostropheLoc + 3 >= len(localizedName):
            localizedName = "F:"+localizedName
            return localizedName
        if not (localizedName[apostropheLoc+1] == 's' and localizedName[apostropheLoc+2] == ' '):
            localizedName = "F:"+localizedName
            return localizedName
        # we are possesive, translate it
        userName = localizedName[:apostropheLoc]
        ageName = localizedName[apostropheLoc+3:]
        localizedName = ageName + " " + xPossesive + " " + userName
    return localizedName
