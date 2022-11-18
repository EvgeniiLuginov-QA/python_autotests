import requests

pet = requests.post("https://petstore.swagger.io/v2/pet", json = {
  "id": 108,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "cow",
  "photoUrls": [
    "https://i.ibb.co/bP1507R/image.jpg"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print (pet.text)

rename = requests.put ("https://petstore.swagger.io/v2/pet", json = {
  "id": 108,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Гаврюша",
  "photoUrls": [
    "https://i.ibb.co/bP1507R/image.jpg"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print (rename.text)

find = requests.get ("https://petstore.swagger.io/v2/pet/108", )
print (find.text)