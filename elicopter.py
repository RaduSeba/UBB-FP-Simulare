from domain.entitati import Elicopter


class ElicopterRepoFile:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        """
        incarca elicopterele din fisier intr o lista
        rtype:list
        """
        f=open(self.__filename,"r")
        elicoptere=[] 
        lines=f.readlines() 
        for line in lines:
            elicopter_id,elicopter_nume,elicopter_scop,elicopter_an=[token.strip() for token in line.split(",")]
            elicopter=Elicopter(elicopter_id,elicopter_nume,elicopter_scop,elicopter_an)
            elicoptere.append(elicopter)
        f.close()
        return elicoptere


    def __save_to_file(self,elicopter_list):
        with open (self.__filename,"w") as f:
            for elicopter in elicopter_list:
                elicopter_string=str(elicopter.getid())+","+str(elicopter.getnume())+","+str(elicopter.getscop())+","+str(elicopter.getan())+"\n"
            f.write(elicopter_string)

    def get_all_elicoptere(self):
        """
        returneaza lista cu toate elicopterele
        rtype:list
        """
        return list(self.__load_from_file())           