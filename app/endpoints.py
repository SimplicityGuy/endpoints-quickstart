from airports import Airports

airport_util = Airports()


def airportName(iataCode):
    """Given an airport IATA code, return that airport's name."""
    maybe_name = airport_util.get_airport_by_iata(iataCode)
    if maybe_name is None:
      return 'IATA code not found : %s' % iataCode, 400
    return maybe_name, 200
