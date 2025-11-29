# Guía de Contribución

Gracias por tu interés en contribuir al Sistema de Gestión de Negocios. Este documento proporciona pautas para contribuir al proyecto.

## Tabla de Contenidos

1. [Código de Conducta](#código-de-conducta)
2. [Cómo Contribuir](#cómo-contribuir)
3. [Estándares de Código](#estándares-de-código)
4. [Proceso de Pull Request](#proceso-de-pull-request)
5. [Reportar Bugs](#reportar-bugs)
6. [Sugerir Mejoras](#sugerir-mejoras)

## Código de Conducta

### Mi Compromiso

Este proyecto se compromete a proporcionar un ambiente acogedor y libre de acoso para todos, independientemente de edad, tamaño corporal, discapacidad, etnia, identidad de género, nivel de experiencia, nacionalidad, apariencia personal, raza, religión o identidad sexual.

### Comportamiento Esperado

- Uso de lenguaje acogedor e inclusivo
- Respeto a diferentes puntos de vista y experiencias
- Aceptación de crítica constructiva
- Enfoque en lo que es mejor para la comunidad
- Empatía hacia otros miembros

## Cómo Contribuir

### Reportar Bugs

Antes de crear un reporte de bug, verifica que el problema no haya sido reportado previamente. Si el bug existe:

1. Usa un título claro y descriptivo
2. Describe los pasos exactos para reproducir el problema
3. Proporciona ejemplos específicos
4. Describe el comportamiento observado vs. esperado
5. Incluye capturas de pantalla si es relevante
6. Especifica tu entorno (OS, versión de Python)

**Ejemplo de reporte**:

```markdown
**Descripción del Bug**
El sistema falla al guardar productos con nombres que contienen comillas

**Pasos para Reproducir**
1. Iniciar sesión como administrador
2. Seleccionar "Agregar producto"
3. Ingresar nombre: Pizza "Especial"
4. Ingresar precio: 15.00
5. Confirmar

**Comportamiento Esperado**
El producto debería guardarse correctamente

**Comportamiento Actual**
JSONDecodeError al intentar guardar

**Entorno**
- OS: macOS 13.0
- Python: 3.9.7
- Versión: 2.0
```

### Sugerir Mejoras

Las sugerencias de mejoras son bienvenidas. Incluye:

1. Título claro de la funcionalidad
2. Descripción detallada del comportamiento propuesto
3. Casos de uso específicos
4. Mockups o ejemplos si aplica
5. Análisis de implementación si es posible

### Tu Primera Contribución

¿No sabes por dónde empezar? Busca issues etiquetados como:
- `good-first-issue` - problemas adecuados para principiantes
- `help-wanted` - issues que necesitan atención

### Pull Requests

1. Fork el repositorio
2. Crea una rama desde `main`
3. Realiza tus cambios
4. Asegúrate de que el código cumple los estándares
5. Actualiza la documentación si es necesario
6. Commit tus cambios
7. Push a tu fork
8. Abre un Pull Request

## Estándares de Código

### Estilo de Python

Seguimos [PEP 8](https://pep8.org/) con algunas adaptaciones:

```python
# Usar 4 espacios para indentación
def funcion_ejemplo():
    if condicion:
        hacer_algo()

# Nombres de clases en PascalCase
class MiClase:
    pass

# Nombres de funciones y variables en snake_case
def mi_funcion():
    mi_variable = 10

# Constantes en MAYÚSCULAS
MAX_CONEXIONES = 100

# Type hints siempre que sea posible
def calcular_total(precio: float, cantidad: int) -> float:
    return precio * cantidad
```

### Documentación

Usa docstrings para todas las clases y funciones:

```python
def procesar_pedido(pedido: dict, usuario: str) -> bool:
    """
    Procesa un pedido y registra la transacción.
    
    Args:
        pedido (dict): Diccionario con productos y cantidades
        usuario (str): Nombre del usuario que realiza el pedido
    
    Returns:
        bool: True si el pedido se procesó exitosamente
    
    Raises:
        ValueError: Si el pedido está vacío
        KeyError: Si un producto no existe en el menú
    """
    pass
```

### Estructura de Commits

Usa mensajes de commit descriptivos:

```
tipo(alcance): descripción breve

Descripción más detallada si es necesaria.

- Punto adicional 1
- Punto adicional 2
```

**Tipos de commit**:
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Formato, punto y coma faltantes, etc
- `refactor`: Refactorización de código
- `test`: Agregar tests
- `chore`: Actualización de tareas de construcción, etc

**Ejemplos**:
```
feat(menu): agregar soporte para categorías de productos

Implementa sistema de categorías que permite:
- Organizar productos por tipo
- Filtrar menú por categoría
- Reportes por categoría

fix(auth): corregir validación de contraseñas con espacios

Las contraseñas que contenían espacios no se validaban
correctamente debido a un trim() no intencional.

docs(readme): actualizar guía de instalación

Agregar instrucciones específicas para Windows 11
```

## Proceso de Pull Request

### Checklist antes de enviar

- [ ] El código sigue los estándares del proyecto
- [ ] He comentado mi código, especialmente en áreas difíciles
- [ ] He actualizado la documentación según sea necesario
- [ ] Mis cambios no generan nuevas advertencias
- [ ] He agregado tests que prueban mi fix o funcionalidad
- [ ] Tests nuevos y existentes pasan localmente

### Revisión

Tu PR será revisado por los mantenedores. Pueden:
- Aprobar y hacer merge
- Solicitar cambios
- Cerrar el PR con explicación

Se paciente y receptivo a los comentarios.

## Áreas de Contribución

### Código

- Nuevas funcionalidades
- Corrección de bugs
- Optimización de rendimiento
- Refactorización

### Documentación

- Mejorar README
- Crear tutoriales
- Documentar APIs
- Traducir documentación

### Testing

- Crear tests unitarios
- Tests de integración
- Tests de rendimiento

### Diseño

- Mejorar UI/UX de terminal
- Diseñar mockups para versión web
- Optimizar visualización de datos

## Roadmap del Proyecto

### Versión 2.1 (Próxima)
- [ ] Tests unitarios completos
- [ ] Sistema de categorías
- [ ] Control de inventario con stock
- [ ] Exportación de reportes a PDF

### Versión 3.0 (Futuro)
- [ ] API REST con FastAPI
- [ ] Base de datos PostgreSQL
- [ ] Frontend web con React
- [ ] Sistema multi-tienda

## Recursos para Contribuidores

### Documentación Técnica
- [Arquitectura del Sistema](README.md#arquitectura-del-sistema)
- [Guía de API](docs/API.md) (próximamente)

### Herramientas Recomendadas
- Editor: VS Code con Python extension
- Linter: pylint o flake8
- Formatter: black
- Type checker: mypy

### Contacto
- Discusiones: GitHub Discussions
- Issues: GitHub Issues
- Email: (jogobonito029@gmail.com)

## Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la misma licencia que el proyecto.

## Preguntas

¿Tienes preguntas sobre cómo contribuir? Abre un issue con la etiqueta `question` o contacta a los mantenedores.

---

¡Gracias por contribuir al Sistema de Gestión de Negocios! 🚀
