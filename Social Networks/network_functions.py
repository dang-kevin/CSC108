from typing import List, Tuple, Dict, TextIO


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]],
                  person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    lst = []
    for line in profiles_file:
        lst.append(line.strip())

    keys = [lst[0]]
    key_list(keys, lst)

    # Create person_to_friends dictionary

    for person in keys:
        person_to_friends[invert_name(person)] = []

    names = []
    names_list(names, lst)

    add_friends(person_to_friends, names)

    remove_key(person_to_friends)

    # Create person_to_networks dictionary

    for person in keys:
        person_to_networks[invert_name(person)] = []

    networks = []
    networks_list(networks, lst)

    add_networks(person_to_networks, networks)

    remove_key(person_to_networks)


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """
    Return the average number of friends that people who appear as keys in the
    given "person to friends" dictionary have.

    >>> get_average_friend_count({'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], \
    'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett',\
    'Jay Pritchett', 'Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett']})
    2.75
    """
    friend_count = 0

    for name in person_to_friends:
        friend_count += len(person_to_friends[name])

    if person_to_friends == {}:
        average = 0
    else:
        average = friend_count / len(person_to_friends)

    return average


def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a "last name to first names" dictionary based on the given "person
    to friends" dictionary.

    >>> get_families({'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': \
    ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', \
    'Luke Dunphy']})
    {'Pritchett': ['Gloria', 'Jay', 'Mitchell'], 'Dunphy': ['Claire', 'Luke', 'Phil'], 'Delgado': ['Manny']}
    """
    family = {}

    for person in person_to_friends:
        family[last_name(person)] = []
        for friend in person_to_friends[person]:
            family[last_name(friend)] = []

    for k in person_to_friends:
        if first_name(k) not in family[last_name(k)]:
            family[last_name(k)].append(first_name(k))
        for list_value in person_to_friends[k]:
            if first_name(list_value) not in family[last_name(list_value)]:
                family[last_name(list_value)].append(first_name(list_value))

    for family_name in family:
        family[family_name].sort()

    return family


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a "network to people" dictionary based on the "person to networks"
    dictionary.

    >>> p2n = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': \
    ['Law Association'], 'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': ['Clown School', \
    'Wizard of Oz Fan Club'], 'Phil Dunphy': ['Real Estate Association'], 'Gloria Pritchett': \
    ['Parent Teacher Association']}
    >>> invert_network(p2n)
    {'Parent Teacher Association': ['Claire Dunphy', 'Gloria Pritchett'], 'Chess Club': ['Alex Dunphy', 'Manny Delgado'], 'Law Association': ['Mitchell Pritchett'], 'Orchestra': ['Alex Dunphy'], 'Clown School': ['Cameron Tucker'], 'Wizard of Oz Fan Club': ['Cameron Tucker'], 'Real Estate Association': ['Phil Dunphy']}
    """
    network_to_people = {}

    for person in person_to_networks:
        networks = person_to_networks[person]
        for network in networks:
            if network not in network_to_people:
                network_to_people[network] = []
            network_to_people[network].append(person)
            network_to_people[network].sort()
    return network_to_people


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], person: str) -> List[str]:
    """
    Return the list of names of people who are friends of the person's friends.

    >>> p2f = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': \
    ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', \
    'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': \
    ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': \
    ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
    ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
    'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_friends_of_friends(p2f, 'Jay Pritchett')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']
    >>> get_friends_of_friends(p2f, 'Claire Dunphy')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', 'Luke Dunphy', 'Manny Delgado']
    """
    lst = []

    for mutual in person_to_friends[person]:
        for friend in person_to_friends[mutual]:
            if friend != person:
                lst.append(friend)
    lst.sort()
    return lst


def make_recommendations(person: str, person_to_friends: Dict[str, List[str]],
                         person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """
    Return the friend recommendations for the given person as a list of tuples
    where the first element of each tuple is a potential friend's name (in the
    same format as the dictionary keys) and the second element is that potential
    friend's score.


    """

    potential_friends = {}

    # recommend by mutual friends
    potential_friends = recommend_mutual_friend(person, person_to_friends, potential_friends)

    # recommend by networks
    potential_friends = recommend_network(person, person_to_networks, potential_friends)

    # recommend by last name
    potential_friends = recommend_last_name(person, person_to_friends, potential_friends)

    # sort by score
    potential_friend_sorted = sort_by_score(potential_friends)

    return convert_to_tuple(potential_friend_sorted, person_to_friends, person)


def last_name(full_name: str) -> str:
    """
    Return the last name of the person's full_name.

    >>> last_name('Kevin Dang')
    'Dang'
    """
    j = 0

    for i in range(len(full_name)):
        if full_name[i] == ' ':
            j = i
    return full_name[j+1:]


def first_name(full_name: str) -> str:
    """
    Return the first name of the person's full_name.

    >>> first_name('Kevin Dang')
    'Kevin'
    """
    j = 0

    for i in range(len(full_name)):
        if full_name[i] == ' ':
            j = i
    return full_name[:j]


def invert_name(name: str) -> str:
    """
    Return the person's inverted name without a comma.

    >>> invert_name('Dang, Kevin')
    'Kevin Dang'
    """
    j = 0

    for i in range(len(name)):
        if name[i] == ',':
            j = i
    return name[j+2:] + ' ' + name[:j]


def add_friends(person_to_friends: Dict[str, List[str]], names: List[str]) -> None:
    """
    Add values from names list to corresponding keys in person_to_friends
    dictionary. Blocks of values are separated by a space.

    >>> p2f = {'Jay Pritchett': []}
    >>> names_list =  ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado', ' ']
    >>> add_friends(p2f, names_list)
    >>> p2f
    {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado']}
    """
    i = 0
    for person in person_to_friends:
        flag = True
        while i < len(names) and flag:
            if names[i] != ' ':
                person_to_friends[person].append(names[i])
                person_to_friends[person].sort()
            else:
                flag = False
            i += 1


def add_networks(person_to_networks: Dict[str, List[str]], networks: List[str]) -> None:
    """
    Add values from networks list to corresponding keys in person_to_networks
    dictionary. Blocks of values are separated by the empty string.

    >>> p2n = {'Claire Dunphy': []}
    >>> networks_list = ['Parent Teacher Association', '', 'Chess Club']
    >>> add_networks(p2n, networks_list)
    >>> p2n
    {'Claire Dunphy': ['Parent Teacher Association']}
    """
    i = 0
    for person in person_to_networks:
        flag = True
        while i < len(networks) and flag:
            if networks[i] != '':
                person_to_networks[person].append(networks[i])
                person_to_networks[person].sort()
            else:
                flag = False
            i += 1


def remove_key(d: Dict[str, List[str]]) -> None:
    """
    Remove keys from the dictionary that have no values.

    >>> d = {'Jay Prichett': [], 'Claire Dunphy': ['Parent Teacher Association']}
    >>> remove_key(d)
    >>> d
    {'Claire Dunphy': ['Parent Teacher Association']}
    """
    no_value = []
    for k in d:
        if d[k] == []:
            no_value.append(k)

    for k in no_value:
        del(d[k])


def key_list(keys: List[str], lst: List[str]) -> None:
    """
    Create a list of keys with the necessary strings from list lst.

    >>> keys = ['Pritchett, Jay']
    >>> lst = ['Pritchett, Jay', 'Pritchett, Gloria', 'Delgado, Manny', 'Dunphy, Claire', '', 'Dunphy, Claire']
    >>> key_list(keys, lst)
    >>> print(keys)
    ['Pritchett, Jay', 'Dunphy, Claire']
    """
    i = 1
    for item in lst:
        if item == '':
            keys.append(lst[i])
            del(lst[i])
        i += 1
    del(lst[0])


def names_list(names: List[str], lst: List[str]) -> None:
    """
    Create a list of names in the format of 'first-name last-name' from the
    appropriate strings in list lst.

    >>> names = []
    >>> lst = ['Dunphy, Claire', 'Parent Teacher Association', 'Dunphy, Phil']
    >>> names_list(names, lst)
    >>> print(names)
    ['Claire Dunphy', 'Phil Dunphy']
    """
    for item in lst:
        if ',' in item or item == '':
            names.append(invert_name(item))


def networks_list(networks: List[str], lst: List[str]) -> None:
    """
    Create a list of networks from the appropriate strings in list lst.

    >>> networks = []
    >>> lst = ['Dunphy, Claire', 'Parent Teacher Association', 'Dunphy, Phil']
    >>> networks_list(networks, lst)
    >>> print(networks)
    ['Parent Teacher Association']
    """
    for item in lst:
        if ',' not in item:
            networks.append(item)


def add_to_score(dict_of_score: Dict[str, int], person: str) -> Dict[str, int]:
    """Add 1 to the person's score returning the updated dictionary.
    Docstring examples not given since result depends on input data.
    """
    if person in dict_of_score:
        dict_of_score[person] += 1
    else:
        dict_of_score[person] = 1

    return dict_of_score


def convert_to_tuple(dict_of_score: Dict[str, int], person_to_friends: Dict[str, List[str]], person: str)\
        -> List[Tuple[str, int]]:
    """Convert dict_of_score to a list of tuples.
    Docstring examples not given since result depends on input data.
    """
    list_of_score = []
    for key in dict_of_score:
        if key not in person_to_friends[person] and key != person:
            tup = tuple([key, dict_of_score[key]])
            list_of_score.append(tup)

    return list_of_score


def recommend_mutual_friend(person: str, person_to_friends: Dict[str, List[str]],
                            dict_pot_friends: Dict[str, int]) -> Dict[str, int]:
    """Recommend potential friends based on mutual friends.
    Docstring examples not given since result depends on input data.
    """
    potential_friends = get_friends_of_friends(person_to_friends, person)
    for friend in potential_friends:
        add_to_score(dict_pot_friends, friend)

    for key in person_to_friends:
        if key not in dict_pot_friends and person in get_friends_of_friends(person_to_friends, key):
            dict_pot_friends = add_to_score(dict_pot_friends, key)

    return dict_pot_friends


def recommend_network(person: str, person_to_networks: Dict[str, List[str]], dict_pot_friends: Dict[str, int]) \
        -> Dict[str, int]:
    """Recommend potential friends based on shared networks.
    Docstring examples not given since result depends on input data.
    """
    network = invert_network(person_to_networks)
    for key in network:
        if person in network[key]:
            for common_member in network[key]:
                dict_pot_friends = add_to_score(dict_pot_friends, common_member)

    return dict_pot_friends


def recommend_last_name(person: str, person_to_friends: Dict[str, List[str]], dict_pot_friends: Dict[str, int]) \
        -> Dict[str, int]:
    """Recommend potential friends based on shared last name.
    Docstring examples not given since result depends on input data.
    """

    family = get_families(person_to_friends)
    for lastname in family:
        if family[lastname] == person.split(' ')[-1]:
            for common_member in family:
                if common_member in dict_pot_friends:
                    dict_pot_friends = add_to_score(dict_pot_friends, common_member)

    return dict_pot_friends


def sort_by_score(d: Dict[str, int]) -> Dict[str, int]:
    """Sort the dictionary from highest to lowest score. If multiple people have the same score, sort alphabetically.
    Docstring examples not given since result depends on input data.
    """
    sort_alphabet = {}
    list_key = list(d.keys())
    list_key.sort()
    for key in list_key:
        sort_alphabet[key] = d[key]

    lst = []
    for key in sort_alphabet:
        lst = sort_alphabet[key]
    lst.sort(reverse=True)

    sort_score = {}
    for score in lst:
        for key in sort_alphabet:
            if score == sort_alphabet[key]:
                sort_score[key] = score

    return sort_score


if __name__ == '__main__':
    import doctest
    doctest.testmod()
