# _*_ coding: utf_8 _*_
import time
import math

ALL = -1
# Entries per page. This is the ammount set
# in iRacing site. We shouldn't increase it.
NUM_ENTRIES = 25

# Minimum time in seconds between two consecutive requests to iRacing site
# (we don't want to flood/abuse the service).
# I'm not sure about the minimum value for this, I'll have to ask a dev.
WAIT_TIME = 0.3

IRATING_OVAL_CHART = 1
IRATING_ROAD_CHART = 2

RACE_TYPE_OVAL = 1
RACE_TYPE_ROAD = 2

LIC_ROOKIE = 1
LIC_D = 2
LIC_C = 3
LIC_B = 4
LIC_A = 5
LIC_PRO = 6
LIC_PRO_WC = 7

SORT_IRATING = 'irating'
SORT_TIME = 'start_time'
SORT_POINTS = 'points'
ORDER_DESC = 'desc'
ORDER_ASC = 'asc'

# List of session eventType
EVENT_TEST = 1
EVENT_PRACTICE = 2
EVENT_QUALY = 3
EVENT_TTRIAL = 4
EVENT_RACE = 5
EVENT_OFFICIAL = 6
EVENT_UNOFFICIAL = 7

# INCIDENT FLAGS
# These are used in the laps data
FLAG_PITTED = 2
FLAG_OFF_TRACK = 4
FLAG_BLACK_FLAG = 8
FLAG_CAR_RESET = 16
FLAG_CONTACT = 32
FLAG_CAR_CONTACT = 64
FLAG_LOST_CONTROL = 128
FLAG_DISCONTINUITY = 256
FLAG_INTERPOLATED_CROSSING = 512
FLAG_CLOCK_SMASH = 1024
FLAG_TOW = 2048

INC_FLAGS = {
    0: "clean",
    2: "pitted",
    4: "off track",
    8: "black flag",
    16: "car reset",
    32: "contact",
    64: "car contact",
    128: "lost control",
    256: "discontinuity",
    512: "interpolated crossing",
    1024: "clock smash",
    2048: "tow"
}

# Initialized Variables for URLS (WiP)
# TODO Polish this up / Better naming
custid = 435144
category = -1
carid = -1
trackid = -1
seasonID = 2866
subsession = 33204934
sessnum = 133411985
seasonquarter = 2
year = 2020
series = 284
event = 5
# iRacing rounds down to the 5 minute mark - Do not change
unixMs = int(math.floor(time.time()/300)*300)*1000
quarter = 2
raceweek = -1
carclass = -1
cDiv = -1  # Club Division

mSite = 'https://members.iracing.com/membersite/member'
mStats = 'https://members.iracing.com/memberstats/member'

# IRACING SERVICE URLS
URL_IRACING_LOGIN = 'https://members.iracing.com/membersite/login.jsp'
URL_IRACING_LOGIN2 = 'https://members.iracing.com/membersite/Login'
URL_IRACING_LOGOUT = 'https://members.iracing.com/membersite/LogOut'
URL_IRACING_HOME = 'https://members.iracing.com/membersite/member/Home.do'

# THE BIG ONES
URL_SSESS_RESULTS = (mSite + '/GetSubsessionResults?'
                             f'subsessionID={subsession}'
                             f'&custid={custid}')
URL_CURRENT_SEASONS = (mSite + '/GetSeasons?' # TODO Shorten
                           'onlyActive=0'
                           '&fields=year,quarter,seriesshortname,seriesid,active,catid,licenseeligible,islite,carclasses,tracks,start,end,cars,raceweek,category,serieslicgroupid,carid,seasonid,seriesid')
URL_SEASON_STANDINGS = (mStats + '/GetSeasonStandings?'
                                 f'seasonid={seasonID}'
                                 f'&carclassid={carclass}'
                                 '&clubid=-1'
                                 f'&raceweek={raceweek}'
                                 f'&division={cDiv}'
                                 '&start=1'
                                 f'&end={NUM_ENTRIES}'
                                 '&sort=points'
                                 '&order=desc')
URL_SERIES_RACERESULTS = (mStats + '/GetSeriesRaceResults'
                                   f'?seasonid={seasonID}'
                                   f'&raceweek={raceweek}')


# RECENT HISTORICAL
URL_LASTRACE_STATS = (mStats + '/GetLastRacesStats?'
                               f'custid={custid}')
URL_LAST_SERIES = (mStats + '/GetLastSeries?'
                            f'custid={custid}')
URL_RESULTS_ARCHIVE = (mStats + '/GetResults?'
                                f'custid={custid}'  # custid required
                                '&showraces=1'
                                '&showquals=0'
                                '&showtts=0'
                                '&showops=0'
                                '&showofficial=1'
                                '&showunofficial=0'
                                '&showrookie=1'
                                '&showclassd=1'
                                '&showclassc=1'
                                '&showclassb=1'
                                '&showclassa=1'
                                '&showpro=1'
                                '&showprowc=1'
                                '&lowerbound=0'
                                f'&upperbound={NUM_ENTRIES}'
                                '&sort=start_time'
                                '&order=desc'
                                '&format=json'
                                '&category%5B%5D=1'
                                '&category%5B%5D=2'
                                '&category%5B%5D=3'
                                '&category%5B%5D=4'
                                f'&seasonyear={year}'
                                f'&seasonquarter={quarter}'
                                f'&raceweek={raceweek}'
                                f'&trackid={trackid}'
                                f'&carclassid={carclass}'
                                f'&carid={carid}')
URL_GET_WORLDRECORD = (mStats + '/GetWorldRecords?'
                                f'seasonyear={year}'
                                f'&seasonquarter={seasonquarter}'
                                f'&carid={carid}'
                                f'&trackid={trackid}'
                                f'&custid={custid}'
                                '&format=json'
                                '&upperbound=1')


# UPCOMING SESSIONS
URL_SESSION_TIMES = (mSite + '/GetSessionTimes?'
                             f'season={seasonID}')
URL_GET_NEXTEVENT = (mSite + '/GetNextEvent?'
                             f'seriesID={series}'
                             f'&evtType={event}'
                             f'&date={unixMs}')
URL_GET_TOTALREGISTERED = (mSite + '/GetTotalSessionJoinedCountsBySeason')
URL_GET_RACEGUIDE = (mSite + '/GetRaceGuide?'
                             f'at={unixMs}'
                             '&showRookie=1'
                             '&showClassD=1'
                             '&showClassC=1'
                             '&showClassB=1'
                             '&showClassA=1'
                             '&showPro=1'
                             '&showProWC=1'
                             '&showOval=1'
                             '&showRoad=1'
                             '&showDirtOval=1'
                             '&showDirtRoad=1'
                             '&hideNotFixedSetup=0'
                             '&hideNotMultiClass=0'
                             '&meetsMPR=0'
                             '&hideUnpopulated=0'
                             '&hideIneligible=0'
                             '&showOfficial=1')
URL_ACTIVEOP_COUNT = (mSite + '/GetActiveOpenPracticeCount?'
                              'maxcount=250'
                              '&include_empty=y'
                              '&excludeLite=0'
                              f'&custid={custid}?')


# DRIVER PROFILE STATS
URL_STATS_CHART = (mStats + '/GetChartData?'
                            f'custId={custid}'
                            f'&catId={category}'
                            '&chartType=1')
URL_CAREER_STATS = (mStats + '/GetCareerStats?'
                             f'custid={custid}')
URL_YEARLY_STATS = (mStats + '/GetYearlyStats?'
                             f'custid={custid}')
URL_PERSONAL_BEST = (mStats + '/GetPersonalBests?'
                              f'&carid={carid}'
                              f'&custid={custid}')


# RACE SPECIFIC RESULTS
URL_GET_LAPS_SINGLE = (mSite + '/GetLaps?'
                               f'subsessionid={subsession}'
                               f'&groupid={custid}'
                               f'&simsessnum={sessnum}')
URL_GET_LAPS_ALL = (mSite + '/GetLapChart?'
                            f'subsessionid={subsession}'
                            '&carclassid=-1')


# UTILITY ?
URL_DRIVER_STATS = (mStats + '/GetDriverStats?'
                             'search=null'
                             '&friend=-1'
                             '&watched=-1'
                             '&recent=-1'
                             '&country=null'
                             '&category=1'
                             '&classlow=-1'
                             '&classhigh=-1'
                             '&iratinglow=-1'
                             '&iratinghigh=-1'
                             '&ttratinglow=-1'
                             '&ttratinghigh=-1'
                             '&avgstartlow=-1'
                             '&avgstarthigh=-1'
                             '&avgfinishlow=-1'
                             '&avgfinishhigh=-1'
                             '&avgpointslow=-1'
                             '&avgpointshigh=-1'
                             '&avgincidentslow=-1'
                             '&avgincidentshigh=-1'
                             '&custid=435144'
                             '&lowerbound=1'
                             '&upperbound=25'
                             '&sort=irating'
                             '&order=desc'
                             '&active=1')
URL_GET_SSID = (mSite + '/GetSubsessionForMember?'
                        f'sessionID={sessnum}')
URL_CARS_DRIVEN = (mStats + '/GetCarsDriven?'
                            f'custid={custid}')
URL_HOSTED_RESULTS = (mStats + '/GetPrivateSessionResults')



# ESSENTIALLY USELESS URLS

# DriverCounts and Status is iRacing 'friends list'
# Unable to return results with "drivername" , replaced with:
URL_DRIVER_STATUS = (mSite + '/GetDriverStatus?'
                             'friends=1'
                             '&studied=1'
                             '&blacklisted=1')
URL_DRIVER_COUNTS = (mSite + '/GetDriverCounts')
URL_GET_MDIVISION = (mSite + '/GetMembersDivision?'
                             f'seasonid={seasonID}'
                             f'&custid={custid}'
                             '&pointstype=race')


# THESE URLS DO NOT RETURN JSON
# THESE URLS DO NOT RETURN JSON
# THESE URLS DO NOT RETURN JSON

URL_GET_EVENTRESULTS = (mSite + '/EventResult.do?'
                                f'subsessionid={subsession}')
URL_GET_EVENTRESULTS_CSV = (mSite + '/GetEventResultsAsCSV?'
                                    f'subsessionid={subsession}'
                                    f'&simsesnum={sessnum}'
                                    '&includeSummary=1')
URL_CURRENT_SERIES = (mSite + '/Series.do')
URL_SELECT_SERIES = (mSite + '/SelectSeries.do?'
                             f'season={seasonID}'
                             '&view=undefined'
                             '&nocache=%s')

# Doesn't work. Loads a page but redirects back to home
URL_GET_PASTSERIES = (mSite + '/PreviousSeasons.do')
URL_SEASON_STANDINGS2 = (mSite + '/statsseries.jsp')





HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Apple\
        WebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17',
    'Referer': 'https://members.iracing.com/membersite/login.jsp',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,'
              'application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Cache-Control': 'max-age=0',
    'Host': 'members.iracing.com',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Origin': 'members.iracing.com',
    'Accept-Language': 'en-US,en;q=0.8'
}


# LOCATIONS
LOC_ALL = 'null'
LOC_AFGHANISTAN = 'AF'
LOC_ALAND_ISLANDS = 'AX'
LOC_ALBANIA = 'AL'
LOC_ALGERIA = 'DZ'
LOC_AMERICAN_SAMOA = 'AS'
LOC_ANDORRA = 'AD'
LOC_ANGOLA = 'AO'
LOC_ANGUILLA = 'AI'
LOC_ANTARCTICA = 'AQ'
LOC_ANTIGUA_AND_BARBUDA = 'AG'
LOC_ARGENTINA = 'AR'
LOC_ARMENIA = 'AM'
LOC_ARUBA = 'AW'
LOC_AUSTRALIA = 'AU'
LOC_AUSTRIA = 'AT'
LOC_AZERBAIJAN = 'AZ'
LOC_BAHAMAS = 'BS'
LOC_BAHRAIN = 'BH'
LOC_BANGLADESH = 'BD'
LOC_BARBADOS = 'BB'
LOC_BELARUS = 'BY'
LOC_BELGIUM = 'BE'
LOC_BELIZE = 'BZ'
LOC_BENIN = 'BJ'
LOC_BERMUDA = 'BM'
LOC_BHUTAN = 'BT'
LOC_BOLIVIA_PLURINATIONAL_STATE_OF = 'BO'
LOC_BOSNIA_AND_HERZEGOVINA = 'BA'
LOC_BOTSWANA = 'BW'
LOC_BOUVET_ISLAND = 'BV'
LOC_BRAZIL = 'BR'
LOC_BRITISH_INDIAN_OCEAN_TERRITORY = 'IO'
LOC_BRUNEI_DARUSSALAM = 'BN'
LOC_BULGARIA = 'BG'
LOC_BURKINA_FASO = 'BF'
LOC_BURUNDI = 'BI'
LOC_CAMBODIA = 'KH'
LOC_CAMEROON = 'CM'
LOC_CANADA = 'CA'
LOC_CAPE_VERDE = 'CV'
LOC_CAYMAN_ISLANDS = 'KY'
LOC_CENTRAL_AFRICAN_REPUBLIC = 'CF'
LOC_CHAD = 'TD'
LOC_CHILE = 'CL'
LOC_CHINA = 'CN'
LOC_CHRISTMAS_ISLAND = 'CX'
LOC_COCOS_KEELING_ISLANDS = 'CC'
LOC_COLOMBIA = 'CO'
LOC_COMOROS = 'KM'
LOC_CONGO = 'CG'
LOC_CONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE = 'CD'
LOC_COOK_ISLANDS = 'CK'
LOC_COSTA_RICA = 'CR'
LOC_COTE_DIVOIRE = 'CI'
LOC_CROATIA = 'HR'
LOC_CUBA = 'CU'
LOC_CYPRUS = 'CY'
LOC_CZECH_REPUBLIC = 'CZ'
LOC_DENMARK = 'DK'
LOC_DJIBOUTI = 'DJ'
LOC_DOMINICA = 'DM'
LOC_DOMINICAN_REPUBLIC = 'DO'
LOC_ECUADOR = 'EC'
LOC_EGYPT = 'EG'
LOC_EL_SALVADOR = 'SV'
LOC_EQUATORIAL_GUINEA = 'GQ'
LOC_ERITREA = 'ER'
LOC_ESTONIA = 'EE'
LOC_ETHIOPIA = 'ET'
LOC_FALKLAND_ISLANDS_MALVINAS = 'FK'
LOC_FAROE_ISLANDS = 'FO'
LOC_FIJI = 'FJ'
LOC_FINLAND = 'FI'
LOC_FRANCE = 'FR'
LOC_FRENCH_GUIANA = 'GF'
LOC_FRENCH_POLYNESIA = 'PF'
LOC_FRENCH_SOUTHERN_TERRITORIES = 'TF'
LOC_GABON = 'GA'
LOC_GAMBIA = 'GM'
LOC_GEORGIA = 'GE'
LOC_GERMANY = 'DE'
LOC_GHANA = 'GH'
LOC_GIBRALTAR = 'GI'
LOC_GREECE = 'GR'
LOC_GREENLAND = 'GL'
LOC_GRENADA = 'GD'
LOC_GUADELOUPE = 'GP'
LOC_GUAM = 'GU'
LOC_GUATEMALA = 'GT'
LOC_GUERNSEY = 'GG'
LOC_GUINEA = 'GN'
LOC_GUINEA_BISSAU = 'GW'
LOC_GUYANA = 'GY'
LOC_HAITI = 'HT'
LOC_HEARD_ISLAND_AND_MCDONALD_ISLANDS = 'HM'
LOC_HOLY_SEE_VATICAN_CITY_STATE = 'VA'
LOC_HONDURAS = 'HN'
LOC_HONG_KONG = 'HK'
LOC_HUNGARY = 'HU'
LOC_ICELAND = 'IS'
LOC_INDIA = 'IN'
LOC_INDONESIA = 'ID'
LOC_IRAN_ISLAMIC_REPUBLIC_OF = 'IR'
LOC_IRAQ = 'IQ'
LOC_IRELAND = 'IE'
LOC_ISLE_OF_MAN = 'IM'
LOC_ISRAEL = 'IL'
LOC_ITALY = 'IT'
LOC_JAMAICA = 'JM'
LOC_JAPAN = 'JP'
LOC_JERSEY = 'JE'
LOC_JORDAN = 'JO'
LOC_KAZAKHSTAN = 'KZ'
LOC_KENYA = 'KE'
LOC_KIRIBATI = 'KI'
LOC_KOREA_DEMOCRATIC_PEOPLES_REPUBLIC_OF = 'KP'
LOC_KOREA_REPUBLIC_OF = 'KR'
LOC_KUWAIT = 'KW'
LOC_KYRGYZSTAN = 'KG'
LOC_LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 'LA'
LOC_LATVIA = 'LV'
LOC_LEBANON = 'LB'
LOC_LESOTHO = 'LS'
LOC_LIBERIA = 'LR'
LOC_LIBYAN_ARAB_JAMAHIRIYA = 'LY'
LOC_LIECHTENSTEIN = 'LI'
LOC_LITHUANIA = 'LT'
LOC_LUXEMBOURG = 'LU'
LOC_MACAO = 'MO'
LOC_MACEDONIA_THE_FORMER_YUGOSLAV_REPUBLIC_OF = 'MK'
LOC_MADAGASCAR = 'MG'
LOC_MALAWI = 'MW'
LOC_MALAYSIA = 'MY'
LOC_MALDIVES = 'MV'
LOC_MALI = 'ML'
LOC_MALTA = 'MT'
LOC_MARSHALL_ISLANDS = 'MH'
LOC_MARTINIQUE = 'MQ'
LOC_MAURITANIA = 'MR'
LOC_MAURITIUS = 'MU'
LOC_MAYOTTE = 'YT'
LOC_MEXICO = 'MX'
LOC_MICRONESIA_FEDERATED_STATES_OF = 'FM'
LOC_MOLDOVA_REPUBLIC_OF = 'MD'
LOC_MONACO = 'MC'
LOC_MONGOLIA = 'MN'
LOC_MONTENEGRO = 'ME'
LOC_MONTSERRAT = 'MS'
LOC_MOROCCO = 'MA'
LOC_MOZAMBIQUE = 'MZ'
LOC_MYANMAR = 'MM'
LOC_NAMIBIA = 'NA'
LOC_NAURU = 'NR'
LOC_NEPAL = 'NP'
LOC_NETHERLANDS = 'NL'
LOC_NETHERLANDS_ANTILLES = 'AN'
LOC_NEW_CALEDONIA = 'NC'
LOC_NEW_ZEALAND = 'NZ'
LOC_NICARAGUA = 'NI'
LOC_NIGER = 'NE'
LOC_NIGERIA = 'NG'
LOC_NIUE = 'NU'
LOC_NORFOLK_ISLAND = 'NF'
LOC_NORTHERN_MARIANA_ISLANDS = 'MP'
LOC_NORWAY = 'NO'
LOC_OMAN = 'OM'
LOC_PAKISTAN = 'PK'
LOC_PALAU = 'PW'
LOC_PALESTINIAN_TERRITORY_OCCUPIED = 'PS'
LOC_PANAMA = 'PA'
LOC_PAPUA_NEW_GUINEA = 'PG'
LOC_PARAGUAY = 'PY'
LOC_PERU = 'PE'
LOC_PHILIPPINES = 'PH'
LOC_PITCAIRN = 'PN'
LOC_POLAND = 'PL'
LOC_PORTUGAL = 'PT'
LOC_PUERTO_RICO = 'PR'
LOC_QATAR = 'QA'
LOC_REUNION = 'RE'
LOC_ROMANIA = 'RO'
LOC_RUSSIAN_FEDERATION = 'RU'
LOC_RWANDA = 'RW'
LOC_SAINT_BARTHELEMY = 'BL'
LOC_SAINT_HELENA_ASCENSION_AND_TRISTAN_DA_CUNHA = 'SH'
LOC_SAINT_KITTS_AND_NEVIS = 'KN'
LOC_SAINT_LUCIA = 'LC'
LOC_SAINT_MARTIN_FRENCH_PART = 'MF'
LOC_SAINT_PIERRE_AND_MIQUELON = 'PM'
LOC_SAINT_VINCENT_AND_THE_GRENADINES = 'VC'
LOC_SAMOA = 'WS'
LOC_SAN_MARINO = 'SM'
LOC_SAO_TOME_AND_PRINCIPE = 'ST'
LOC_SAUDI_ARABIA = 'SA'
LOC_SENEGAL = 'SN'
LOC_SERBIA = 'RS'
LOC_SEYCHELLES = 'SC'
LOC_SIERRA_LEONE = 'SL'
LOC_SINGAPORE = 'SG'
LOC_SLOVAKIA = 'SK'
LOC_SLOVENIA = 'SI'
LOC_SOLOMON_ISLANDS = 'SB'
LOC_SOMALIA = 'SO'
LOC_SOUTH_AFRICA = 'ZA'
LOC_SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 'GS'
LOC_SPAIN = 'ES'
LOC_SRI_LANKA = 'LK'
LOC_SUDAN = 'SD'
LOC_SURINAME = 'SR'
LOC_SVALBARD_AND_JAN_MAYEN = 'SJ'
LOC_SWAZILAND = 'SZ'
LOC_SWEDEN = 'SE'
LOC_SWITZERLAND = 'CH'
LOC_SYRIAN_ARAB_REPUBLIC = 'SY'
LOC_TAIWAN_PROVINCE_OF_CHINA = 'TW'
LOC_TAJIKISTAN = 'TJ'
LOC_TANZANIA_UNITED_REPUBLIC_OF = 'TZ'
LOC_THAILAND = 'TH'
LOC_TIMOR_LESTE = 'TL'
LOC_TOGO = 'TG'
LOC_TOKELAU = 'TK'
LOC_TONGA = 'TO'
LOC_TRINIDAD_AND_TOBAGO = 'TT'
LOC_TUNISIA = 'TN'
LOC_TURKEY = 'TR'
LOC_TURKMENISTAN = 'TM'
LOC_TURKS_AND_CAICOS_ISLANDS = 'TC'
LOC_TUVALU = 'TV'
LOC_UGANDA = 'UG'
LOC_UKRAINE = 'UA'
LOC_UNITED_ARAB_EMIRATES = 'AE'
LOC_UNITED_KINGDOM = 'GB'
LOC_UNITED_STATES = 'US'
LOC_UNITED_STATES_MINOR_OUTLYING_ISLANDS = 'UM'
LOC_URUGUAY = 'UY'
LOC_UZBEKISTAN = 'UZ'
LOC_VANUATU = 'VU'
LOC_VENEZUELA_BOLIVARIAN_REPUBLIC_OF = 'VE'
LOC_VIET_NAM = 'VN'
LOC_VIRGIN_ISLANDS_BRITISH = 'VG'
LOC_VIRGIN_ISLANDS_US = 'VI'
LOC_WALLIS_AND_FUTUNA = 'WF'
LOC_WESTERN_SAHARA = 'EH'
LOC_YEMEN = 'YE'
LOC_ZAMBIA = 'ZM'
LOC_ZIMBABWE = 'ZW'

# List of SIDs (SeriesID) listed in order from /GetRaceGuide
# Note: removed any dashs due to errors
SID_Carburetor_Cup = 116
SID_DIRTcar_Street_Stock_Series_Fixed = 290
SID_Fanatec_Global_Mazda_MX5_Cup = 139
SID_Fanatec_Street_Stock_Series_R = 182
SID_iRacing_Advanced_Legends_Cup = 32
SID_iRacing_Dirt_Legends_Cup = 315
SID_PickUp_Cup = 259
SID_Pro_2_Lite_Truck_Championship = 387
SID_Rookie_iRacing_Rallycross_Series = 326
SID_Sling_Mud_for_Fun_Sprint_Cars = 303
SID_Trak_Racer_Dallara_Dash = 258
SID_BMW_120_Challenge_Fixed = 397
SID_BMW_SIM_120_Cup = 400
SID_DIRTcar_Limited_Late_Model_Series = 291
SID_Fanatec_DIRTcar_305_Sprint_Car_Series = 292
SID_Fanatec_Global_Challenge = 210
SID_iRacing_ARCA_Menards_Series = 167
SID_iRacing_Formula_Renault_20 = 269
SID_iRacing_Late_Model_Tour = 33
SID_iRacing_Rallycross_Series = 325
SID_iRacing_Spec_Racer_Ford_Challenge = 63
SID_Lucas_Oil_Off_Road_Racing_Pro_4_Series = 391
SID_NASCAR_SK_Modified_Weekly_Series = 45
SID_Nurburgring_Endurance_Championship = 275
SID_Pure_Driving_School_Formula_Sprint = 384
SID_Ruf_GT3_Challenge = 277
SID_SimLab_Production_Car_Challenge = 112
SID_Skip_Barber_Race_Series = 34
SID_Advanced_Mazda_MX5_Cup_Series = 231
SID_DIRTcar_360_Sprint_Car_Series_ = 305
SID_DIRTcar_Class_C_Street_Stock_Series_Fixed = 311
SID_DIRTcar_Pro_Late_Model_Series_ = 306
SID_Fanatec_GT_Challenge = 278
SID_Grand_Prix_Legends = 201
SID_IMSA_Michelin_Pilot_Challenge = 386
SID_IMSA_Sportscar_Championship = 227
SID_Indy_Pro_2000_Championship = 414
SID_IndyCar_iRacing_Series = 374
SID_IndyCar_Series_Oval_Fixed = 165
SID_iRacing_Dirt_Midget_Cup = 327
SID_iRacing_Endurance_Series = 408
SID_iRacing_F3_Championship = 358
SID_iRacing_Street_Stock_Series_C = 190
SID_iRacing_Super_Late_Model_Series = 223
SID_iRacing_Super_Late_Model_Series_Fixed = 416
SID_Kamel_GT_Championship_ = 285
SID_Lucas_Oil_Off_Road_Racing_Pro_2_Series = 378
SID_NASCAR_iRacing_Class_C = 47
SID_NASCAR_iRacing_Class_C_Fixed = 164
SID_NASCAR_iRacing_Series_Fixed = 207
SID_NASCAR_iRacing_Series_Open = 229
SID_NASCAR_iRacing_Tour_Modified_Series = 102
SID_NASCAR_iRacing_Tour_Modified_Series_Fixed = 417
SID_NASCAR_Legends_Series = 413
SID_Porsche_Esports_Sprint_Challenge = 410
SID_Porsche_iRacing_Cup = 299
SID_Radical_Racing_Challenge_C = 74
SID_Supercars_Series = 399
SID_Supercars_Series_Australian_Server_Only = 405
SID_USAC_360_Sprint_Car_Series = 310
SID_VRS_GT_Endurance_Series = 237
SID_World_of_Outlaws_Late_Model_Series_Fixed = 369
SID_AMSOIL_USAC_Sprint_Car = 309
SID_Classic_Lotus_Grand_Prix = 65
SID_DIRTcar_UMP_Modified_Series = 316
SID_IndyCar_Series_Road = 133
SID_iRacing_Endurance_Le_Mans_Series = 331
SID_iRacing_Formula_35_Championship = 359
SID_iRacing_Le_Mans_Series = 330
SID_iRacing_Silver_Crown_Cup = 53
SID_iRacing_Sprint_Car_Cup = 131
SID_NASCAR_iRacing_Class_B = 62
SID_NASCAR_iRacing_Class_B_Fixed = 103
SID_VRS_GT_Sprint_Series = 228
SID_World_of_Outlaws_Late_Model_Series_ = 308
SID_World_of_Outlaws_Sprint_Car_Series = 307
SID_iRacing_Grand_Prix_Series = 260
SID_NASCAR_iRacing_Class_A = 58
SID_NASCAR_iRacing_Class_A_Fixed_ = 191
SID_NASCAR_Road_to_Pro = 328
SID_Porsche_TAG_Heuer_Esports_Supercup = 409
SID_WoO_Late_Model_WC_Series = 339
SID_eNASCAR_CocaCola_Series = 402
