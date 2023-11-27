# Development Environment Setup Guide

## Mac:

### 1. Install VS Code
- Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Download and install the macOS version.

### 2. Open VS Code and Set Up Integrated Terminal
- Open VS Code.
- Press ``Ctrl + ` ``backtick (`) `` to open the integrated terminal.

### 3. Install Homebrew
- Official Homebrew Documentation: [https://brew.sh/](https://brew.sh/)
- Run in the integrated terminal:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

### 4. Install NVM
- Official NVM Documentation: [https://github.com/nvm-sh/nvm](https://github.com/nvm-sh/nvm)
- Install using Homebrew:
  ```bash
  brew install nvm
  ```

### 5. Install Node
- Official Node.js Documentation: [https://nodejs.org/](https://nodejs.org/)
- Install the latest LTS version using NVM:
  ```bash
  nvm install --lts
  nvm use --lts
  ```

### 6. Install Python
- Official Python Documentation: [https://www.python.org/](https://www.python.org/)
- Python comes pre-installed; use Homebrew for a different version:
  ```bash
  brew install python
  ```

### 7. Install Sequelize and PSQL
- Official Sequelize Documentation: [https://sequelize.org/](https://sequelize.org/)
- Official PostgreSQL Documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- Install Sequelize globally:
  ```bash
  npm install -g sequelize-cli
  ```
- Install Postgres using Homebrew:
  ```bash
  brew install postgresql
  brew services start postgresql
  ```

## Windows:

### 1. Install VS Code
- Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Download and install the Windows version.

### 2. Open VS Code and Set Up Integrated Terminal
- Open VS Code.
- Press ``Ctrl + ` ``backtick (`) `` to open the integrated terminal.


### 3. Install NVM for Windows
- Official NVM-Windows Repository: [https://github.com/coreybutler/nvm-windows](https://github.com/coreybutler/nvm-windows)
- Download the installer from the releases page: [https://github.com/coreybutler/nvm-windows/releases](https://github.com/coreybutler/nvm-windows/releases)
- Follow the installation instructions provided on the repository.

### 4. Install Node
- Official Node.js Documentation: [https://nodejs.org/](https://nodejs.org/)
- Open a new terminal (Cmd or PowerShell) and install the latest LTS version using NVM:
  ```powershell
  nvm install --lts
  nvm use --lts
  ```

### 5. Install Python
- Official Python Documentation: [https://www.python.org/](https://www.python.org/)
- Download the Windows installer from the Python website and follow the installation instructions.

### 6. Install Sequelize and PSQL
- Official Sequelize Documentation: [https://sequelize.org/](https://sequelize.org/)
- Official PostgreSQL Documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- Install Sequelize globally:
  ```powershell
  npm install -g sequelize-cli
  ```
- Download and install the Postgres installer for Windows: [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)
- Follow the installation instructions and remember your Postgres password.
- Ensure the Postgres bin directory is in your system's PATH.
```