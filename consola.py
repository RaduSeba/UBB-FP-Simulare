from domain.entitati import Elicopter
from repository.elicopter import ElicopterRepoFile
from service.service_elicopter import ElicopterService

class Consola:
    def __init__(self,elicopter_service):
        self.__service=elicopter_service

    def __print_menu(self):
        print("Vor fi suportate urmatoarele operatii: afisare_scop, afisare_scop_an, all_scop, exit")

    def __show_elicopter1(self,elicoptere):
        if len(elicoptere)==0:
            print("Nu exista elicoptere cu scopul dat.")
        else:
                print("Lista de elicoptere este:")
                for elicopter in elicoptere:
                    print("ID:",elicopter.getid()," Nume: ",elicopter.getnume()," Scop: ",elicopter.getscop()," An:",elicopter.getan())

    def __show_elicopter2(self,elicoptere,scop):
        if len(elicoptere)==0:
            print("Nu exista elicoptere cu scopul dat.")
        else:
                print(scop,":")
                for elicopter in elicoptere:
                    print(elicopter.getan())  

    def __cautare_scop(self):
        scop=input("Cautati scopul elicopterului:")
        l=self.__service.cautare_by_scop(scop)
        self.__show_elicopter1(l)  

    def __cautare_scop_an(self):
        scop=input("Cautati scopul elicopterului:")
        l=self.__service.cautare_by_scop(scop)
        self.__show_elicopter2(l,scop)

    def __all_scop(self,all_elicoptere):

        for elicopter in all_elicoptere:
            scop=elicopter.getscop()
            l=self.__service.cautare_by_scop(scop)
            self.__show_elicopter2(l,scop)



    def show_ui(self):
        while True:
            self.__print_menu()
            cmd=input("Comanda este:")
            cmd=cmd.lower().strip() 
            if cmd=="afisare_scop":
                self.__cautare_scop()
            elif cmd=="afisare_scop_an":
                self.__cautare_scop_an()
            elif cmd=="exit":
                return
            elif cmd=="all_scop":
                self.__all_scop(self.__service.get_elicoptere())    
            else:
                print("Comanda Invalida")               


