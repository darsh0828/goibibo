from configparser import ConfigParser


# config = ConfigParser()
# config.read('config.ini')
# print(config.get("locator", "username"))
# print(config.get("basic info", "testurl"))

def readConfig(section, key):
    config = ConfigParser()
    config.read('/Volumes/Entertainme/Automation/goibiboNewProject/configurationData/conf.ini')
    return config.get(section, key)



