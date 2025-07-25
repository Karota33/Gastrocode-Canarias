# Resumen de MVP Ideal

## Funcionalidades Imprescindibles para la Primera Versión

Basado en el análisis exhaustivo del sector y la validación de la hipótesis sobre la relación entre madurez de gestión y rentabilidad, se han identificado las funcionalidades imprescindibles para el MVP (Producto Mínimo Viable) de la solución digital para gestión de costos operativos en restauración canaria.

### 1. Gestión Básica de Inventario y Compras

**Justificación**: El control de inventario es el punto de partida para la optimización de costos. La evidencia muestra que la transición de G0 a G1 (que incluye control básico de inventario) genera una mejora promedio de +10,1 puntos porcentuales en el margen neto.

**Funcionalidades específicas**:
- Registro de productos e ingredientes con categorización
- Control de stock mínimo y alertas de reposición
- Registro de proveedores y precios
- Generación de órdenes de compra básicas
- Registro de entradas y salidas de inventario

**Alcance del MVP**: Enfoque en usabilidad y simplicidad, priorizando los 20-30 ingredientes/productos más relevantes para cada tipo de negocio.

### 2. Escandallos Digitales y Análisis de Rentabilidad

**Justificación**: Los escandallos (fichas técnicas con costos) son fundamentales para conocer la rentabilidad real de cada plato. Todos los segmentos analizados muestran mejoras significativas al implementar esta funcionalidad.

**Funcionalidades específicas**:
- Creación de recetas con ingredientes y cantidades
- Cálculo automático del costo por plato
- Análisis de margen por producto
- Clasificación básica de productos (alta/baja rentabilidad, alta/baja popularidad)
- Sugerencias simples de optimización (ajuste de porciones, precios o ingredientes)

**Alcance del MVP**: Interfaz intuitiva que permita crear escandallos sin conocimientos técnicos avanzados.

### 3. Planificación Básica de Personal

**Justificación**: Los costos de personal representan entre el 25-47% de los ingresos según el tipo de negocio. La optimización de turnos y plantilla tiene un impacto directo y significativo en la rentabilidad.

**Funcionalidades específicas**:
- Registro de empleados y posiciones
- Creación de turnos y horarios
- Cálculo básico de costos laborales
- Visualización de cobertura por franjas horarias
- Exportación de planillas para empleados

**Alcance del MVP**: Enfoque en planificación manual asistida, sin algoritmos complejos de optimización automática.

### 4. Dashboard de KPIs Básicos

**Justificación**: La visibilidad de indicadores clave es fundamental para la toma de decisiones. La transición de gestión reactiva (G0) a gestión basada en datos (G2-G3) muestra mejoras de hasta 25 puntos porcentuales en el margen.

**Funcionalidades específicas**:
- Ventas diarias, semanales y mensuales
- Costos de materia prima (% sobre ventas)
- Costos de personal (% sobre ventas)
- Top 10 productos más vendidos
- Top 10 productos más rentables
- Evolución de márgenes

**Alcance del MVP**: Dashboard simple, visual e intuitivo, con métricas actualizadas diariamente.

### 5. Control Básico de Mermas

**Justificación**: Las mermas representan entre un 5-15% del costo total de alimentos. Su control sistemático puede mejorar significativamente la rentabilidad, especialmente en pastelerías y restaurantes.

**Funcionalidades específicas**:
- Registro de productos desechados
- Categorización por causa (caducidad, errores, devoluciones)
- Valoración económica de las mermas
- Informes básicos de tendencias
- Alertas de productos próximos a caducar

**Alcance del MVP**: Interfaz simple para registro rápido durante la operación diaria.

## Módulos para Fases Posteriores

Los siguientes módulos, aunque valiosos, pueden dejarse fuera del MVP inicial para garantizar un desarrollo ágil y enfocado:

### 1. Predicción Avanzada de Demanda (IA)

**Justificación para exclusión**: Aunque impactante, requiere acumulación de datos históricos y desarrollo de algoritmos complejos. El MVP puede funcionar con previsiones manuales básicas.

**Consideraciones**: Preparar la arquitectura de datos para facilitar su implementación futura.

### 2. Integración con Plataformas de Delivery

**Justificación para exclusión**: Relevante solo para segmentos específicos (delivery, dark kitchens) y requiere desarrollo de APIs específicas para cada plataforma.

**Consideraciones**: Diseñar el sistema con capacidad de expansión para estas integraciones.

### 3. Optimización Energética y de Suministros

**Justificación para exclusión**: Aunque valioso, tiene menor impacto inmediato que las funcionalidades core de control de alimentos y personal.

**Consideraciones**: Incluir campos básicos para registro manual de consumos, preparando la base para funcionalidades futuras.

### 4. Gestión Avanzada Multi-Local

**Justificación para exclusión**: La mayoría de negocios en Canarias son mono-local. La complejidad adicional no justifica su inclusión en el MVP.

**Consideraciones**: Diseñar la arquitectura de datos contemplando la futura expansión a gestión multi-local.

### 5. Marketing y Fidelización de Clientes

**Justificación para exclusión**: Aunque complementario, el foco del MVP debe ser la optimización de costos operativos.

**Consideraciones**: Preparar la estructura de datos de clientes para futuras funcionalidades de marketing.

## Arquitectura Técnica Recomendada para el MVP

### Enfoque Cloud-First
- Aplicación web responsive accesible desde cualquier dispositivo
- Posibilidad de funcionamiento offline básico con sincronización posterior
- Almacenamiento seguro en la nube

### Interfaz de Usuario
- Diseño intuitivo optimizado para uso en entorno de restauración
- Flujos de trabajo simplificados para tareas frecuentes
- Adaptación a pantallas táctiles y dispositivos móviles

### Integración con Sistemas Existentes
- API para conexión con TPVs comunes en Canarias
- Exportación de datos en formatos estándar (CSV, Excel)
- Importación inicial de catálogos de productos

## Roadmap Sugerido Post-MVP

### Fase 1 (1-3 meses post-MVP)
- Refinamiento de funcionalidades core basado en feedback de usuarios
- Mejora de reportes y visualizaciones
- Optimización de rendimiento y usabilidad

### Fase 2 (4-6 meses post-MVP)
- Implementación de predicción básica de demanda
- Integración con principales TPVs
- Funcionalidades avanzadas de escandallos

### Fase 3 (7-12 meses post-MVP)
- Algoritmos de IA para optimización de compras y personal
- Integración con plataformas de delivery
- Módulo de optimización energética

## Conclusión

El MVP propuesto se centra en las funcionalidades con mayor impacto inmediato en la rentabilidad, priorizando la facilidad de adopción y el valor percibido por los usuarios. Este enfoque permitirá validar rápidamente la propuesta de valor con usuarios reales, generando mejoras tangibles en su gestión de costos mientras se establece la base para funcionalidades más avanzadas en fases posteriores.

La evidencia recopilada sugiere que incluso con estas funcionalidades básicas, un negocio podría transicionar de nivel G0-G1 a nivel G2, lo que representa una mejora promedio de +18 puntos porcentuales en el margen neto.
