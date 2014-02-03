#####################################################################
#
# File:        __init__.py
# Author:   Loek Wensveen
# Date:      03/01/2014
# Version: 1.0.0
# About:        This plugin alows jou to watch itvonline in plex form kpn
#
#####################################################################

# no global imports (import are infront of function)

#####################################################################

VIDEO_PREFIX = "/video/itvonline"
NAME = "iTVOnline"

ART = u'art-default.jpg'

ICONS = {
    u'KPN' : u'KPN icon-default.png',
    u'Telfort' : u'Telford icon-default.png'
}

ICON_TV = u'icon-default.jpg'
ICON_GIDS = u'Recent.png'
ICON_MISS = u'History.png'
ICON_VIDEOTHEEK = u'TV.png'
ICON_OPNAMES = u'Record.png'

SUB_DOMEIN = lambda : DOMEIN_DICT[Prefs['provider']]
BASE_URL = lambda : u"http://%s.itvonline.nl" % SUB_DOMEIN()
API_URL = lambda : BASE_URL() + u"/AVS/besc"
SEC_BASE_URL = lambda : u"https://%s.itvonline.nl" % SUB_DOMEIN()
SEC_API_URL = lambda : SEC_BASE_URL() + u"/AVS/besc"

PLAY_MISS_URL = lambda : BASE_URL() + u"/videotheek/spelen/%s"
PLAY_VIDEOTHEEK_URL = lambda : BASE_URL() + u"/videotheek/spelen/%s"
PLAY_CHANNEL_URL = lambda : BASE_URL() + u"/?channelId=%s"

prijsRegex = Regex("^prijs : (.*)$" , Regex.MULTILINE)
CookieRegex = Regex("\.itvonline\.nl$")

DOMEIN_DICT = {
    u'KPN' : u'www',
    u'Telfort' : u'telfort'
}

# Plex media center ondersteund geen versleutelde http live streaming
EXCLUDE_CLIENT_DICT = [
    ClientPlatform.MacOSX,
    ClientPlatform.Linux,
    ClientPlatform.Windows
]

#don't add hd Channels
PACKAGE_EXCLUDE = [
    
]

#Don't add special case hd channels
CHANNEL_EXCLUDE = [
    
]

THUMB_DICT = {
    ClientPlatform.MacOSX : u'desktopThumb',
    ClientPlatform.Linux : u'desktopThumb',
    ClientPlatform.Windows : u'desktopThumb',
    u"Plex Home Theater" : u'desktopThumb',
    u"Default" : u'default'
}

CHANNEL_LIST = {
    '18' : {u'name' : u'Nederland 1',    u'thumb' : {u'default' : u'Nederland 1.png', u'desktopThumb' : u'Nederland 1_pht.png'}, u'art' : u'Nederland_Art.jpg'},
    '19' : {u'name' : u'Nederland 2',    u'thumb' : {u'default' : u'Nederland 2.png', u'desktopThumb' : u'Nederland 2_pht.png'}, u'art' : u'Nederland_Art.jpg'},
    '20' : {u'name' : u'Nederland 3',    u'thumb' : {u'default' : u'Nederland 3.png', u'desktopThumb' : u'Nederland 3_pht.png'}, u'art' : u'Nederland_Art.jpg'},
    '21' : {u'name' : u'RTL 4',    u'thumb' : {u'default' : u'RTL 4.png', u'desktopThumb' : u'RTL 4_pht.png'}, u'art' : u'rtl4_art.jpg'},
    '22' : {u'name' : u'RTL 5',    u'thumb' : {u'default' : u'RTL 5.png', u'desktopThumb' : u'RTL 5_pht.png'}, u'art' : u'rtl5_art.jpg'},
    '23' : {u'name' : u'SBS 6',    u'thumb' : {u'default' : u'SBS 6.png', u'desktopThumb' : u'SBS 6_pht.png'}, u'art' : u'SBS6_art.jpg'},
    '24' : {u'name' : u'RTL 7',    u'thumb' : {u'default' : u'RTL 7.png', u'desktopThumb' : u'RTL 7_pht.png'}, u'art' : u'rtl7_art.jpg'},
    '25' : {u'name' : u'NET 5',    u'thumb' : {u'default' : u'NET 5.png', u'desktopThumb' : u'NET 5_pht.png'}, u'art' : u'Net5_art.jpg'},
    '26' : {u'name' : u'Veronica / Disney XD',    u'thumb' : {u'default' : u'Veronica.png', u'desktopThumb' : u'Veronica_pht.png'}, u'art' : u'Veronica_art.jpg'},
    '27' : {u'name' : u'RTL 8',    u'thumb' : {u'default' : u'RTL 8.png', u'desktopThumb' : u'RTL 8_pht.png'}, u'art' : u'RTL8_art.jpg'},
    '30' : {u'name' : u'Comedy Central / Kindernet',    u'thumb' : {u'default' : u'comedy central.png', u'desktopThumb' : u'comedy central_pht.png'}, u'art' : u''},
    '31' : {u'name' : u'Nickelodeon',    u'thumb' : {u'default' : u'Nickelodeon.png', u'desktopThumb' : u'Nickelodeon_pht.png'}, u'art' : u''},
    '29' : {u'name' : u'MTV',    u'thumb' : {u'default' : u'MTV.png', u'desktopThumb' : u'MTV_pht.png'}, u'art' : u''},
    '205' : {u'name' : u'Fox',    u'thumb' : {u'default' : u'Fox.png', u'desktopThumb' : u'Fox_pht.png'}, u'art' : u''},
    '32' : {u'name' : u'Discovery Channel',    u'thumb' : {u'default' : u'Discovery Channel.png', u'desktopThumb' : u'Discovery Channel_pht.png'}, u'art' : u''},
    '33' : {u'name' : u'National Geographic',    u'thumb' : {u'default' : u'National Geographic.png', u'desktopThumb' : u'National Geographic_pht.png'}, u'art' : u''},
    '34' : {u'name' : u'TLC',    u'thumb' : {u'default' : u'TLC.png', u'desktopThumb' : u'TLC_pht.png'}, u'art' : u''},
    '28' : {u'name' : u'Videotheek TV',    u'thumb' : {u'default' : u'Videotheek TV.png', u'desktopThumb' : u'Videotheek TV_pht.png'}, u'art' : u''},
    '175' : {u'name' : u'24Kitchen',    u'thumb' : {u'default' : u'24Kitchen.png', u'desktopThumb' : u'24Kitchen_pht.png'}, u'art' : u''},
    '39' : {u'name' : u'BBC1',    u'thumb' : {u'default' : u'BBC1.png', u'desktopThumb' : u'BBC1_pht.png'}, u'art' : u''},
    '40' : {u'name' : u'BBC2',    u'thumb' : {u'default' : u'BBC2.png', u'desktopThumb' : u'BBC2_pht.png'}, u'art' : u''},
    '98' : {u'name' : u'BBC3',    u'thumb' : {u'default' : u'BBC3.png', u'desktopThumb' : u'BBC3_pht.png'}, u'art' : u''},
    '99' : {u'name' : u'BBC4',    u'thumb' : {u'default' : u'BBC4.png', u'desktopThumb' : u'BBC4_pht.png'}, u'art' : u''},
    '37' : {u'name' : u'één',    u'thumb' : {u'default' : u'een.png', u'desktopThumb' : u'een_pht.png'}, u'art' : u''},
    '38' : {u'name' : u'Canvas',    u'thumb' : {u'default' : u'Canvas.png', u'desktopThumb' : u'Canvas_pht.png'}, u'art' : u''},
    '176' : {u'name' : u'Ketnet',    u'thumb' : {u'default' : u'Ketnet.png', u'desktopThumb' : u'Ketnet_pht.png'}, u'art' : u''},
    '41' : {u'name' : u'Eurosport',    u'thumb' : {u'default' : u'Eurosport.png', u'desktopThumb' : u'Eurosport_pht.png'}, u'art' : u''},
    '42' : {u'name' : u'Humor TV 24',    u'thumb' : {u'default' : u'Humor TV 24.png', u'desktopThumb' : u'Humor TV 24_pht.png'}, u'art' : u''},
    '43' : {u'name' : u'NOS Journaal 24',    u'thumb' : {u'default' : u'NOS Journaal 24.png', u'desktopThumb' : u'NOS Journaal 24_pht.png'}, u'art' : u''},
    '44' : {u'name' : u'13th Street',    u'thumb' : {u'default' : u'13th Street.png', u'desktopThumb' : u'13th Street_pht.png'}, u'art' : u''},
    '45' : {u'name' : u'CNN',    u'thumb' : {u'default' : u'CNN.png', u'desktopThumb' : u'CNN_pht.png'}, u'art' : u''},
    '47' : {u'name' : u'BBC World News',    u'thumb' : {u'default' : u'BBC World News.png', u'desktopThumb' : u'BBC World News_pht.png'}, u'art' : u''},
    '190' : {u'name' : u'Xite',    u'thumb' : {u'default' : u'Xite.png', u'desktopThumb' : u'Xite_pht.png'}, u'art' : u''},
    '100' : {u'name' : u'Nick Jr.',    u'thumb' : {u'default' : u'Nick Jr.png', u'desktopThumb' : u'Nick Jr_pht.png'}, u'art' : u''},
    '101' : {u'name' : u'Baby TV',    u'thumb' : {u'default' : u'Baby TV.png', u'desktopThumb' : u'Baby TV_pht.png'}, u'art' : u''},
    '96' : {u'name' : u'JimJam',    u'thumb' : {u'default' : u'JimJam.png', u'desktopThumb' : u'JimJam_pht.png'}, u'art' : u''},
    '214' : {u'name' : u'Pebble TV',    u'thumb' : {u'default' : u'Pebble TV.png', u'desktopThumb' : u'Pebble TV_pht.png'}, u'art' : u''},
    '130' : {u'name' : u'Z@ppelin / Z@pp 24',    u'thumb' : {u'default' : u'Z@ppelin / Z@pp 24.png', u'desktopThumb' : u'Z@ppelin / Z@pp 24_pht.png'}, u'art' : u''},
    '54' : {u'name' : u'TV5 MONDE',    u'thumb' : {u'default' : u'TV5 MONDE.png', u'desktopThumb' : u'TV5 MONDE_pht.png'}, u'art' : u''},
    '103' : {u'name' : u'Politiek 24',    u'thumb' : {u'default' : u'Politiek 24.png', u'desktopThumb' : u'Politiek 24_pht.png'}, u'art' : u''},
    '104' : {u'name' : u'Holland Doc 24',    u'thumb' : {u'default' : u'Holland Doc 24.png', u'desktopThumb' : u'Holland Doc 24_pht.png'}, u'art' : u''},
    '106' : {u'name' : u'History',    u'thumb' : {u'default' : u'history channel.png', u'desktopThumb' : u'history channel_pht.png'}, u'art' : u''},
    '107' : {u'name' : u'Discovery Science',    u'thumb' : {u'default' : u'Discovery Science.png', u'desktopThumb' : u'Discovery Science_pht.png'}, u'art' : u''},
    '108' : {u'name' : u'Discovery World',    u'thumb' : {u'default' : u'Discovery World.png', u'desktopThumb' : u'Discovery World_pht.png'}, u'art' : u''},
    '178' : {u'name' : u'Animal Planet',    u'thumb' : {u'default' : u'Animal Planet.png', u'desktopThumb' : u'Animal Planet_pht.png'}, u'art' : u''},
    '110' : {u'name' : u'Travel Channel',    u'thumb' : {u'default' : u'Travel Channel.png', u'desktopThumb' : u'Travel Channel_pht.png'}, u'art' : u''},
    '111' : {u'name' : u'Nat Geo Wild',    u'thumb' : {u'default' : u'Nat Geo Wild.png', u'desktopThumb' : u'Nat Geo Wild_pht.png'}, u'art' : u''},
    '113' : {u'name' : u'Cultura 24',    u'thumb' : {u'default' : u'Cultura 24.png', u'desktopThumb' : u'Cultura 24_pht.png'}, u'art' : u''},
    '114' : {u'name' : u'NostalgieNet',    u'thumb' : {u'default' : u'NostalgieNet.png', u'desktopThumb' : u'NostalgieNet_pht.png'}, u'art' : u''},
    '115' : {u'name' : u'Eurosport 2',    u'thumb' : {u'default' : u'Eurosport 2.png', u'desktopThumb' : u'Eurosport 2_pht.png'}, u'art' : u''},
    '117' : {u'name' : u'Motors TV',    u'thumb' : {u'default' : u'Motors TV.png', u'desktopThumb' : u'Motors TV_pht.png'}, u'art' : u''},
    '172' : {u'name' : u'HBO',    u'thumb' : {u'default' : u'HBO.png', u'desktopThumb' : u'HBO_pht.png'}, u'art' : u''},
    '173' : {u'name' : u'HBO2',    u'thumb' : {u'default' : u'HBO2.png', u'desktopThumb' : u'HBO2_pht.png'}, u'art' : u''},
    '174' : {u'name' : u'HBO3',    u'thumb' : {u'default' : u'HBO3.png', u'desktopThumb' : u'HBO3_pht.png'}, u'art' : u''},
    '143' : {u'name' : u'Sport1 Select',    u'thumb' : {u'default' : u'Sport1 Select.png', u'desktopThumb' : u'Sport1 Select_pht.png'}, u'art' : u''},
    '144' : {u'name' : u'Sport1 Voetbal',    u'thumb' : {u'default' : u'Sport1 Voetbal.png', u'desktopThumb' : u'Sport1 Voetbal_pht.png'}, u'art' : u''},
    '145' : {u'name' : u'Sport1 Golf',    u'thumb' : {u'default' : u'Sport1 Golf.png', u'desktopThumb' : u'Sport1 Golf_pht.png'}, u'art' : u''},
    '146' : {u'name' : u'Sport1 Tennis',    u'thumb' : {u'default' : u'Sport1 Tennis.png', u'desktopThumb' : u'Sport1 Tennis_pht.png'}, u'art' : u''},
    '147' : {u'name' : u'Sport1 Extra1',    u'thumb' : {u'default' : u'Sport1 Extra1.png', u'desktopThumb' : u'Sport1 Extra1_pht.png'}, u'art' : u''},
    '148' : {u'name' : u'Sport1 Extra2',    u'thumb' : {u'default' : u'Sport1 Extra2.png', u'desktopThumb' : u'Sport1 Extra2_pht.png'}, u'art' : u''},
    '206' : {u'name' : u'Film1 Premiere',    u'thumb' : {u'default' : u'Film1 Premiere.png', u'desktopThumb' : u'Film1 Premiere_pht.png'}, u'art' : u''},
    '207' : {u'name' : u'Film1 Action',    u'thumb' : {u'default' : u'Film1 Action.png', u'desktopThumb' : u'Film1 Action_pht.png'}, u'art' : u''},
    '208' : {u'name' : u'Film1 Comedy & Kids',    u'thumb' : {u'default' : u'Film1 Comedy & Kids.png', u'desktopThumb' : u'Film1 Comedy & Kids_pht.png'}, u'art' : u''},
    '209' : {u'name' : u'Film1 Spotlight',    u'thumb' : {u'default' : u'Film1 Spotlight.png', u'desktopThumb' : u'Film1 Spotlight_pht.png'}, u'art' : u''},
    '210' : {u'name' : u'Film1 Sundance',    u'thumb' : {u'default' : u'Film1 Sundance.png', u'desktopThumb' : u'Film1 Sundance_pht.png'}, u'art' : u''},
    '120' : {u'name' : u'Best 24',    u'thumb' : {u'default' : u'Best 24.png', u'desktopThumb' : u'Best 24_pht.png'}, u'art' : u''},
    '169' : {u'name' : u'Comedy Central Extra',    u'thumb' : {u'default' : u'Comedy Central Extra.png', u'desktopThumb' : u'Comedy Central Extra_pht.png'}, u'art' : u''},
    '123' : {u'name' : u'Comedy Central Family',    u'thumb' : {u'default' : u'Comedy Central Family.png', u'desktopThumb' : u'Comedy Central Family_pht.png'}, u'art' : u''},
    '126' : {u'name' : u'101 TV',    u'thumb' : {u'default' : u'101 TV.png', u'desktopThumb' : u'101 TV_pht.png'}, u'art' : u''},
    '127' : {u'name' : u'OUT TV',    u'thumb' : {u'default' : u'OUT TV.png', u'desktopThumb' : u'OUT TV_pht.png'}, u'art' : u''},
    '195' : {u'name' : u'Ginx TV',    u'thumb' : {u'default' : u'Ginx TV.png', u'desktopThumb' : u'Ginx TV_pht.png'}, u'art' : u''},
    '170' : {u'name' : u'Family 7',    u'thumb' : {u'default' : u'Family 7.png', u'desktopThumb' : u'Family 7_pht.png'}, u'art' : u''},
    '133' : {u'name' : u'VH1',    u'thumb' : {u'default' : u'VH1.png', u'desktopThumb' : u'VH1_pht.png'}, u'art' : u''},
    '134' : {u'name' : u'MTV Brand New',    u'thumb' : {u'default' : u'MTV Brand New.png', u'desktopThumb' : u'MTV Brand New_pht.png'}, u'art' : u''},
    '135' : {u'name' : u'MTV Music24',    u'thumb' : {u'default' : u'MTV Music24.png', u'desktopThumb' : u'MTV Music24_pht.png'}, u'art' : u''},
    '58' : {u'name' : u'SLAM! TV',    u'thumb' : {u'default' : u'SLAM! TV.png', u'desktopThumb' : u'SLAM! TV_pht.png'}, u'art' : u''},
    '196' : {u'name' : u'Djazz TV',    u'thumb' : {u'default' : u'Djazz.png', u'desktopThumb' : u'Djazz_pht.png'}, u'art' : u''},
    '137' : {u'name' : u'TV Oranje',    u'thumb' : {u'default' : u'TV Oranje.png', u'desktopThumb' : u'TV Oranje_pht.png'}, u'art' : u''},
    '197' : {u'name' : u'192 TV',    u'thumb' : {u'default' : u'192 TV.png', u'desktopThumb' : u'192 TV_pht.png'}, u'art' : u''},
    '198' : {u'name' : u'iConcerts',    u'thumb' : {u'default' : u'iConcerts.png', u'desktopThumb' : u'iConcerts_pht.png'}, u'art' : u''},
    '139' : {u'name' : u'Trace TV',    u'thumb' : {u'default' : u'Trace TV.png', u'desktopThumb' : u'Trace TV_pht.png'}, u'art' : u''},
    '140' : {u'name' : u'BravaNL',    u'thumb' : {u'default' : u'BravaNL.png', u'desktopThumb' : u'BravaNL_pht.png'}, u'art' : u''},
}

RECORD_TYPE = {
    u"FINISHED" : {u"name" : u"Opgenomen" , u"popupTitle" : u"Opgemomen opnames" , u"thumb" : u""},
    u"SCHEDULED" : {u"name" : u"Gepland" , u"popupTitle" : u"Geplande opnames" , u"thumb" : u""},
    u"ONGOING" : {u"name" : u"Opname loopt" , u"popupTitle" : u"Lopende opnames" , u"thumb" : u""},
    u"FAILED" : {u"name" : u"Mislukt" , u"popupTitle" : u"Mislukte opnames" , u"thumb" : u""},
    u"ALL" : {u"popupTitle" : u"Alle opnames"}
}

MISS_EXT = u"poster-hl.jpg"
VIDEOTHEEK_EXT = u"poster-vl.jpg"

POSTER_URLS = [
    u"http://x1.itvonline.nl/kpn/kpnwebtv/%s/%s",
    u"http://x2.itvonline.nl/kpn/kpnwebtv/%s/%s",
    u"http://x3.itvonline.nl/kpn/kpnwebtv/%s/%s",
    u"http://x4.itvonline.nl/kpn/kpnwebtv/%s/%s",
    u"http://x5.itvonline.nl/kpn/kpnwebtv/%s/%s"
]
ICON_URLS = [
    u"http://x6.itvonline.nl/kpn/kpnwebtv/%s",
    u"http://x7.itvonline.nl/kpn/kpnwebtv/%s",
    u"http://x8.itvonline.nl/kpn/kpnwebtv/%s",
    u"http://x9.itvonline.nl/kpn/kpnwebtv/%s",
]

#####################################################################

class LoginException(Exception):
    pass

def auth(Force=False):
    def auth_deco(f):
        def real_auth(*args , **kwargs):
            if not NeedLogin() and not Force:
                try:
                    ret =  f(*args , **kwargs)
                except LoginException:
                    pass
                else:
                    prams = {
                        'action' : 'KeepAlive',
                        'channel' : 'IPAD'
                    }
                    DataUrl = buildURL(API_URL() , prams)
                    data = JSON.ObjectFromURL(DataUrl , cacheTime=0)

                    Log.Info(data)
                    
                    return ret
            
            HTTP.ClearCookies()
            
            prams = {
                'action' : 'IpAuthentication',
                'channel' : 'PCTV'
            }
            url = buildURL(API_URL() , prams)
            data = JSON.ObjectFromURL(url , cacheTime=0)
            
            if len(data["errorDescription"]):
                Log.Exception(JSON.StringFromObject(data))
                if data['errorDescription'] == "ACN_3055":
                    raise LoginException("Login Error : Je bent niet binnen een netwerk van KPN of Telfort.")
                else:
                    raise LoginException("Login Error : %s" % data['message'])
            
            Dict[u'tan'] = data[u'resultObj'][u'tan']

            return f(*args , **kwargs)
        return real_auth
    return auth_deco

def NeedLogin():
    "this functions makes sure we only login if we absolutely have to"
    l = []
    for c in HTTP.Cookies:
        if c.name in ['ACE' , 'JSESSIONID' , 'avs_cookie'] and CookieRegex.search(c.domain):
            l.append(c.name)
            if c.is_expired():
                return True
    for k in ['ACE' , 'JSESSIONID' , 'avs_cookie']:
        if k not in l:
            return True
    return False

#####################################################################

def Start():
    # Initialize the plugin
    Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
    Plugin.AddViewGroup("InfoList", viewMode = "InfoList", mediaType = "items")
    Plugin.AddViewGroup('EpisodeList', viewMode='Episodes', mediaType='items')
    
    # Setup the default attributes for the ObjectContainer
    ObjectContainer.title1 = NAME
    ObjectContainer.view_group = 'List'
    ObjectContainer.art = R(ART)
    
    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
    HTTP.CacheTime = CACHE_1DAY
    HTTP.ClearCookies()
    
    Log.Info("##########################  Plugins Started  #################################")

@auth(Force=True)
def authDummy():
    pass

def ValidatePrefs():
    u"The auth decoretor will return an raise an LoginException with header and message set to the right error if there is an error"
    try:
        authDummy()
    except LoginException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Auth Error" , message=unicode(e))
    return

#####################################################################

@handler(VIDEO_PREFIX, NAME, ICONS[Prefs['provider']] , ART)
def MainMenu():
    Log.Info("##########################  MainMenu  #################################")
    if Client.Platform in EXCLUDE_CLIENT_DICT:
        oc = ObjectContainer(
            objects = [
                DirectoryObject(
                    key = Callback(dummy),
                    title = u"Client niet volledig ondersteunt",
                    summary = u"Deze client wordt niet volledig ondersteun door deze plugin.\n Probeer de laatste versie van Plex Home Theater te downloaden. Deze wordt wel volledig onsteund.",
                    thumb = R(u"FlagRed.png")
                ),
                DirectoryObject(
                    key = Callback(Gids),
                    title = u"Gids",
                    summary = u"Bekijk de gids en plan opnames.",
                    thumb = R(ICON_GIDS)
                ),
                PopupDirectoryObject(
                    key = Callback(MijnOpnames),
                    title = u"Mijn Opnames",
                    summary = u"Beheer en verwijder uw opnames met Plex.",
                    thumb = R(ICON_OPNAMES)
                ),
                PrefsObject(title=u"Instellingen" , summary=u"Selecteer uw provider en andere opties.")
            ]
        )
        return oc

    oc = ObjectContainer(
        objects = [
            DirectoryObject(
                key = Callback(Channels),
                title = u"Live TV Kanalen",
                summary = u"Bekijk uw live TV rechtstreek vanuit Plex.",
                thumb = R(ICON_TV)
            ),
			DirectoryObject(
                key = Callback(Gids),
                title = u"Gids",
                summary = u"Bekijk de gids en plan opnames.",
                thumb = R(ICON_GIDS)
            ),
            DirectoryObject(
                key = Callback(Gemist),
                title = u"Programma Gemist",
                summary = u"Bekijk gemiste programma's.",
                thumb = R(ICON_MISS)
            ),
            DirectoryObject(
                key = Callback(VideoTheek),
                title = u"Videotheek",
                summary = u"Bekijk trailers van de films momenteel verkrijgbaar in de iTVonline Videotheek.",
                thumb = R(ICON_VIDEOTHEEK)
            ),
            PopupDirectoryObject(
                key = Callback(MijnOpnames),
                title = u"Mijn Opnames",
                summary = u"Beheer en verwijder uw opnames met Plex.",
                thumb = R(ICON_OPNAMES)
            ),
            PrefsObject(title=u"Instellingen" , summary=u"Selecteer uw provider en andere opties.")
        ]
    )
    return oc
    
#####################################################################

@route(VIDEO_PREFIX + '/channels')
def Channels():
    Log.Info("##########################  Channels  #################################")
    oc = ObjectContainer(title2 = u"Live TV")

    channelIds = GetChannelIds()
    prams = {
        u'action' : u'GetEpg',
        u'channel':u'PCTV' , 
        u'startTimeStamp': Datetime.Now(), 
        u'maxResultsPerChannel': 2 , 
        u'channelId': channelIds
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    
    Log.Info(epg)
    
    channels = epg[u'resultObj'][u'channelList']
    for channel in sorted(channels , key=lambda channel : channelIds.index(channel[u'channelId'])):
        oc.add(
            VideoClipObject(
                url = PLAY_CHANNEL_URL() % channel[u'channelId'],
                title = channel[u'channelName'],
                summary = u'%s\n%s\n\n%s\n\n%s\n%s\n\n%s' % (channel['programList'][0]['title'] ,\
                                                            channel['programList'][0]['subtitle'] ,\
                                                            channel['programList'][0]['contentDescription'] ,\
                                                            channel['programList'][1]['title'] if len(channel['programList'])>1 else " " ,\
                                                            channel['programList'][1]['subtitle'] if len(channel['programList'])>1 else " ",\
                                                            channel['programList'][1]['contentDescription'] if len(channel['programList'])>1 else " "),
                thumb = R(getResourceName(channel[u'channelId'])),
                art = R(getResourceName(channel[u'channelId'] , art=True))
            )
        )
    return oc

#####################################################################

@route(VIDEO_PREFIX + '/gids')
def Gids():
    Log.Info("##########################  Gids  #################################")
    oc = ObjectContainer(title2 = u"Gids")
    prams = {
        u'action' : u'GetEpg',
        u'channel':u'PCTV' , 
        u'startTimeStamp': Datetime.Now(), 
        u'maxResultsPerChannel':'2' , 
        u'channelId': GetChannelIds()
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    channels = epg[u'resultObj'][u'channelList']
    for channel in channels:
        oc.add(
            PopupDirectoryObject(
                key = Callback(AskGidsDay , id=channel[u'channelId']),
                title = channel[u'channelName'],
                summary = u'%s\n%s\n\n%s\n\n%s\n%s\n\n%s' % (channel[u'programList'][0][u'title'] ,\
                                                            channel[u'programList'][0][u'subtitle'] ,\
                                                            channel[u'programList'][0][u'contentDescription'] ,\
                                                            channel[u'programList'][1][u'title'] if len(channel[u'programList'])>1 else " " ,\
                                                            channel[u'programList'][1][u'subtitle'] if len(channel[u'programList'])>1 else " ",\
                                                            channel[u'programList'][1][u'contentDescription'] if len(channel[u'programList'])>1 else " "),
                thumb = R(getResourceName(channel[u'channelId'])),
                art = R(getResourceName(channel[u'channelId'] , art=True))
            )
        )
    return oc

@route(VIDEO_PREFIX + '/gids/askday' , id=str)
def AskGidsDay(id):
    Log.Info("##########################  AskGidsDay  #################################")
    oc = ObjectContainer(title2 = u"Gids")
    daysList = [u"Vandaag" , u"Gisteren" , u"Morgen" , u"Overmorgen" , u"Over 3 Dagen" , u"Over 4 Dagen" , u"Over 5 Dagen" , u"Over 6 Dagen" , u"Over 7 Dagen"]
    days = {u"Vandaag" : 0 , u"Gisteren" : -1 , u"Morgen" : 1 , u"Overmorgen" : 2 , u"Over 3 Dagen" : 3 , u"Over 4 Dagen" : 4 , u"Over 5 Dagen" : 5 , u"Over 6 Dagen" : 6 , u"Over 7 Dagen" : 7}
    for key in daysList:
        oc.add(
            DirectoryObject(
                key = Callback(ChannelGids , id=id , days=days[key]),
                title = key
            )
        )
    return oc

@route(VIDEO_PREFIX + '/gids/channels' , id=str , days=int)
def ChannelGids(id , days):
    Log.Info("##########################  ChannelGids  #################################")
    oc = ObjectContainer(title2 = u"Gids")
    if days == 0:
        startTime = Datetime.Now()
    else:
        startTime = Datetime.Now().replace(hour = 0, minute = 0, second = 0, microsecond =0) + Datetime.Delta(days=days)
    endTime = startTime + Datetime.Delta(days=1)
    prams = {
        u'action' : u'GetEpg',
        u'channel':u'PCTV' , 
        u'startTimeStamp': startTime, 
        u'endTimeStamp': endTime , 
        u'channelId': id
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    programs = epg[u'resultObj'][u'channelList'][0][u'programList']
    for program in programs:
        oc.add(
            PopupDirectoryObject(
                key = Callback(ProgramOptions , id=program[u'contentId']) ,
                title = program['title'],
                summary = u'%s\n\n%s' % (program[u'subtitle'] , program[u'contentDescription']),
                thumb = R(getResourceName(channel[u'channelId'])),
                art = R(getResourceName(channel[u'channelId'] , art=True))
            )
        )
    return oc

@route(VIDEO_PREFIX + '/gids/options' , id=str)
def ProgramOptions(id):
    Log.Info("##########################  ProgramOptions  #################################")
    oc = ObjectContainer(title2 = u"Gids")
    time = Datetime.TimestampFromDatetime(Datetime.Now())
    prams = {
        u'action' : u'GetLiveInfo',
        u'channel' : u'PCTV',
        u'contentId' : id
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    program = epg[u'resultObj']
    if program[u'starttime'] < time and program[u'endtime'] > time:
        oc.add(
            VideoClipObject(
                url = PLAY_CHANNEL_URL() % program[u'channelId'],
                title = u"Nu Bekijken",
                summary = u'%s\n%s\n\n%s' % (program[u'title'] , program[u'subtitle'] , program[u'longdescription']),
                thumb = R(CHANNEL_LIST[program[u'channelId']][u'thumb']),
                art = R(CHANNEL_LIST[program[u'channelId']][u'art'])
            )
        )
    oc.add(
        DirectoryObject(
            key = Callback(RecordProgram , externalChannelId=program[u'externalChannelId'] , programRefNr=program[u'externalContentId'] , programStartTime=program[u'starttime']*1000),
            title = u"Nu Opnemen" if program[u'starttime'] < time and program[u'endtime'] > time else u"Opnamen Plannen",
            summary = u'%s\n%s\n\n%s' % (program[u'title'] , program[u'subtitle'] , program[u'longdescription']),
            thumb = R(CHANNEL_LIST[program[u'channelId']][u'thumb']),
            art = R(CHANNEL_LIST[program[u'channelId']][u'art'])
        )
    )
    return oc

@route(VIDEO_PREFIX + '/gids/record' , externalChannelId=str , programRefNr=str , programStartTime=str)
def RecordProgram(externalChannelId , programRefNr , programStartTime):
    Log.Info("##########################  RecordProgram  #################################")
    try:
        epg = SetRecodings(externalChannelId , programRefNr , programStartTime)
    except LoginException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Record Error" , message=unicode(e))

    Log.Info(epg)

    return  ObjectContainer(header=u"Opnamen ingepland" , message=u"Uw opnamen is ingelpand")
    

#####################################################################

@route(VIDEO_PREFIX + '/gemist')
def Gemist():
    Log.Info("##########################  Gemist  #################################")
    oc = ObjectContainer(
        title2 = u"Gemist",
        objects = [
            DirectoryObject(
                key = Callback(JustMiss),
                title = u"Net gemist",
                summary = u"De laatste 20 gemiste shows van alle kanalen"
            ),
			DirectoryObject(
                key = Callback(ChannelMiss),
                title = u"Per Kanaal"
            ),
            PopupDirectoryObject(
                key = Callback(DayMiss),
                title = u"Per dag"
            )
        ]
    )
    return oc

@route(VIDEO_PREFIX + '/gemist/netgemist' , allow_sync=True)
def JustMiss():
    Log.Info("##########################  JustMiss  #################################")
    oc = ObjectContainer(title2 = u"Gemist")
    endTime = Datetime.Now()
    startTime = endTime  - Datetime.Delta(days=10)
    prams = {
        u'action' : u'GetCatchUpTV', 
        u'channel' : u'PCTV',
        u'startDate' : startTime,
        u'endDate' : endTime,
        u'maxResults' : 30
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    for day in reversed(epg[u'resultObj'][u'categoryList']):
        for miss in day[u'contents']:
            oc.add(
                VideoClipObject(
                    url = PLAY_MISS_URL() % miss[u'contentId'],
                    title = miss[u'contentTitle'],
                    tagline = u"%s , %s" % (miss[u'contentSubtitle'] , miss[u'channelName']),
                    summary = miss[u'contentDescription'],
                    duration = miss[u'duration'] * 1000,
                    thumb = Resource.ContentsOfURLWithFallback(Util.RandomItemFromList(POSTER_URLS) % (miss[u'urlPictures'] , MISS_EXT))
                )
            )
    return oc

@route(VIDEO_PREFIX + '/gemist/kanalen')
def ChannelMiss():
    Log.Info("##########################  ChannelMiss  #################################")
    oc = ObjectContainer(title2 = u"Gemist")
    endTime = Datetime.Now()
    startTime = endTime-Datetime.Delta(days=10)
    prams = {
        u'action' : u'GetCatchUpTVChannelsList', 
        u'channel' : u'PCTV',
        u'startDate' : startTime,
        u'endDate' : endTime
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    for channel in epg[u'resultObj'][u'channelList']:
        try:
            oc.add(
                DirectoryObject(
                    key = Callback(DisplayMiss , startTime = startTime , endTime=endTime , channel=channel[u'channelName']),
                    title = channel[u'channelName'],
                    thumb = R(CHANNEL_LIST[str(int(channel[u'channelId'])-1000)][u'thumb'])
                )
            )
        except KeyError:
            pass
    return oc

@route(VIDEO_PREFIX + '/gemist/askday')
def DayMiss():
    Log.Info("##########################  DayMiss  #################################")
    oc = ObjectContainer(title2 = u"Gemist")
    monthList = {1 : u"Januari" , 2 : u"Februari" , 3 : u"Maart" , 4 : u"April" , 5 : u"Mei" , 6 : u"Juni" , 7 : u"Juli", 8 : u"Augustus" , 9 : u"September" , 10 : u"Oktober" , 11 : u"November" , 12 : u"December"}
    daysList = {0 : u"Maandag" , 1 : u"Dinsdag" , 2 : u"Woendag" , 3 : u"Donderdag" , 4 : u"Vrijdag" , 5 : u"Zaterdag" , 6 : u"Zondag"}
    midnight = Datetime.Now().replace(hour = 0, minute = 0, second = 0, microsecond =0)
    oc.add(
        DirectoryObject(
            key = Callback(DisplayMiss , startTime = midnight , endTime=Datetime.Now()),
            title = u"Vandaag",
        )
    )
    oc.add(
        DirectoryObject(
            key = Callback(DisplayMiss , startTime = midnight - Datetime.Delta(days=1) , endTime=midnight),
            title = u"Gisteren",
        )
    )
    for day in range(2 , 7):
        startTime = midnight - Datetime.Delta(days=day)
        endTime = startTime + Datetime.Delta(days=1)
        oc.add(
            DirectoryObject(
                key = Callback(DisplayMiss , startTime=startTime , endTime=endTime),
                title = u"%s %d %s" % (daysList[startTime.weekday()] , startTime.day , monthList[startTime.month])
            )
        )
    return oc

@route(VIDEO_PREFIX + '/gemist/display' , startTime=Datetime , endTime=Datetime , channel=str , allow_sync=True)
def DisplayMiss(startTime , endTime , channel=None):
    Log.Info("##########################  DisplayMiss  #################################")
    oc = ObjectContainer(title2 = u"Gemist")
    prams = {
        u'action' : u'GetCatchUpTV', 
        u'channel' : u'PCTV',
        u'startDate' : startTime,
        u'endDate' : endTime
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    for day in reversed(epg[u'resultObj'][u'categoryList']):
        for miss in day[u'contents']:
            if not channel or channel==miss[u'channelName']:
                oc.add(
                    VideoClipObject(
                        url = PLAY_MISS_URL() % miss[u'contentId'],
                        title = miss[u'contentTitle'],
                        tagline = u"%s , %s" % (miss[u'contentSubtitle'] , miss[u'channelName']),
                        summary = u"%s , %s\n\n%s" % (miss[u'contentSubtitle'] , miss[u'channelName'] , miss[u'contentDescription']),
                        duration = miss[u'duration'] * 1000,
                        thumb = Resource.ContentsOfURLWithFallback(Util.RandomItemFromList(POSTER_URLS) % (miss[u'urlPictures'] , MISS_EXT))
                    )
                )
    return oc

#####################################################################

@route(VIDEO_PREFIX + '/videotheek')
def VideoTheek():
    Log.Info("##########################  VideoTheek  #################################")
    oc = ObjectContainer(
        title2 = u"Videotheek",
        objects = [
            DirectoryObject(
                key = Callback(MyVideoTheek),
                title = u"Mijn Videotheek"
            ),
            DirectoryObject(
                key = Callback(VideoTheekPopulair),
                title = u"Populair"
            ),
            DirectoryObject(
                key = Callback(VideoTheekVideo , id=730),
                title = u"Nieuw"
            ),
            DirectoryObject(
                key = Callback(VideoTheekVideo , id=23),
                title = u"Acties"
            ),
            DirectoryObject(
                key = Callback(VideoTheekVideo , id=1100),
                title = u"Top 20"
            ),
			DirectoryObject(
                key = Callback(VideoTheekCategorie),
                title = u"Categorieen"
            )
        ]
    )
    return oc
    
@route(VIDEO_PREFIX + '/videotheek/my' , allow_sync=True)
def MyVideoTheek():
    Log.Info("##########################  MyVideoTheek  #################################")
    try:
        movie = GetRentMovies()
    except LoginException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Videotheek Error" , message=unicode(e))
    if movie:
        Log.Info(movie)
        return ObjectContainer(header=u"Niet ondersteund" , message=u"Deze functie wordt niet ondersteund door deze plugin")
    else:
        return ObjectContainer(header=u"Geen Films" , message=u"U heeft momenteel geen films in uw persoonlijke videotheek\n (Deze functie wordt ook nog niet ondesteund)")

@route(VIDEO_PREFIX + '/videotheek/categorie' , catList=list)
def VideoTheekCategorie(catList=[]):
    Log.Info("##########################  VideoTheekCategorie  #################################")
    exculde = [730 , 23 , 1100 , 541 if Prefs['Erotiek'] else 99999999]
    oc = ObjectContainer(title2 = u"Videotheek",)
    if not len(catList):
        prams = {
            u'action' : u'GetCatalogueTree',
            u'channel' : u'PCTV',
            u'maxCategoryResults' : 30
        }
        url = buildURL(API_URL() , prams)
        epg = JSON.ObjectFromURL(url)
        Log.Info(epg)
        catList = epg[u'resultObj'][u'categoryList'][0][u'categoryList']
    for cat in catList:
        if cat[u'categoryId'] in exculde:
            continue
        if not len(cat[u'categoryList']):
            oc.add(
                DirectoryObject(
                    key = Callback(VideoTheekVideo , id=cat[u'categoryId']),
                    title = cat[u'categoryName'],
                    summary = u"%s"% cat[u'contentTitle'],
                    thumb = Resource.ContentsOfURLWithFallback(Util.RandomItemFromList(POSTER_URLS) % (cat[u'urlPictures'] , VIDEOTHEEK_EXT))
                )
            )
        else:
            oc.add(
                DirectoryObject(
                    key = Callback(VideoTheekCategorie , catList=cat[u'categoryList']),
                    title = cat[u'categoryName'],
                    summary = u"%s" % cat[u'contentTitle'],
                    thumb = Resource.ContentsOfURLWithFallback(Util.RandomItemFromList(POSTER_URLS) % (cat[u'urlPictures'] , VIDEOTHEEK_EXT))
                )
            )
    return oc

@route(VIDEO_PREFIX + '/videotheek/videos' , id=int)
def VideoTheekVideo(id):
    Log.Info("##########################  VideoTheekVideo  #################################")
    prams = {
        u'action' : u'GetContentList',
        u'channel' : u'PCTV',
        u'catToRetrieve' : id
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url)
    Log.Info(epg)
    return buildVideoList(epg[u'resultObj'][u'contentList'])

@route(VIDEO_PREFIX + '/videotheek/populair')
def VideoTheekPopulair():
    Log.Info("##########################  VideoTheekPopulair  #################################")
    prams = {
        u'action' : u'GetSpecialContents',
        u'channel' : u'PCTV',
        u'maxCategoryResults' : 30
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url)
    Log.Info(epg)
    return buildVideoList(epg[u'resultObj'][u'categoryList'][1][u'contents'])
    
@route(VIDEO_PREFIX + '/videotheek/display' , video=dict , allow_sync=True)
def DisplayVideo(video):
    Log.Info("##########################  DisplayVideo  #################################")
    oc = ObjectContainer(title2 = u"Videotheek")
    videoItem = URLService.MetadataObjectForURL(PLAY_VIDEOTHEEK_URL() % video[u'contentId'])

    if CheckContentRights(video[u'contentId']):
        oc.add(videoItem)
    else:
        videoItem.title = u"Trailer"
        oc.add(videoItem)
        prijs = prijsRegex.findall(videoItem.summary)[0]
        Log.Info(prijs)
        oc.add(
            PopupDirectoryObject(
                key = Callback(AskBuy , video=video , price=prijs),
                title = u"Film Huren",
                summary = videoItem.summary
            )
        )
    return oc

def AskBuy(video , price):
    Log.Info("##########################  AskBuy  #################################")
    oc = ObjectContainer(
        title2 = u"Videotheek",
        objects = [
            DirectoryObject(
                key = Callback(dummy),
                title = u"Terug"
            ),
            DirectoryObject(
                key = Callback(BuyMovie , video=video),
                title = u"Huur deze film voor %s" % price
            )
        ]
    )
    return oc

def BuyMovie(video):
    Log.Info("##########################  BuyMovie  #################################")
    return ObjectContainer(header=u"Niet ondersteunt" , message="Deze functie wordt helaas niet ondersteunt door deze plugin")
    
def buildVideoList(catList):
    Log.Info("##########################  buildVideoList  #################################")
    oc = ObjectContainer(title2 = u"Videotheek")
    for video in catList:
        oc.add(
            PopupDirectoryObject(
                key = Callback(DisplayVideo , video = video),
                title = video[u'contentTitle'],
                summary = u"%s \n\n%s" % (video[u'contentSubtitle'] , video[u'contentDescription'] if u'contentDescription' in video else u''),
                thumb = Resource.ContentsOfURLWithFallback(Util.RandomItemFromList(POSTER_URLS) % (video[u'urlPictures'] , VIDEOTHEEK_EXT))
            )
        )
    return oc

#####################################################################

@route(VIDEO_PREFIX + '/opnames')
def MijnOpnames():
    Log.Info("##########################  MijnOpnames  #################################")
    oc = ObjectContainer(title2 = u"Mijn Opnamens")
    
    for type in (u"ALL" , u"FINISHED" , u"ONGOING" , u"FAILED"):
        oc.add(
            DirectoryObject(
                key = Callback(RecordType , type=type) ,
                title = RECORD_TYPE[type][ u"popupTitle"],
            )
        )
    return oc

@route(VIDEO_PREFIX + '/opnames/type')
def RecordType(type=u"ALL"):
    Log.Info("##########################  RecordType  #################################")
    try:
        records = GetRecodings(type)
    except LoginException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Record Error" , message=unicode(e))
    
    Log.Info(records)
    
    oc = ObjectContainer(title2 = u"Mijn Opnamens" , no_cache=True)
    for record in reversed(records[u'listOfRecordings']):
        status = RECORD_TYPE[record[u'recordingStatus']][u'name'] + (u"\n%s" % record[u'infoMessage'] if record[u'recordingStatus'] == u'FAILED' else u'')
        oc.add(
            PopupDirectoryObject(
                key = Callback(RecordOptions , id=record[u'recordID'] , userStartTimeMarker=record[u'userStartTimeMarker']) ,
                title = record[u'programTitle'],
                summary = u'%s\n\n%s' % (status , record[u'programDescription']),
                thumb = RECORD_TYPE[record[u'recordingStatus']][u'thumb']
            )
        )
    return oc

@route(VIDEO_PREFIX + '/opnames/options' , id=str)
def RecordOptions(id , userStartTimeMarker):
    Log.Info("##########################  RecordOptions  #################################")
    oc = ObjectContainer(
        title2 = u"Mijn Opnamens",
        objects = [
            DirectoryObject(
                key = Callback(dummy),
                title = u"Terug"
            ),
            DirectoryObject(
                key = Callback(DeleteRecord , id=id , userStartTimeMarker=userStartTimeMarker),
                title = u"Verwijderen"
            )
            
        ]
    )
    return oc

@route(VIDEO_PREFIX + '/opnames/delete' , id=str)
def DeleteRecord(id , userStartTimeMarker):
    Log.Info("##########################  DeleteRecord  #################################")
    try:
        epg = DelRecodings(id , userStartTimeMarker)
    except LoginException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Delete Record Error" , message=unicode(e))

    return  ObjectContainer(header=u"Opnamen Verwijderd" , message=u"Uw opnamen is verwijderd")
    
#####################################################################

@auth()
def GetRecodings(type=u"ALL"):
    prams = {
        u'action' : u'GetRecordingList',
        u'channel' : u'PCTV',
        u'typeOfRecording' : u'individual',
        u'stateOfRecording': type
    }
    url = buildURL(API_URL() , prams)
    
    LogCookies()
    
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    Log.Info(epg)
    if len(epg[u'errorDescription']):
        raise LoginException(epg[u'message'])
    return epg[u'resultObj']

# programStartTime is een unix time *1000
@auth()
def SetRecodings(externalChannelId , programRefNr , programStartTime):
    prams = {
        u'action' : u'SetRecording',
        u'channel' : u'PCTV',
        u'externalChannelId' : externalChannelId,
        u'programRefNr': programRefNr,
        u'programStartTime': programStartTime,
        u'enableAutoDelete': u'N'
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    Log.Info(epg)
    if len(epg[u'errorDescription']):
        raise LoginException(epg[u'message'])
    return epg

@auth()
def DelRecodings(id , userStartTimeMarker):
    prams = {
        u'action' : u'DeleteRecordings',
        u'channel' : u'PCTV',
        u'recordIDList' : id,
        u'userStartTimeMarkList' : userStartTimeMarker
    }

    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    Log.Info(epg)
    if len(epg[u'errorDescription']):
        raise LoginException(epg[u'message'])
    return epg[u'resultObj']

@auth()
def GetRentMovies():
    prams = {
        u'action' : u'GetRentedMovies',
        u'channel' : u'PCTV'
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    Log.Info(epg)
    if len(epg[u'errorDescription']):
        Log.Critical(epg)
        raise LoginException(epg[u'message'])
    return epg[u'resultObj']

@auth()
def BuyRentMovie(id , pin):
    prams = {
        u'action' : u'ContentPurchase',
        u'channel' : u'PCTV',
        u'contentId': id,
        u'rememberPin' : u'N',
        u'PURCHASE_CC' : u'N',
        u'securityPIN' : pin,
        u'_' : Datetime.Now()
    }
    url = buildURL(SEC_API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    
    Log.Info(epg)
    
    if len(epg[u'errorDescription']):
        Log.Critical(epg)
        raise LoginException(epg[u'message'])
    return True

@auth()
def CheckContentRights(id):
    prams = {
        u'action' : u'CheckContentRights',
        u'channel' : u'PCTV',
        u'contentId': id,
        u'type' : u'VOD',
        u'_' : Datetime.Now()
    }
    url = buildURL(SEC_API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    
    Log.Info(epg)
    
    if epg[u'resultCode'] == u'OK':
        return True
    elif epg[u'resultCode'] == u'KO_BUY':
        return False
    else:
        Log.Critical(epg)
        raise LoginException(epg[u'message'])

@auth()
def GetProfiel():
    if u'tan' not in Dict:
        raise LoginException(u"tan not in Dict")
    prams = {
        u'action' : u'GetProfile',
        u'channel' : u'PCTV',
        u'crmAccountId' : Dict[u'tan'],
        u'_' : Datetime.Now()
    }
    url = buildURL(SEC_API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    
    Log.Info(epg)
    
    if len(epg[u'errorDescription']):
        Log.Critical(epg)
        raise LoginException(epg[u'message'])
    return epg[u'resultObj']

def GetPackageIds():
    profiel = GetProfiel()
    ids = []
    for package in profiel[u'packageList']:
        ids.append(package[u'packageId'])
    return ids

def GetChannelIds():
    channelCache = Cache['CHANNELS']['LiveChannels']
    if not channelCache.expired:
        Log.Info('Returning Channel ids from Cache')
        Log.Info(channelCache.ids)
        return channelCache.ids
    
    prams = {
        u'action' : u'GetLiveChannels',
        u'channel': u'PCTV'
    }
    url = buildURL(API_URL() , prams)
    channelData = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)[u'resultObj']
    
    Log.Info(channelData)
    
    packageIds = GetPackageIds()
    channelIds = []
    for channel in channelData['channelList']:
        if channel[u'channelType'] == u'Extended' and channel[u'channelId'] not in CHANNEL_EXCLUDE:
            for package in channel[u'packageList']:
                if package[u'packageId'] in packageIds and package[u'packageType'] == u'LIVE_SUB' and package[u'packageId'] not in PACKAGE_EXCLUDE:
                    channelIds.append(unicode(channel[u'channelId']))
                    break
    
    channelCache.ids = channelIds
    channelCache.set_expiry_interval(CACHE_1DAY)
    
    Log.Info(channelIds)
    
    return channelIds

#####################################################################

@route(VIDEO_PREFIX + '/dummy')
def dummy():
    pass

@route(VIDEO_PREFIX + '/imageHelper' , id=str , art=bool , client=str)
def imageHelper(id , art=False , client=None):
    return DataObject(Resource.Load(getResourceName(id , art , client)) , 'image/png')

#####################################################################

from datetime import datetime
import urllib
def buildURL(base , args):
    parms = {}
    for k ,v in args.iteritems():
        if isinstance(v , list):
            parms[k] = u";".join(v)
        elif isinstance(v , datetime):
            parms[k] = u"%0.0f" % Datetime.TimestampFromDatetime(v)
        else:
            parms[k] = v
    Log.Info(u"%s?%s" % (base , urllib.urlencode(parms)))
    return u"%s?%s" % (base , urllib.urlencode(parms))

def getResourceName(id , art=False , client=None):
    if art:
        try:
            return CHANNEL_LIST[id][u'art']
        except KeyError:
            return u''

    thumbName = THUMB_DICT.get(client , THUMB_DICT.get(Client.Platform , THUMB_DICT.get(Client.Product , THUMB_DICT[u'Default'])))
    try:
        return CHANNEL_LIST[id][u'thumb'][thumbName]
    except KeyError:
        return u''
        
       
#####################################################################