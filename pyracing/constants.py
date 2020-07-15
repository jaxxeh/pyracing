# _*_ coding: utf_8 _*_
import time
import math
import urllib.parse

# iRacing rounds down to the 5 minute mark - DO NOT CHANGE
now_unix_ms = int(math.floor(time.time() / 300) * 300) * 1000

# Context sites for the 2 types of endpoints
mSite = 'https://members.iracing.com/membersite/member'
mStats = 'https://members.iracing.com/memberstats/member'

# IRACING SERVICE URLS
URL_LOGIN = 'https://members.iracing.com/membersite/login.jsp'
URL_LOGIN2 = 'https://members.iracing.com/membersite/Login'
URL_LOGOUT = 'https://members.iracing.com/membersite/LogOut'
URL_HOME = 'https://members.iracing.com/membersite/member/Home.do'

# THE BIG ONES
URL_SUBS_RESULTS = (mSite + '/GetSubsessionResults')
URL_CURRENT_SEASONS = (mSite + '/GetSeasons')
URL_SEASON_STANDINGS = (mStats + '/GetSeasonStandings')
URL_SERIES_RACERESULTS = (mStats + '/GetSeriesRaceResults')

# RECENT HISTORICAL
URL_LASTRACE_STATS = (mStats + '/GetLastRacesStats')
URL_LAST_SERIES = (mStats + '/GetLastSeries')
URL_RESULTS = (mStats + '/GetResults')
URL_WORLD_RECORDS = (mStats + '/GetWorldRecords')

# UPCOMING SESSIONS
URL_SESSION_TIMES = (mSite + '/GetSessionTimes')
URL_NEXT_EVENT = (mSite + '/GetNextEvent')
URL_TOTALREGISTERED = (mSite + '/GetTotalSessionJoinedCountsBySeason')
URL_RACEGUIDE = (mSite + '/GetRaceGuide')
URL_ACTIVEOP_COUNT = (mSite + '/GetActiveOpenPracticeCount')

# DRIVER PROFILE STATS
URL_STATS_CHART = (mStats + '/GetChartData')
URL_CAREER_STATS = (mStats + '/GetCareerStats')
URL_YEARLY_STATS = (mStats + '/GetYearlyStats')
URL_PERSONAL_BESTS = (mStats + '/GetPersonalBests')

# RACE SPECIFIC RESULTS
URL_LAPS_SINGLE = (mSite + '/GetLaps')
URL_LAPS_ALL = (mSite + '/GetLapChart')

# UTILITY ?
URL_DRIVER_STATS = (mStats + '/GetDriverStats')
URL_MEM_SUBSESSID = (mSite + '/GetSubsessionForMember')
URL_CARS_DRIVEN = (mStats + '/GetCarsDriven')
URL_PRIVATE_RESULTS = (mStats + '/GetPrivateSessionResults')
URL_CAR_CLASS = (mSite + '/GetCarClassById')
URL_TICKER_SESSIONS = (mSite + '/GetTickerSessions')
URL_SEASON_FOR_SESSION = (mSite + '/GetSeasonForSession')
URL_ALL_SUBSESSIONS = (mSite + '/GetAllSubsessions')

# OTHER
URL_TEAM_STANDINGS = (mStats + 'GetTeamStandings?'
                               'raceWeekNum=-1'
                               '&seasonid=2621'
                               '&carClassId=67'
                               '&carId=-1')
URL_SESSION_TEAMS = (mStats + '/GetSessionTeams?'
                              'subSessionID=')

# ESSENTIALLY USELESS URLS

# Driver Status is the
URL_MY_RACERS = (mSite + '/GetDriverStatus')
URL_MEM_DIVISION = (mSite + '/GetMembersDivision')


class License:
    rookie = 1
    d_class = 2
    c_class = 3
    b_class = 4
    a_class = 5
    pro_class = 6
    pro_wc_class = 7

    def number_to_string(self, number):
        if number == self.rookie:
            return 'R'
        elif number == self.d_class:
            return 'D'
        elif number == self.c_class:
            return 'C'
        elif number == self.b_class:
            return 'B'
        elif number == self.a_class:
            return 'A'
        elif number == self.pro_class:
            return 'P'
        elif number == self.pro_wc_class:
            return 'P-DWC'
        else:
            return None


# LOCATIONS (AKA Country Code)


class Category:
    """Holds the index for each type of racing discipline
    """
    oval = 1
    road = 2
    dirt_oval = 3
    dirt_road = 4

    def number_to_string(self, number):
        if number == self.oval:
            return 'Oval'
        elif number == self.road:
            return 'Road'
        elif number == self.dirt_oval:
            return 'Dirt Oval'
        elif number == self.dirt_road:
            return 'Dirt Road'
        else:
            return None


class ChartType:
    """Holds the index for the charts available from stats_chart()
    """
    irating = 1
    ttrating = 2
    license_class = 3

    def number_to_string(self, number):
        if number == self.irating:
            return 'iRating'
        elif number == self.ttrating:
            return 'TTRating'
        elif number == self.license_class:
            return 'License Class'
        else:
            return None


class EventType:
    """Holds the index for the session event type
    """
    test = 1
    practice = 2
    qualify = 3
    time_trial = 4
    race = 5
    official = 6
    unofficial = 7

    def number_to_string(self, number):
        if number == self.test:
            return 'Test'
        elif number == self.practice:
            return 'Practice'
        elif number == self.qualify:
            return 'Qualify'
        elif number == self.time_trial:
            return 'Time Trial'
        elif number == self.race:
            return 'Race'
        elif number == self.official:
            return 'Official'
        elif number == self.unofficial:
            return 'Unofficial'
        else:
            return None


class SimSesNum:
    race = 0
    qualify = -1
    practice = -2


class IncFlags:
    clean = 0
    pitted = 2
    off_track = 4
    black_flag = 8
    car_reset = 16
    contact = 32
    car_contact = 64
    lost_control = 128
    discontinuity = 256
    interpolated_crossing = 512
    clock_smash = 1024
    tow = 2048

    def number_to_string(self, number):
        if number == self.clean:
            return 'Clean'
        elif number == self.pitted:
            return 'Pitted'
        elif number == self.off_track:
            return 'Off Track'
        elif number == self.black_flag:
            return 'Black Flag'
        elif number == self.car_reset:
            return 'Car Reset'
        elif number == self.contact:
            return 'Contact'
        elif number == self.lost_control:
            return 'Lost Control'
        elif number == self.discontinuity:
            return 'Discontinuity'
        elif number == self.interpolated_crossing:
            return 'Interpolated Crossing'
        elif number == self.clock_smash:
            return 'Clock Smash'
        elif number == self.tow:
            return 'Tow'
        else:
            return None


class Sort:
    """Holds the strings used for types of 'sort by'
    """
    irating = 'irating'
    start_time = 'start_time'
    champ_points = 'points'
    descending = 'desc'
    ascending = 'asc'
    session_name = 'sessionname'


# TODO Construct dictionary of seriesIDs from /GetSeasons
# TODO Construct dictionary of seasonIDs from /GetSeasons
# TODO Construct dictionary of carIDs


class SessionStatus:
    registered = 1
    do_not_join = 2
    ok_to_join = 3
    joined = 4
    assigned = 5
    withdrawn = 6
    rejected = 7


class CountryCodes:
    """Hold the string index of Country Codes that
    iRacing uses for seperating drivers into clubs
    """
    ALL = 'null',
    AFGHANISTAN = 'AF',
    ALAND_ISLANDS = 'AX',
    ALBANIA = 'AL',
    ALGERIA = 'DZ',
    AMERICAN_SAMOA = 'AS',
    ANDORRA = 'AD',
    ANGOLA = 'AO',
    ANGUILLA = 'AI',
    ANTARCTICA = 'AQ',
    ANTIGUA_AND_BARBUDA = 'AG',
    ARGENTINA = 'AR',
    ARMENIA = 'AM',
    ARUBA = 'AW',
    AUSTRALIA = 'AU',
    AUSTRIA = 'AT',
    AZERBAIJAN = 'AZ',
    BAHAMAS = 'BS',
    BAHRAIN = 'BH',
    BANGLADESH = 'BD',
    BARBADOS = 'BB',
    BELARUS = 'BY',
    BELGIUM = 'BE',
    BELIZE = 'BZ',
    BENIN = 'BJ',
    BERMUDA = 'BM',
    BHUTAN = 'BT',
    BOLIVIA_PLURINATIONAL_STATE_OF = 'BO',
    BOSNIA_AND_HERZEGOVINA = 'BA',
    BOTSWANA = 'BW',
    BOUVET_ISLAND = 'BV',
    BRAZIL = 'BR',
    BRITISH_INDIAN_OCEAN_TERRITORY = 'IO',
    BRUNEI_DARUSSALAM = 'BN',
    BULGARIA = 'BG',
    BURKINA_FASO = 'BF',
    BURUNDI = 'BI',
    CAMBODIA = 'KH',
    CAMEROON = 'CM',
    CANADA = 'CA',
    CAPE_VERDE = 'CV',
    CAYMAN_ISLANDS = 'KY',
    CENTRAL_AFRICAN_REPUBLIC = 'CF',
    CHAD = 'TD',
    CHILE = 'CL',
    CHINA = 'CN',
    CHRISTMAS_ISLAND = 'CX',
    COCOS_KEELING_ISLANDS = 'CC',
    COLOMBIA = 'CO',
    COMOROS = 'KM',
    CONGO = 'CG',
    CONGO_THE_DEMOCRATIC_REPUBLIC_OF_THE = 'CD',
    COOK_ISLANDS = 'CK',
    COSTA_RICA = 'CR',
    COTE_DIVOIRE = 'CI',
    CROATIA = 'HR',
    CUBA = 'CU',
    CYPRUS = 'CY',
    CZECH_REPUBLIC = 'CZ',
    DENMARK = 'DK',
    DJIBOUTI = 'DJ',
    DOMINICA = 'DM',
    DOMINICAN_REPUBLIC = 'DO',
    ECUADOR = 'EC',
    EGYPT = 'EG',
    EL_SALVADOR = 'SV',
    EQUATORIAL_GUINEA = 'GQ',
    ERITREA = 'ER',
    ESTONIA = 'EE',
    ETHIOPIA = 'ET',
    FALKLAND_ISLANDS_MALVINAS = 'FK',
    FAROE_ISLANDS = 'FO',
    FIJI = 'FJ',
    FINLAND = 'FI',
    FRANCE = 'FR',
    FRENCH_GUIANA = 'GF',
    FRENCH_POLYNESIA = 'PF',
    FRENCH_SOUTHERN_TERRITORIES = 'TF',
    GABON = 'GA',
    GAMBIA = 'GM',
    GEORGIA = 'GE',
    GERMANY = 'DE',
    GHANA = 'GH',
    GIBRALTAR = 'GI',
    GREECE = 'GR',
    GREENLAND = 'GL',
    GRENADA = 'GD',
    GUADELOUPE = 'GP',
    GUAM = 'GU',
    GUATEMALA = 'GT',
    GUERNSEY = 'GG',
    GUINEA = 'GN',
    GUINEA_BISSAU = 'GW',
    GUYANA = 'GY',
    HAITI = 'HT',
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = 'HM',
    HOLY_SEE_VATICAN_CITY_STATE = 'VA',
    HONDURAS = 'HN',
    HONG_KONG = 'HK',
    HUNGARY = 'HU',
    ICELAND = 'IS',
    INDIA = 'IN',
    INDONESIA = 'ID',
    IRAN_ISLAMIC_REPUBLIC_OF = 'IR',
    IRAQ = 'IQ',
    IRELAND = 'IE',
    ISLE_OF_MAN = 'IM',
    ISRAEL = 'IL',
    ITALY = 'IT',
    JAMAICA = 'JM',
    JAPAN = 'JP',
    JERSEY = 'JE',
    JORDAN = 'JO',
    KAZAKHSTAN = 'KZ',
    KENYA = 'KE',
    KIRIBATI = 'KI',
    KOREA_DEMOCRATIC_PEOPLES_REPUBLIC_OF = 'KP',
    KOREA_REPUBLIC_OF = 'KR',
    KUWAIT = 'KW',
    KYRGYZSTAN = 'KG',
    LAO_PEOPLES_DEMOCRATIC_REPUBLIC = 'LA',
    LATVIA = 'LV',
    LEBANON = 'LB',
    LESOTHO = 'LS',
    LIBERIA = 'LR',
    LIBYAN_ARAB_JAMAHIRIYA = 'LY',
    LIECHTENSTEIN = 'LI',
    LITHUANIA = 'LT',
    LUXEMBOURG = 'LU',
    MACAO = 'MO',
    MACEDONIA_THE_FORMER_YUGOSLAV_REPUBLIC_OF = 'MK',
    MADAGASCAR = 'MG',
    MALAWI = 'MW',
    MALAYSIA = 'MY',
    MALDIVES = 'MV',
    MALI = 'ML',
    MALTA = 'MT',
    MARSHALL_ISLANDS = 'MH',
    MARTINIQUE = 'MQ',
    MAURITANIA = 'MR',
    MAURITIUS = 'MU',
    MAYOTTE = 'YT',
    MEXICO = 'MX',
    MICRONESIA_FEDERATED_STATES_OF = 'FM',
    MOLDOVA_REPUBLIC_OF = 'MD',
    MONACO = 'MC',
    MONGOLIA = 'MN',
    MONTENEGRO = 'ME',
    MONTSERRAT = 'MS',
    MOROCCO = 'MA',
    MOZAMBIQUE = 'MZ',
    MYANMAR = 'MM',
    NAMIBIA = 'NA',
    NAURU = 'NR',
    NEPAL = 'NP',
    NETHERLANDS = 'NL',
    NETHERLANDS_ANTILLES = 'AN',
    NEW_CALEDONIA = 'NC',
    NEW_ZEALAND = 'NZ',
    NICARAGUA = 'NI',
    NIGER = 'NE',
    NIGERIA = 'NG',
    NIUE = 'NU',
    NORFOLK_ISLAND = 'NF',
    NORTHERN_MARIANA_ISLANDS = 'MP',
    NORWAY = 'NO',
    OMAN = 'OM',
    PAKISTAN = 'PK',
    PALAU = 'PW',
    PALESTINIAN_TERRITORY_OCCUPIED = 'PS',
    PANAMA = 'PA',
    PAPUA_NEW_GUINEA = 'PG',
    PARAGUAY = 'PY',
    PERU = 'PE',
    PHILIPPINES = 'PH',
    PITCAIRN = 'PN',
    POLAND = 'PL',
    PORTUGAL = 'PT',
    PUERTO_RICO = 'PR',
    QATAR = 'QA',
    REUNION = 'RE',
    ROMANIA = 'RO',
    RUSSIAN_FEDERATION = 'RU',
    RWANDA = 'RW',
    SAINT_BARTHELEMY = 'BL',
    SAINT_HELENA_ASCENSION_AND_TRISTAN_DA_CUNHA = 'SH',
    SAINT_KITTS_AND_NEVIS = 'KN',
    SAINT_LUCIA = 'LC',
    SAINT_MARTIN_FRENCH_PART = 'MF',
    SAINT_PIERRE_AND_MIQUELON = 'PM',
    SAINT_VINCENT_AND_THE_GRENADINES = 'VC',
    SAMOA = 'WS',
    SAN_MARINO = 'SM',
    SAO_TOME_AND_PRINCIPE = 'ST',
    SAUDI_ARABIA = 'SA',
    SENEGAL = 'SN',
    SERBIA = 'RS',
    SEYCHELLES = 'SC',
    SIERRA_LEONE = 'SL',
    SINGAPORE = 'SG',
    SLOVAKIA = 'SK',
    SLOVENIA = 'SI',
    SOLOMON_ISLANDS = 'SB',
    SOMALIA = 'SO',
    SOUTH_AFRICA = 'ZA',
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = 'GS',
    SPAIN = 'ES',
    SRI_LANKA = 'LK',
    SUDAN = 'SD',
    SURINAME = 'SR',
    SVALBARD_AND_JAN_MAYEN = 'SJ',
    SWAZILAND = 'SZ',
    SWEDEN = 'SE',
    SWITZERLAND = 'CH',
    SYRIAN_ARAB_REPUBLIC = 'SY',
    TAIWAN_PROVINCE_OF_CHINA = 'TW',
    TAJIKISTAN = 'TJ',
    TANZANIA_UNITED_REPUBLIC_OF = 'TZ',
    THAILAND = 'TH',
    TIMOR_LESTE = 'TL',
    TOGO = 'TG',
    TOKELAU = 'TK',
    TONGA = 'TO',
    TRINIDAD_AND_TOBAGO = 'TT',
    TUNISIA = 'TN',
    TURKEY = 'TR',
    TURKMENISTAN = 'TM',
    TURKS_AND_CAICOS_ISLANDS = 'TC',
    TUVALU = 'TV',
    UGANDA = 'UG',
    UKRAINE = 'UA',
    UNITED_ARAB_EMIRATES = 'AE',
    UNITED_KINGDOM = 'GB',
    UNITED_STATES = 'US',
    UNITED_STATES_MINOR_OUTLYING_ISLANDS = 'UM',
    URUGUAY = 'UY',
    UZBEKISTAN = 'UZ',
    VANUATU = 'VU',
    VENEZUELA_BOLIVARIAN_REPUBLIC_OF = 'VE',
    VIET_NAM = 'VN',
    VIRGIN_ISLANDS_BRITISH = 'VG',
    VIRGIN_ISLANDS_US = 'VI',
    WALLIS_AND_FUTUNA = 'WF',
    WESTERN_SAHARA = 'EH',
    YEMEN = 'YE',
    ZAMBIA = 'ZM',
    ZIMBABWE = 'ZW'


def parse_iracing_string(string):
    return urllib.parse.unquote(string).replace('+', ' ')