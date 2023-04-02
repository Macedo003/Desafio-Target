def fibonacci(numero):
    if numero<=1:
        return numero
    else:
        return(fibonacci(numero-1) + fibonacci(numero-2) )

while True:
    print('Bem vindo a sequencia de fibonacci')

    numero= input('Digite um numero: ')

    numero_valido = None
    try:
        int_numero= int(numero)
        numero_valido = True
    except:
        numero_valido = None


    if numero_valido is None:
        print('Voce não Digitou um numero')
        continue
        
        

    print('A sequencia até o valor indicado: ')
    for i in range(int_numero):
        print(fibonacci(i),end='->')
        if fibonacci(i) == int_numero or fibonacci(i) > int_numero:
            break



    pertence = False
    for i in range(int_numero):
        if fibonacci(i) == int_numero:
            pertence = True
            break
        

    if pertence is True:
        print('\n O numero pertence a sequencia')
    else:
        print('\n O numero não pertence a sequencia')

    sair = input('Quer sair? [s]im: ')
    sair = sair.lower().startswith('s')
    
    if sair is True:
        print('Até logo')
        break