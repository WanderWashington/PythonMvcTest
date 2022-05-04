from models.person import Person
from views.view import showPeopleQuantityView
from views.view import showPeopleQuantityInSouthAmericaView

def showPeopleQuantity():
   people = Person.getAllData()
   return showPeopleQuantityView(people)


def showPeopleQuantityInSouthAmerica():
    people = Person.getAllData()
    return showPeopleQuantityInSouthAmericaView(people)


def start():
   t =  input('1 - showPeopleQuantity \n2 - showPeopleQuantityInSouthAmerica \nOther Value - Close \n')
   if t == '1':
      return showPeopleQuantity()
   elif t == '2':
      return showPeopleQuantityInSouthAmerica()
   else:
      return

if __name__ == "__main__":
   #running controller function
   start()