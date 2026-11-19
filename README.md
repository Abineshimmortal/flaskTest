# Flask To-Do List

A small Flask app for adding tasks, marking them complete, and deleting them. Tasks are saved in a local SQLite database at `instance/todos.sqlite3`, so they remain after you stop and restart the app.

## Requirements

- Windows 10 or 11
- Python 3 installed and available as `py` in PowerShell

If Python is not installed, install it from [python.org](https://www.python.org/downloads/windows/). In the installer, enable **Add python.exe to PATH**. Close and reopen PowerShell after installation.

Check Python is available:

```powershell
py --version
```

## First-time setup and run (PowerShell)

1. Open PowerShell.
2. Go to the project folder:

   ```powershell
   cd "$HOME\OneDrive\Documents\GitHub\flaskTest"
   ```

   If you saved the project somewhere else, use that folder path instead.
3. Create a virtual environment. You only need to do this once:

   ```powershell
   py -m venv .venv
   ```
4. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
5. Install the required packages:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install --upgrade pip
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

   The virtual environment path ensures these packages are installed for this project and does not depend on the global `python` command.

6. Start the app:

   ```powershell
   .\.venv\Scripts\python.exe -m flask --app app run --debug
   ```
7. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
8. Add tasks in the box. Use **Done** to mark a task complete and **Undo** to reopen it; use **Delete** to remove a task.
9. To stop the app, return to PowerShell and press **Ctrl+C**.

## If PowerShell blocks activation

Run these from the project folder instead of activating the environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

## Start the app later

Open PowerShell, go to the project folder, and run:

```powershell
.\.venv\Scripts\python.exe -m flask --app app run --debug
```

Alternatively, activate the environment and use `python`:

```powershell
.\.venv\Scripts\Activate.ps1
python -m flask --app app run --debug
```

Your tasks are stored in `instance/todos.sqlite3`. Keep that file to preserve your list.
