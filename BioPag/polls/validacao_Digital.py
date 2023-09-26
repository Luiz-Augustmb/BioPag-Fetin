import time

import serial
import django

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

if __name__ == "__main__":
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


    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
    finally:
        ser.close()
        print("Conexão serial encerrada.")