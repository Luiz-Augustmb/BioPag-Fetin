import serial
import django
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Funções de views

#Funcções de render ->
def index(request):
    return render(request, 'html/index.html')

def segundaAplicacao(request):
    return render(request, 'html/segundaAplicacao.html')

def entrada_Valor(request):
    return render(request, 'html/entrada_Valor.html')

def forma_Pagamento(request):
    return render(request, 'html/forma_Pagamento.html')

def opcao_Pagamento(request):
    return render(request, 'html/opcao_Pagamento.html')

def verifica_Digital(request):
    return render(request, 'html/verifica_Digital.html')

def pag_Aprovado(request):
    return render(request, 'html/pag_Aprovado.html')

def pag_Negado(request):
    return render(request, 'html/pag_Negado.html')

def cadastroDigital(request):
    return render(request, 'html/cadastroDigital.html')

def deletaDigital(request):
    return render(request, 'html/deletaDigital.html')

#Validação da Digital ->

def connect_serial(port, baud_rate):
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Conexão serial estabelecida em {port} com baud rate {baud_rate}")
        return ser
    except Exception as e:
        print(f"Erro ao conectar na porta {port}: {e}")
        return None

def read_data(ser):
    try:
        data = ser.readline().decode().strip()
        return data
    except UnicodeDecodeError:
        print("Erro ao decodificar dados recebidos.")
        return None


def verify_fingerprint(request):
    # Substitua as informações da porta serial pelo necessário
    porta_serial = 'COM5'  # Substitua 'COM5' pela porta correta do Arduino
    taxa_transmissao = 9600

    ser = connect_serial(porta_serial, taxa_transmissao)
    if not ser:
        return JsonResponse({'conexao': False, 'valid': False})  # Adicione 'conexao' aqui

    try:
        while True:
            ser.write(b'V')
            data = read_data(ser)
            if data:
                print("Dados recebidos:", data)
            if data == "Impressão digital verificada com sucesso!":
                ser.close()
                return JsonResponse({'conexao': True, 'valid': True})  # Adicione 'conexao' aqui
            elif data == "Impressão digital não encontrada.":
                ser.close()
                return JsonResponse({'conexao': True, 'valid': False})  # Adicione 'conexao' aqui
            elif data == "Erro na verificação da impressão digital.":
                ser.close()
                return JsonResponse({'conexao': True, 'valid': False})  # Adicione 'conexao' aqui
            elif data == "Erro ao converter imagem.":
                ser.close()
                return JsonResponse({'conexao': True, 'valid': False})  # Adicione 'conexao' aqui
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial encerrada.")



@csrf_exempt  # Use isso se você estiver tendo problemas com o CSRF Token
def enroll_fingerprint(request, fingerprint_id):
    valor_digitado = request.GET.get('valor_digitado')
    # Substitua as informações da porta serial pelo necessário
    porta_serial = 'COM5'  # Substitua 'COM5' pela porta correta do Arduino
    taxa_transmissao = 9600

    ser = connect_serial(porta_serial, taxa_transmissao)
    if not ser:
        exit(1)
    try:
        while True:
            ser.write(b'E')
            data = read_data(ser)
            if data:
                print("Dados recebidos:", data)
            if data == "Escolha uma posição para armazenar a digital (0-255):":
                ser.write(valor_digitado.encode())
            if data == "Imagem convertida com sucesso.":
                print("teste")
            if data == "Segunda imagem convertida com sucesso.":
                ser.close()
                return JsonResponse({'success': True, 'message': 'Nova digital cadastrada no ID ' + valor_digitado + ' com sucesso!'})


    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial encerrada.")

# funcao para limpar o banco de dados do sensor

def limpa_banco(request):
    # Substitua as informações da porta serial pelo necessário
    porta_serial = 'COM5'  # Substitua 'COM5' pela porta correta do Arduino
    taxa_transmissao = 9600

    ser = connect_serial(porta_serial, taxa_transmissao)
    if not ser:
        return JsonResponse({'conexao': False, 'valid': False})

    try:
        while True:
            ser.write(b'M')
            data = read_data(ser)
            if data:
                print("Dados recebidos:", data)
                if data == "Banco de dados esvaziado com sucesso!":
                    ser.close()
                    return JsonResponse({'conexao': True, 'valid': True})

    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial encerrada.")


def deleteDigital(request, fingerprint_id):
    valor_digitado = request.GET.get('valor_digitado')
    # Substitua as informações da porta serial pelo necessário
    porta_serial = 'COM5'  # Substitua 'COM5' pela porta correta do Arduino
    taxa_transmissao = 9600

    ser = connect_serial(porta_serial, taxa_transmissao)
    if not ser:
        exit(1)
    try:
        while True:
            ser.write(b'D')
            data = read_data(ser)
            if data:
                print("Dados recebidos:", data)
                print(valor_digitado)
            if data == "Aguardando posição a ser excluída...":
                ser.write(valor_digitado.encode())
            if data == "Impressão digital na posição " + valor_digitado + " excluída com sucesso!":
                ser.close()
                return JsonResponse({'success': True, 'message': 'Digital excluída com sucesso!'})

    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial encerrada.")