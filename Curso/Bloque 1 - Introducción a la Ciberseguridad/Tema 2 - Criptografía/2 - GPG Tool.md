De acuerdo, aquí tienes el informe sin citas ni referencias.

-----

# GPG Tool: Cifrado y Descifrado de Archivos

GPG (GNU Privacy Guard) es una suite de cifrado que permite cifrar, descifrar, firmar y verificar archivos y mensajes. Puede utilizar tanto criptografía simétrica como asimétrica. Además, GPG permite interactuar con servidores de claves públicos en internet para enviar y descargar claves, así como gestionar la revocación de claves.

## ¿Cómo funciona GPG?

GPG se basa en el uso de pares de claves: una clave pública y una clave privada.

  * **Clave Pública:** Es la clave que puedes distribuir libremente a otros usuarios. Se utiliza para cifrar mensajes que solo el poseedor de la clave privada correspondiente podrá descifrar, o para verificar firmas digitales creadas con la clave privada.
  * **Clave Privada:** Es la clave que debes mantener en secreto y proteger. Se utiliza para descifrar mensajes que fueron cifrados con tu clave pública, y para firmar digitalmente archivos, garantizando la autenticidad e integridad de la información.

Cuando generas un par de claves, GPG solicita un nombre y una dirección de correo electrónico, los cuales se asocian a las claves para identificarlas. También te pedirá una frase de contraseña (passphrase) para proteger tu clave privada. Es crucial proteger esta frase, ya que la clave privada es un activo crítico.

Las claves se almacenan en el directorio `.gnupg` en el home del usuario. Cada clave pública tiene una "huella digital" (fingerprint) única, que es una forma de verificar la autenticidad de una clave, especialmente cuando se importa de otro usuario o de un servidor de claves.

GPG también permite generar certificados de revocación para tus claves. Esto es útil en caso de que tu clave privada se vea comprometida o ya no la vayas a utilizar. Al generar un certificado de revocación, puedes especificar la razón de la revocación.

### Servidores de Claves (Keyservers)

Los servidores de claves son repositorios públicos en internet donde los usuarios pueden subir sus claves públicas para que otros las encuentren y descarguen. Esto facilita el intercambio de claves públicas sin necesidad de enviarlas directamente, por ejemplo, por correo electrónico. Puedes buscar claves por dirección de correo electrónico y exportar tu propia clave a un servidor de claves.

## Comandos Esenciales de GPG

A continuación, se listan algunos de los comandos más importantes de GPG:

  * `--generate-key`: Genera un par de claves (pública y privada).
  * `--full-generate-key`: Genera un par de claves con opciones más detalladas.
  * `--list-keys`: Lista las claves almacenadas en tu sistema.
  * `--import <file.key>`: Importa una clave pública desde un archivo.
  * `--export <email>`: Exporta tu clave pública. Puedes usar `--armor` para un formato ASCII legible.
  * `--send-keys --keyserver <domain keyserver> <fingerprint>`: Sube tu clave pública a un servidor de claves.
  * `--search-keys <email>`: Busca claves en un servidor de claves público.
  * `--fingerprint <email>`: Muestra la huella digital (fingerprint) de una clave.
  * `--gen-revoke <email>`: Genera un certificado para revocar una clave.
  * `--encrypt --recipient <email> <file>`: Cifra un archivo para un destinatario específico.
  * `--encrypt --armor --recipient <email> <file>`: Cifra un archivo para un destinatario específico, generando una salida en formato ASCII legible.
  * `--decrypt <file>`: Descifra un archivo.
  * `--sign <file>`: Firma digitalmente un archivo.
  * `--verify <file.sig>`: Verifica la firma digital de un archivo.
  * `--output <file>`: Especifica el nombre del archivo de salida.

## Cifrado y Descifrado Paso a Paso con GPG

A continuación, se explica cómo cifrar, descifrar y firmar archivos desde la terminal.

### 1\. Generar un Par de Claves

Antes de poder cifrar o descifrar, necesitas un par de claves.

**Comando:**

```bash
gpg --generate-key
```

**Pasos:**

1.  Ejecuta el comando.
2.  GPG te pedirá tu nombre real y tu dirección de correo electrónico. Por ejemplo:
      * `Real name: pablogonzalezpe`
      * `Email address: pablo@mypublicinbox.com`
3.  Confirma los datos ingresados (`o` para OK).
4.  Se te solicitará una frase de contraseña (passphrase) para proteger tu clave privada. Introduce una frase segura y confírmala.
5.  GPG generará entropía para crear las claves. Esto puede tardar un poco.
6.  Una vez completado, verás la confirmación de que la clave pública y privada han sido creadas, junto con su fingerprint y fecha de expiración.

**Ejemplo de Salida:**

```
pub   rsa3072 2024-04-11 [SC] [expires: 2026-04-11]
      B6CB7A5DAC39F93A0F45818AA7287AA54BF91913
uid           [ultimate] pablogonzalezpe <pablo@mypublicinbox.com>
sub   rsa3072 2024-04-11 [E] [expires: 2026-04-11]
```

### 2\. Listar Claves

Para ver las claves que tienes en tu sistema:

**Comando:**

```bash
gpg --list-keys
```

**Ejemplo de Salida:**

```
/home/kali/.gnupg/pubring.kbx
pub   rsa3072 2024-04-11 [SC] [expires: 2026-04-11]
      B6CB7A5DAC39F93A0F45818AA7287AA54BF91913
uid           [ultimate] pablogonzalezpe <pablo@mypublicinbox.com>
sub   rsa3072 2024-04-11 [E] [expires: 2026-04-11]
```

### 3\. Crear un Archivo de Ejemplo

Para el proceso de cifrado, vamos a crear un archivo de texto simple.

**Comando (usando `nano`):**

```bash
nano secret
```

**Contenido del archivo (ejemplo):**

```
Hi, i am a secret
```

Guarda y cierra el archivo. Puedes verificar el tamaño del archivo con `ls -l secret`.

### 4\. Cifrar un Archivo

Existen dos formas principales de cifrar un archivo con GPG, que resultan en diferentes formatos de salida:

#### a) Cifrado con `--armor` (Salida ASCII Legible)

Esta opción genera un archivo cifrado en formato ASCII (Base64), lo que lo hace legible y fácil de copiar y pegar en correos electrónicos o documentos de texto.

**Comando:**

```bash
gpg --encrypt --armor --recipient <email_del_destinatario> <nombre_del_archivo>
```

**Ejemplo Práctico:**

```bash
gpg --encrypt --armor --recipient pablo2@mypublicinbox.com secret
```

Esto creará un archivo llamado `secret.asc` en el mismo directorio.

**Visualizar el archivo cifrado (legible, pero incomprensible):**

```bash
cat secret.asc
```

Verás un bloque de texto que comienza con `-----BEGIN PGP MESSAGE-----` y termina con `-----END PGP MESSAGE-----`.

#### b) Cifrado sin `--armor` (Salida Binaria Ilegible)

Esta opción genera un archivo cifrado en formato binario. Es más compacto pero no es legible directamente.

**Comando:**

```bash
gpg --encrypt --recipient <email_del_destinatario> <nombre_del_archivo>
```

**Ejemplo Práctico:**

```bash
gpg --encrypt --recipient pablo2@mypublicinbox.com secret
```

Esto creará un archivo llamado `secret.gpg`.

**Visualizar el archivo cifrado (ilegible):**

```bash
cat secret.gpg
```

Verás una secuencia de caracteres incomprensibles. Puedes usar `file secret.gpg` para confirmar que es un bloque PGP.

### 5\. Descifrar un Archivo

Para descifrar un archivo, necesitas la clave privada correspondiente a la clave pública con la que fue cifrado el archivo. GPG te pedirá la frase de contraseña de tu clave privada si no está ya en caché.

**Comando:**

```bash
gpg --decrypt <nombre_del_archivo_cifrado>
```

Por defecto, el contenido descifrado se mostrará en la salida estándar (terminal).

**Ejemplo Práctico (descifrando `secret.asc`):**

```bash
gpg --decrypt secret.asc
```

El contenido original del archivo (`Hi, i am a secret`) se imprimirá en la terminal.

**Para guardar el contenido descifrado en un nuevo archivo:**

Puedes redirigir la salida del comando `gpg --decrypt` a un nuevo archivo usando `>`.

**Comando:**

```bash
gpg --decrypt <nombre_del_archivo_cifrado> > <nombre_del_archivo_descifrado>
```

**Ejemplo Práctico (descifrando `secret.gpg` y guardando en `new_secret.txt`):**

```bash
gpg --decrypt secret.gpg > new_secret.txt
```

O usando el parámetro `--output`:

```bash
gpg --output new_secret.txt --decrypt secret.gpg
```

Luego, puedes verificar el contenido del nuevo archivo:

```bash
cat new_secret.txt
```

### 6\. Firmar un Archivo

La firma digital se utiliza para verificar la autenticidad e integridad de un archivo, no para cifrarlo.

**Comando:**

```bash
gpg --output <nombre_del_archivo_firma> --sign <nombre_del_archivo_original>
```

**Ejemplo Práctico:**

```bash
gpg --output secret.sig --sign secret
```

Esto creará un archivo de firma llamado `secret.sig`.

### 7\. Verificar una Firma

Para verificar que un archivo no ha sido alterado y que proviene del firmante legítimo, se utiliza la clave pública del firmante.

**Comando:**

```bash
gpg --verify <nombre_del_archivo_firma>
```

**Ejemplo Práctico:**

```bash
gpg --verify secret.sig
```

**Ejemplo de Salida (firma válida):**

```
gpg: Signature made Fri 12 Apr 2024 08:13:43 PM +09
gpg:                using RSA key B6CB7A5DAC39F93A0F45818AA7287AA54BF91913
gpg: Good signature from "pablogonzalezpe <pablo@mypublicinbox.com>" [ultimate]
```

Si la firma es válida, GPG indicará "Good signature". Si el archivo original ha sido modificado o la firma no corresponde, GPG lo detectará.

### 8\. Cifrado Simétrico (por Contraseña)

GPG también permite el cifrado simétrico, donde se utiliza una única contraseña para cifrar y descifrar el archivo, sin necesidad de pares de claves.

**Comando:**

```bash
gpg -c <nombre_del_archivo>
```

**Ejemplo Práctico:**

```bash
gpg -c secret
```

Se te pedirá una frase de contraseña para cifrar el archivo. Esto generará un archivo `secret.gpg` (sobrescribirá el anterior si existe).

**Descifrar un archivo cifrado simétricamente:**

**Comando:**

```bash
gpg -d <nombre_del_archivo_cifrado>
```

**Ejemplo Práctico:**

```bash
gpg -d secret.gpg
```

Se te pedirá la frase de contraseña utilizada para el cifrado. El contenido descifrado se mostrará en la terminal.

**Para guardar el contenido descifrado en un nuevo archivo:**

```bash
gpg -d secret.gpg > d
```
