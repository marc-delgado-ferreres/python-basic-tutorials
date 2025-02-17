### Estructura de Control ###

# Qué función tiene #

# Los condicionales "if", "elif" y "else" se utilizan para tomar decisiones basadas en una condición.
# Permite ejecutar un bloque de código si la condición es verdadera y otro bloque de código si la condición es falsa.

# If #

# El condicional "if" se utiliza para ejecutar un bloque de código si una condición es verdadera.
# El bloque de código dentro del "if" se ejecuta solo si la condición se cumple. Si la condición no se cumple, se salta el bloque "if".

if 10 > 5:
    print("Diez es mayor que cinco")
if 3 != 4:
    print("Tres es distinto de cuatro")
if 7 <= 2:
    print("Siete es menor o igual que dos")
if "Python" != "Cpp":
    print("Python es diferente de Cpp")

# En este ejemplo, podemos observar cuatro condicionales "if" seguidos.
# El tercer condicional "if" no se cumple, por tanto, no se activa el bloque respectivo.
# Los demás condicionales "if" se cumplen, por lo que se activan los bloques y se imprimen los mensajes respectivos.
# El resultado será:
# Diez es mayor que cinco
# Tres es distinto de cuatro
# Python es diferente de Cpp

# Else #

# El condicional "else" se utiliza en combinación con el "if" para proporcionar un bloque de código alternativo que se ejecuta cuando la condición del "if" no se cumple.
# El bloque de código dentro del "else" se ejecuta solo si la condición del "if" no se cumple.

edad = 20

if edad % 10 == 0:
    print("Tienes una edad redonda")
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# En este ejemplo, podemos observar tres condicionales, dos condicionales "if" y un condicional "else".
# El primer condicional "if" se cumplen, por lo que se activa el bloque y se imprime el mensaje respectivo.
# El segundo condicional "if" no se cumple, por tanto, no se activa el bloques respectivo.
# El tercer condicional "else" se activa por descarte, por tanto, se activa el bloque y se imprime el mensaje respectivo.
# El resultado será:
# Tienes una edad redonda
# Eres mayor de edad

# Elif #

# El condicional "elif" es una abreviatura de "else if" y se utiliza para comprobar múltiples condiciones en secuencia.
# Se puede utilizar después del "if" o de otro "elif" para proporcionar bloques de código adicionales que se ejecutan cuando se cumplen ciertas condiciones.
# Solo se ejecutará el bloque de código correspondiente a la primera condición que se cumpla.

temperatura = 25

if temperatura < 0:
    print("Hace una temperatura muy baja")
elif temperatura < 15:
    print("Hace una temperatura baja")
elif temperatura < 30:
    print("Hace una temperatura media")
elif temperatura < 50:
    print("Hace una temperatura alta")
else:
    print("Hace una temperatura muy alta")

# En este ejemplo, podemos observar cinco condicionales, un condicional "if", tres condicionales "elif" y un condicional "else".
# El primer condicional "if" no se cumple, por tanto, no se activa el bloque respectivo.
# El segundo condicional "elif" no se cumple, por tanto, no se activa el bloque respectivo.
# El tercer condicional "elif" se cumple, por tanto, se activa el bloque y se imprime el mensaje respectivo.
# El cuarto condicional "elif" no se activa el bloque respectivo debido a que ya ha habido un bloque que se ha activado.
# El quinto condicional "else" no se activa el bloque respectivo debido a que ya ha habido un bloque que se ha activado.
# El resultado será:
# Hace una temperatura media

# Marc Delgado Ferreres