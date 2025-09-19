import os
import yaml

def load_config(config_path):
    try:
        with open(config_path, 'r') as config_object:
            config = yaml.safe_load(config_object)
    except yaml.YAMLError as e:
        print(f"\nThe .yaml file you requested seems to be malformed...\nError: {e}\n\n")
        return None
    except FileNotFoundError as e:
        print(f"\nThe file you requested cannot be found...\nError: {e}\n\n")
        return None
    return config

def analyze_log(config):
    pattern_counts = {}

    for indi_pattern in config['patterns']:
        pattern_counts[indi_pattern] = 0

    log_file_path = config['log_file']
    try:
        with open(log_file_path, 'r') as readable_logs:
            for line_number, line_content in enumerate(readable_logs, 1):
                for indi_pattern in config['patterns']:
                    if indi_pattern in line_content:
                        pattern_counts[indi_pattern] += 1
    except FileNotFoundError as e:
        print(f"Log file not found at {config['log_file']}")
        return {}
    return pattern_counts

if __name__ == "__main__":
    current_wd = os.path.dirname(__file__)
    config_dir_path = os.path.join(current_wd, '../config/')
    config_file_path = os.path.join(config_dir_path, 'config.yaml')
    config_dict_final = load_config(config_file_path)
    load_config(os.path.join(config_dir_path, 'nonexistent'))
    load_config(os.path.join(config_dir_path, 'broken_config.yaml'))

    result_dict_text = analyze_log(config_dict_final)

    print(f"\nThese are the current config options:\n---\n{config_dict_final}\n\n")

    print(f"\nThese are the counts of searched patterns found:\n---\n{result_dict_text}")
