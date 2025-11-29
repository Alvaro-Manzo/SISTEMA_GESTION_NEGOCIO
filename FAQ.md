# Preguntas Frecuentes (FAQ)

## Índice
1. [General](#general)
2. [Instalación](#instalación)
3. [Configuración](#configuración)
4. [Uso](#uso)
5. [Problemas Comunes](#problemas-comunes)
6. [Desarrollo](#desarrollo)

## General

### ¿Para qué sirve este sistema?
Es un sistema de punto de venta (POS) y gestión de inventario diseñado para negocios pequeños y medianos. Permite administrar productos, procesar ventas, generar reportes y llevar un control completo de las operaciones.

### ¿Qué tipos de negocios pueden usar este sistema?
- Restaurantes y cafeterías
- Tiendas minoristas
- Food trucks
- Panaderías
- Farmacias
- Librerías
- Cualquier negocio que venda productos

### ¿Es gratuito?
Sí, el sistema es completamente gratuito y de código abierto bajo licencia MIT.

### ¿Necesito conexión a Internet?
No, el sistema funciona completamente offline. Toda la información se almacena localmente.

### ¿Puedo usar este sistema en producción?
El sistema está diseñado para uso educativo y negocios pequeños. Para producción a gran escala, se recomienda implementar las mejoras de seguridad sugeridas en el README.

## Instalación

### ¿Qué necesito instalar?
Solo necesitas Python 3.6 o superior. No hay dependencias externas.

### ¿Funciona en Windows?
Sí, funciona en Windows, macOS y Linux. En Windows se recomienda usar Windows Terminal o PowerShell para mejor visualización de colores.

### ¿Cómo verifico que está instalado correctamente?
Ejecuta `python3 test_system.py` para verificar todos los requisitos.

### Error al instalar en Mac
Si recibes errores de permisos en Mac:
```bash
# Usar python3 explícitamente
python3 main.py

# Si sigue fallando, verificar instalación
which python3
python3 --version
```

## Configuración

### ¿Cómo cambio el nombre de mi negocio?
Edita el archivo `inventory.json` y modifica el valor de `business_name`.

### ¿Puedo usar otra moneda?
Sí, cambia el valor de `currency` en `inventory.json`. Ejemplos:
- Dólar: "$"
- Euro: "€"
- Peso mexicano: "MXN $"
- Peso colombiano: "COP $"

### ¿Cómo agrego nuevos usuarios?
Edita `inventory.json` y agrega usuarios en la sección correspondiente:

```json
{
  "users": {
    "admin": {
      "nuevo_admin": "contraseña_segura"
    },
    "regular": {
      "nuevo_usuario": "contraseña"
    }
  }
}
```

### ¿Cómo cambio las contraseñas?
Edita directamente el archivo `inventory.json`. **Importante**: Las contraseñas están en texto plano, no las compartas.

### ¿Puedo tener múltiples administradores?
Sí, puedes agregar tantos administradores como necesites en la sección `users.admin`.

## Uso

### ¿Cómo inicio el sistema?
```bash
python3 main.py
```

### ¿Cómo agrego un producto?
1. Inicia sesión como administrador
2. Selecciona opción "Agregar producto"
3. Ingresa nombre y precio
4. El producto se guarda automáticamente

### ¿Puedo eliminar productos?
Sí, los administradores pueden eliminar productos desde el panel de administración.

### ¿Cómo proceso una venta?
1. Inicia sesión como usuario
2. Ver menú
3. Agregar productos al carrito
4. Procesar pago
5. Se genera automáticamente un ID de transacción

### ¿Dónde veo mis ventas?
Los administradores pueden ver:
- Opción 5: Reporte de ventas con estadísticas
- Opción 6: Últimas 10 transacciones
- Archivo `transactions.json` con historial completo

### ¿Se pueden cancelar ventas?
Una vez procesado el pago, la venta queda registrada. No hay función de cancelación integrada (se puede agregar como mejora futura).

### ¿Cómo veo productos más vendidos?
Panel de administración → Opción 5 (Ver reporte de ventas)

## Problemas Comunes

### No veo colores en la terminal
**Solución**: Usa una terminal moderna:
- Windows: Windows Terminal
- Mac: iTerm2 o Terminal.app (nativo)
- Linux: GNOME Terminal, Konsole

### Error: "inventory.json not found"
**Solución**:
```bash
cp config.example.json inventory.json
```
Luego edita `inventory.json` con tus datos.

### Error de JSON inválido
**Solución**:
1. Verifica que uses comillas dobles (")
2. No debe haber comas finales
3. Usa un validador JSON online
4. Restaura desde backup en carpeta `/backups`

### Las contraseñas no funcionan
**Solución**:
- Las contraseñas son case-sensitive (distinguen mayúsculas/minúsculas)
- Verifica que no haya espacios adicionales
- Revisa el archivo `inventory.json`

### No se guardan los cambios
**Solución**:
```bash
# Verifica permisos
ls -la inventory.json

# Dar permisos de escritura
chmod 644 inventory.json
```

### El programa se cierra inesperadamente
**Solución**:
1. Revisa `business.log` para ver el error
2. Verifica la estructura de `inventory.json`
3. Ejecuta `python3 test_system.py`

### Archivo business.log muy grande
**Solución**:
```bash
# Respaldar y limpiar
mv business.log business.log.old
touch business.log
```

## Desarrollo

### ¿Puedo modificar el código?
Sí, el sistema es de código abierto. Lee `CONTRIBUTING.md` para pautas.

### ¿Cómo agrego nuevas funcionalidades?
1. Fork el repositorio
2. Crea una rama para tu funcionalidad
3. Implementa siguiendo los estándares de código
4. Crea un Pull Request

### ¿Puedo integrarlo con una base de datos?
Sí, puedes extender las clases para usar PostgreSQL, MySQL u otro motor de base de datos.

### ¿Se puede crear una versión web?
Sí, se puede crear una API REST con FastAPI y un frontend con React/Vue. Ver sección "Extendiendo el Sistema" en README.

### ¿Hay tests unitarios?
Actualmente no, pero están en el roadmap para la versión 2.1.

### ¿Puedo comercializar este software?
Sí, la licencia MIT permite uso comercial. Lee el archivo LICENSE para más detalles.

### ¿Dónde reporto bugs?
Abre un issue en GitHub con:
- Descripción del problema
- Pasos para reproducir
- Comportamiento esperado vs. actual
- Información del entorno

### ¿Cómo contribuyo?
Lee el archivo `CONTRIBUTING.md` para información detallada sobre cómo contribuir al proyecto.

### ¿Hay soporte técnico?
El proyecto es mantenido por la comunidad. Puedes:
- Abrir issues en GitHub
- Participar en Discussions
- Consultar la documentación

## Preguntas Adicionales

### ¿Puedo usar esto para mi tarea/proyecto escolar?
Sí, puedes usar este código para fines educativos. Se recomienda entender el código y personalizarlo.

### ¿Funciona en Raspberry Pi?
Sí, mientras tenga Python 3.6+ instalado.

### ¿Puedo conectar un lector de código de barras?
No está implementado nativamente, pero puedes extender el sistema para soportarlo.

### ¿Soporta impresión de tickets?
No actualmente, pero se puede agregar usando librerías como `python-escpos`.

### ¿Hay versión móvil?
No, pero se puede crear una usando frameworks como React Native o Flutter.

### ¿Los backups son automáticos?
Sí, se crea un backup automáticamente cada vez que se modifica el inventario. Se mantienen los últimos 10 backups.

### ¿Puedo exportar reportes?
Actualmente solo se muestran en pantalla. La exportación a PDF/Excel está en el roadmap.

### ¿Hay límite de productos o transacciones?
No hay límite técnico, pero el rendimiento puede verse afectado con miles de registros debido al uso de JSON.

## ¿No encontraste tu pregunta?

Si tu pregunta no está aquí:
1. Revisa la documentación completa en README.md
2. Busca en los issues de GitHub
3. Abre un nuevo issue con tu pregunta
4. Consulta CONTRIBUTING.md para guías de desarrollo

---

**Última actualización**: Noviembre 2025
