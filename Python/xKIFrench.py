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
This module contains all the strings that need to localized for the KI
"""

from PlasmaConstants import *


#--- invitation notices (KI)
xInviteVisitTitle = "Invitation � %s"
xInviteVisitBody = "Venez visiter l'�ge %s en vous rendant au MT Nexus et en utilisant votre Lien priv�e\n\nSign�(e),\n%s (Propri�taire)\n"
xRevokeVisitorTitle = "Visite � %s supprim�e"
xRevokeVisitorBody = "Votre droit de visite � l'�ge %s n'est plus valide.\n\n<Pardon>\n\nSign�,\n%s (Propri�taire)"
#--- KI configuration strings
xKIConfiguration = "Param�tres du KI"
xVolumeConfiguration = "Volume"
xOwnerConfiguration = "Param�tres de %s"
xOwnerVistors = "%s visiteurs"
xOwnerCoOwners = "%s propri�taires"
xDevicesFolderName = "Appareils"
#--- KI add/create entry
#xCreateBuddyTitle = "<ajouter l'ID d'un ami>"
#--- KI leave messages
xLeaveGameMessageNormal = "�tes-vous s�r(e) de vouloir quitter Uru�?"
xLeaveGameMessageNano = xLeaveGameMessageNormal
xLeaveGameMessageMicro = xLeaveGameMessageNormal
#xLeaveGameMessageNormal = "Ne partez pas�! �tes-vous s�r(e) de vouloir quitter�?"
#xLeaveGameMessageNano = "Vous n'avez pas fait grand-chose. �tes-vous s�r(e) de vouloir quitter�?"
#xLeaveGameMessageMicro = "Il vous reste tant � d�couvrir�! �tes-vous s�r(e) de vouloir quitter�?"
#--- send to something error messages
xSendToErrorMessage1 = "Envoi impossible"
xSendToErrorMessage2 = "Joueur introuvable"
xSendToErrorMessage3 = "Type de joueur inconnu"
xSendToErrorMessage4 = "�l�ment de journal incorrect"
xSendToErrorMessage5 = "Doit �tre en texte uniquement"
xCommandErrorMessage1 = "Impossible de '%s'"
xKITimeBroke = "<liaison temporelle rompue>"
#--- delete messages
xDeletePictureAsk = '�tes-vous s�r(e) de vouloir supprimer "%s"�?'
xDeleteJournalAsk = '�tes-vous s�r(e) de vouloir supprimer "%s"�?'
xDeletePlayerAsk = '�tes-vous s�r(e) de vouloir retirer "%s" de votre dossier "%s"�?'
#--- KI is full error messages
xKIFullImagesError = "Votre KI ne peut plus stocker les images dans votre journal. Il est plein."
xKIFullNotesError = "Votre KI ne peut plus stocker de texte dans votre journal. Il est plein."
xKIFullMarkersError = "Votre KI ne peut plus stocker les marqueurs dans votre journal. Il est plein."
#--- CCR conversation
xCCRConversationStarted = '(d�but de conversation)'
xCCRConversationEnded = '(fin de conversation)'
xCCRNoCCRInContact = '(Aucun CCR en contact, message non envoy�)'
xCCRPetitionSent = '(%s envoy�) %s'
#--- KI - Chat strings
xChatNoOneToReply = "(Il n'y a personne � qui r�pondre.)"
xChatLeftTheAge = "(%s a quitt� l'�ge)"
xChatLeftTheGame = '(%s a quitt� le jeu)'
xChatWentOffline = '(%s est hors ligne. Conversation impossible.)'
xChatCannotFindBuddy = "(Impossible de trouver '%s' dans les listes de joueurs.)"
xChatBroadcastMsgRecvd = ""
xChatPrivateMsgRecvd = "De "
xChatInterAgeMsgRecvd = "De "
xChatInterAgePlayerRecvd = "%s dans %s"
xChatBroadcastSendTo = ""
xChatPrivateSendTo = "� "
xChatInterAgeSendTo = "� "
xChatTOPrompt = "��:"
xChatAllAgeCommand = "/crier"
xChatClearAll = "/effacerconversation"
xChatPrivateCommand = "/p"
xChatNeighborsCommand = "/voisins"
xChatBuddiesCommand = "/amis"
xChatNoOneListening = "(Vous �tes trop loin. Vous devriez peut-�tre crier�?)"
xChatInterAgeNotAvailable = "(Commutateur Inter-�ge non disponible)"
xChatReplyCommand = "/r�pondre"
xChatStartLogCommand = "/d�marrerlog"
xChatStopLogCommand = "/arr�terlog"
xChatLogStarted = "D�but de Chat.log..."
xChatLogStopped = "...Fin de Chat.log."
xChatPetitionCommands = {   "/p�tition" : PtCCRPetitionType.kGeneralHelp,
                            "/aide" : PtCCRPetitionType.kGeneralHelp,
                            "/bug" : PtCCRPetitionType.kBug,
                            "/opinion" : PtCCRPetitionType.kFeedback,
                            "/exploit" : PtCCRPetitionType.kExploit,
                            "/harc�lement" : PtCCRPetitionType.kHarass,
                            "/coinc�" : PtCCRPetitionType.kStuck,
                            "/supporttechnique" : PtCCRPetitionType.kTechnical
                        }
xChatCCRPetitionTitle = "P�tition en ligne"
xChatCCRCommand = "/pac"
xChatCCRMsgRecvd = 'De PAC�:'
xChatCCRSendTo = '� PAC�:'
xChatErrorMsgRecvd = 'Erreur�:'
xChatCCRFromPlayer = 'De %d � PAC�:'
xChatWeeBeeAFK = " (Je suis � la surface. Je serai de retour dans une minute)"
xCCRHelpPopupMenu = [   ("Rapport de bug",PtCCRPetitionType.kBug),
                        ("Remarques et suggestions",PtCCRPetitionType.kFeedback),
                        ("Exploits et probl�mes de cheats",PtCCRPetitionType.kExploit),
                        ("Harc�lement et code de conduite",PtCCRPetitionType.kHarass),
                        ("Coinc�",PtCCRPetitionType.kStuck),
                        ("Probl�mes techniques",PtCCRPetitionType.kTechnical),
                        ("Aide g�n�rale",PtCCRPetitionType.kGeneralHelp)
                    ]
xCCRHelpPopupDefault = 6
#--- Offer link to
xOfferLinkToMessage = 'On vous propose une liaison vers "%s" <cool�!>. Souhaitez-vous y aller�?'
#--- KI - neighborhood strings
xAgeOwnedStatusLine = "%d propri�taire%s et %d visiteur%s."
xPorPAgeOwnedStatusLine = "%d propri�taire%s et %d visiteur%s. Il s'agit d'un �ge %s."
xNeighborhoodBottomLine = "%s sur %s"
xNeighborhoodNone = "Aucune inscription dans aucun quartier"
xNeighborhoodNoName = "<aucun nom>"
xNeighborhoodMakePorP = "Rendre %s"
# --- Player expanded strings
#xPlayerEnterID = "Entrez votre num�ro ID�:"
#xPlayerNumberOnly = "Veuillez entrer un num�ro."
#xPlayerNotYourself = "Vous ne pouvez pas vous ajouter en tant qu�ami."
xPlayerInCleft = "est en ligne, perdu(e) dans la crevasse."
xPlayerInCloset = "est en ligne et change de v�tements."
xPlayerInAge = "est en ligne et explore l'�ge %s."
xPlayerOffline = "est hors ligne."
#---- KI Journal strings
xJournalInitialMessage = "<�crire un message>"
xJournalInitialTitle = "<�crire un titre>"
# --- KI IMage strings
xImageInitialTitle = "<�crire une l�gende>"

xFolderVisLists = "Listes de visiteurs�:"
xFolderOwnLists = "Listes de propri�taires de l'�ge�:"

# --- Marker Game strings
xMarkerFolderPopupMenu = [   ("1 min",60),
                        ("2 min",120),
                        ("5 min",300),
                        ("10 min",600),
                    ]
xChatMarkerTOAllTeams = "��: Toutes les �quipes >"
xChatMarkerTOGreenTeam = "��: �quipe verte >"
xChatMarkerTORedTeam = "��: �quipe rouge >"
xChatMarkerAllTeams = "Toutes les �quipes"
xChatMarkerGreenTeam = "�quipe verte"
xChatMarkerRedTeam = "�quipe rouge"
xMarkerGamePrematureEnding = "Le Ma�tre de jeu a interrompu la partie�!"
xMarkerGameCaptureGame = "Partie Capture"
xMarkerGameHoldGame = "Partie D�fense"
xMarkerGameQuestGame = "Partie Qu�te"
xMarkerGameBegins = "Que la partie commence�!"
xMarkerGameGreenTeamWins = "L'�quipe verte a gagn�! %d � %d"
xMarkerGameTieGame = "�galit�.  %d � %d"
xMarkerGameRedTeamWins = "L'�quipe rouge a gagn�! %d � %d"
xMarkerGameEnded = "Fin de la partie... %s"
xMarkerGameResults = "R�sultats de la partie�:"
xMarkerGameNoMarkers = "aucun marqueur"
xMarkerGameOneMarker = "un marqueur"
xMarkerGameNMarkers = "%d marqueurs"
xMarkerGameCaptured = "captur�(s)"
xMarkerGameFoundMarker = "Marqueur '%s' trouv�."
xMarkerGameLastMarker = "C'�tait le dernier marqueur."
xMarkerGameOneMoreLeft = "Il ne reste plus qu'un marqueur�!"
xMarkerGameCaptures = "%s a captur� '%s'. %s"

xMarkerGameEditButton = "Modifier la partie"
xMarkerGamePlayButton = "Jouer"
xMarkerGameDoneEditButton = "Modification termin�e"
xMarkerGameAddMarkerButton = "Ajouter un marqueur"
xMarkerGameMarkerListButton = "Liste des marqueurs"
xMarkerGameRemoveMarkerButton = "Supprimer un marqueur"
xMarkerGameGoBackButton = "Pr�c�dent"
xMarkerGameInviteButton = "Inviter un joueur"
xMarkerGameStartGameButton = "Commencer la partie"
xMarkerGameEndGameButton = "Terminer la partie"
xMarkerGameStopPlayingButton = "Arr�ter de jouer"
xMarkerGameResetGameButton = "R�initialiser la partie"
xMarkerGameStatusNoMarkers = "Il n'y a aucun marqueur"
xMarkerGameStatusOneMarker = "Il y a un marqueur"
xMarkerGameStatusNMarkers = "Il y a %d marqueurs"
xMarkerGameStatusIn = " dans %s"
xMarkerGameStatusAllFound = "Tous les marqueurs de la qu�te ont �t� trouv�s."
xMarkerGameStatusNotAllFound = "Tous les marqueurs de la qu�te n'ont pas �t� trouv�s."
#--- question on invite to marker game
xWaitingForStartText = "En attente du d�marrage"
xTimeRemainingText = "Temps restant�: %01d:%02d"
xMarkerGameMarkersRemaining = "Marqueurs restants�: %d"
xMarkerGameMarkersUnclaimed = "Marqueurs non demand�s�: %d"
xMarkerGameGreenTeamScore = "�quipeverte(%d)"
xMarkerGameRedTeamScore = "�quiperouge(%d)"
xMarkerGameNameCapture = "capture"
xMarkerGameInstructCapNoMarker = "Cependant, puisqu'il n'y a aucun marqueur dans cette partie... tout le monde gagne et tout le monde perd�!"
xMarkerGameInstructCapOneMarker = "L'�quipe qui capture l'unique marqueur en moins de %d minute%s... gagne�!"
xMarkerGameInstructCapNMarkers = "L'�quipe qui capture le plus grand nombre de marqueurs parmi les %d marqueurs en moins de %d minute%s... gagne�!"
xMarkerGameNameHold = "d�fense"
xMarkerGameInstructHoldNoMarker = "Cependant, puisqu'il n'y a aucun marqueur dans cette partie... tout le monde gagne et tout le monde perd�!"
xMarkerGameInstructHoldNMarkers = "L'�quipe qui capture et d�fend le plus grand nombre de marqueurs parmi les %d marqueurs en moins de %d minute%s... gagne�!"
xMarkerGameNameQuest = "qu�te"
xMarkerGameInstructQuest = "Impossible d'inviter des joueurs... c'est un partie en solo."
xMarkerGameNameUnknown = "style inconnu"
xMarkerGameQTitle = "Rejoindre le Jeu de marqueurs de %s"
xMarkerGameQMessage = "    %s souhaiterait vous inviter pour une partie de %s.\n    %s\n\nsouhaitez-vous jouer�?"
xMarkerGameInviteRecvd = "Invitation � un Jeu de marqueurs re�ue. V�rifiez vos messages."

# --- Yes/No Dialog
xYesNoYESbutton = "Oui"
xYesNoOKbutton = "Ok"
xYesNoAcceptButton = "Accepter"
xYesNoDeclineButton = "Refuser"
xYesNoQuitbutton = "Quitter"
xYesNoNoButton = "Non"

# ---- Option Menu strings
xOptMenuKeyMap = "Assigner les commandes"
xOptMenuGameSettings = "Param�tres du jeu"
xOptMenuURULive = "URU Live"
xOptMenuHelp = "Aide"
xOptMenuCredits = "Cr�dits URU"
xOptMenuQuit = "Quitter URU"
xOptMenuOk = "Reprendre la partie"
xOptMenuCancel = "Annuler"

xMoveForward = "Avancer"
xMoveBackward = "Reculer"
xRotateLeft = "Pivoter � gauche"
xRotateRight = "Pivoter � droite"
xJump = "Sauter"
xExitMode = "Quitter un mode"
xPushToTalk = "Appuyer pour parler"


# --- OK Dialog
# The following is all NEW, don't translate the \n followed by a number (not that it would translate)
xOKDialogDict = { # "code": "translation"
        "": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#01",
        "TERMINATED: Server LogOff. Reason: Logged In Elsewhere": "Vous avez �t� d�connect�(e) car quelqu�un d�autre utilise d�j� votre compte.\n#02",
        "TERMINATED: Server LogOff. Reason: Timed Out": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#03",
        "TERMINATED: Server LogOff. Reason: Not Authenticated": "Un probl�me est survenu pendant la connexion. Veuillez v�rifier votre compte et votre mot de passe et r�essayer.\n#04",
        "TERMINATED: Server LogOff. Reason: Kicked Off": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#05",
        "TERMINATED: Server LogOff. Reason: Unknown Reason": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#06",
        "TERMINATED: Server LogOff. Reason: CCRs must use a protected lobby": "Vous avez �t� refus�(e) car les PAC doivent se connecter par le biais d�une salle prot�g�e.\n#07",
        "TERMINATED: Server LogOff. Reason: CCRs must have internal client code": "Vous avez �t� refus�(e) car les PAC doivent disposer d�un code client interne.\n#08",
        "TERMINATED: Server LogOff. Reason: UNKNOWN REASON CODE": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#09",
        "SERVER SILENCE": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#10",
        "BAD VERSION": "Cette version d�Uru est trop ancienne. Veuillez quitter le programme et mettre le jeu � jour.\n#11",
	    "Player Disabled": "Le joueur que vous avez s�lectionn� n�est pas autoris� � Uru. Veuillez contacter le support client�le pour plus d�informations.\n#12",
	    "CAN'T FIND AGE": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#13",
	    "AUTH RESPONSE FAILED": "Un probl�me est survenu pendant la connexion. Veuillez v�rifier votre compte et votre mot de passe et r�essayer.\n#14",
        "AUTH TIMEOUT": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#15",
        "SDL Desc Problem": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#16",
        "Unspecified error": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#17",
		"Failed to send msg": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#18",
		"Authentication timed out": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#19",
		"Peer timed out": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#20",
		"Server silence": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#21",
		"Protocol version mismatch": "Cette version d�Uru est trop ancienne. Veuillez quitter le programme et mettre le jeu � jour.\n#22",
		"Auth failed": "Un probl�me est survenu pendant la connexion. Veuillez v�rifier votre compte et votre mot de passe et r�essayer.\n#23",
		"Failed to create player": "Un probl�me est survenu pendant la cr�ation de votre joueur. Veuillez quitter le programme et r�essayer.\n#24",
		"Invalid error code": "Il semble y avoir un probl�me avec la connexion. Veuillez quitter le programme et r�essayer.\n#25",
		"linking banned": "Votre capacit� de liaison a �t� d�sactiv�e\n#26",
		"linking restored": "Votre capacit� de liaison a �t� r�tablie\n#27",
		"silenced": "Votre aptitude � la discussion a �t� d�sactiv�e\n#28",
		"unsilenced": "Votre aptitude � la discussion a �t� r�tablie\n#29"
}


# --- xInvite strings
xInviteKeyAdded = "Touche d'invitation ajout�e�: %s"
xMaxInvites = "Nombre max d'invitations atteint"
xMissingInviteFolder = "Dossier d'invitation manquant"
xInviteUsage = "Utilisation�: /inviter <Mot de passe>"
xInviteAccepted = "Invitation en cours d'acceptation avec l'Ami�: %s et la Touche�: %s"
xAcceptUsage = "Utilisation�: /accepter <Nom de l'ami> <Mot de passe>"
xCouldNotCast = "Impossible de diffuser l'�l�ment de liste vers la note"
xKeys = "Touches�: "
xRemoveNodeFailed = "�chec de la suppression du Noeud"
xInviteNotFound = "Invitation introuvable"
xUninviteUsage = "Utilisation�: /supinvit <Mot de passe>"
xDeletedInvitation = "Invitation supprim�e�: "

# --- xKIExtChatCommands strings
xSitCmd = "assis"
xAfkCmd = "absent"
xInviteCmd = "inviter"
xUninviteCmd = "supinvit"
xAcceptCmd = "accepter"
xShowInvitesCmd = "montrerinvit"
xWaveCmd = "signemain"
xWaveString = "%s fait un signe de la main"
xSneezeCmd = "�ternuer"
xSneezeString = "%s �ternue"
xClapCmd = "applaudir"
xClapString = "%s applaudit"
xLaughCmd = "rire"
xLaughString = "%s rit"
xLOLCmd = "mdr"
xLOLString = "%s est mort de rire"
xROTFLCmd = "mdrept"
xROTFLString = "%s est mort de rire �croul� par terre"
xDanceCmd = "danser"
xDanceString = "%s danse"
xYesCmd = "oui"
xYesString = "%s acquiesce de la t�te"
xNoCmd = "non"
xNoString = "%s refuse de la t�te"
xYawnCmd = "b�iller"
xYawnString = "%s b�ille"
xCheerCmd = "salut"
xCheerString = "%s salue"
xThanksCmd = "merci"
xThanksString = "%s vous remercie bien�!"
xThxCmd = "mrc"
xThxString = "%s vous remercie"
xCryCmd = "pleurer"
xCryString = "<snif> %s est triste"
xCriesCmd = "pleurnicher"
xCriesString = "%s pleurniche"
xDontKnowCmd = "jenesaispas"
xDontKnowString = "%s hausse les �paules"
xShrugCmd = "�paules"
xShrugString = "%s hausse les �paules"
xDunnoCmd = "chaispas"
xDunnoString = "%s hausse les �paules"
xPointCmd = "pointer"
xPointString = "%s pointe du doigt"

xKISettingsFontSizeText = "Taille de police :"
xKISettingChatFadeTimeText = "Temps de fondu des discussions :"
xKISettingsOnlyBuddiesText = "Uniquement accepter les messages priv�s et les e-mails des Amis"
xKIDescriptionText = "Description :"
xMarkerGameOwnerTitle = "PROPRI�TAIRE :"
xMarkerGameTimeText = "Temps de jeu :"
xCCRAwayText = "PAC momentan�ment absent"
xCCRPetitionTypeText = "Type de p�tition :"
xCCRSubjectText = "Objet :"
xCCRCommentText = "Commentaire :"
xCCRSubmitBtnText = "Valider"
xCCRCancelBtnText = "Annuler"

#latest strings to be translated (build 36)
xKIStatusNexusLinkAdded = "Un lien a �t� ajout� a votre Nexus"

# updated strings in build .37
xPlayerEnterID = "F:Enter player ID or name:"
xPlayerNumberOnly = "F:Please enter a player ID or current Age player name."
xPlayerNotYourself = "F:Can't be yourself."
#--- KI add/create entry
xCreateBuddyTitle = "<F:add buddy by ID or name if in Age>"

# new strings starting in build .37
xChatAddBuddyCmd = "/addbuddy"
xChatRemoveBuddyCmd = "/removebuddy"
xChatIgnoreCmd = "/ignore"
xChatUnIgnoreCmd = "/unignore"
xPlayerAlreadyAdded = "F:Player has already been added."
xPlayerNotFound = "F:Player not found."
xPlayerAdded = "F:Player added."
xPlayerRemoved = "F:Player removed."
