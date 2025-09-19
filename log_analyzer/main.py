import os
import re
import sys
import yaml
import argparse

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
                    if re.search(indi_pattern, line_content):
                        pattern_counts[indi_pattern] += 1
    except FileNotFoundError as e:
        print(f"\nLog file not found at {config['log_file']}\nError: {e}\n\n")
        return {}
    except PermissionError as e:
        print(f"\nLog file seems to be inaccessible to your permissions...\nError: {e}\n\n")
        return{}
    return pattern_counts

def generate_report(pattern_counts, config):
    out_file_path = config['report_output']

    try:
        with open(out_file_path, 'w') as out_file:
            print("---    LOG ANALYSIS SUMMARY    ---", file=out_file)
            for pattern in pattern_counts:
                print(f"Found {pattern} :{pattern_counts[pattern]}", file=out_file)
        return out_file_path

    except IOError as e:
        print(f"\nThere was a problem attempting to write to the file path: {out_file_path}\nError: {e}\n\n")
        return None

    except PermissionError as e:        
        print(f"\nOutput file seems to be inaccessible to your permissions...\nError: {e}\n\n")
        return None

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Analyze log files for specific pattern.')
    parser.add_argument('--config', help='Points application to the full filepath of the specified configuration file.')
    args = parser.parse_args()

    if args.config:
        config_path = args.config
    else:
        current_wd = os.path.dirname(__file__)
        config_path = os.path.join(current_wd, '../config/config.yaml')

    config = load_config(config_path)

    if config is None:
        print("Error: Configuration failed to load. Exiting application now.")
        sys.exit(1)
    
    result_dict_text = analyze_log(config)
    if result_dict_text:
        generate_report(result_dict_text, config)
        print(f"Report generated at {config['report_output']}.")
