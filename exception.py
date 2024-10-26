# def divide(a,b):
#     if b == 0:
#         raise ValueError('divisão por zero')
#     return a/b

# try:
#     print(divide(10, 0))
# except ValueError as e:
#     print(e)

################################
#levantar a exceção novamente

# try:
#    print(divide(10, 0))
# except ValueError:
#     print('deu erro aq')
#     raise

###########################
#levantar exceções personalizadas

#gerar a  classe do erro que eu desejo

class MinhaExcecao(Exception):
    pass

def verifica_numero(num):
    if num < 0:
        raise MinhaExcecao('numero nao pode ser negativo')
    return num

try:
    print(verifica_numero(-1))
except MinhaExcecao as e:
    print(e)
