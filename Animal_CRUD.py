from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:45881/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):

        #Verify that dictionary containing record data was provided, else raise an exception
        if data is not None:

            #Store the results of the insert to variable
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary

            #If insert was successful, return True, else, return False
            if insert_result.inserted_id:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save, because data parameter is empty")

#Method to load database
    def read(self, record):
        return self.database.animals.find(record,{"_id": False})

# Method to implement the R in CRUD.
    def locate(self, query):

        #Verify that search criteria was provided, else raise an exception
        if query is not None:

            #Search animals collection in the AAC database & print cursor location
            search_result = self.database.animals.find(query)
            self.database.animals.find(query)

            #If the animal was located, return record, else display an error message
            if search_result is not None:
                return search_result
            else:
                return("Animal not found.")
        else:
            raise Exception("No search criteria provided")
            
#Method to implement the U in CRUD.
    def update(self, animal, change):

        #store the user values to local variables
        animalToFind = animal
        informationToUpdate = change

        #Verify that update criteria was provided
        if change is not None:
            result = self.database.animals.find_one_and_update(animalToFind, informationToUpdate)
            if result is not None:
                return result
            else:
                return("Update failed. Try again.")
        else:
            raise Exception("No change provided")
            
#Method to implement the D in CRUD
    def delete(self, animal):

        #Verify that deletion record was provided
        if animal is not None:
            delete_result = self.database.animals.delete_one(animal)
            return delete_result
        else:
            raise Exception("No animal ID provided")

