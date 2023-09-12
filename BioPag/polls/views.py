import serial
import django
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Funções de views

#Funcções de render ->
def index(request):
    return render(request, 'html/index.html')

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
        return JsonResponse({'valid': False})

    try:
        while True:
            data = read_data(ser)
            if data == "Found a print match!":
                ser.close()
                return JsonResponse({'valid': True})
            elif data == "Did not find a match":
                ser.close()
                return JsonResponse({'valid': False})
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial encerrada.")