import streamlit as st 

def menu():
    while True:
        print("/nMenu")
        print("oposto")
        print("sinal")
        print("sair")

        escolha = input("escolha uma opção")

        if escolha == '1':
            numero = float(input("digite um numero:"))
            numero_invertido = -numero
            print(f"O numero invertido é: {numero_invertido}")

        elif escolha == '2' :
            numero = 3 
            numero_invertido = -numero
            print(f"O número 3 invertido é: {numero_invertido}")

        elif escolha == '3':
            print("saindo...")
            continue #renicie se a opção não existir

    menu()