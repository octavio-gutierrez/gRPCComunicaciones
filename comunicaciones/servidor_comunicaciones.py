from concurrent import futures
import grpc
import comunicacion_pb2
import comunicacion_pb2_grpc


class Comunicador(comunicacion_pb2_grpc.ComunicadorServicer):

    elementos = {}
    folio = 0

    def listador_elementos1(self, request, context): # (Empty)   
        for elemento in Comunicador.elementos.values(): 
            yield elemento

    def listador_elementos2(self, request, context): # (Empty) 
        listado = []
        for elemento in Comunicador.elementos.values(): 
             listado.append(elemento)
        return comunicacion_pb2.ListadoElementos(objetos=listado)

    def agregador(self, request_iterator, context):

        for elemento in request_iterator: 
            Comunicador.folio += 1             
            Comunicador.elementos[Comunicador.folio] = comunicacion_pb2.Elemento(id=Comunicador.folio, 
                                                                                 descripcion=elemento.descripcion)
        # Double checking
        for elemento in Comunicador.elementos.values(): 
            print(elemento)

        return comunicacion_pb2.Status(success=True)
            



def ofrece_servicios():
    puerto = "50051"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comunicacion_pb2_grpc.add_ComunicadorServicer_to_server(Comunicador(), servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    print("Ofreciendo servicios de comunicacion")
    ofrece_servicios()
    