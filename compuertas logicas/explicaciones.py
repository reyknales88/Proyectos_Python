# Operadores bit a bit
# Sin embargo, existen cuatro operadores que permiten manipular bits individuales de datos . Se denominan operadores bit a bit .

# Cubren todas las operaciones que mencionamos antes en el contexto lógico y un operador adicional.
# # Este es elxor(como en el operador exclusivo o ), y se denota como^(signo de intercalación).

# Aquí están todos ellos:

# &(ampersand) ‒ conjunción bit a bit;
# |(barra) ‒ disyunción bit a bit;
# ~(tilde) ‒ negación bit a bit;
# ^(caret) ‒ bit a bit exclusivo o (xor).

# Hagámoslo más fácil:

#               &requiere exactamente dos1s para proporcionar1como resultado;
#               |requiere al menos uno1Proporcionar1como resultado;
#               ^requiere exactamente uno1Proporcionar1como resultado.

'''1. Python admite los siguientes operadores lógicos:

y→ si ambos operandos son verdaderos, la condición es verdadera, por ejemplo,(Verdadero y cierto)esVerdadero,
o→ si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo,(Verdadero o falso)esVerdadero,
no→ devuelve falso si el resultado es verdadero, y devuelve verdadero si el resultado es falso, por ejemplo,No es ciertoesFALSO.
2. Puede utilizar operadores bit a bit para manipular bits individuales de datos. Los siguientes datos de ejemplo:

x = 15, que es0000 1111en binario,
y = 16, que es0001 0000en binario.
Se utilizará para ilustrar el significado de los operadores bit a bit en Python. Analice los ejemplos siguientes:

&hace un and bit a bit , por ejemplo,x y y = 0, que es0000 0000en binario,
|hace un bit a bit o , por ejemplo,x | y = 31, que es0001 1111en binario,
˜hace un no bit a bit , p. ej.˜x = 240*, que es1111 0000en binario,
^hace un xor bit a bit , por ejemplo,x ^ y = 31, que es0001 1111en binario,
>>realiza un desplazamiento bit a bit a la derecha , por ejemplo,y >> 1 = 8, que es0000 1000en binario,
<<realiza un desplazamiento bit a bit a la izquierda , por ejemplo,y << 3 = 128, que es1000 0000en binario.
*-16(decimal del complemento a 2 con signo) - lea más sobre la operación de complemento a dos .'''