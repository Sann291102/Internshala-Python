##Assingment solution 1
class Player:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        self.teams = []
        self.stats = {
            "Test": {},
            "ODI": {},
            "T20": {}
        }
    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)
    def update_stats(self, format, matches, runs, wickets, average):
        if format in self.stats:
            self.stats[format] = {
                "Matches": matches,
                "Runs": runs,
                "Wickets": wickets,
                "Average": average
            }
    def display_stats(self):
        print(f"Player: {self.name}, Age: {self.age}, Country: {self.country}")
        print(f"Teams: {', '.join(self.teams)}")
        print("\nStats by Format:")
        for format, stat in self.stats.items():
            if stat:
                print(f"{format} - Matches: {stat['Matches']}, Runs: {stat['Runs']}, Wickets: {stat['Wickets']}, Average: {stat['Average']}")
            else:
                print(f"{format} - No data available")
player = Player("Virat Kohli", 35, "India")
player.add_team("Royal Challengers Bangalore")
player.add_team("India")
player.update_stats("Test", matches=108, runs=8500, wickets=0, average=49.95)
player.update_stats("ODI", matches=265, runs=12000, wickets=4, average=58.15)
player.update_stats("T20", matches=99, runs=3300, wickets=0, average=51.5)
player.display_stats()
