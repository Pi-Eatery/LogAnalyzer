import PyYAML


def load_config(config_path):
    config_dict = {}
    try:
        with open('config_path', 'r') as config_object:
            config = yaml.safe_load(config_object)
    except if not config_object as e:
        print(f"The file you requested cannot be found...\nError: {e}")
        return None
    except if yaml.YAMLError as e:
        print(f"The file you requested seems to be malformed...\nError: {e}")
        return None
    if config:
        config_dict.expand(config)
        return config_dict
    return None

