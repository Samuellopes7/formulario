def funcion(senha):
   
    num = "1,2,3,4,5,6,7,8,9,10"
    espe = "!,@,#,$,%,&,*,"
    if ((len(senha)) >8) and ((len(senha)) < 8):
        return "Mais de uma maiusculo"
    if not any(char.isupper() for char in senha):
        return "Mais de uma maiuscolo" 
    if num in senha:
        return "Erro de não ter número"
    if espe in senha:
        return "Erro de não ter caractere especial"
    if " " in senha:
        return "Muito espaço"
    return "Senha válida"
senha = input("Digite uma senha:")
resultado = funcion(senha) 
print(resultado)           