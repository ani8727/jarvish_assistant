# Jarvish Voice Assistant (Eel + frontend)

Step-by-step: run locally (Windows PowerShell)

1. Open PowerShell and change to project directory:

```powershell
cd 'C:\Users\anike\Desktop\Coding\project\jarvish_assistant'
```

2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the app:

```powershell
python main.py
```

The app will start a local Eel (Python) server and open your default browser at `http://localhost:8000/index.html`.

Configuration
- To change the port or host, set environment variables before running:

```powershell
$env:PORT = '9000'; $env:HOST = '0.0.0.0'
python main.py
```

Notes & suggested improvements for deployment (beginner-friendly)
- Packaging as a desktop app: use PyInstaller to create a single executable. Example:

```powershell
pip install pyinstaller
pyinstaller --onefile --add-data "www;www" main.py
```

- Distribute the executable to users; they won't need Python.
- Deploy as a web app: Eel is primarily a desktop bridge (Python + frontend). For web deployment, separate frontend and backend:
  - Serve `www` static files from a standard web server (Nginx, GitHub Pages, Vercel) and run any backend logic as an API (Flask/FastAPI).
  - Be aware: microphone and other native APIs may need user permission; web deployment may require HTTPS.

- Containerization (optional): Create a Docker image that runs the Python process and exposes the port. Example `Dockerfile` (basic):

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]
```

- Security & production notes:
  - Do not open the app to the public internet without adding authentication and HTTPS.
  - For remote deployment, replace browser-opening logic and run as a service.

What I changed
- `main.py`: now reads `HOST`/`PORT` from environment, starts Eel non-blocking, opens the default browser via `webbrowser` (with Windows fallback), and keeps the process alive.
- `requirements.txt`: adds `eel` dependency.
- `README.md`: step-by-step run instructions and beginner deployment suggestions.

If you want, I can:
- Create a `pyinstaller` script and test a build locally.
- Add a simple `Dockerfile` and `docker-compose.yml` for beginners.
- Revert to the old behavior of forcing Edge if you prefer that.

---

Deploying with Docker (beginner)

- Build the image:

```powershell
docker build -t jarvish-assistant:latest .
```

- Run the container (exposes port 8000):

```powershell
docker run --rm -p 8000:8000 jarvish-assistant:latest
```

By default the container sets `NO_BROWSER=1`, so it will not attempt to open a browser.

Building a Windows executable (PyInstaller)

- Use the included `build_exe.ps1` helper. Open PowerShell in the project root and run:

```powershell
.\build_exe.ps1
```

- After the script completes, the single-file executable will be in the `dist` folder.

Notes for deployment
- Desktop (recommended for Eel): distribute the PyInstaller-built executable.
- Server/container: use Docker. Set `HOST=0.0.0.0` and `NO_BROWSER=1` in the container.
- Web hosting: split frontend into static hosting and move Python logic to a web API if you need multi-user remote access.

