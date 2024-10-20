from collections import defaultdict

deks = defaultdict(set)
players = defaultdict(set)
card_name_to_id = {}
card_id_counter = 0
while s := input():
    s = s.split("/")
    if s[0].strip().isdecimal():
        if s[1] not in card_name_to_id:
            card_name_to_id[s[1]] = card_id_counter
            card_id_counter += 1
        card_id = card_name_to_id[s[1]]
        deks[int(s[0])].add(card_id)
    else:
        player_name = s[0]
        deck_number = int(s[1])
        players[player_name].add(deck_number)

max_pack_size = 0
player_pack_sizes = {}

for player_name, deck_numbers in players.items():
    unique_cards = set()
    for deck_number in deck_numbers:
        if deck_number in deks:
            unique_cards.update(deks[deck_number])
    pack_size = len(unique_cards)
    player_pack_sizes[player_name] = pack_size
    if pack_size > max_pack_size:
        max_pack_size = pack_size

players_with_max_pack = [player_name for player_name, size in player_pack_sizes.items() if size == max_pack_size]

print(*sorted(players_with_max_pack), sep="\n")
