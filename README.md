# entropypass
A Python-based tool to generate high-entropy passwords using Leet substitutions and entropy optimization.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

`entropypass` is a Python-based CLI tool designed to generate high-entropy passwords for secure authentication. It offers flexibility in generating passwords by specifying entropy levels, input files for bulk processing, and output files for saving generated passwords. This tool is perfect for individuals and developers who prioritize password security and cryptographic robustness.

---

## Features

- **Custom Entropy Levels:** Specify entropy levels between 0 and 200 (default: 60).
- **Bulk Processing:** Provide an input file containing multiple passwords and generate new passwords for each.
- **Command-Line Interface (CLI):** Easy-to-use command-line tool for generating and managing passwords.
- **Output File Support:** Save generated passwords directly to a specified file.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Tcookie47/entropypass.git
   cd entropypass
   ```

2. **Install the Package Locally:**
   ```bash
   python setup.py install
   ```

3. **OR Install via `pip`:**
   If uploaded to PyPI, install with:
   ```bash
   pip install entropypass
   ```

---

## Usage

### Command-Line Interface (CLI)
The tool provides several commands for password generation.

1. **Generate a Password (Default Mode):**
   ```bash
   entropypass [-e ENTROPY] <PASSWORD>
   ```
   Example:
   ```bash
   entropypass -e 75 MySecurePassword
   ```

2. **Process an Input File:**
   ```bash
   entropypass -i <INPUT_FILE> -o <OUTPUT_FILE> [-e ENTROPY]
   ```
   Example:
   ```bash
   entropypass -i input_passwords.txt -o output_passwords.txt -e 90
   ```

### Flags

| Flag               | Description                                                                                  | Default |
|--------------------|----------------------------------------------------------------------------------------------|---------|
| `-e`, `--entropy`  | Entropy level (0-200). A higher value increases randomness and complexity of the password.   | 60      |
| `-i`, `--input`    | Path to an input file containing passwords (1 per line).                                    | None    |
| `-o`, `--output`   | Path to an output file to save generated passwords.                                         | None    |

---

## Examples

1. **Default Entropy with Password:**
   ```bash
   entropypass MySecurePassword
   ```

2. **Custom Entropy with Password:**
   ```bash
   entropypass -e 120 MySecurePassword
   ```

3. **Bulk Processing with Input and Output Files:**
   ```bash
   entropypass -i passwords.txt -o new_passwords.txt -e 80
   ```

---

## Development

### Project Structure

```
High-Entropy-Password-Generator/
│
├── entropypass/              # Package folder
│   ├── __init__.py           # Makes this a package
│   ├── password_generator.py # Core logic
│   └── cli.py                # CLI implementation
│
├── setup.py                  # Metadata for packaging
├── README.md                 # Documentation
├── requirements.txt          # Dependencies
└── tests/                    # Not implimneted yet
```

### Running Tests
To ensure the project works as intended, you can run the test suite:

1. Install `pytest`:
   ```bash
   pip install pytest
   ```

2. Run Tests:
   ```bash
   pytest tests/
   ```

---

## Contributing

We welcome contributions! To get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

For issues, feature requests, or questions, please create an issue on the [GitHub repository](https://github.com/YourUsername/High-Entropy-Password-Generator/issues).

---

## Acknowledgments

This project was inspired by the need for stronger password management tools. Special thanks to the contributors and the open-source community for their support.

