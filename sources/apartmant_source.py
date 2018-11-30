from configuration import *

class ApartmantSource(object):
    def get_available_apartmants(self):
        return list(db.apartmants.find({'deleted': {'$in':[False, 'False','false']}}))

    def add_apartmant(self, apartmant):
        result = db.apartmants.insert_one(apartmant)

    def update_apartment_by_id(self, apartment_id, apartment):
        result = db.apartmants.update_one({'id':apartment_id},{'$set':apartment})

    def get_apartment_by_id(self, apartment_id):
        apartment = db.apartmants.find_one({'id':apartment_id})
        return apartment