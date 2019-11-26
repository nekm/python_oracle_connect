import configparser

parser = configparser.ConfigParser()
parser.read('config/myconfig.ini')
for sect in parser.sections():
    if sect == 'oracle_prod':
        for k,v in parser.items(sect):
            if k == 'username' :
                username = v
            if k == 'password' :
                password = v
            if k == 'databasename' :
                databasename = v

  