country = input() # adding country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # creating list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


def add_new_country(country_name, number_of_visits, list_of_cities_visited):
  new_country = {}
  new_country["country"] = country_name
  new_country["visits"] = number_of_visits
  new_country["cities"] = list_of_cities_visited
  travel_log.append(new_country)

  # 2nd way
  #travel_log.append({"country": country,
  #                   "visits" : visits,
  #                   "cities": list_of_cities})

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
