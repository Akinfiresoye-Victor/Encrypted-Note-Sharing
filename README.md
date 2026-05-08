# Secure Note Sharing

A simple Python project for sharing encrypted text notes between a client and server over a socket connection.

## Overview

This project demonstrates a basic secure note sharing system using RSA public-key encryption and Python sockets.

- `server_note.py` runs the server and accepts incoming connections.
- `client_note.py` connects to the server and sends encrypted notes.
- `encrypt.py` contains a separate simple character-substitution utility for shared-key encryption.

## Requirements

- Python 3.11+ (recommended)
- `rsa` library

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Setup

A virtual environment is included under `env/`.

To activate it on Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
.\env\Scripts\activate.bat
```

## Running the Server

Start the server first:

```bash
python server_note.py
```

The server listens on the local machine's IP address and port `1234`.

## Running the Client

In a separate terminal, run:

```bash
python client_note.py
```

Enter a username, then type notes to send to the server.

- Type `quit` to disconnect.
- Notes are encrypted with RSA before being sent.
- The server returns a confirmation message after receiving each note.

## Notes

- The server and client use RSA key pairs generated at runtime.
- The note length limit is 1024 characters.
- `encrypt.py` is an independent file showing a shared-secret substitution cipher and is not wired into the client/server flow.

## Project Structure

- `client_note.py` - client application
- `server_note.py` - server application
- `encrypt.py` - optional substitution cipher utility
- `requirements.txt` - dependency list
- `env/` - virtual environment files

## License

This repository is provided as-is for learning and experimentation.
