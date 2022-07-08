class Elicopter:
    """
    clasa elicpter care contine id,nume,scop,an elicopter
    """
    def __init__(self,id,nume,scop,an):
        self.__id=id
        self.__nume=nume
        self.__scop=scop
        self.__an=an

    def getnume(self):
        return self.__nume

    def getid(self):
        return self.__id

    def getscop(self):
        return self.__scop

    def getan(self):
        return self.__an

    def __str__(self) :
        return "ID: "+str(self.__id)+" Nume:"+str(self.__nume)+" Scop:"+str(self.__scop)











def test_elicopter():
    elicopter=Elicopter("8","Wizair","vacanta","2000")
    assert(elicopter.getid()=="8")
    assert(elicopter.getnume()=="Wizair")
    assert(elicopter.getscop()=="vacanta")
    assert(elicopter.getan()=="2000")


test_elicopter()    


