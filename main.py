"""
Sistema de Gestión de Negocios Profesional
Sistema avanzado de punto de venta con gestión de inventario, reportes y análisis.
Desarrollado para empresas que requieren control total de sus operaciones.
"""

import time
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import hashlib
import shutil


class Color:
    """Códigos ANSI para colores en terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    """Sistema de logging profesional"""
    
    @staticmethod
    def log(message: str, level: str = "INFO"):
        """Registra eventos en archivo de log"""
        log_file = "business.log"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    
    @staticmethod
    def info(message: str):
        Logger.log(message, "INFO")
    
    @staticmethod
    def warning(message: str):
        Logger.log(message, "WARNING")
    
    @staticmethod
    def error(message: str):
        Logger.log(message, "ERROR")
    
    @staticmethod
    def success(message: str):
        Logger.log(message, "SUCCESS")


class ConfigManager:
    """Gestor profesional de configuración con backups"""
    
    CONFIG_FILE = 'inventory.json'
    BACKUP_DIR = 'backups'
    
    @staticmethod
    def crear_backup():
        """Crea backup automático de la configuración"""
        if not os.path.exists(ConfigManager.BACKUP_DIR):
            os.makedirs(ConfigManager.BACKUP_DIR)
        
        if os.path.exists(ConfigManager.CONFIG_FILE):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{ConfigManager.BACKUP_DIR}/inventory_backup_{timestamp}.json"
            shutil.copy2(ConfigManager.CONFIG_FILE, backup_file)
            Logger.info(f"Backup creado: {backup_file}")
            
            # Mantener solo los últimos 10 backups
            ConfigManager._limpiar_backups_antiguos()
    
    @staticmethod
    def _limpiar_backups_antiguos():
        """Mantiene solo los últimos 10 backups"""
        if not os.path.exists(ConfigManager.BACKUP_DIR):
            return
        
        backups = sorted([f for f in os.listdir(ConfigManager.BACKUP_DIR) 
                         if f.startswith('inventory_backup_')])
        
        while len(backups) > 10:
            oldest = backups.pop(0)
            os.remove(os.path.join(ConfigManager.BACKUP_DIR, oldest))
            Logger.info(f"Backup antiguo eliminado: {oldest}")
    
    @staticmethod
    def cargar_config() -> dict:
        """Carga configuración con validación"""
        if not os.path.exists(ConfigManager.CONFIG_FILE):
            Logger.error(f"Archivo de configuración '{ConfigManager.CONFIG_FILE}' no encontrado")
            print(f"{Color.FAIL}Error: Archivo de configuración no encontrado.{Color.ENDC}")
            print(f"{Color.WARNING}Por favor crea un archivo inventory.json{Color.ENDC}")
            exit(1)
        
        try:
            with open(ConfigManager.CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Validar estructura de configuración
            ConfigManager._validar_config(config)
            Logger.info("Configuración cargada exitosamente")
            return config
            
        except json.JSONDecodeError as e:
            Logger.error(f"Error de formato JSON: {e}")
            print(f"{Color.FAIL}Error: Formato JSON inválido en inventory.json{Color.ENDC}")
            exit(1)
        except Exception as e:
            Logger.error(f"Error al cargar configuración: {e}")
            print(f"{Color.FAIL}Error al cargar configuración: {e}{Color.ENDC}")
            exit(1)
    
    @staticmethod
    def _validar_config(config: dict):
        """Valida que la configuración tenga la estructura correcta"""
        required_keys = ['business_name', 'currency', 'users', 'menu']
        
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Falta la clave requerida: {key}")
        
        if 'admin' not in config['users'] or 'regular' not in config['users']:
            raise ValueError("La configuración de usuarios debe tener 'admin' y 'regular'")
    
    @staticmethod
    def guardar_config(config: dict):
        """Guarda configuración con backup automático"""
        try:
            # Crear backup antes de guardar
            ConfigManager.crear_backup()
            
            with open(ConfigManager.CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            Logger.info("Configuración guardada exitosamente")
            
        except Exception as e:
            Logger.error(f"Error al guardar configuración: {e}")
            print(f"{Color.FAIL}Error al guardar configuración: {e}{Color.ENDC}")


class TransactionManager:
    """Gestor de transacciones y historial"""
    
    TRANSACTIONS_FILE = 'transactions.json'
    
    @staticmethod
    def registrar_venta(usuario: str, pedido: dict, total: float, moneda: str):
        """Registra una venta en el historial"""
        transaction = {
            "id": TransactionManager._generar_id(),
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "usuario": usuario,
            "pedido": pedido,
            "total": total,
            "moneda": moneda
        }
        
        transactions = TransactionManager._cargar_transacciones()
        transactions.append(transaction)
        
        with open(TransactionManager.TRANSACTIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(transactions, f, indent=2, ensure_ascii=False)
        
        Logger.success(f"Venta registrada: ID {transaction['id']} - Total: {moneda}{total}")
    
    @staticmethod
    def _generar_id() -> str:
        """Genera ID único para la transacción"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        return hashlib.md5(timestamp.encode()).hexdigest()[:8].upper()
    
    @staticmethod
    def _cargar_transacciones() -> list:
        """Carga historial de transacciones"""
        if os.path.exists(TransactionManager.TRANSACTIONS_FILE):
            with open(TransactionManager.TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    @staticmethod
    def obtener_estadisticas() -> dict:
        """Calcula estadísticas de ventas"""
        transactions = TransactionManager._cargar_transacciones()
        
        if not transactions:
            return {
                "total_ventas": 0,
                "cantidad_transacciones": 0,
                "promedio_venta": 0,
                "productos_mas_vendidos": {}
            }
        
        total_ventas = sum(t['total'] for t in transactions)
        cantidad_transacciones = len(transactions)
        promedio_venta = total_ventas / cantidad_transacciones
        
        # Productos más vendidos
        productos_vendidos = {}
        for t in transactions:
            for producto, cantidad in t['pedido'].items():
                productos_vendidos[producto] = productos_vendidos.get(producto, 0) + cantidad
        
        return {
            "total_ventas": total_ventas,
            "cantidad_transacciones": cantidad_transacciones,
            "promedio_venta": promedio_venta,
            "productos_mas_vendidos": productos_vendidos
        }


class MenuManager:
    """Gestor avanzado del menú"""
    
    def __init__(self, config: dict):
        self.config = config
        self.menu = config.get('menu', {})
        self.business_name = config.get('business_name', 'Negocio')
        self.currency = config.get('currency', '$')
    
    def mostrar_menu(self, mostrar_header: bool = True):
        """Muestra el menú con formato profesional"""
        if mostrar_header:
            self._mostrar_header()
        
        print(f"\n{Color.BOLD}{Color.OKCYAN}{'='*60}{Color.ENDC}")
        print(f"{Color.BOLD}{Color.OKGREEN}MENÚ - {self.business_name}{Color.ENDC}".center(70))
        print(f"{Color.BOLD}{Color.OKCYAN}{'='*60}{Color.ENDC}\n")
        
        if not self.menu:
            print(f"{Color.WARNING}No hay productos disponibles en el menú{Color.ENDC}\n")
            return
        
        print(f"{Color.BOLD}{'Producto':<40} {'Precio':>15}{Color.ENDC}")
        print(f"{Color.OKCYAN}{'-'*60}{Color.ENDC}")
        
        for idx, (item, precio) in enumerate(self.menu.items(), 1):
            print(f"{Color.OKBLUE}{idx}. {item:<37}{Color.ENDC} {Color.OKGREEN}{self.currency}{precio:>10.2f}{Color.ENDC}")
        
        print(f"{Color.OKCYAN}{'='*60}{Color.ENDC}\n")
    
    def _mostrar_header(self):
        """Muestra header del sistema"""
        print(f"\n{Color.BOLD}{Color.HEADER}{'='*60}{Color.ENDC}")
        print(f"{Color.BOLD}{Color.HEADER}  SISTEMA DE GESTIÓN DE NEGOCIOS v2.0{Color.ENDC}".center(70))
        print(f"{Color.BOLD}{Color.HEADER}{'='*60}{Color.ENDC}\n")
    
    def agregar_producto(self, nombre: str, precio: float) -> bool:
        """Agrega un nuevo producto al menú"""
        try:
            if nombre in self.menu:
                print(f"{Color.WARNING}El producto '{nombre}' ya existe en el menú{Color.ENDC}")
                return False
            
            self.menu[nombre] = precio
            self.config['menu'] = self.menu
            ConfigManager.guardar_config(self.config)
            
            print(f"{Color.OKGREEN}Producto agregado exitosamente: {nombre} - {self.currency}{precio}{Color.ENDC}")
            Logger.info(f"Producto agregado: {nombre} - Precio: {precio}")
            return True
            
        except Exception as e:
            Logger.error(f"Error al agregar producto: {e}")
            print(f"{Color.FAIL}Error al agregar producto: {e}{Color.ENDC}")
            return False
    
    def eliminar_producto(self, nombre: str) -> bool:
        """Elimina un producto del menú"""
        try:
            if nombre not in self.menu:
                print(f"{Color.WARNING}El producto '{nombre}' no existe en el menú{Color.ENDC}")
                return False
            
            precio = self.menu[nombre]
            del self.menu[nombre]
            self.config['menu'] = self.menu
            ConfigManager.guardar_config(self.config)
            
            print(f"{Color.OKGREEN}Producto eliminado: {nombre}{Color.ENDC}")
            Logger.info(f"Producto eliminado: {nombre} - Precio anterior: {precio}")
            return True
            
        except Exception as e:
            Logger.error(f"Error al eliminar producto: {e}")
            print(f"{Color.FAIL}Error al eliminar producto: {e}{Color.ENDC}")
            return False
    
    def modificar_precio(self, nombre: str, nuevo_precio: float) -> bool:
        """Modifica el precio de un producto"""
        try:
            if nombre not in self.menu:
                print(f"{Color.WARNING}El producto '{nombre}' no existe en el menú{Color.ENDC}")
                return False
            
            precio_anterior = self.menu[nombre]
            self.menu[nombre] = nuevo_precio
            self.config['menu'] = self.menu
            ConfigManager.guardar_config(self.config)
            
            print(f"{Color.OKGREEN}Precio modificado: {nombre}{Color.ENDC}")
            print(f"  Anterior: {self.currency}{precio_anterior} → Nuevo: {self.currency}{nuevo_precio}")
            Logger.info(f"Precio modificado: {nombre} - {precio_anterior} → {nuevo_precio}")
            return True
            
        except Exception as e:
            Logger.error(f"Error al modificar precio: {e}")
            print(f"{Color.FAIL}Error al modificar precio: {e}{Color.ENDC}")
            return False
    
    def calcular_total(self, pedido: dict) -> float:
        """Calcula el total de un pedido"""
        total = sum(self.menu.get(item, 0) * cantidad for item, cantidad in pedido.items())
        return round(total, 2)
    
    def validar_producto(self, nombre: str) -> bool:
        """Valida que un producto exista en el menú"""
        return nombre in self.menu


class AuthManager:
    """Gestor de autenticación y usuarios"""
    
    def __init__(self, config: dict):
        self.admins = config.get('users', {}).get('admin', {})
        self.users = config.get('users', {}).get('regular', {})
    
    def autenticar(self, username: str, password: str, rol: str) -> bool:
        """Autentica un usuario"""
        if rol == 'admin':
            resultado = self.admins.get(username) == password
        else:
            resultado = self.users.get(username) == password
        
        if resultado:
            Logger.info(f"Autenticación exitosa: {username} ({rol})")
        else:
            Logger.warning(f"Intento de autenticación fallido: {username} ({rol})")
        
        return resultado


class ReportManager:
    """Gestor de reportes y estadísticas"""
    
    @staticmethod
    def generar_reporte_ventas():
        """Genera reporte detallado de ventas"""
        stats = TransactionManager.obtener_estadisticas()
        
        print(f"\n{Color.BOLD}{Color.HEADER}{'='*60}{Color.ENDC}")
        print(f"{Color.BOLD}{Color.HEADER}  REPORTE DE VENTAS{Color.ENDC}".center(70))
        print(f"{Color.BOLD}{Color.HEADER}{'='*60}{Color.ENDC}\n")
        
        print(f"{Color.BOLD}Estadísticas Generales:{Color.ENDC}")
        print(f"{Color.OKCYAN}{'─'*60}{Color.ENDC}")
        print(f"  Total de Transacciones: {Color.OKGREEN}{stats['cantidad_transacciones']}{Color.ENDC}")
        print(f"  Ventas Totales: {Color.OKGREEN}${stats['total_ventas']:.2f}{Color.ENDC}")
        print(f"  Promedio por Venta: {Color.OKGREEN}${stats['promedio_venta']:.2f}{Color.ENDC}")
        
        if stats['productos_mas_vendidos']:
            print(f"\n{Color.BOLD}Productos Más Vendidos:{Color.ENDC}")
            print(f"{Color.OKCYAN}{'─'*60}{Color.ENDC}")
            
            productos_ordenados = sorted(
                stats['productos_mas_vendidos'].items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            for idx, (producto, cantidad) in enumerate(productos_ordenados[:10], 1):
                print(f"  {idx}. {producto:<40} {Color.OKGREEN}{cantidad} unidades{Color.ENDC}")
        
        print(f"\n{Color.OKCYAN}{'='*60}{Color.ENDC}\n")
        
        Logger.info("Reporte de ventas generado")
    
    @staticmethod
    def generar_reporte_transacciones(limite: int = 10):
        """Muestra las últimas transacciones"""
        transactions = TransactionManager._cargar_transacciones()
        
        if not transactions:
            print(f"\n{Color.WARNING}No hay transacciones registradas{Color.ENDC}\n")
            return
        
        print(f"\n{Color.BOLD}{Color.HEADER}{'='*60}{Color.ENDC}")
        print(f"{Color.BOLD}{Color.HEADER}  ÚLTIMAS TRANSACCIONES{Color.ENDC}".center(70))
        print(f"{Color.BOLD}{Color.HEADER}{'='*60}{Color.ENDC}\n")
        
        ultimas = transactions[-limite:]
        ultimas.reverse()
        
        for trans in ultimas:
            print(f"{Color.BOLD}ID: {trans['id']}{Color.ENDC}")
            print(f"  Fecha: {Color.OKCYAN}{trans['fecha']}{Color.ENDC}")
            print(f"  Usuario: {Color.OKBLUE}{trans['usuario']}{Color.ENDC}")
            print(f"  Total: {Color.OKGREEN}{trans['moneda']}{trans['total']:.2f}{Color.ENDC}")
            print(f"  Productos: {', '.join([f'{k} ({v})' for k, v in trans['pedido'].items()])}")
            print(f"{Color.OKCYAN}{'─'*60}{Color.ENDC}")
        
        print()
        Logger.info("Reporte de transacciones generado")


class OrderManager:
    """Gestor de pedidos"""
    
    def __init__(self, menu_manager: MenuManager):
        self.menu_manager = menu_manager
        self.pedido = {}
    
    def agregar_item(self, item: str, cantidad: int):
        """Agrega un ítem al pedido"""
        if self.menu_manager.validar_producto(item):
            self.pedido[item] = self.pedido.get(item, 0) + cantidad
            print(f"{Color.OKGREEN}Agregado: {cantidad}x {item}{Color.ENDC}")
            return True
        else:
            print(f"{Color.FAIL}Producto no encontrado: {item}{Color.ENDC}")
            return False
    
    def mostrar_pedido(self):
        """Muestra el pedido actual"""
        if not self.pedido:
            print(f"\n{Color.WARNING}El carrito está vacío{Color.ENDC}\n")
            return
        
        print(f"\n{Color.BOLD}{Color.OKBLUE}{'─'*60}{Color.ENDC}")
        print(f"{Color.BOLD}  CARRITO DE COMPRAS{Color.ENDC}")
        print(f"{Color.BOLD}{Color.OKBLUE}{'─'*60}{Color.ENDC}\n")
        
        total = 0
        for item, cantidad in self.pedido.items():
            precio = self.menu_manager.menu[item]
            subtotal = precio * cantidad
            total += subtotal
            print(f"  {cantidad}x {item:<35} {self.menu_manager.currency}{precio:.2f} = {Color.OKGREEN}{self.menu_manager.currency}{subtotal:.2f}{Color.ENDC}")
        
        print(f"{Color.OKBLUE}{'─'*60}{Color.ENDC}")
        print(f"{Color.BOLD}  TOTAL: {Color.OKGREEN}{self.menu_manager.currency}{total:.2f}{Color.ENDC}\n")
    
    def procesar_pago(self, usuario: str):
        """Procesa el pago del pedido"""
        if not self.pedido:
            print(f"{Color.WARNING}No hay productos en el pedido{Color.ENDC}")
            return False
        
        total = self.menu_manager.calcular_total(self.pedido)
        
        print(f"\n{Color.BOLD}Procesando pago...{Color.ENDC}")
        time.sleep(1)
        
        # Registrar transacción
        TransactionManager.registrar_venta(
            usuario,
            self.pedido.copy(),
            total,
            self.menu_manager.currency
        )
        
        print(f"{Color.OKGREEN}Pago procesado exitosamente{Color.ENDC}")
        time.sleep(0.5)
        print(f"{Color.OKGREEN}Enviando orden a cocina...{Color.ENDC}")
        time.sleep(1)
        print(f"{Color.BOLD}{Color.OKGREEN}¡Gracias por tu compra!{Color.ENDC}\n")
        
        # Limpiar pedido
        self.pedido = {}
        return True


class BusinessSystem:
    """Sistema principal de gestión de negocios"""
    
    def __init__(self):
        self.config = ConfigManager.cargar_config()
        self.menu_manager = MenuManager(self.config)
        self.auth_manager = AuthManager(self.config)
        Logger.info("Sistema iniciado")
    
    def ejecutar(self):
        """Ejecuta el sistema principal"""
        self.menu_manager._mostrar_header()
        print(f"{Color.BOLD}Bienvenido al {self.config['business_name']}{Color.ENDC}\n")
        
        rol = self._solicitar_rol()
        username, password = self._solicitar_credenciales()
        
        if not self.auth_manager.autenticar(username, password, rol):
            print(f"\n{Color.FAIL}Credenciales incorrectas. Acceso denegado.{Color.ENDC}")
            Logger.warning(f"Acceso denegado para usuario: {username}")
            time.sleep(2)
            return
        
        print(f"\n{Color.OKGREEN}Acceso concedido. Bienvenido, {username}!{Color.ENDC}")
        time.sleep(1)
        
        if rol == 'admin':
            self._menu_administrador()
        else:
            self._menu_usuario(username)
    
    def _solicitar_rol(self) -> str:
        """Solicita el rol del usuario"""
        while True:
            print(f"{Color.OKCYAN}Seleccione su rol:{Color.ENDC}")
            print(f"  1. {Color.OKBLUE}Administrador{Color.ENDC}")
            print(f"  2. {Color.OKBLUE}Usuario{Color.ENDC}")
            
            opcion = input(f"\n{Color.BOLD}Opción: {Color.ENDC}").strip()
            
            if opcion == '1':
                return 'admin'
            elif opcion == '2':
                return 'user'
            else:
                print(f"{Color.FAIL}Opción inválida. Intente nuevamente.{Color.ENDC}\n")
    
    def _solicitar_credenciales(self) -> Tuple[str, str]:
        """Solicita credenciales del usuario"""
        print()
        username = input(f"{Color.BOLD}Usuario: {Color.ENDC}").strip()
        password = input(f"{Color.BOLD}Contraseña: {Color.ENDC}").strip()
        return username, password
    
    def _menu_administrador(self):
        """Menú del administrador"""
        while True:
            print(f"\n{Color.BOLD}{Color.HEADER}{'─'*60}{Color.ENDC}")
            print(f"{Color.BOLD}{Color.HEADER}  PANEL DE ADMINISTRACIÓN{Color.ENDC}")
            print(f"{Color.BOLD}{Color.HEADER}{'─'*60}{Color.ENDC}\n")
            
            print(f"{Color.OKCYAN}1.{Color.ENDC} Ver menú")
            print(f"{Color.OKCYAN}2.{Color.ENDC} Agregar producto")
            print(f"{Color.OKCYAN}3.{Color.ENDC} Eliminar producto")
            print(f"{Color.OKCYAN}4.{Color.ENDC} Modificar precio")
            print(f"{Color.OKCYAN}5.{Color.ENDC} Ver reporte de ventas")
            print(f"{Color.OKCYAN}6.{Color.ENDC} Ver últimas transacciones")
            print(f"{Color.OKCYAN}7.{Color.ENDC} Crear backup manual")
            print(f"{Color.OKCYAN}8.{Color.ENDC} {Color.FAIL}Salir{Color.ENDC}")
            
            opcion = input(f"\n{Color.BOLD}Seleccione una opción: {Color.ENDC}").strip()
            
            if opcion == '1':
                self.menu_manager.mostrar_menu(False)
            elif opcion == '2':
                self._agregar_producto()
            elif opcion == '3':
                self._eliminar_producto()
            elif opcion == '4':
                self._modificar_precio()
            elif opcion == '5':
                ReportManager.generar_reporte_ventas()
            elif opcion == '6':
                ReportManager.generar_reporte_transacciones()
            elif opcion == '7':
                ConfigManager.crear_backup()
                print(f"{Color.OKGREEN}Backup creado exitosamente{Color.ENDC}")
            elif opcion == '8':
                print(f"\n{Color.OKGREEN}Cerrando sesión...{Color.ENDC}")
                time.sleep(1)
                break
            else:
                print(f"{Color.FAIL}Opción inválida{Color.ENDC}")
    
    def _agregar_producto(self):
        """Interfaz para agregar producto"""
        print(f"\n{Color.BOLD}Agregar Nuevo Producto{Color.ENDC}")
        print(f"{Color.OKCYAN}{'─'*60}{Color.ENDC}")
        
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print(f"{Color.FAIL}Nombre inválido{Color.ENDC}")
            return
        
        try:
            precio = float(input("Precio: ").strip())
            if precio <= 0:
                print(f"{Color.FAIL}El precio debe ser mayor a 0{Color.ENDC}")
                return
            
            self.menu_manager.agregar_producto(nombre, precio)
        except ValueError:
            print(f"{Color.FAIL}Precio inválido. Debe ser un número{Color.ENDC}")
    
    def _eliminar_producto(self):
        """Interfaz para eliminar producto"""
        self.menu_manager.mostrar_menu(False)
        nombre = input(f"\n{Color.BOLD}Nombre del producto a eliminar: {Color.ENDC}").strip()
        
        if nombre:
            confirmar = input(f"{Color.WARNING}¿Está seguro? (sí/no): {Color.ENDC}").strip().lower()
            if confirmar in ['sí', 'si', 'yes', 's']:
                self.menu_manager.eliminar_producto(nombre)
    
    def _modificar_precio(self):
        """Interfaz para modificar precio"""
        self.menu_manager.mostrar_menu(False)
        nombre = input(f"\n{Color.BOLD}Nombre del producto: {Color.ENDC}").strip()
        
        if nombre and nombre in self.menu_manager.menu:
            try:
                nuevo_precio = float(input(f"Nuevo precio (actual: {self.menu_manager.currency}{self.menu_manager.menu[nombre]}): ").strip())
                if nuevo_precio <= 0:
                    print(f"{Color.FAIL}El precio debe ser mayor a 0{Color.ENDC}")
                    return
                
                self.menu_manager.modificar_precio(nombre, nuevo_precio)
            except ValueError:
                print(f"{Color.FAIL}Precio inválido{Color.ENDC}")
        else:
            print(f"{Color.FAIL}Producto no encontrado{Color.ENDC}")
    
    def _menu_usuario(self, username: str):
        """Menú del usuario"""
        order_manager = OrderManager(self.menu_manager)
        
        while True:
            print(f"\n{Color.BOLD}{Color.OKBLUE}{'─'*60}{Color.ENDC}")
            print(f"{Color.BOLD}{Color.OKBLUE}  REALIZAR PEDIDO{Color.ENDC}")
            print(f"{Color.BOLD}{Color.OKBLUE}{'─'*60}{Color.ENDC}\n")
            
            print(f"{Color.OKCYAN}1.{Color.ENDC} Ver menú")
            print(f"{Color.OKCYAN}2.{Color.ENDC} Agregar producto al carrito")
            print(f"{Color.OKCYAN}3.{Color.ENDC} Ver carrito")
            print(f"{Color.OKCYAN}4.{Color.ENDC} Procesar pago")
            print(f"{Color.OKCYAN}5.{Color.ENDC} {Color.FAIL}Cancelar y salir{Color.ENDC}")
            
            opcion = input(f"\n{Color.BOLD}Seleccione una opción: {Color.ENDC}").strip()
            
            if opcion == '1':
                self.menu_manager.mostrar_menu(False)
            elif opcion == '2':
                self._agregar_al_carrito(order_manager)
            elif opcion == '3':
                order_manager.mostrar_pedido()
            elif opcion == '4':
                if order_manager.procesar_pago(username):
                    time.sleep(2)
                    break
            elif opcion == '5':
                print(f"\n{Color.WARNING}Pedido cancelado{Color.ENDC}")
                time.sleep(1)
                break
            else:
                print(f"{Color.FAIL}Opción inválida{Color.ENDC}")
    
    def _agregar_al_carrito(self, order_manager: OrderManager):
        """Interfaz para agregar productos al carrito"""
        self.menu_manager.mostrar_menu(False)
        
        producto = input(f"\n{Color.BOLD}Nombre del producto: {Color.ENDC}").strip()
        
        if not producto:
            return
        
        try:
            cantidad = int(input(f"{Color.BOLD}Cantidad: {Color.ENDC}").strip())
            if cantidad <= 0:
                print(f"{Color.FAIL}La cantidad debe ser mayor a 0{Color.ENDC}")
                return
            
            order_manager.agregar_item(producto, cantidad)
        except ValueError:
            print(f"{Color.FAIL}Cantidad inválida{Color.ENDC}")


def main():
    """Función principal"""
    try:
        system = BusinessSystem()
        system.ejecutar()
    except KeyboardInterrupt:
        print(f"\n\n{Color.WARNING}Programa interrumpido por el usuario{Color.ENDC}")
        Logger.warning("Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n{Color.FAIL}Error inesperado: {e}{Color.ENDC}")
        Logger.error(f"Error inesperado: {e}")
    finally:
        print(f"\n{Color.BOLD}Gracias por usar el sistema{Color.ENDC}\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
