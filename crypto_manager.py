from cryptography.fernet import Fernet

class CryptoManager:
    def __init__(self, key=None):
        """
        Inicializa o gerenciador de criptografia.
        :param key: Chave de criptografia (opcional). Se não for fornecida, uma nova chave será gerada.
        """
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()  # Gera uma nova chave
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        """
        Criptografa os dados.
        :param data: Dados a serem criptografados (string ou bytes)
        :return: Dados criptografados (bytes)
        """
        if isinstance(data, str):
            data = data.encode()  # Converte string para bytes
        return self.cipher.encrypt(data)

    def decrypt(self, encrypted_data):
        """
        Descriptografa os dados.
        :param encrypted_data: Dados criptografados (bytes)
        :return: Dados descriptografados (string)
        """
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return decrypted_data.decode()  # Converte bytes para string

    def save_key(self, file_path="secret.key"):
        """
        Salva a chave de criptografia em um arquivo.
        :param file_path: Caminho do arquivo para salvar a chave
        """
        with open(file_path, "wb") as key_file:
            key_file.write(self.key)

    @staticmethod
    def load_key(file_path="secret.key"):
        """
        Carrega a chave de criptografia de um arquivo.
        :param file_path: Caminho do arquivo contendo a chave
        :return: Chave de criptografia (bytes)
        """
        with open(file_path, "rb") as key_file:
            return key_file.read()