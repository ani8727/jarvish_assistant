# 🤖 Jarvish Assistant - AI Desktop Assistant

A modern desktop AI assistant application built with Python and web technologies. This intelligent assistant provides a sleek interface for voice interactions and commands, inspired by the iconic JARVIS system.

## 🌐 Live Demo
**Live Website:** [https://jarvish-assistant.vercel.app/](https://jarvish-assistant.vercel.app/)

## 📞 Contact & Links
- **GitHub Repository:** [jarvish_assistant](https://github.com/ani8727/jarvish_assistant)
- **LinkedIn:** [Aniket Gupta](https://www.linkedin.com/in/aniket-gupta-ani8727)
- **Live Website:** [jarvish-assistant.vercel.app](https://jarvish-assistant.vercel.app/)
- **Portfolio:** [golden-bienenstich-e0b208.netlify.app](https://golden-bienenstich-e0b208.netlify.app)

## 🛠️ Technologies Used

### Backend
- **Python 3.x** - Core application logic
- **Eel Framework** - Python-JavaScript bridge for desktop GUI
- **PyInstaller** - Executable creation

### Frontend
- **HTML5 & CSS3** - User interface structure and styling
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - Responsive UI framework
- **Bootstrap Icons** - Modern icon library
- **Texllate.js** - Text animation effects
- **Particle.js** - Dynamic background animations

### Deployment & DevOps
- **Vercel** - Web deployment platform
- **Docker** - Containerization
- **PowerShell** - Build automation
- **Git & GitHub** - Version control

## ✨ Features

- 🎙️ **Voice Command Interface** - Interactive voice recognition and response
- 💻 **Desktop Application** - Cross-platform desktop GUI using web technologies
- 🌐 **Web Version** - Accessible through browser deployment
- 🎨 **Modern UI Design** - Sleek, futuristic interface with animations
- ⚡ **Real-time Processing** - Fast command processing and response
- 📱 **Responsive Design** - Works on different screen sizes
- 🎯 **Modular Architecture** - Clean, maintainable code structure
- 🔧 **Easy Deployment** - Multiple deployment options available

## 📁 Project Structure

```
jarvish_assistant/
├── main.py                    # Main Python application entry point
├── requirements.txt           # Python dependencies
├── build_exe.ps1            # Windows executable build script
├── Dockerfile               # Docker configuration
├── vercel.json              # Vercel deployment configuration
├── README.md                # Project documentation
├── www/                     # Frontend web assets
│   ├── index.html          # Main HTML interface
│   ├── script.js           # Core JavaScript functionality
│   ├── controller.js       # Application controller logic
│   ├── main.js             # Main JavaScript entry point
│   ├── style.css           # Custom styles
│   ├── eel.js              # Eel framework JavaScript bridge
│   └── assets/             # Static assets
│       ├── audio/          # Audio files
│       ├── img/            # Images and icons
│       └── vendore/        # Third-party libraries
│           └── texllate/   # Text animation library
│               ├── animate.css
│               ├── jquery.fittext.js
│               ├── jquery.lettering.js
│               └── style.css
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+** installed on your system
- **pip** package manager
- **Git** for version control

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ani8727/jarvish_assistant.git
cd jarvish_assistant
```

2. **Create virtual environment** (recommended)
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python main.py
```

5. **Access the interface**
   - Desktop application will open automatically
   - Or visit: `http://localhost:8000`

## 📦 Build & Deploy

### Build Desktop Executable

**Windows:**
```powershell
# Run the build script
.\build_exe.ps1
```

**Manual build:**
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --add-data "www;www" main.py
```

The executable will be created in the `dist/` folder.

### Deploy to Web

**Deploy to Vercel:**
1. Connect your GitHub repository to Vercel
2. Deploy automatically on every push to main branch
3. Web version available at: [jarvish-assistant.vercel.app](https://jarvish-assistant.vercel.app/)

**Docker Deployment:**
```bash
# Build Docker image
docker build -t jarvish-assistant .

# Run container
docker run -p 8000:8000 jarvish-assistant
```

### Environment Variables
```bash
HOST=localhost        # Application host (default: localhost)
PORT=8000            # Application port (default: 8000)
```

## 🔧 Development Scripts

```bash
# Start development server
python main.py

# Build executable (Windows)
.\build_exe.ps1

# Install dependencies
pip install -r requirements.txt

# Update dependencies
pip freeze > requirements.txt
```

## 🎯 How It Works

1. **Python Backend** - Handles core logic and system interactions
2. **Eel Framework** - Bridges Python functions with JavaScript frontend
3. **Web Interface** - Provides modern UI for user interactions
4. **Command Processing** - Processes voice/text commands and generates responses

### Key Components:
- **`main.py`** - Main application server and Eel integration
- **`www/index.html`** - User interface layout
- **`www/script.js`** - Frontend JavaScript logic
- **`www/controller.js`** - Application state management

## 🤖 Assistant Functions

The assistant currently supports:
- Voice command recognition
- Text-based interaction
- Real-time response generation
- UI state management
- Audio feedback

*Note: This is a foundational framework that can be extended with additional AI capabilities, speech recognition, and natural language processing.*

## 👨‍💻 About the Developer

**Aniket Gupta** - Passionate developer creating modern applications with cutting-edge technologies. This assistant represents innovation in desktop AI applications using web technologies.

### Skills Demonstrated:
- **Python Development** (Eel, PyInstaller)
- **Full-Stack Web Development** (HTML5, CSS3, JavaScript)
- **Desktop Application Development**
- **Cloud Deployment** (Vercel, Docker)
- **UI/UX Design** (Bootstrap, Animations)
- **Version Control** (Git, GitHub)

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. **Fork the repository**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

## 📄 License

This project is open source and available under the **MIT License**.

## 🔮 Future Enhancements

- 🧠 Advanced AI integration (OpenAI, Google AI)
- 🗣️ Enhanced speech recognition and synthesis
- 🌍 Multi-language support
- 📊 Analytics and usage tracking
- 🔌 Plugin system for extensibility
- 📱 Mobile companion app

## 📧 Contact

**Aniket Gupta**

- **LinkedIn:** [aniket-gupta-ani8727](https://www.linkedin.com/in/aniket-gupta-ani8727)
- **GitHub:** [ani8727](https://github.com/ani8727)
- **Portfolio:** [golden-bienenstich-e0b208.netlify.app](https://golden-bienenstich-e0b208.netlify.app)
- **Live Demo:** [jarvish-assistant.vercel.app](https://jarvish-assistant.vercel.app/)

---

⭐ **If you found this project helpful, please give it a star!** ⭐

*Built with ❤️ using Python & Web Technologies*
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

