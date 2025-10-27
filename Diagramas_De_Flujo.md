# Diagramas de Flujo del Sistema Cafecito

Este documento contiene los diagramas de flujo que describen el funcionamiento completo del sistema de gestión de pedidos **Cafecito**, desde la toma del pedido hasta la administración y resolución de incidencias.

---

##  Diagrama 1: Modulo de toma y registro de pedidos 

```mermaid
flowchart TD
    A[Inicio] --> B[Cliente realiza pedido al mozo]
    B --> C[Mozo registra pedido en sistema POS]
    C --> D{¿Pedido confirmado?}
    D -->|No| B
    D -->|Sí| E[Enviar pedido a la cocina]
    E --> F[Mostrar pedido en pantalla de cocina]
    F --> G[Actualizar estado: En preparación]
    G --> H[Fin]
```

---

##  Diagrama 2: Modulo de produccion

```mermaid
flowchart TD
    A[Inicio] --> B[Recepción automática del pedido desde POS]
    B --> C[Mostrar pedido en pantalla de cocina]
    C --> D{¿Iniciar preparación?}
    D -->|No| C
    D -->|Sí| E[Actualizar estado: En preparación]
    E --> F[Elaborar los productos del pedido]
    F --> G{¿Pedido finalizado?}
    G -->|No| F
    G -->|Sí| H[Actualizar estado: Listo para entrega]
    H --> I[Notificar al mozo que el pedido está listo]
    I --> J[Enviar pedido al módulo de Despacho / Entrega]
    J --> K[Fin]
```

---

##  Diagrama 3: Modulo de despacho y entrega

```mermaid
flowchart TD
    A[Inicio] --> B[Recepción de pedido preparado desde cocina]
    B --> C[Despacho verifica contenido y calidad del pedido]
    C --> D{¿Pedido correcto?}
    D -->|No| E[Registrar incidencia y notificar a cocina]
    D -->|Sí| F{¿Tipo de entrega?}
    F -->|Presencial| G[Notificar al mozo para recogida en despacho]
    F -->|Despacho / Delivery| H[Asignar a repartidor y preparar despacho]
    G --> I[Mozo recoge pedido en área de despacho]
    H --> J[Repartidor recoge pedido en área de despacho]
    I --> K[Confirmar salida del pedido en el sistema]
    J --> K
    K --> L[Actualizar estado a En tránsito / En servicio]
    L --> M[Fin]
```

---

##  Diagrama 4: Modulo de facturacion y pagos

```mermaid
flowchart TD
    A[Inicio] --> B[Pedido entregado desde modulo de despacho]
    B --> C{Pedido completo y sin pendientes}
    C -->|No| D[Esperar confirmacion de cocina o mozo]
    C -->|Si| E[Generar pre factura en sistema POS]
    E --> F[Seleccionar metodo de pago]
    F --> G{Tipo de pago}
    G -->|Efectivo| H[Registrar pago manual en POS]
    G -->|Tarjeta o Transferencia| I[Procesar pago con pasarela]
    H --> J[Confirmar pago recibido]
    I --> J
    J --> K{Pago exitoso}
    K -->|No| L[Notificar soporte y reintentar pago]
    K -->|Si| M[Emitir comprobante electronico]
    M --> N[Actualizar estado a Pagado y Cerrado]
    N --> O[Enviar registro al modulo de administracion]
    O --> P[Fin]
```

---

##  Diagrama 5: Modulo de administracion y reportes

```mermaid
flowchart TD
    A[Inicio] --> B[Ingreso del administrador al sistema]
    B --> C{¿Credenciales válidas?}
    C -->|No| D[Denegar acceso y mostrar mensaje de error]
    C -->|Sí| E[Acceder al panel administrativo]
    E --> F[Seleccionar tipo de reporte o consulta]
    F --> G{¿Reporte de ventas, pedidos o rendimiento?}
    G -->|Ventas| H[Generar reporte de ventas consolidado]
    G -->|Pedidos| I[Mostrar detalle de pedidos atendidos y pendientes]
    G -->|Rendimiento| J[Calcular métricas de eficiencia del personal]
    H --> K[Exportar o imprimir reporte]
    I --> K
    J --> K
    K --> L[Registrar auditoría del acceso]
    L --> M[Fin]
```

---

##  Diagrama 6: Modulo de abastecimiento e inventario

```mermaid
flowchart TD
    A[Inicio] --> B[Verificar existencias en inventario]
    B --> C{¿Stock suficiente?}
    C -->|Sí| D[Registrar uso de insumos en cocina]
    C -->|No| E[Generar alerta de reposición]
    E --> F[Registrar solicitud de compra o pedido al proveedor]
    F --> G[Registrar ingreso de nuevos insumos al almacén]
    G --> H[Actualizar inventario general]
    D --> H
    H --> I[Registrar fecha de actualización y responsable]
    I --> J[Generar reporte de movimientos e inventario]
    J --> K[Enviar información al módulo de administración]
    K --> L[Fin]
```

---

##  Diagrama 7: Modulo de soporte y mantenimiento del sistema 

```mermaid
flowchart TD
    A[Inicio] --> B[Recepción de alerta o incidencia]
    B --> C[Registrar incidente en el sistema]
    C --> D[Clasificar nivel de severidad]
    D --> E{¿Error crítico?}
    E -->|Sí| F[Notificar de inmediato al administrador del sistema]
    E -->|No| G[Asignar incidencia a soporte técnico]
    F --> H[Ejecutar diagnóstico y solución prioritaria]
    G --> H
    H --> I[Verificar resolución del problema]
    I --> J{¿Incidencia resuelta?}
    J -->|No| K[Escalar caso a nivel superior]
    J -->|Sí| L[Registrar solución y cerrar incidencia]
    L --> M[Actualizar bitácora de mantenimiento]
    M --> N[Generar reporte periódico al módulo de administración]
    N --> O[Fin]
```

---

## 📘 Descripción General

Estos diagramas representan el flujo lógico y funcional de los principales módulos del sistema:

- **Diagrama 1**: Modulo de toma y registro de pedidos 
- **Diagrama 2**: Modulo de produccion 
- **Diagrama 3**: Modulo de despacho y entrega 
- **Diagrama 4**: Modulo de facturacion y pagos  
- **Diagrama 5**: Modulo de administracion y reportes
- **Diagrama 6**: Modulo de abastecimiento e inventario
- **Diagrama 7**: Modulo de soporte y mantenimiento del sistema  

Proyecto Universitario de Gestión Cafecito



