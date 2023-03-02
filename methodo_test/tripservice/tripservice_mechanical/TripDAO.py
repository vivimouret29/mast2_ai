
from tripservice_mechanical.DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException

class TripDAO:
  # @staticmethod
  def findTripsByUser(user):
    raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on an unit test.")

