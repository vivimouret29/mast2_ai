#!/usr/bin/env python


#
# Exceptions
#
from tripservice_mechanical.UserSession import UserSession


class DependendClassCallDuringUnitTestException(Exception):
  pass

class UserNotLoggedInException(Exception):
  pass

#
# Classes
#
class Trip:
  pass

class User:
  def __init__(self):
    self.trips = []
    self.friends = []
  
  def addFriend(self, user):
    self.friends.append(user)
  
  def addTrip(self, trip):
    self.trips.append(trip)
  
  def getFriends(self):
    return self.friends

#
# Functions
#
def _isUserLoggedIn(user):
  raise DependendClassCallDuringUnitTestException(
    "UserSession.isUserLoggedIn() should not be called in an unit test"
  )

def _getLoggedUser():
  raise DependendClassCallDuringUnitTestException(
    "UserSession.getLoggedUser() should not be called in an unit test"
  )

def _findTripsByUser(user):
  raise DependendClassCallDuringUnitTestException(
    "TripDAO should not be invoked on an unit test."
  )

def getTripsByUser(user):
    loggedUser = UserSession.getLoggedUser().isUserLoggedIn()
    if loggedUser:
      if loggedUser in user.getFriends():
        return _findTripsByUser(user)
      else:
        return []
    else:
      raise UserNotLoggedInException()

if __name__ == "__main__":
  pass
