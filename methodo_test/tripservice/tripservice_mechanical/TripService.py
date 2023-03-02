from tripservice_mechanical.TripDAO import TripDAO
from tripservice_mechanical.UserSession import UserSession
from tripservice_mechanical.UserNotLoggedInException import UserNotLoggedInException

class TripService:
  def getTripsByUser(self, user):
    logged_user = UserSession.getInstance().getLoggedUser()
    isFriend = False
    tripList = []
    if logged_user:
      for friend in user.getFriends():
        if friend is logged_user:
          isFriend = True
          break
      if isFriend:
        tripList = TripDAO.findTripsByUser(user)
      return tripList
    else:
      raise UserNotLoggedInException()


