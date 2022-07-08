from repository.elicopter import ElicopterRepoFile
from service.service_elicopter import ElicopterService
from ui.consola import Consola

elicopter_repo=ElicopterRepoFile("data/elicopter.txt")
elicopter_service=ElicopterService(elicopter_repo)

ui=Consola(elicopter_service)
ui.show_ui()