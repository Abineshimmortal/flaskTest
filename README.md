# Flask Test

A small Flask app that displays a welcome page at `http://127.0.0.1:5000`.

## Requirements

- Windows 10 or 11
- Python 3 installed and available as `py` in PowerShell

If Python is not installed, install it from [python.org](https://www.python.org/downloads/windows/). In the installer, enable **Add python.exe to PATH**. Close and reopen PowerShell after installation.

To check that Python is available, run:

```powershell
py --version
```

## Run the app (PowerShell)

1. Open PowerShell.
2. Change to the project folder:

   ```powershell
   cd "$HOME\OneDrive\Documents\GitHub\flaskTest"
   ```

   If your project is stored elsewhere, replace that path with its location.
3. Create a virtual environment (you only need to do this once):

   ```powershell
   py -m venv .venv
   ```
4. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell says script execution is disabled, you can skip activation and use the direct commands shown under **PowerShell activation alternative** below.
5. Install Flask (first run, and whenever dependencies change):

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
6. Start the development server:

   ```powershell
   python -m flask --app app run --debug
   ```
7. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
8. To stop the server, return to PowerShell and press **Ctrl+C**.

## PowerShell activation alternative

If activation is blocked, run these commands from the project folder instead. They use the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

## Run it again later

Open PowerShell, change to the project folder, activate the environment with `\.venv\Scripts\Activate.ps1`, then start the server with `python -m flask --app app run --debug`. Flask is already installed in the virtual environment, so you do not need to install it again.
