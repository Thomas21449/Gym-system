import serial

class CactousController:
    def __init__(self, porta='COM3', baudrate=9600):
        self.porta = porta
        self.baudrate = baudrate

    def liberar_catraca(self):
        try:
            ser = serial.Serial(self.porta, self.baudrate)
            ser.write(b'\x01')  # Comando para liberar (ajuste conforme a Cactous)
            ser.close()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False