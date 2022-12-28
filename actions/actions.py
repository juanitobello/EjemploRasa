# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

#imports to custom actions
import webbrowser


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def openLink():
    webbrowser.open('https://google.com',  new=1, autoraise=True)

def openRicaurte():
    webbrowser.open('https://infra-geo-ouverte.github.io/igo2/?context=_default&zoom=13&center=-78.99208,-2.8762&invisiblelayers=*&visiblelayers=89053566f0abfa20b936f539b27066bd,935177c0cf3af93c98ede61d8664ad47,92dbfd9238c22d3f8dcd9b288185d242,6143562e58898a852eeb658ba493e8e7,fond_osm_hot&wmsUrl=https%3A%2F%2Fgis.uazuay.edu.ec%2Fgeoserver%2Fcobertura_vegetal_5k%2Fwms%3F&wmsLayers=(ricaurte_construcciones:igoz16)',  new=1, autoraise=True)

def openPostes():
    webbrowser.open('https://infra-geo-ouverte.github.io/igo2/?context=_default&zoom=17&center=-79.00376,-2.89791&invisiblelayers=*&visiblelayers=508b5791b7ff3809f103bc57e1b50970,935177c0cf3af93c98ede61d8664ad47,92dbfd9238c22d3f8dcd9b288185d242,6143562e58898a852eeb658ba493e8e7,fond_osm_hot&arcgisUrl=https%3A%2F%2Fgeoservicios2.centrosur.gob.ec%2Fgeoservicios%2Frest%2Fservices%2FGeoportal_Publico%2FGeopPublic_RedesDist_rsgis1%2FMapServer&arcgisLayers=(2:igoz17)',  new=1, autoraise=True)

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hola Juan")

        return []


class ActionButtonsSiNo(Action):

    def name(self) -> Text:
        return "action_buttons_sino"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ops=[
            {"payload":'/affirmacion', "title": "Sí"},
            {"payload":'/int_saltar', "title": "Saltar"},
        ]

        dispatcher.utter_message(text="Bienvenido! ¿Deseas más instrucciones?", buttons=ops)

        return []


#Open indes
class ActionOpenIndex(Action):

    def name(self) -> Text:
        return "action_open_index"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Redirigiendo...")
        openLink()
        return []

#Open Ricaurte
class ActionOpenRicaurte(Action):

    def name(self) -> Text:
        return "action_open_ricaurte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Redirigiendo...")
        openRicaurte()
        return []

#Open Postes
class ActionOpenPostes(Action):

    def name(self) -> Text:
        return "action_open_postes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Redirigiendo...")
        openPostes()
        return []



#Actions para 4 votones
class ActionButtons(Action):

    def name(self) -> Text:
        return "action_buttons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/int_movimiento_de_tierra{"tipo_emergencia":"movimientos"}', "title": "Movimientos en Masa"},
            {"payload":'/int_deslizamiento{"tipo_emergencia":"deslizamientos"}', "title": "Deslizamientos"},
            {"payload":'/int_inundaciones{"tipo_emergencia":"inundaciones"}', "title": "Inundaciones"},
            {"payload":'/int_volcanes"{"tipo_emergencia":"volcanes"}', "title": "Volcanes"},
        ]
        dispatcher.utter_message(text="Escoge un ítem para mostrar en el mapa:", buttons=buttons)
        #dispatcher.utter_message(text="http://localhost:4200/?context=igm_geopedologia&zoom=14&center=-78.51865,-0.22732&visiblelayers=*&invisiblelayers=a24677c2b5530b3e04f38f091dfae324,fond_osm_hot", buttons=buttons)

        return []



    