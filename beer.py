import requests

API_KEY = 'a49e3307ae88ed372c85cf6602e256e7'

# API URIs
BEER_CATEGORIES_URI = 'http://api.brewerydb.com/v2/categories?key={0}'
BEER_STYLES_URI     = 'http://api.brewerydb.com/v2/styles?key={0}'
BEER_URI            = 'http://api.brewerydb.com/v2/beers?key={0}&styleId={1}'

# The brewery database associates a beer with it's style but not with it's category.
# Threrefore in order to fetch the beers belonging to a category, we first need to
# fetch all the styles associated with that category, for each style fetch the beer
# and finally aggregate the results of all styles

# Associate all the styles with the respective categories
def map_styles_to_categories(styles, categories):
    map = {}
    for category in categories['data']:
        if category['id'] not in map:
            map[category['id']] = [];
    for style in styles['data']:
        map[style['category']['id']].append(style['id'])
    return map
    
# Return and the category id for the choosen ordinal
def get_objectId_from_ordinal(categories, ordinal):
    return categories[ordinal]['id']

# get all the beers belonging to a category
def get_beers_for_category(category_with_styles, categoryId):
    beers = []
    for style in category_with_styles[categoryId]:
        r_beers = requests.get(BEER_URI.format(API_KEY, style))
        for beer in r_beers.json()['data']:
            beers.append(beer)
    return beers


categories = requests.get(BEER_CATEGORIES_URI.format(API_KEY)).json()
r_beer_styles = requests.get(BEER_STYLES_URI.format(API_KEY))
categories_to_styles_map = map_styles_to_categories(r_beer_styles.json(), categories)

print "Categories:\n"
for i, category in enumerate(categories['data']):
    print str(i) + " : " + category['name']

print "Please choose a category: ", 
choice = get_objectId_from_ordinal(categories['data'], int(raw_input()))

for beer in get_beers_for_category(categories_to_styles_map, choice):
    print beer['name'].encode("utf-8")




 
    
  



