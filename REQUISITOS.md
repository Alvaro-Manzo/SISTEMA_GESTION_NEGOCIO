# Requisitos del Sistema

## Requisitos de Software

### Obligatorios
- Python 3.6 o superior
- Sistema operativo: Windows, macOS, Linux
- Terminal con soporte para códigos ANSI (colores)

### Bibliotecas Estándar (No requieren instalación)
- `json` - Procesamiento de archivos JSON
- `os` - Operaciones del sistema
- `time` - Manejo de tiempo y delays
- `datetime` - Timestamp y fechas
- `typing` - Type hints para mejor código
- `hashlib` - Generación de IDs únicos
- `shutil` - Operaciones de archivos

## Requisitos de Hardware

### Mínimos
- Procesador: 1 GHz
- RAM: 512 MB
- Almacenamiento: 10 MB libres
- Display: Resolución mínima 800x600

### Recomendados
- Procesador: 2 GHz o superior
- RAM: 1 GB o superior
- Almacenamiento: 100 MB libres (para logs y backups)
- Display: Resolución 1920x1080 para mejor visualización

## Compatibilidad de Terminal

### Terminales Compatibles
- **macOS**: Terminal.app, iTerm2
- **Linux**: GNOME Terminal, Konsole, Terminator, xterm
- **Windows**: Windows Terminal, PowerShell 7+, Git Bash

### Terminales con Limitaciones
- **Windows**: CMD (sin colores ANSI nativos)
  - Solución: Usar Windows Terminal o PowerShell

## Permisos Necesarios

### Permisos de Archivo
- Lectura: `inventory.json`, `config.example.json`
- Escritura: `inventory.json`, `transactions.json`, `business.log`
- Creación de carpetas: `backups/`

### Comandos de Configuración
```bash
# Linux/macOS
chmod 644 inventory.json
chmod 644 transactions.json
chmod 644 business.log
chmod 755 backups/

# Verificar permisos
ls -la
```

## Instalación

### Verificar Python
```bash
# Verificar versión instalada
python3 --version

# Debería mostrar: Python 3.6.0 o superior
```

### Instalación de Python

#### macOS
```bash
# Usando Homebrew
brew install python3

# O descargar desde python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Linux (Fedora/RHEL)
```bash
sudo dnf install python3 python3-pip
```

#### Windows
1. Descargar desde [python.org](https://www.python.org/downloads/)
2. Ejecutar instalador
3. Marcar "Add Python to PATH"
4. Completar instalación

## Configuración Inicial

### Paso 1: Clonar o Descargar
```bash
git clone <repository-url>
cd HAMBURGUESAS
```

### Paso 2: Crear Configuración
```bash
cp config.example.json inventory.json
```

### Paso 3: Editar Configuración
Abrir `inventory.json` y personalizar:
- business_name: Nombre de tu negocio
- currency: Símbolo de moneda
- users: Credenciales de acceso
- menu: Productos y precios

### Paso 4: Ejecutar
```bash
python3 main.py
```

## Opcional: Entorno Virtual

### Crear Entorno Virtual
```bash
# Crear
python3 -m venv venv

# Activar (macOS/Linux)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate

# Ejecutar aplicación
python main.py

# Desactivar
deactivate
```

## Troubleshooting

### Python no encontrado
```bash
# Verificar instalación
which python3

# Si no está instalado, instalar según OS
```

### Sin permisos de escritura
```bash
# Dar permisos
chmod -R 755 .
```

### Colores no se muestran
- Usar terminal moderna
- En Windows: Usar Windows Terminal

## Recursos Adicionales

### Documentación Python
- [Python Official Docs](https://docs.python.org/3/)
- [JSON en Python](https://docs.python.org/3/library/json.html)

### Tutoriales
- [Python para Principiantes](https://docs.python.org/es/3/tutorial/)
- [Trabajando con JSON](https://realpython.com/python-json/)
