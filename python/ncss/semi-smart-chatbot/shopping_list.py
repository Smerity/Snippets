import spacy

nlp = spacy.load('en_core_web_md')

def similar(a, b):
    return nlp(a).similarity(nlp(b))

def find_best_spot(w, collection):
    best_score = 0
    best_category = None
    best_match = None
    for category in collection:
        for item in collection[category]:
            score = similar(w, item)
            if score > best_score:
                best_score = score
                best_category = category
                best_match = item
    return best_category, best_score, best_match

ghost_list = {
    'the supermarket': ['apples', 'cereal', 'milk', 'tissues'],
    'Kmart': ['shoes', 'handbag', 'shirts', 'underwear'],
    'Bunnings': ['hammers', 'nails', 'concrete', 'lawnmowers', 'ladders'],
    'Ikea': ['chairs', 'tables', 'glasses', 'lamps', 'cutlery'],
    'the computer store': ['iPads', 'computers', 'iPhones', 'laptops', 'USB', 'cables'],
}

shopping_list = {}

while True:
    item = input('> What item do you want? ')
    if item == 'shopping list' or item == 'list':
        print('Your shopping list is:')
        if shopping_list:
            for cat in shopping_list:
                print(f' - {cat} = {", ".join(shopping_list[cat])}')
        else:
            print('... empty ...')
    else:
        best_category, _, best_match = find_best_spot(item, ghost_list)
        print(f"I'll remind you when you're near {best_category} as they have {best_match}")
        if best_category not in shopping_list:
            shopping_list[best_category] = []
        shopping_list[best_category].append(item)
