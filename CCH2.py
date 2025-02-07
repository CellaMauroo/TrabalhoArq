from abc import ABC, abstractmethod

# Subject: Define a interface comum
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject: Implementa a lógica real
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        # Simula o carregamento de uma imagem custosa
        print(f"Carregando '{self.filename}' do disco...")

    def display(self):
        print(f"Exibindo '{self.filename}'")

# Proxy: Controla o acesso ao RealImage
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None  # O objeto real ainda não foi instanciado

    def display(self):
        # Instancia o objeto real somente na primeira chamada
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Exemplo de uso
if __name__ == '__main__':
    # Cria o proxy para a imagem
    imagem = ProxyImage("paisagem.jpg")
    print("Proxy criado. A imagem real não foi carregada ainda.")
    
    # Ao chamar display, o objeto real é instanciado e a imagem é carregada e exibida
    print("\nPrimeira chamada de display():")
    imagem.display()
    
    # Na segunda chamada, o objeto real já foi criado, evitando nova operação custosa
    print("\nSegunda chamada de display():")
    imagem.display()
