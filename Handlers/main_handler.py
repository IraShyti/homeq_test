from Handlers.base_handler import *
from sources.apartmant_source import *
import json

class MainHandler(BaseHandler):
    def get(self):
        apartments = ApartmantSource().get_available_apartmants()
        self.render("index.html" ,title="HomeQ", list_of_apartments=apartments)

    def post(self):
        payload = json.loads(self.request.body)
        ApartmantSource().add_apartmant(payload)
