def  num_triangular(n):
    resultado = 0
    for i in range(1, n + 1):
        resultado += i
    return resultado
def fazer_triangulo(n):
    for linha in range(n, 0, -1):
        linha_triangular = "*" * linha
        print(linha_triangular)
def principal():
    n = int(input("Digite um número natural: "))
    if n <= 0:
        print("Insira um número natural maior que zero.")
        return
    resultado =  num_triangular(n)
    print(f"O {n}-ésimo número triangular é: {resultado}")
    print(f"O triângulo equivalente ao {n}-ésimo número triangular é:")
    fazer_triangulo(n)
principal()