from super_secret_secrets import PET_FINDER_API_KEY, API_SECRET
import requests
import random

def get_oauth_token():
    """ Gets an Oauth token from PetFinder API """

    response = requests.post("https://api.petfinder.com/v2/oauth2/token",
                data = {
                    "grant_type" : "client_credentials",
                    "client_id" : PET_FINDER_API_KEY,
                    "client_secret" : API_SECRET
                })
    
    return response.json()["access_token"]


def get_random_pet(auth_token):
    """ Gets a random pet from PetFinder API """

    response = requests.get('https://api.petfinder.com/v2/animals',
             headers={"Authorization": f"Bearer {auth_token}"},
             params={"limit": "100"})
            
    random_animal = response.json()["animals"][random.randint(0, 99)]

    photo_url = ""

    if len(random_animal["photos"]) != 0: 
        photo_url = random_animal["photos"][0]["medium"]

    # photo_url = random_animal["photos"][0] if len(random_animal["photos"]) != 0 else ""

    return {
            'name': random_animal["name"],
            'age': random_animal["age"],
            'photo_url': photo_url
            }


