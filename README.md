# Sistema de Monitoreo con Tolerancia a Fallas

## Problema

En muchas aplicaciones críticas es necesario asegurar que el servicio principal
permanezca activo. Si el proceso falla, el sistema debe poder recuperarse
automáticamente sin intervención humana.

## Ejecución en segundo plano

Se utiliza un proceso demonio que monitorea constantemente el estado del
servicio principal. Este monitor se ejecuta en segundo plano y verifica
periódicamente si el proceso sigue activo.

## Posibles fallas

El servicio principal puede fallar inesperadamente debido a errores internos,
problemas de memoria o condiciones externas.

En este proyecto se simula una falla aleatoria del sistema.

## Estrategia de tolerancia a fallas

Se implementa un proceso monitor (demonio) que:

    1. Inicia el servicio principal
    2. Verifica periódicamente si sigue activo
    3. Si detecta que el servicio terminó inesperadamente,
       lo reinicia automáticamente.

## Características implementadas

    - Procesos en segundo plano
    - Monitoreo continuo
    - Reinicio automático de procesos
    - Manejo de señales del sistema (SIGTERM y SIGINT)
    - Registro persistente de eventos en archivo log
