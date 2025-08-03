# Ataque Ping Flood (DoS) en IPv4: Ejecución y Mitigación

Un **Ping Flood** es un tipo de ataque de **Denial-of-Service (DoS)** que busca sobrecargar un sistema objetivo enviando una cantidad masiva y repetitiva de paquetes ICMP "Echo Request" (ping) a una alta frecuencia. Este bombardeo de solicitudes puede saturar la capacidad de procesamiento y el ancho de banda del sistema, impidiendo que maneje tráfico legítimo y provocando una denegación de servicio para los usuarios. Aunque es relativamente simple de ejecutar, puede causar daños significativos en la disponibilidad de los recursos de red, afectando a usuarios legítimos y dificultando el funcionamiento normal de los sistemas.

Este ataque se enfoca principalmente en IPv4 debido a la naturaleza del protocolo ICMP, que es un componente fundamental de IPv4. ICMP (Internet Control Message Protocol) es utilizado por el comando `ping` estándar y no tiene un equivalente directo con las mismas vulnerabilidades en IPv6 para este tipo específico de ataque.

El flujo de un ataque Ping Flood implica que un atacante envíe solicitudes de eco ICMP masivas al sistema objetivo, lo que satura los componentes de red y la capacidad de procesamiento del sistema, resultando en una sobrecarga y, finalmente, en una interrupción del servicio que afecta a los usuarios legítimos.

## Realización de un Ataque Ping Flood

Para demostrar un ataque Ping Flood, se utilizan dos máquinas Ubuntu: una como atacante y otra como víctima.

### 1\. Identificación de Direcciones IP

Primero, se identifican las direcciones IP de ambas máquinas:

  * Máquina de ataque: `10.211.55.17`
  * Máquina de defensa (víctima): `10.211.55.5`

Se puede verificar la dirección IP de cada máquina usando el comando `ip addr`:

```bash
ip addr
```

Este comando muestra las interfaces de red y sus configuraciones IP asociadas.

### 2\. Preparación del Ataque con Hping3

En la máquina atacante, se utiliza la herramienta `hping3` para generar el Ping Flood. Si no está instalada, se puede instalar con `sudo apt install hping3`.

El comando para el Ping Flood es el siguiente:

```bash
sudo hping3 --flood --rand-source --icmp 10.211.55.5
```

  * `sudo`: Ejecuta el comando con privilegios de superusuario.
  * `hping3`: Invoca la herramienta para generar y analizar paquetes.
  * `--flood`: Este parámetro indica que `hping3` debe enviar paquetes lo más rápido posible, sin esperar respuestas, con el fin de saturar la red.
  * `--rand-source`: Este parámetro hace que `hping3` utilice direcciones IP de origen aleatorias para cada paquete enviado. Esto dificulta que los dispositivos de red, como firewalls, **IDS** o **IPS**, bloqueen el ataque basándose en la dirección IP de la fuente, ya que simula que los paquetes provienen de múltiples orígenes.
  * `--icmp`: Indica a `hping3` que genere paquetes **ICMP**, específicamente del tipo "Echo Request" (solicitudes de ping estándar).
  * `10.211.55.5`: Es la dirección IP de la máquina víctima.

### 3\. Monitorización del Ataque con EtherApe

Para visualizar el impacto del ataque en la máquina víctima, se utiliza `EtherApe`, una herramienta de visualización de red en tiempo real.

1.  **Instalar EtherApe en la máquina víctima:**

    ```bash
    sudo apt install etherape
    ```

    Este comando descarga e instala la aplicación `EtherApe`.

2.  **Lanzar EtherApe:**

    ```bash
    sudo etherape
    ```

    Una vez abierto, es crucial verificar que EtherApe esté capturando el tráfico en la interfaz de red correcta (por ejemplo, `eth0`).

3.  **Ejecutar el Ping Flood (desde la máquina atacante):**
    Una vez que EtherApe está abierto y configurado en la máquina víctima, se lanza el ataque `hping3` desde la máquina atacante.

### 4\. Consecuencias del Ataque

Al iniciar el Ping Flood, se observan las siguientes consecuencias en la máquina víctima:

  * **Ralentización del sistema:** La máquina víctima se ralentiza considerablemente.
  * **Saturación de la CPU:** El monitor del sistema de Ubuntu muestra que la utilización de la CPU llega al 100%. Esto se debe a que la CPU está dedicando todos sus recursos a intentar responder a las innumerables solicitudes de eco ICMP.
  * **Congestión de la red:** El historial de la red en el monitor del sistema muestra un tráfico inusual y una saturación significativa, ya que la máquina intenta procesar los paquetes entrantes.
  * **Saturación de la memoria (RAM):** La memoria RAM también se utiliza al máximo para intentar gestionar la avalancha de solicitudes.
  * **Dificultad de visualización en EtherApe:** EtherApe tiene problemas para dibujar correctamente la arquitectura de la red debido a la gran cantidad de nodos y tráfico que intenta procesar, lo que indica la magnitud de la saturación.
  * **Denegación de Servicio:** Si el ataque continúa, la máquina puede llegar a colapsar o provocar errores, impidiendo que pueda prestar servicios legítimos.

## Mitigación de Ataques Ping Flood (DoS)

Para defenderse contra ataques Ping Flood, se pueden implementar varias estrategias de mitigación.

  * **Limitación de tasa (Rate Limiting):**
    Consiste en configurar firewalls y routers para limitar el número de solicitudes ICMP permitidas por segundo, ya sea desde una única fuente o hacia un único destino. Esto evita que un atacante sature la red con un alto volumen de tráfico.

  * **Listas de Control de Acceso (ACLs):**
    Se pueden configurar ACLs en dispositivos de red para bloquear o restringir el tráfico ICMP entrante, o el tráfico dirigido a direcciones IP específicas que no deberían recibir o enviar pings. Las ACLs actúan como filtros de tráfico en función de reglas predefinidas.

  * **Detección de Anomalías:**
    Utilizar sistemas de detección de intrusiones (**IDS**) y sistemas de prevención de intrusiones (**IPS**). Estas herramientas pueden identificar patrones de tráfico inusual, como una inundación ICMP, y tomar acciones para bloquear el tráfico sospechoso.

En resumen, el ataque Ping Flood representa una amenaza significativa para la disponibilidad de la red. Al inundar un objetivo con un exceso de paquetes ICMP Echo Request, provoca una congestión en la red y una interrupción en los servicios. La implementación de estrategias de mitigación como la limitación de tasa, las ACLs y la detección de anomalías es fundamental para defenderse contra este tipo de ataques y preservar la funcionalidad de la red.