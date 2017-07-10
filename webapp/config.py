import urllib
from os import path 
#from webapp.app_config import SQLSERVER_PASSWORD, SQLSERVER_USERNAME

class Config(object):
    SECRET_KEY = '67a6dd4017a702fcf141038666d7faa9'
    RECAPTCHA_PUBLIC_KEY = "6LdKkQQTAAAAAEH0GFj7NLg5tGicaoOus7G9Q5Uw"    
    RECAPTCHA_PRIVATE_KEY = '6LdKkQQTAAAAAMYroksPTJ7pWhobYb88fTAcxcYn' 
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    testing=True
    SQLSERVER_PASSWORD = "password"
    SQLSERVER_USERNAME = "username"
    mssql_db = "mssql+pyodbc://localhost\\SQLEXPRESS/masteringflask?driver=SQL+Server+Native+Client+10.0"
    mssql_local = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=masteringflask;Trusted_Connection=yes'
    sqlite_conn = "sqlite:///masteringflask.sqlite"
    #SQLALCHEMY_DATABASE_URI = mssql_local
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    conDEBUG = "DRIVER={SQL Server};Database=MasteringFlask;SERVER=localhost\SQLEXPRESS;UID="+SQLSERVER_USERNAME+";PWD="+ SQLSERVER_PASSWORD
    conDEBUG = urllib.parse.quote_plus(conDEBUG)
    ## Uncomment below before doing flask migrate
    #conDEBUG = conDEBUG.replace('%','%%')
    conDEBUG = "mssql+pyodbc:///?odbc_connect=%s" % conDEBUG

    SQLALCHEMY_DATABASE_URI = sqlite_conn