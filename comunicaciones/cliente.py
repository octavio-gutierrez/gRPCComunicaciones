import grpc
import comunicacion_pb2
import comunicacion_pb2_grpc

def generador_elementos(elementos):
    for elemento in elementos:
        yield comunicacion_pb2.Elemento(descripcion=elemento) 

def run():
    print("Intentando registrar")
    with grpc.insecure_channel("localhost:50051") as channel:

        stub = comunicacion_pb2_grpc.ComunicadorStub(channel)

        iterador_elementos = generador_elementos(["Elemento A", "Elemento B", "Elemento C"])
        respuesta = stub.agregador(iterador_elementos)        

        for elemento in stub.listador_elementos1(comunicacion_pb2.Empty()):
            print(elemento.id, elemento.descripcion)

        listado = stub.listador_elementos2(comunicacion_pb2.Empty())
        for elemento in listado.objetos:
            print("Elemento: ", elemento)


if __name__ == "__main__":
    run()