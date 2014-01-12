#####################################################################
#
# File:        __init__.py
# Author:   Loek Wensveen
# Date:      03/01/2014
# Version: 1.0.0
# About:        This plugin alows jou to watch itvonline in plex form kpn
#
#####################################################################

auth = SharedCodeService.commen.auth

#####################################################################

VIDEO_PREFIX = "/video/itvonline"
NAME = "iTVOnline"

ART = u'art-default.jpg'
ICON = u'icon-default.jpg'
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

DOMEIN_DICT = {
    u'KPN' : u'www',
    u'Telfort' : u'telfort'
}

#'18;19;20;21;22;23;24;25;26;27;30;31;29;28;32;33;34;175;39;40;37;38;176;41;42;43;44;45;47;54;58'
CHANNELS_ORDERD = [ '18','19','20','21','22','23','24','25','26','27','30','31','29','205','32','33','34','28','175','39','40','37','38','176','41','42','43','44','45','47','190','100','28']
CHANNEL_LIST = {
    '18': {u'name' : u'Nederland 1' , u'thumb' : u'nederland1.png', u'art' : u'Nederland_Art.jpg'},
    '19': {u'name' : u'Nederland 2' , u'thumb' : u'nederland2.png', u'art' : u'Nederland_Art.jpg'},
    '20': {u'name' : u'Nederland 3' , u'thumb' : u'nederland3.png', u'art' : u'Nederland_Art.jpg'},
    '21': {u'name' : u'RTL 4' , u'thumb' : u'rtl4_nl.png', u'art' : u'rtl4_art.png'},
    '22': {u'name' : u'RTL 5' , u'thumb' : u'rtl5.png', u'art' : u''},
    '23': {u'name' : u'SBS 6' , u'thumb' : u'sbs6.png', u'art' : u'sbs6_art.jpg'},
    '24': {u'name' : u'RTL 7' , u'thumb' : u'rtl7.png', u'art' : u''},
    '25': {u'name' : u'Net 5' , u'thumb' : u'net5.png', u'art' : u''},
    '26': {u'name' : u'Veronica / Disney XD',  u'thumb' : u'disney_xd_nl.png', u'thumb2' : 'veronica.png', u'art' : ''},
    '27': {u'name' : u'RTL 8' , u'thumb' : u'rtl8.png', u'art' : u''},
    '100': {u'name' : u'Nick Jr.' , u'thumb' : u'nick_jr.png', u'art' : u''},
    '30': {u'name' : u'Comedy Central / Kindernet' , u'thumb' : u'comedy_central_nl.png', u'art' : u''},
    '31': {u'name' : u'Nickelodeon' , u'thumb' : u'nickelodeon_nl.png', u'art' : u''}, # need thumb
    '29': {u'name' : u'MTV' , u'thumb' : u'mtv_nl.png', u'art' : u''},
    '205': {u'name' : u'Fox' , u'thumb' : u'Fox.png', u'art' : u''}, # need thumb
    '32': {u'name' : u'Discovery Channel' , u'thumb' : u'discovery.png', u'art' : u''},
    '33': {u'name' : u'National Geographic' , u'thumb' : u'nat_geo.png', u'art' : u''},
    '34': {u'name' : u'TLC' , u'thumb' : u'tlc.png', u'art' : u''}, # Need thumb
    '175': {u'name' : u'24Kitchen' , u'thumb' : u'24_kitchen.png', u'art' : u''},
    '39': {u'name' : u'BBC1', u'thumb' : u'bbc_one.png', u'art' : u''},
    '40': {u'name' : u'BBC2', u'thumb' : u'bbc_two.png', u'art' : u''},
    #'98': {u'name' : u'BBC3', u'thumb' : u'BBC 3.png', u'art' : u''},
    #'99': {u'name' : u'BBC4', u'thumb' : u'BBC 4.png', u'art' : u''},
    '37': {u'name' : u'één', u'thumb' : u'vrt_een.png', u'art' : u''},
    '38': {u'name' : u'Canvas' , u'thumb' : u'vrt_canvas.png', u'art' : u''},# Need thumb
    '176': {u'name' : u'Ketnet' , u'thumb' : u'vrt_ketnet.png', u'art' : u''},# Need thumb
    '41': {u'name' : u'Eurosport' , u'thumb' : u'eurosport.png', u'art' : u''},
    '42': {u'name' : u'Humor TV 24' , u'thumb' : u'npo_humor_tv_24.png', u'art' : u''},
    '43': {u'name' : u'NOS Journaal 24' , u'thumb' : u'npo_journaal_24.png', u'art' : u''},# Need thumb
    '44': {u'name' : u'13th Street' , u'thumb' : u'13th_street_nl.png', u'art' : u''},
    '45': {u'name' : u'CNN' , u'thumb' : u'cnn.png', u'art' : u''},# Need thumb
    '47': {u'name' : u'BBC World News' , u'thumb' : u'bbc_world_news.png', u'art' : u''},
    '190': {u'name' : u'xite' , u'thumb' : 'xite.png', 'art' : ''},# Need thumb
    #'59': {u'name' : u'TV5 Monde' , u'thumb' : u'tv5_monde.png', u'art' : u''},# Need thumb
    '28': {u'name' : u'Alles Over Videoland' , u'thumb' : u'videoland_1.png', u'art' : u''}
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

@auth(Prefs)
def authDummy():
    pass

def ValidatePrefs():
    u"The auth decoretor will return an raise an APIException with header and message set to the right error if there is an error"
    try:
        authDummy()
    except Ex.APIException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Auth Error" , message=unicode(e))
    return

#####################################################################

@handler(VIDEO_PREFIX, NAME, ICON, ART)
def MainMenu():
    oc = ObjectContainer(
        objects = [
            DirectoryObject(
                key = Callback(Channels),
                title = u"Live TV Kanalen",
                summary = u"Bekijk uw live TV rechtstreek vanuit Plex.",
                thumb = R(ICON)
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
    oc = ObjectContainer(title2 = u"Live TV")

    prams = {
        u'action' : u'GetEpg',
        u'channel':u'PCTV' , 
        u'startTimeStamp': Datetime.Now(), 
        u'maxResultsPerChannel': 2 , 
        u'channelId': CHANNELS_ORDERD
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=CACHE_1MINUTE*5)
    Log.Info(epg)
    channels = epg[u'resultObj'][u'channelList']
    for channel in sorted(channels , key=lambda channel : CHANNELS_ORDERD.index(channel[u'channelId'])):
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
                thumb = R(CHANNEL_LIST[channel[u'channelId']][u'thumb']),
                art = R(CHANNEL_LIST[channel[u'channelId']][u'art'])
            )
        )
    return oc

#####################################################################

@route(VIDEO_PREFIX + '/gids')
def Gids():
    oc = ObjectContainer(title2 = u"Gids")
    prams = {
        u'action' : u'GetEpg',
        u'channel':u'PCTV' , 
        u'startTimeStamp': Datetime.Now(), 
        u'maxResultsPerChannel':'2' , 
        u'channelId':CHANNEL_LIST.keys()
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
                thumb = R(CHANNEL_LIST[channel[u'channelId']][u'thumb']),
                art = R(CHANNEL_LIST[channel[u'channelId']][u'art'])
            )
        )
    return oc

@route(VIDEO_PREFIX + '/gids/askday' , id=str)
def AskGidsDay(id):
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
                thumb = R(CHANNEL_LIST[id][u'thumb']),
                art = R(CHANNEL_LIST[id][u'art'])
            )
        )
    return oc

@route(VIDEO_PREFIX + '/gids/options' , id=str)
def ProgramOptions(id):
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
    try:
        epg = SetRecodings(externalChannelId , programRefNr , programStartTime)
    except Ex.APIException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Record Error" , message=unicode(e))

    Log.Info(epg)

    return  ObjectContainer(header=u"Opnamen ingepland" , message=u"Uw opnamen is ingelpand")
    

#####################################################################

@route(VIDEO_PREFIX + '/gemist')
def Gemist():
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
    try:
        movie = GetRentMovies()
    except Ex.APIException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Videotheek Error" , message=unicode(e))
    if movie:
        Log.Info(movie)
        return ObjectContainer(header=u"Niet ondersteund" , message=u"Deze functie wordt niet ondersteund door deze plugin")
    else:
        return ObjectContainer(header=u"Geen Films" , message=u"U heeft momenteel geen films in uw persoonlijke videotheek\n (Deze functie wordt ook nog niet ondesteund)")

@route(VIDEO_PREFIX + '/videotheek/categorie' , catList=list)
def VideoTheekCategorie(catList=[]):
    exculde = [730 , 23 , 1100 , 541 if not Prefs['Erotiek'] else 99999]
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
    oc = ObjectContainer(title2 = u"Videotheek")
    video = URLService.MetadataObjectForURL(PLAY_VIDEOTHEEK_URL() % video[u'contentId'])

    if CheckContentRights(video[u'contentId']):
        oc.add(video)
    else:
        video.title = u"Trailer"
        oc.add(video)
        prijs = prijsRegex.findall(video.summary)[0]
        Log.Info(prijs)
        oc.add(
            PopupDirectoryObject(
                key = Callback(AskBuy , video=video , price=prijs),
                title = u"Film Huren",
                summary = video.summary
            )
        )
    return oc

def AskBuy(video , price):
    oc = ObjectContainer(
        title2 = u"Videotheek",
        objects = [
            DirectoryObject(
                key = Callback(dummy),
                title = u"Terug"
            ),
            DirectoryObject(
                key = Callback(BuyMovie),
                title = u"Huur deze film voor %s" % price
            )
        ]
    )
    return oc

def BuyMovie():
    return ObjectContainer(header=u"Niet ondersteunt" , message="Deze functie wordt helaas niet ondersteunt door deze plugin")
    
def buildVideoList(catList):
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
    oc = ObjectContainer(title2 = u"Mijn Opnamens")
    
    for type in (u"ALL" , u"FINISHED" , u"ONGOING" , u"FAILED"):
        oc.add(
            DirectoryObject(
                key = Callback(RecordType , type=type) ,
                title = RECORD_TYPE[type][ u"popupTitle"],
            )
        )
    return oc
    
def RecordType(type=u"ALL"):
    try:
        records = GetRecodings(type)
    except Ex.APIException as e:
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
    try:
        epg = DelRecodings(id , userStartTimeMarker)
    except Ex.APIException as e:
        Log.Exception(unicode(e))
        return ObjectContainer(header=u"Delete Record Error" , message=unicode(e))

    return  ObjectContainer(header=u"Opnamen Verwijderd" , message=u"Uw opnamen is verwijderd")
    
#####################################################################

@auth(Prefs)
def GetRecodings(type=u"ALL"):
    prams = {
        u'action' : u'GetRecordingList',
        u'channel' : u'PCTV',
        u'typeOfRecording' : u'individual',
        u'stateOfRecording': type
    }
    url = buildURL(API_URL() , prams)
    epg = JSON.ObjectFromURL(url , cacheTime=0)
    Log.Info(epg)
    if len(epg[u'errorDescription']):
        raise Ex.APIException(epg[u'message'])
    return epg[u'resultObj']

# programStartTime is een unix time *1000
@auth(Prefs)
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
        raise Ex.APIException(epg[u'message'])
    return epg

@auth(Prefs)
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
        raise Ex.APIException(epg[u'message'])
    return epg[u'resultObj']

@auth(Prefs)
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
        raise Ex.APIException(epg[u'message'])
    return epg[u'resultObj']

@auth(Prefs)
def BuyRentMovie(id , pin):
    prams = {
        u'action' : u'ContentPurchase',
        u'channel' : u'PCTV'
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
        raise Ex.APIException(epg[u'message'])
    return True

@auth(Prefs)
def CheckContentRights(id):
    prams = {
        u'action' : u'CheckContentRights',
        u'channel' : u'PCTV'
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
        raise Ex.APIException(epg[u'message'])

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

@route(VIDEO_PREFIX + '/dummy')
def dummy():
    pass

@route(VIDEO_PREFIX + '/imageHelper' , id=str)
def imageHelper(id):
    return DataObject(Resource.Load(CHANNEL_LIST[id][u'thumb']) , 'image/png')
