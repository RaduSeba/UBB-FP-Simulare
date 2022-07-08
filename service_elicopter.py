from repository.elicopter import ElicopterRepoFile
from domain.entitati import Elicopter


class ElicopterService:
    def __init__(self,repo):
        self.__repo=repo

    def get_elicoptere(self):
        return self.__repo.get_all_elicoptere()

    def cautare_by_scop(self, str_to_search):
        """
        functia care cauta dupa scop
        rtype:list
        """
        all_elicoptere= self.get_elicoptere()
        filtered_list = [elicopter for elicopter in all_elicoptere if str_to_search in elicopter.getscop()]
        return filtered_list


