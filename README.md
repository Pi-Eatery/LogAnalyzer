# Log Analyzer
A simple log analyzer tool that processes log files and generates summary reports.

## Features
- Parse log files in YAML format.
- Generate summary reports in a clean and readable format.
- Easy to use command-line interface.
- Easily switchable configuration file path.
- Error handling for missing or invalid log files.
- Uses ReGex for flexible log parsing.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/Pi-Eatery/LogAnalyzer.git .
    ```
2. Navigate to the project directory:
    ```
    cd LogAnalyzer
    ```
3. (Optional) Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Instructions
1. Ensure you have Python 3.x installed on your machine.
2. Follow the installation steps above to clone the repository.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
4. Run the log analyzer:
   ```
   python log_analyzer/main.py --config config.yaml 
   ## OR
   python log_analyzer/main.py
   ```