# Port-Scanner-Simulator
A simple terminal-based port scanner simulator built with python

This project scans ports from 1 to 1024 and checks for open TCP and UDP ports on a target IPv4 address.

## What The Code Can Do

- IPv4 address validation
- TCP port scanning
- UDP port scanning
- Port timeout handling
- Scans ports 1–1024
- Displays detected open ports in the terminal

## Technologies

- Python
- Socket library

## How It Works

The program asks the user to enter an IPv4 address.

It then:

1. Validates the IP address.
2. Scans ports from 1 to 1024.
3. Attempts TCP connections to each port.
4. Sends UDP packets to each port.
5. Displays ports that respond or accept connections.
6. Completes the scan and displays the results.

!!The process would take 6 - 7 minutes to complete the scanning!!
