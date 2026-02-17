
print("■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□")
print("  Algoritimo para ajudar na Rotina de Trabalho!")

while True:
    try:
        turno = int(input("""
        Que turno você trabalha?: 
        Digite:
        [1] - Manhã
        [2] - Tarde
        [3] - Noite
        [0] - Sair
        Resposta: """))


        if turno == 1:
            print("Rotina para Quem Trabalha de Manhã")

            print("1. Definir o horário de saída para chegar ao trabalho no horário.")
            print("2. Calcular o horário de acordar.")
            print("3. Programar o despertador.")

            print("\nAo despertar:")
            print("4. Levantar ao tocar o alarme (não usar soneca).")
            print("5. Abrir as cortinas ou acender a luz.")
            print("6. Realizar higiene pessoal (escovar dentes, lavar rosto, banho).")

            print("\nPreparação pessoal:")
            print("7. Vestir a roupa separada na noite anterior.")
            print("8. Verificar o clima e ajustar vestuário se necessário.")

            print("\nAlimentação:")
            print("9. Preparar um café da manhã rápido e nutritivo.")
            print("10. Alimentar-se com calma por pelo menos 10 minutos.")

            print("\nOrganização final:")
            print("11. Conferir itens essenciais: celular, carteira, chaves, documentos.")
            print("12. Verificar bateria do celular.")
            print("13. Desligar luzes e conferir portas e janelas.")

            print("\nSaída:")
            print("14. Sair de casa com 5 minutos de antecedência.")
            print("15. Ir ao trabalho pelo meio de transporte planejado.")
            print("■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□")
            break

        elif turno == 2:
            print("Rotina para Quem Trabalha à Tarde")

            print("1. Definir o horário de saída para chegar ao trabalho no horário.")
            print("2. Calcular o horário ideal para acordar.")
            print("3. Programar o despertador.")

            print("\nAo despertar:")
            print("4. Levantar ao tocar o alarme.")
            print("5. Abrir as janelas para iluminar o ambiente.")
            print("6. Realizar higiene pessoal (escovar dentes, lavar rosto, banho).")

            print("\nManhã Produtiva:")
            print("7. Tomar um café da manhã tranquilo.")
            print("8. Realizar uma atividade produtiva (estudo, exercício físico ou tarefas domésticas).")
            print("9. Organizar o que será necessário levar para o trabalho.")

            print("\nAlmoço:")
            print("10. Preparar ou organizar o almoço.")
            print("11. Alimentar-se com calma.")
            print("12. Higienizar-se novamente, se necessário.")

            print("\nPreparação para saída:")
            print("13. Vestir o uniforme ou roupa de trabalho.")
            print("14. Conferir itens essenciais: celular, carteira, chaves, documentos.")
            print("15. Verificar bateria do celular.")
            print("16. Desligar luzes e conferir portas e janelas.")

            print("\nSaída:")
            print("17. Sair de casa com antecedência de pelo menos 5 minutos.")
            print("18. Deslocar-se ao trabalho pelo meio de transporte planejado.")
            print("■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□")
            break

        elif turno == 3:
            print("Rotina para Quem Trabalha à Noite")

            print("1. Definir o horário de saída para chegar ao trabalho no horário.")
            print("2. Calcular o horário ideal para acordar (garantindo descanso suficiente durante o dia).")
            print("3. Programar o despertador.")

            print("\nAo despertar (período da tarde):")
            print("4. Levantar ao tocar o alarme.")
            print("5. Abrir janelas ou acender as luzes para estimular o despertar.")
            print("6. Realizar higiene pessoal (escovar dentes, lavar rosto, banho).")

            print("\nInício da 'manhã' pessoal:")
            print("7. Fazer a primeira refeição do dia (café da tarde reforçado).")
            print("8. Realizar atividades pessoais (estudos, exercícios leves ou tarefas domésticas).")
            print("9. Separar uniforme ou roupa de trabalho.")

            print("\nPreparação para o trabalho:")
            print("10. Fazer uma refeição principal antes de sair (jantar).")
            print("11. Vestir-se adequadamente para o turno noturno.")
            print("12. Conferir itens essenciais: celular, carteira, chaves, documentos.")
            print("13. Verificar bateria do celular.")
            print("14. Levar lanche para a madrugada, se necessário.")

            print("\nSaída:")
            print("15. Desligar luzes e conferir portas e janelas.")
            print("16. Sair de casa com antecedência de pelo menos 5 minutos.")
            print("17. Deslocar-se ao trabalho pelo meio de transporte planejado.")

            print("\nPós-trabalho:")
            print("18. Retornar para casa.")
            print("19. Realizar higiene pessoal.")
            print("20. Preparar o ambiente para dormir (reduzir luz e ruídos).")
            print("■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□")
            break

        elif turno == 0:
            print("Fim do programa")
            print("■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□")
            break
        
        else:
            print("Digite uma opção válida(1,2,3 ou 0)")

    except ValueError:
        print("Apenas digite números")