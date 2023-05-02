#!/usr/bin/env python3
''' Script to print basic labels to the Brady BBP12 printer

Example:
python print.py <text to print>
python print.py Hello I am a label

Author: Evan Thomas <evan.thomas@epfl.ch>

'''

import socket
import sys


HOST: str = ""    # Add the IP of the printer here
PORT: int = 9100  # The same for the port

# Coordinates to start printing from
X_START = -400
Y_START = 100


def main(
    input_text: str
) -> None:
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((HOST, PORT))  # Connecting to host
        mysocket.send(
            f'''
            ^XA^FT{X_START},{Y_START}
            ^A0N,50,50
            ^FH^FD{input_text}
            ^FS^MMC^XZ
            '''.encode()
        )
        mysocket.close()  # Closing connection
    except Exception:
        print("Error with the connection")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError(
            f"Please enter some text to print. For example {sys.argv[0]} "
            "<enter text to print>"
        )

    if len(HOST) == 0:
        raise ValueError(
            "You need to add the IP address of the "
            "printer to the HOST variable in the script.")
    # Get text to print from command line
    input_text = " ".join(sys.argv[1:])

    # Output the print
    print(f"Printing: {input_text}")

    # Run the application
    main(input_text)
