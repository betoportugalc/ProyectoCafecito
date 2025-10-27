
<center><h1> PROYECTO CAFECITO ☕ </h1>
<h2>Sistema de Gestión y Pedidos para Café Virtual</h2>Proyecto Académico - TECSUP 2025

</center>

--------------

##  Descripción General

**CAFECITO** es un sistema desarrollado con el propósito de **digitalizar y optimizar la operación de un café ficticio lo mas parecido a uno real**.  
Integra en un solo entorno los procesos de **pedido, cocina, pago, administración y soporte**, mejorando la eficiencia, reduciendo errores y ofreciendo una experiencia moderna para el cliente y el personal.

El proyecto combina el uso de **PSeInt** (para diseño lógico) y **Python** (para implementación práctica).


##  Estructura del Sistema

El sistema se compone de **8 módulos principales**, diseñados de forma **modular e incremental**, lo que facilita su comprensión, mantenimiento y expansión futura.
<br>
<br>

###  1.Pedido del Cliente

###  Objetivo
Permitir que el cliente explore la carta de productos del café, seleccione lo que desea consumir y genere un pedido inicial.

###  Descripción del proceso
- El cliente navega por el menú digital o físico del establecimiento.  
- Selecciona los productos de su preferencia.  
- Puede agregar, modificar o eliminar ítems antes de confirmar el pedido.  
- Una vez conforme, el pedido queda registrado y visible para el mozo.

###  Resultado final
Se genera un pedido preliminar que será atendido por el mozo para su confirmación y envío a cocina.

###  Relación con otros módulos
Conecta con el **módulo del Mozo**, quien valida el pedido y lo remite al área de **Cocina**.

<br>

###  2.Registro y Envío del Pedido

###  Objetivo
Registrar formalmente el pedido del cliente y enviarlo al sistema de cocina para su preparación.

###  Descripción del proceso
- El mozo recibe el pedido (oralmente o desde el sistema).  
- Verifica la disponibilidad de los productos y registra cualquier modificación.  
- Envía el pedido confirmado al sistema de cocina.  
- Supervisa el estado del pedido hasta su entrega.

###  Resultado final
El pedido confirmado queda registrado en el sistema y visible en la pantalla de cocina.

###  Relación con otros módulos
Conecta con el **módulo de Cocina** y posteriormente con el de **Confirmación y Pago**.

<br>

###  3.Preparación en Cocina

###  Objetivo
Gestionar la preparación de los pedidos confirmados, mostrando las órdenes en cola de manera organizada y eficiente.

###  Descripción del proceso
- El sistema de cocina recibe los pedidos enviados por los mozos.  
- El personal inicia la preparación según el orden de llegada.  
- Cuando un pedido está listo, se marca como “Finalizado”.  
- Se notifica al mozo para la entrega al cliente.

###  Resultado final
Los pedidos se completan y quedan listos para ser entregados o servidos.

###  Relación con otros módulos
Conecta con el **Mozo** (para la entrega) y con el módulo de **Confirmación y Pago**.

<br>

###  4.Confirmación y Recepción de Pago

###  Objetivo
Registrar la confirmación del pedido entregado y procesar el pago correspondiente.

###  Descripción del proceso
- El mozo confirma que el pedido ha sido entregado.  
- Se genera la orden de pago con el detalle del consumo.  
- El cliente elige el método de pago (efectivo, tarjeta, etc.).  
- El pago es verificado y registrado en el sistema.

###  Resultado final
El pago del pedido queda confirmado y validado, cerrando el ciclo de venta.

###  Relación con otros módulos
Vinculado con el **módulo de Caja / Registro de Pagos** y **Gerencia** para control y reportes.

<br>

###  5.Gestión de Problemas

###  Objetivo
Identificar, registrar y resolver incidentes operativos o fallas del sistema que puedan afectar el servicio.

###  Descripción del proceso
- Se detecta un problema (error de pedido, falla técnica, etc.).  
- El incidente se registra con nivel de prioridad.  
- El responsable analiza la causa y aplica la solución.  
- Se actualiza el estado del problema (pendiente, en revisión, resuelto).

###  Resultado final
Los problemas quedan documentados y controlados, garantizando la continuidad del servicio.

###  Relación con otros módulos
Puede conectarse con cualquier otro módulo (especialmente **Cocina**, **Mozo** o **Pagos**).

<br>

###  6.Caja / Registro de Pagos

###  Objetivo
Centralizar y registrar todos los pagos realizados, asegurando el control financiero diario.

###  Descripción del proceso
- El sistema recibe las confirmaciones de pago.  
- Se registran los montos, métodos de pago y número de pedido.  
- Se generan reportes diarios de ingresos.  
- Los datos se envían al módulo de Gerencia.

###  Resultado final
Los pagos quedan consolidados en un registro contable y financiero.

###  Relación con otros módulos
Conecta con **Confirmación y Pago**, **Gerencia** y **Proveedores** (para control de gastos).

<br>

###  7.Gerencia / Supervisión y Reportes

###  Objetivo
Proporcionar a la administración una visión general del desempeño del café mediante reportes de ventas, productividad y eficiencia.

###  Descripción del proceso
- El sistema recopila información de los módulos de pedidos, pagos y caja.  
- Genera reportes automáticos de ingresos, rotación y tiempos de atención.  
- Permite visualizar alertas de incidencias o demoras.  
- Exporta datos para análisis contable o decisiones gerenciales.

###  Resultado final
La gerencia obtiene información actualizada para mejorar la gestión y la toma de decisiones.

###  Relación con otros módulos
Conecta con **Caja**, **Proveedores** y **Gestión de Problemas**.

<br>

###  8.Gestión de Proveedores e Insumos

###  Objetivo
Controlar el abastecimiento de productos e insumos necesarios para la operación del café.

###  Descripción del proceso
- Se registran los proveedores y los productos ofrecidos.  
- Se generan órdenes de compra según la demanda.  
- Se actualiza el inventario al recibir los suministros.  
- Se notifican faltantes o retrasos.

###  Resultado final
El sistema mantiene un control eficiente del stock e insumos, garantizando la continuidad del servicio.

###  Relación con otros módulos
Vinculado con **Cocina** (por uso de insumos) y **Gerencia** (por control de gastos y reposiciones).
<br>


## Futuras Implementaciones

**- Control de Mesas y Reservas:**  
   Visualización de mesas ocupadas, libres y reservadas.  
   Gestión de horarios de reserva por cliente.  

**- Panel Estadístico en Tiempo Real:**  
   Reportes dinámicos de pedidos, ventas y productividad.  

**- Integración con Base de Datos en la Nube:**  
   Sincronización de datos y respaldo automático.  

**- App móvil (versión futura):**  
   Pedidos y pagos desde dispositivos móviles.

<br>

## Metodologia

Se empleó una **metodología incremental y modular**, desarrollando el sistema por etapas:

1. **Análisis y diseño lógico (PSeInt)**  
2. **Desarrollo del código base en Python**  
3. **Integración de módulos y pruebas**  
4. **Documentación y mejora continua**

<br>

## Herramientas Utilizadas

| Tipo | Herramienta |
|------|--------------|
| Lenguaje | Python |
| Diseño lógico | PSeInt |
| Entorno de desarrollo | VS Code |
| Control de versiones | GitHub |
| Documentación | Word, PDF, Excel |
<br>

## Conclusión

El proyecto **CAFECITO** representa una solución tecnológica moderna y escalable para la gestión integral de cafés. 
Su enfoque modular permite **eficiencia operativa, reducción de errores y mayor control administrativo**, además de sentar las bases para una futura **plataforma completa de gestión gastronómica**.
<br>
