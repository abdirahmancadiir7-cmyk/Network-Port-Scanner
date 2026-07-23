# Network Port Scanner

A Python-based TCP port scanner that scans a range of ports on a target host. This project was created to learn socket programming, networking fundamentals, and basic port scanning techniques.

## Features

- Scan a range of TCP ports
- Detect open ports
- Fast socket timeout
- Display scan start and finish time
- Lightweight and easy to use

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/abdirahmancadiir7-cmyk/network-port-scanner.git
```

Move into the project directory:

```bash
cd network-port-scanner
```

Run the scanner:

```bash
python3 scanner.py
```

## Example

```text
Enter Target IP or Host:
scanme.nmap.org

Start Port:
20

End Port:
100

[OPEN] Port 22
[OPEN] Port 80
```

## Project Files

- `scanner.py` — Main scanner
- `README.md` — Documentation
- `requirements.txt` — Dependencies
- `.gitignore` — Git ignored files
- `LICENSE` — MIT License

## Future Improvements

- Multi-threaded scanning
- Service detection
- Banner grabbing
- Export scan reports
- Command-line arguments

## License

This project is licensed under the MIT License.
