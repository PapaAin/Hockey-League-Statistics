# Write your solution here
import json

class Player:
    def __init__(self,item):
        self.name = item["name"]
        self.nationality= item["nationality"]
        self.assists = item["assists"]
        self.goals = item["goals"]
        self.penalties = item["penalties"]
        self.team = item["team"]
        self.games = item["games"]
    
    def get_name(self):
        return self.name

    def get_nationality(self):
        return self.nationality
    
    def get_team(self):
        return self.team
    
    def get_points(self):
        return self.assists + self.goals
    
    def __str__(self):
        return f"{self.name:21}{self.team:5}{self.goals:2} + {self.assists:2} = {self.goals+self.assists:3}"
    
def search_for_player(instances,name):
    return [instance for instance in instances if instance.name == name]

def get_team(instances:list):
    team = set(map(lambda instance: instance.team,instances))
    return sorted(team)

def get_country(instances:list):
    country = set(map(lambda instance: instance.nationality,instances))
    return sorted(country)

def players_in_team(instances:list,team):
    players = [instance for instance in instances if instance.team == team]
    return sorted(players,key=lambda player: player.get_points(),reverse=True)

def players_in_country(instances:list,country):
    players = [instance for instance in instances if instance.nationality == country]
    return sorted(players,key=lambda player: player.get_points(),reverse=True)

def most_points(instances:list):
    return sorted(instances,key=lambda instance:(instance.get_points(),instance.goals),reverse=True)

def most_goals(instances:list):
    return sorted(instances,key=lambda instance:(-instance.goals,instance.games))

class HockeyLeagueApplication:

    # List of commands to be used
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        # Reading the JSON file
        filename = input("")
        with open(filename,"r") as file:
            data = json.load(file)

        print(f"read the data of {len(data)} players\n")
        print("commands:")
        self.help()
        
        instances = [Player(item) for item in data]

        
        while True:
            command = int(input(""))

            if command == 0:
                break

            elif command == 1:
                name = input("")
                person = search_for_player(instances,name)
                for item in person:
                    print(item)

            elif command == 2:
                teams = get_team(instances)
                for team in teams:
                    print(team)

            elif command == 3:
                countries = get_country(instances)
                for country in countries:
                    print(country)

            elif command == 4:
                team = input("")
                players = players_in_team(instances,team)
                for player in players:
                    print(player)

            elif command == 5:
                country = input("")
                players = players_in_country(instances,country)
                for player in players:
                    print(player)

            elif command == 6:
                number = int(input(""))
                array = most_points(instances)
                for i in range(number):
                    print(array[i])

            elif command == 7:
                number = int(input(""))
                array = most_goals(instances)
                for i in range(number):
                    print(array[i])
        
application = HockeyLeagueApplication()
application.execute()