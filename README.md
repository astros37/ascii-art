# ASCII Art Generator

A simple Python script that generates ASCII art from text and saves it to a file or displays it in the console.

## Features
- Converts input text into beautiful ASCII art.
- Saves the generated ASCII art to a file (`banner.txt`).
- Supports different fonts via the `pyfiglet` library.

## Requirements
- Python 3.x
- `pyfiglet` library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ascii-art-generator.git
   cd ascii-art-generator
   ```

2. Install the required library:
   ```bash
   pip install pyfiglet
   ```

## Usage
1. Run the script:
   ```bash
   python ascii_art_generator.py
   ```

2. Enter the text you want to convert to ASCII art when prompted.

3. View the generated ASCII art in the console or in the `banner.txt` file.

## Example Output
```text
    _____       _ _     _    
   |  _  |     (_) |   | |   
   | | | |_   _ _| | __| | __
   | | | | | | | | |/ _` |/ _\
   \ \_/ / |_| | | | (_| |  __/
    \___/ \__,_|_|_|\__,_|\___|
```

## Customization
You can customize the font used in the ASCII art by modifying this line in the script:
```python
figlet = Figlet(font='slant')
```
Replace `'slant'` with any supported font from the [pyfiglet fonts list](https://github.com/pwaller/pyfiglet/blob/master/pyfiglet/fonts.md).

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

