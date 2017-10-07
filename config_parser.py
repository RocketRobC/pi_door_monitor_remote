import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file)

try:
    for settings in config:
        for k, v in config[settings].items():
            exec("%s = '%s'" % (k, v))
except:
    print('loading settings failed')
