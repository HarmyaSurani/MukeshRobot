class Config(object):
    LOGGER = True
    API_ID = "23386579" 
    API_HASH = "2accf0ba2d9160023ca22c4ce75dbcfd"
    TOKEN = "6249945411:AAFK0Ed1o88jSX9jzw5PfhsigOmfRoakfz8"  
    OWNER_ID= "6420416044"
    
    SUPPORT_CHAT = "-1001645761817" 
    START_IMG = "https://i.postimg.cc/DwsTK9DP/web-logo-no-bg.webp"
    EVENT_LOGS = ()
    MONGO_DB_URI= "mongodb+srv://nexusbytes:2024NexusBytes@linkshortify.kls74lp.mongodb.net/"
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
