from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Carregando '{self.filename}' do disco...")

    def display(self):
        print(f"Exibindo '{self.filename}'")

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None  

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

if __name__ == '__main__':
    imagem = ProxyImage("paisagem.jpg")
    print("Proxy criado. A imagem real não foi carregada ainda.")
    
    print("\nPrimeira chamada de display():")
    imagem.display()
    
    print("\nSegunda chamada de display():")
    imagem.display()
