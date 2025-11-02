class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
            print(f"Person {name} added to the network.")
        else:
            print(f"Person {name} already exists in the network.")
    
    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created, {person1_name} not found in the network.")
        if person2_name not in self.people:
            print(f"Friendship not created, {person2_name} not found in the network.")

        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
            print(f"Friendship created between {person1_name} and {person2_name}.")

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names) if friend_names else 'No friends'}")



# Test your code here
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
print(network.people) # {'Alex': <__main__.Person object at 0x1004c7380>,'Jordan': <__main__.Person object at 0x10503d810>}
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny") # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

"""
Why is a graph the right structure to represent a social network?
A graph is the right and best structure because it makes sense, like a spiderweb where people can be connected in all types of ways to each other. Each person can have multiple friends, and those friends can also be friends with each other, which wouldn't work with a tree or other structures.

Why wouldn’t a list or tree work as well for this?
A list doesnt work as well for this because the structure isnt effecient due to them being linear, and searching for friends would take much longer. A tree wouldnt work as good either because trees are hierarchical, where friendships are not and wouldn't work well like that.

What performance or structural trade-offs did you notice when adding friends or printing the network?
A graph is the best structure to represent a social network because it lets relationships between friends as connections, like edges between nodes. Each person can have multiple friends, and those friends can be mutually connected, which can be shown well in a graph structure.

"""