from sources.apartmant_source import *
from Handlers.base_handler import *

class ApartmentsWorker():
    def proceed_apartments(self, apartment):
        # CHECK IF APARTMENT EXISTS IN DB
        if 'id' in apartment:
            existing_apartment = ApartmantSource().get_apartment_by_id(apartment['id'])
            if existing_apartment:
                ApartmantSource().update_apartment_by_id(apartment_id=apartment['id'], apartment=apartment)
            else:
                ApartmantSource().add_apartmant(apartment)

        else:
            ApartmantSource().add_apartmant(apartment)
