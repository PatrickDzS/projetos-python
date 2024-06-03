
mesMenorTemperatura = "" # Variavel para pegar o mês com menor temperatura
mesMaiorTemperatura = "" # Variavel para pegar o mês com maior temperatura
maiorTemperatura = -60 # Variavel que inicia com a menor temperatura limnite, para que se saiba quais são as temperaturas mais baixas.
menorTemperatura = 50 # Variavel que inicia com 50 que e a temperatura mais alta, isso para que se saiba quais são as temperaturas mais altas.


qtdMesesEscaldantes = 0 # Variavel para amarzenar a quantidades de meses que foram escaldantes
somaTemperaturasMaximas = 0 # Variavel que devolve a soma das temperaturas máximas registradas
somaMesesEscaldantes = 0 # Variavel que recebe a soma dos meses que foram escaldantes 
temperaturasMaximas = [] # Variavel para armazenar as temeperaturas que foram altas


for cont in range(12): 

    temperatura = float(input(f"Entre com a temperatura da sua cidade em Celsius : ")) # Entrada para os dados de temperatura

    if temperatura< -60: # Condição para erro, quando o valor não estiver dentro do intervalo
        print("Valor inválido. A temperatura mínima aceitável é -60 graus Celsius")
        continue
    
    elif temperatura > 50: # Condição para seguir com a entrada correta
        print(f"A temperatura em celsius é: {temperatura}\n")
        
    if temperatura > 31: # Condição para o calculo e para armazenar os valores das entradas de temperaturas
        temperaturasMaximas.append(temperatura)
        somaTemperaturasMaximas += temperatura 
        mediaMaioresGraus = somaTemperaturasMaximas / len(temperaturasMaximas)
        qtdMesesEscaldantes += 1
    
    mes = int(input("Entre com mês que foi averiquada a temperatura, dentro de um intervalo (1 a 12): ")) # Entrada de dados para o mês da dada que foi colocado

    if mes < 1 or mes > 12: # Condição para cair em erro se a dada não estiver dentro do valor
        print("Erro, mês invalido")
        continue

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] # Calendario para as datas que serão escolhidas

    if temperatura > maiorTemperatura: # Condição para verificar a maio temperatura relatada 
        maiorTemperatura = temperatura
        mesMaiorTemperatura = meses[mes - 1]
    elif temperatura < menorTemperatura: # Condição para verificar a menor temperatura relatada
        menorTemperatura = temperatura
        mesMenorTemperatura = meses[mes - 1]
    
    print(f"O mês é: {meses[mes - 1]}") # Print para escrever o mês que foi escolhido


print("\n") # Quebra de linha 
print(f"A maior temperatura registrada foi: {maiorTemperatura} graus Celsius no mês de {mesMaiorTemperatura}") # Escreve a maior temperatura 
print(f"A menor temperatura registrada foi: {menorTemperatura} graus Celsius no mês de {mesMenorTemperatura}") # Escreve a menor temperatura 
print(f"A soma de todas as temperaturas máximas é: {somaTemperaturasMaximas}") # Escreve a soma das temperaturas máximas 
print(f"Quantidade de meses que foram escaldantes: {qtdMesesEscaldantes}") # Escreve a quantidades de meses escaldantes 
print(f"A média máxima anual é: {mediaMaioresGraus}") # Escreve a media anual 


















        




