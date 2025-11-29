# Sistema de Gestión de Negocios Profesional v2.0 

Sistema empresarial avanzado de punto de venta con gestión de inventario, análisis de ventas, reportes y control total de operaciones. Basado en arquitectura modular con almacenamiento JSON.

## Descripción General

Esta es una aplicación versátil de gestión de negocios que puede adaptarse a cualquier negocio minorista o de servicios, incluyendo restaurantes, cafeterías, tiendas, food trucks y más. El sistema cuenta con control de acceso basado en roles, gestión de inventario en tiempo real y un flujo de trabajo simple para procesamiento de pedidos.

## Características Principales

### Gestión Avanzada
- **Sistema Universal para Negocios**: Adaptable a restaurantes, tiendas, cafeterías, servicios y más
- **Arquitectura Orientada a Objetos**: Código modular, mantenible y escalable con type hints
- **Gestión Completa de Inventario**: Agregar, eliminar y modificar productos con validación robusta
- **Sistema de Backups Automático**: Respaldo automático antes de cada modificación
- **Logging Profesional**: Registro detallado de todas las operaciones del sistema

### Transacciones y Ventas
- **Historial de Transacciones**: Registro completo de todas las ventas con ID único
- **Sistema de Carrito de Compras**: Gestión de pedidos antes del pago
- **Procesamiento de Pagos**: Flujo completo de checkout con confirmación
- **Generación de IDs Únicos**: Identificadores únicos usando hash MD5

### Reportes y Análisis
- **Reportes de Ventas**: Estadísticas completas de ingresos y rendimiento
- **Productos Más Vendidos**: Análisis de popularidad de productos
- **Historial de Transacciones**: Consulta de ventas pasadas con detalles
- **Promedios y Totales**: Cálculos automáticos de métricas clave

### Interfaz y UX
- **Interface Colorida en Terminal**: Colores ANSI para mejor experiencia visual
- **Menús Intuitivos**: Navegación clara y profesional
- **Validación de Datos**: Prevención de errores con validación en tiempo real
- **Mensajes Informativos**: Feedback claro de todas las operaciones

### Seguridad y Confiabilidad
- **Control de Acceso por Roles**: Separación completa entre administradores y usuarios
- **Validación de Configuración**: Verificación de estructura JSON al inicio
- **Manejo de Errores**: Gestión robusta de excepciones
- **Backup y Recuperación**: Sistema de backups con retención automática

## Arquitectura del Sistema

### Componentes Principales

El sistema está construido con arquitectura modular orientada a objetos:

```
BusinessSystem (Sistema Principal)
├── ConfigManager (Gestión de Configuración)
│   ├── Carga y validación de JSON
│   ├── Sistema de backups automáticos
│   └── Limpieza de backups antiguos
│
├── MenuManager (Gestión de Menú)
│   ├── Visualización profesional
│   ├── CRUD de productos
│   ├── Cálculo de totales
│   └── Validación de productos
│
├── AuthManager (Autenticación)
│   ├── Verificación de credenciales
│   └── Control de roles
│
├── TransactionManager (Transacciones)
│   ├── Registro de ventas
│   ├── Generación de IDs únicos
│   ├── Historial persistente
│   └── Cálculo de estadísticas
│
├── OrderManager (Gestión de Pedidos)
│   ├── Carrito de compras
│   ├── Procesamiento de pagos
│   └── Visualización de pedidos
│
├── ReportManager (Reportes)
│   ├── Reporte de ventas
│   ├── Productos más vendidos
│   └── Historial de transacciones
│
└── Logger (Sistema de Logs)
    ├── Registro de eventos
    ├── Niveles: INFO, WARNING, ERROR, SUCCESS
    └── Archivo: business.log
```

### Estructura del Archivo de Configuración

El sistema utiliza `inventory.json` como archivo de configuración principal:

```json
{
  "business_name": "Nombre de tu Negocio",
  "currency": "$",
  "users": {
    "admin": {
      "usuario": "contraseña"
    },
    "regular": {
      "usuario": "contraseña"
    }
  },
  "menu": {
    "Nombre del Producto": precio
  }
}
```

### Roles de Usuario

**Administrador**
- Ver menú completo con precios
- Agregar nuevos productos al inventario
- Eliminar productos existentes
- Modificar precios de productos
- Ver reportes de ventas y estadísticas
- Consultar historial de transacciones
- Crear backups manuales del sistema
- Acceso completo al sistema

**Usuario Regular**
- Ver menú y precios
- Agregar productos al carrito
- Ver carrito de compras
- Procesar pagos y completar órdenes
- Generar transacciones registradas

## Instalación

### Requisitos Previos

- Python 3.6 o superior
- No se requieren dependencias externas (usa la biblioteca estándar de Python)

### Instrucciones de Configuración

1. Clona o descarga este repositorio:
```bash
git clone <https://github.com/Alvaro-Manzo/SISTEMA_GESTION_NEGOCIO.git>
cd HAMBURGUESAS
```

2. Crea tu archivo de configuración:
```bash
cp config.example.json inventory.json
```

3. Edita `inventory.json` con la información de tu negocio:
   - Establece el nombre de tu negocio
   - Configura el símbolo de moneda
   - Agrega credenciales de administrador y usuarios
   - Define tus productos y precios

4. Ejecuta la aplicación:
```bash
python main.py
```

## Guía de Uso

### Para Administradores

#### Iniciar Sesión
1. Ejecuta la aplicación y selecciona opción `1` (Administrador)
2. Ingresa credenciales de administrador
3. Accede al Panel de Administración

#### Funciones Disponibles

**1. Ver Menú**
- Visualiza todos los productos con formato profesional
- Muestra precios actualizados

**2. Agregar Producto**
- Ingresa nombre del nuevo producto
- Define el precio
- Se guarda automáticamente con backup

**3. Eliminar Producto**
- Selecciona producto del menú
- Confirma la eliminación
- Se actualiza el inventario

**4. Modificar Precio**
- Selecciona producto
- Ingresa nuevo precio
- Visualiza comparación anterior/nuevo

**5. Ver Reporte de Ventas**
- Total de transacciones
- Ventas totales acumuladas
- Promedio por venta
- Top 10 productos más vendidos

**6. Ver Últimas Transacciones**
- Muestra las últimas 10 transacciones
- Incluye: ID, fecha, usuario, total, productos

**7. Crear Backup Manual**
- Genera copia de seguridad instantánea
- Se almacena en carpeta `/backups`

### Para Usuarios Regulares

#### Proceso de Compra

1. **Iniciar Sesión**
   - Selecciona opción `2` (Usuario)
   - Ingresa credenciales

2. **Ver Menú**
   - Revisa productos disponibles
   - Consulta precios

3. **Agregar al Carrito**
   - Selecciona productos por nombre
   - Indica cantidad deseada
   - Confirma agregado

4. **Ver Carrito**
   - Revisa productos agregados
   - Verifica cantidades y subtotales
   - Visualiza total a pagar

5. **Procesar Pago**
   - Confirma la compra
   - Sistema procesa el pago
   - Se genera ID de transacción
   - Pedido enviado a cocina/producción

### Ejemplo de Sesión Completa

```
============================================================
  SISTEMA DE GESTIÓN DE NEGOCIOS v2.0
============================================================

Bienvenido al Hamburguesas Pumas

Seleccione su rol:
  1. Administrador
  2. Usuario

Opción: 2

Usuario: user1
Contraseña: user

Acceso concedido. Bienvenido, user1!

────────────────────────────────────────────────────────────
  REALIZAR PEDIDO
────────────────────────────────────────────────────────────

1. Ver menú
2. Agregar producto al carrito
3. Ver carrito
4. Procesar pago
5. Cancelar y salir

Seleccione una opción: 1

============================================================
MENÚ - Hamburguesas Pumas
============================================================

Producto                                          Precio
────────────────────────────────────────────────────────────
1. Hamburguesa Sencilla                           $50.00
2. Hamburguesa Doble                              $80.00
3. Papas Fritas                                   $30.00
4. Refresco                                       $20.00
5. Hot-Dog                                        $20.00
============================================================

Seleccione una opción: 2

Nombre del producto: Hamburguesa Doble
Cantidad: 2
Agregado: 2x Hamburguesa Doble

Seleccione una opción: 2

Nombre del producto: Papas Fritas
Cantidad: 1
Agregado: 1x Papas Fritas

Seleccione una opción: 3

────────────────────────────────────────────────────────────
  CARRITO DE COMPRAS
────────────────────────────────────────────────────────────

  2x Hamburguesa Doble                    $80.00 = $160.00
  1x Papas Fritas                         $30.00 = $30.00
────────────────────────────────────────────────────────────
  TOTAL: $190.00

Seleccione una opción: 4

Procesando pago...
Pago procesado exitosamente
Enviando orden a cocina...
¡Gracias por tu compra!
```

## Personalización para Diferentes Tipos de Negocios

### Restaurante / Comida Rápida
```json
{
  "business_name": "Pizzería de José",
  "currency": "$",
  "menu": {
    "Pizza Margarita": 12.99,
    "Pizza Pepperoni": 14.99,
    "Pan de Ajo": 5.99,
    "Refresco": 2.50
  }
}
```

### Cafetería
```json
{
  "business_name": "Café Artesanal",
  "currency": "$",
  "menu": {
    "Espresso": 3.50,
    "Cappuccino": 4.75,
    "Latte": 5.00,
    "Croissant": 3.25
  }
}
```

### Tienda Minorista
```json
{
  "business_name": "Tienda de Gadgets Tech",
  "currency": "$",
  "menu": {
    "Cable USB": 9.99,
    "Mouse Inalámbrico": 24.99,
    "Teclado": 49.99,
    "Audífonos": 79.99
  }
}
```

### Negocio Internacional
```json
{
  "business_name": "Panadería Europea",
  "currency": "€",
  "menu": {
    "Baguette": 2.50,
    "Croissant": 1.80,
    "Pain au Chocolat": 2.20
  }
}
```

## Estructura de Archivos

```
HAMBURGUESAS/
├── main.py                    # Aplicación principal (800+ líneas)
├── inventory.json             # Configuración activa del negocio
├── config.example.json        # Plantilla de configuración
├── transactions.json          # Historial de ventas (generado automáticamente)
├── business.log              # Archivo de logs (generado automáticamente)
├── backups/                  # Carpeta de backups (generada automáticamente)
│   ├── inventory_backup_YYYYMMDD_HHMMSS.json
│   └── ... (últimos 10 backups)
├── README.md                 # Documentación principal
└── .gitignore               # Configuración de Git
```

## Detalles Técnicos

### Arquitectura de Clases

**Color**: Gestión de colores ANSI para terminal
- Códigos de color para diferentes tipos de mensajes
- Mejora significativa de la experiencia visual

**Logger**: Sistema de logging profesional
- Registro de eventos con timestamps
- Niveles: INFO, WARNING, ERROR, SUCCESS
- Almacenamiento persistente en `business.log`

**ConfigManager**: Gestión de configuración
- Carga y validación de JSON
- Sistema de backups automáticos antes de cada cambio
- Mantiene últimos 10 backups automáticamente
- Validación de estructura de datos

**TransactionManager**: Gestión de transacciones
- Registro de todas las ventas
- Generación de IDs únicos con hash MD5
- Cálculo de estadísticas en tiempo real
- Persistencia en `transactions.json`

**MenuManager**: Gestión del menú
- CRUD completo de productos
- Visualización profesional con colores
- Cálculos automáticos de totales
- Validación de productos

**AuthManager**: Sistema de autenticación
- Verificación de credenciales
- Separación por roles (admin/user)
- Registro de intentos de acceso

**ReportManager**: Generación de reportes
- Estadísticas de ventas
- Productos más vendidos
- Historial de transacciones
- Formato profesional con colores

**OrderManager**: Gestión de pedidos
- Carrito de compras
- Cálculo de subtotales y totales
- Procesamiento de pagos
- Integración con TransactionManager

**BusinessSystem**: Sistema principal
- Coordinación de todos los componentes
- Flujo de navegación
- Manejo de excepciones global
- Interface de usuario

### Persistencia de Datos

#### Archivos JSON

**inventory.json**: Configuración principal
- Se carga al inicio del sistema
- Se guarda automáticamente después de cada cambio
- Backup automático antes de cada modificación

**transactions.json**: Historial de ventas
- Se crea automáticamente en la primera venta
- Cada venta agrega un registro
- Incluye: ID, fecha, usuario, productos, total

**backups/**: Carpeta de respaldos
- Se crea automáticamente cuando es necesaria
- Mantiene últimos 10 backups
- Formato: inventory_backup_YYYYMMDD_HHMMSS.json

#### Sistema de Logging

**business.log**: Registro de eventos
- Timestamp de cada evento
- Nivel de severidad
- Descripción del evento
- Crece indefinidamente (considerar rotación para producción)

### Consideraciones de Seguridad

**Importante**: Esta aplicación está diseñada para uso educativo y negocios pequeños. Para entornos de producción, considera:

**Implementaciones Críticas**:
- Implementar hashing de contraseñas (bcrypt, argon2) en lugar de almacenamiento en texto plano
- Agregar SSL/TLS para comunicaciones de red si se extiende a servidor web
- Implementar tokens JWT para autenticación de sesiones
- Agregar rate limiting para prevenir ataques de fuerza bruta
- Implementar RBAC (Role-Based Access Control) más granular

**Validación y Sanitización**:
- Validación estricta de todas las entradas de usuario
- Sanitización de datos antes de almacenar en JSON
- Prevención de inyección de código
- Límites en longitud de strings y valores numéricos

**Infraestructura**:
- Configurar permisos apropiados de archivos (chmod 600 para archivos sensibles)
- Usar base de datos relacional (PostgreSQL, MySQL) en lugar de JSON
- Implementar sistema de auditoría completo
- Rotación de logs para evitar crecimiento infinito
- Encriptación de datos sensibles en reposo

**Mejores Prácticas**:
- Variables de entorno para configuración sensible
- Separación de configuración de desarrollo y producción
- Pruebas unitarias y de integración
- Documentación de API si se extiende a servicios web

### Manejo de Errores

La aplicación incluye manejo robusto de errores para:

**Errores de Configuración**:
- Archivos de configuración faltantes
- Formato JSON inválido
- Estructura de configuración incorrecta
- Claves requeridas ausentes

**Errores de Autenticación**:
- Credenciales de usuario incorrectas
- Usuarios inexistentes
- Roles inválidos

**Errores de Operación**:
- Selecciones de productos inválidas
- Entradas de cantidad inválidas (no numéricas, negativas)
- Entradas de precio inválidas
- Productos duplicados
- Operaciones en productos inexistentes

**Errores de Sistema**:
- Permisos de archivo insuficientes
- Espacio en disco insuficiente
- Interrupciones de usuario (Ctrl+C)
- Excepciones inesperadas

Todos los errores son registrados en `business.log` con timestamp y nivel de severidad.

## Extendiendo el Sistema

### Funcionalidades Propuestas

El diseño modular permite agregar características fácilmente:

#### 1. Sistema de Inventario con Stock
Agregar control de cantidades disponibles:

```json
{
  "menu": {
    "Producto": {
      "precio": 10.00,
      "stock": 50,
      "stock_minimo": 10,
      "categoria": "Comida"
    }
  }
}
```

Modificar `MenuManager` para:
- Verificar disponibilidad antes de vender
- Decrementar stock automáticamente
- Alertas de stock bajo
- Reporte de productos agotados

#### 2. Sistema de Categorías
Organizar productos por categorías:

```python
class CategoryManager:
    def get_products_by_category(self, category: str)
    def add_category(self, name: str, description: str)
    def list_categories(self)
```

#### 3. Sistema de Descuentos y Promociones
Implementar lógica de precios especiales:

```json
{
  "promociones": {
    "2x1_hamburguesas": {
      "tipo": "2x1",
      "productos": ["Hamburguesa Sencilla"],
      "activo": true
    },
    "descuento_combo": {
      "tipo": "porcentaje",
      "descuento": 15,
      "productos": ["Hamburguesa Doble", "Papas Fritas", "Refresco"],
      "activo": true
    }
  }
}
```

#### 4. Sistema de Múltiples Ubicaciones
Soporte para cadenas con varias sucursales:

```json
{
  "sucursales": {
    "centro": {
      "direccion": "...",
      "inventario": {...},
      "ventas": [...]
    },
    "norte": {
      "direccion": "...",
      "inventario": {...},
      "ventas": [...]
    }
  }
}
```

#### 5. Integración con Base de Datos
Migrar de JSON a PostgreSQL/MySQL:

```python
class DatabaseManager:
    def __init__(self, connection_string: str)
    def execute_query(self, query: str, params: tuple)
    def get_products(self)
    def save_transaction(self, transaction: dict)
```

#### 6. API REST con FastAPI
Exponer funcionalidad vía API:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.post("/api/products")
async def create_product(product: Product):
    # Lógica de creación

@app.get("/api/sales/report")
async def get_sales_report():
    # Retornar estadísticas
```

#### 7. Interface Web
Crear frontend con React/Vue:

```
frontend/
├── src/
│   ├── components/
│   │   ├── AdminPanel.jsx
│   │   ├── ProductList.jsx
│   │   ├── ShoppingCart.jsx
│   │   └── SalesReport.jsx
│   ├── services/
│   │   └── api.js
│   └── App.jsx
```

#### 8. Sistema de Notificaciones
Alertas por email/SMS:

```python
class NotificationManager:
    def send_low_stock_alert(self, product: str)
    def send_sale_confirmation(self, transaction_id: str)
    def send_daily_report(self)
```

#### 9. Análisis Avanzado con Pandas
Reportes más sofisticados:

```python
import pandas as pd
import matplotlib.pyplot as plt

class AnalyticsManager:
    def generate_sales_trends(self)
    def predict_demand(self)
    def customer_segmentation(self)
```

#### 10. Sistema de Empleados
Gestión de personal:

```json
{
  "empleados": {
    "EMP001": {
      "nombre": "Juan Pérez",
      "rol": "cajero",
      "turno": "mañana",
      "ventas_realizadas": 45
    }
  }
}
```

## Solución de Problemas

### Problemas Comunes y Soluciones

#### Error: FileNotFoundError: inventory.json no encontrado
**Causa**: El archivo de configuración no existe
**Solución**: 
```bash
cp config.example.json inventory.json
# Edita inventory.json con tus datos
```

#### Error: JSONDecodeError
**Causa**: Sintaxis JSON inválida en inventory.json
**Solución**: 
- Verifica que todas las comillas sean dobles (")
- Asegúrate de que no haya comas finales
- Usa un validador JSON online
- Revisa el último backup en `/backups`

#### La autenticación falla constantemente
**Causa**: Credenciales incorrectas o sensibilidad a mayúsculas
**Solución**: 
- Verifica usuario y contraseña en inventory.json
- Las credenciales son case-sensitive
- Revisa espacios adicionales

#### Los productos no se guardan
**Causa**: Permisos de archivo insuficientes
**Solución**: 
```bash
chmod 644 inventory.json
chmod 755 backups/
```

#### Error: PermissionError al crear backups
**Causa**: No hay permisos para crear carpeta backups
**Solución**: 
```bash
mkdir backups
chmod 755 backups/
```

#### Los colores no se muestran en terminal
**Causa**: Terminal no soporta códigos ANSI
**Solución**: 
- Usa terminal moderna (iTerm2, Windows Terminal)
- En Windows: Activa VT100 en consola

#### Error: ModuleNotFoundError
**Causa**: Python < 3.6
**Solución**: 
```bash
python3 --version  # Verifica versión
# Actualiza a Python 3.6+
```

#### Archivo business.log muy grande
**Causa**: Uso prolongado sin limpieza
**Solución**: 
```bash
# Respaldar y limpiar logs
mv business.log business.log.old
touch business.log
# O implementar rotación de logs
```

#### Transacciones no se registran
**Causa**: Permisos o error en escritura
**Solución**: 
```bash
# Verifica permisos
ls -la transactions.json
# Regenerar archivo
rm transactions.json
# El sistema lo creará automáticamente
```

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del repositorio
2. Crea una rama de característica
3. Haz commit de tus cambios
4. Empuja a la rama
5. Crea un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

## Soporte

Para problemas, preguntas o sugerencias, por favor abre un issue en el repositorio.

## Registro de Cambios

### Versión 2.0 - Sistema Profesional (Actual)

**Nuevas Características Principales**:
- Sistema completo de clases orientadas a objetos
- Interfaz colorida con códigos ANSI
- Sistema de logging profesional
- Backups automáticos con retención
- Historial completo de transacciones
- IDs únicos para cada venta
- Reportes de ventas con estadísticas
- Top 10 productos más vendidos
- Carrito de compras antes de pagar
- Panel de administración completo
- Eliminación de productos
- Modificación de precios
- Validación robusta de datos

**Mejoras Técnicas**:
- Type hints para mejor mantenibilidad
- Separación de responsabilidades (SoC)
- Manejo de errores mejorado
- Documentación inline completa
- Arquitectura escalable y modular

**Archivos Nuevos**:
- business.log (logging automático)
- transactions.json (historial de ventas)
- backups/ (respaldos automáticos)

### Versión 1.0 - Sistema Básico
- Lanzamiento inicial
- Autenticación básica de usuarios
- Procesamiento simple de pedidos
- Menú hardcodeado en código
- Sin persistencia de cambios
- Sin reportes ni estadísticas
