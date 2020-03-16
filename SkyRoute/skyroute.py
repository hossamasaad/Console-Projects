from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices


stations_under_construction = []                                          # list contain station under constructions
landmark_string = ""                                                      # landmark string to print to user

# Convert landmarks map to string to print to user

for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)

# The root function of whole program

def skyroute():
    greet()
    new_route()
    goodbye()
  
# To greet user at the beginning of the program

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)
    
# To say goodbye at the end of the program

def goodbye():
    print("Thanks for using SkyRoute!")

# set start point and end point that user enterd

def set_start_and_end(start_point,end_point):
    if start_point != None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == 'b':                                   # In case user want to change to destination 
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':                                 # In Case user want to change start point only
            start_point = get_start()
        elif change_point == 'd':                                 # In case user want to change destination point only
            end_point = get_end()
        else:                                                     # in case entered fault character
            print("Oops, that isn't 'o', 'd', or 'b'...")
            set_start_and_end()                                   # ask for points again
    else:
        start_point = get_start();
    end_point = get_end()
    return start_point,end_point                                  # return start and end point

# A function to get start point from user

def get_start():
    start_point = ""
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
      start_point = landmark_choices[start_point_letter]
      return start_point
    else:
      print("Sorry, that's not a landmark we have data on. Let's try this again...")
      get_start()

# A function used to get destination point from the user

def get_end():
  end_point = ""
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
      end_point = landmark_choices[end_point_letter]
      return end_point
  else:
      print("Sorry, that's not a landmark we have data on. Let's try this again...")
      get_end()

# To prepare the route for the user

def new_route(start_point = None, end_point = None):
    start_point,end_point = set_start_and_end(start_point,end_point)
    shortest_route = get_route(start_point,end_point)
    shortest_route_string = '\n'.join(shortest_route)
    if shortest_route_string:
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
        again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        show_landmarks()
        new_route(start_point,end_point)
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))

# To generate the route

def get_route(start_point,end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            route = bfs(metro_system,start_station,end_station)
            if route:
                possible_route = dfs(metro_system,start_station,end_station)
            if possible_route == None:
                return None
            routes.append(route)
    shortest_route = min(routes)
    return shortest_route

# Show landmarks again for the user

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == "y":
        print(landmark_string)


# if there is stations under constructions

def get_active_stations():
    update_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station , neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                update_metro[current_station] -= set(stations_under_constructions)
            else :
                update_metro[current_station] = set([])
    return update_metro


if __name__ == "__main__":
    skyroute()
