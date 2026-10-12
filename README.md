# 🛡️ WindowsGuard

**Windows system monitoring utility built with Python.**

WindowsGuard is a lightweight desktop application designed to help users explore their Windows system, inspect running processes, and view basic system information.

> **Version:** `0.1` · **Status:** Early development · **Platform:** Windows

## ✨ Features

- **📊 Task Manager** — view running processes, including their names, PIDs, parent PIDs, and statuses.
- **💻 System Information** — retrieve basic information about your computer.
- **🚀 Startup Information** — inspect information about applications configured to start automatically.
- **🖥️ Graphical Interface** — interact with the application through a Tkinter-based GUI.

WindowsGuard is an educational project that is actively being developed. More features and improvements may be added in future releases.

## 🛠️ Built With

| Library | Purpose |
|---|---|
| `tkinter` | Graphical user interface |
| `psutil` | Process and system information |
| `platform` | Operating system and platform information |
| `winreg` | Access to the Windows Registry |
| `secrets` | Secure random value generation |
| `string` | Character sets and string utilities |

**Dependencies:** Most libraries listed above are included with Python. Only `psutil` is required as an external runtime library for the current setup.

## 📥 Installation

### 1. Requirements

- Windows 10 or Windows 11
- Python 3 installed, if running from source
- Git (optional, for cloning the repository)

### 2. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd WindowsGuard
```

Replace `YOUR_REPOSITORY_URL` with the URL of your GitHub repository.

Alternatively, download the repository as a ZIP archive and extract it.

### 3. Install dependencies

Open a terminal in the project directory and run:

```bash
python -m pip install psutil
```

To run the application, execute its entry-point file:

```bash
python main.py
```

If your main Python file has a different name, replace `main.py` with the correct filename.

## 📦 Building an Executable

You can package WindowsGuard into a standalone `.exe` file using **PyInstaller**.

### 1. Install PyInstaller

```bash
python -m pip install pyinstaller
```

### 2. Build WindowsGuard

Run the following command from the project directory:

```bash
python -m PyInstaller --onefile --windowed --name WindowsGuard main.py
```

**Command options:**
- `--onefile` — packages the application into a single executable.
- `--windowed` — prevents a separate console window from appearing.
- `--name WindowsGuard` — sets the executable's name.
- `main.py` — the entry-point script; change it if necessary.

### 3. Find the executable

After the build completes, the executable will be located at:

```text
WindowsGuard/
├── build/
├── dist/
│   └── WindowsGuard.exe
├── main.py
└── WindowsGuard.spec
```

You can launch `WindowsGuard.exe` from the `dist` directory.

**Note:** Build the executable on Windows for Windows. Test the resulting `.exe` before distributing it. PyInstaller bundles Python and the required dependencies, so users generally won't need to install Python separately to run the packaged application.

## 🔒 Important Notes

- WindowsGuard is currently an early-stage project (`v0.1`).
- It is **not an antivirus** and does not guarantee malware detection or protection.
- Information available to the application may depend on Windows permissions.
- Do not assume that a process is safe or malicious based on its name or status alone.

## 🗺️ Roadmap

Potential improvements for future releases:

- [ ] Improve the interface and layout.
- [ ] Enhance process monitoring and refreshing.
- [ ] Add more detailed process information.
- [ ] Explore network activity monitoring.
- [ ] Introduce additional system diagnostic tools.

## 🎯 Project Goal

WindowsGuard is a personal learning project focused on Python development, Windows internals, process monitoring, and cybersecurity.

The goal is to gradually evolve it into a more capable Windows system inspection tool while improving the codebase and learning how operating systems work.

---

**WindowsGuard v0.1** — Built with Python 🐍
