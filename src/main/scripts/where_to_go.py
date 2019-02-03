import json


def places_to_go(*args):
    user_config_filename = 'params/users.json'
    user_config = read_config(user_config_filename)
    i = 0
    while i < (len(user_config)):
        if list(set(user_config[i]["drinks"]).intersection(args[0]["drinks"])) > 0:
            if len(set(args[0]["food"]) - set(user_config[i]["wont_eat"])) > 0:
                pass
            else:
                avoid_reason = "There is nothing for {} to eat".format(user_config[i]["name"])
                return None, args[0]["name"], avoid_reason
        else:
            avoid_reason = "There is nothing for {} to drink".format(user_config[i]["name"])
            return None, args[0]["name"], avoid_reason
        i += 1
    return args[0]["name"], None, None


def read_config(config_filepath):
    with open(config_filepath) as config_file:
        config = json.load(config_file)
        return config


def main():
    venues_config_filename = 'params/venues.json'
    venues_config = read_config(venues_config_filename)
    final_to_go_list = []
    final_avoid_list = []
    avoid_reason = []
    i = 0
    while i < len(venues_config):
        output = places_to_go(venues_config[i])
        if output[0]:
            final_to_go_list.append(output[0])
        elif output[1]:
            final_avoid_list.append(output[1])
            avoid_reason.append(output[2])
        i += 1

    print("Places to go")
    print("\n".join(final_to_go_list))
    print("Places to avoid")
    j = 0
    while j < len(final_avoid_list):
        print (final_avoid_list[j])
        print (avoid_reason[j])
        j += 1


if __name__ == '__main__':
    main()
