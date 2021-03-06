# GrocerEase API

GrocerEase is designed to help eliminate the emotional labor of grocery shopping. Users can create list tags which can then be assigned to named lists. Lists automatically are assigned a date created once the list data is submitted. Users can then populate the lists by entering a product name, item quantity, and a category choice. Once the user accesses their saved items via a GET request it will return a sorted grocery list. The list is sorted by common grocery store layout, based on market research. 


## Installation

Once this repo has been cloned, use pipenv to install all of the necessary dependencies from the Pipfile. 

```bash
pipenv install 
```

## REST API Endpoints

Please see the list of endpoints and their respective functionality below. This application is deployed via Heroku.com and has a base URL of:

```bash
https://grocerease.herokuapp.com
```
#### Input:
List name as a string. Must have an auth token/be logged in so that list is associated with respective user. 
#### POST: 
Creates a list with a list name, associated user, tags, and date created. 
#### JSON:
```bash
{
	"name": "Weeknight Dinners",
	"tags": [1]
}
```
#### GET: 
Provides all created lists for a given logged-in user. 
List name as a string. Must have an auth token/be logged in so that list is associated with respective user. 
#### JSON:
```bash
{
	"pk": 5,
	"name": "Weeknight Dinners",
	"user": 1,
	"tags": [
		1
	],
	"date_created": "2022-01-31T18:35:33.677009Z"
}
```
```bash
https://grocerease.herokuapp.com/grocerease/list_detail/id/
```
#### Input:
ID of the respective list in the URL. Requires an auth token in the authorization header.  
#### GET: 
This endpoint retrieves a single list, excluding items, by a given list id. 
#### JSON:
```bash
{
	"pk": 2,
	"name": "Baby Shower Grocery List",
	"user": 1,
	"tags": [
		1
	],
	"date_created": "2022-01-29T15:13:11Z"
}
```
```bash
https://grocerease.herokuapp.com/grocerease/delete_list/id/
```
#### Input:
ID of the respective list in the URL. Requires an auth token in the authorization header.   
#### DELETE: 
Once list is accessed will delete entire list giving a 204 response. 

```bash
https://grocerease.herokuapp.com/grocerease/edit_list/id/
```
#### Input:
ID of the respective list in the URL. List name(as a string) and tags(as ID) can be updated. Requires an auth token in the authorization header.    
#### PUT/PATCH: 
Retrieves and updates existing lists. This endpoint for updating the name of a list or tags, but not for adding new items to a list.
Name will take a string and tags take a tag ID. 
#### JSON:
```bash
{
	"pk": 7,
	"name": "Essential Shopping List",
	"user": 2,
	"tags": [1],
	"date_created": "2022-01-21T06:12:06.159448Z"
}
```
```bash
https://grocerease.herokuapp.com/grocerease/create_tag/
```
#### Input:
Tag name as a string.
#### POST:
Creates a tag which can then later be associated with a list by ID.
#### JSON:
```bash
{
	"tag": "Bulk Shopping"
}
```
```bash
https://grocerease.herokuapp.com/grocerease/lists/list_id/items/
```
#### Input:
List-ID in Url. For POST will require item name. Both GET and POST require an auth token. This field will take  "name" and "item_quantity". Please note "item_quantity" does default to a value of 1.
Requires an auth token in the authorization header. 
#### POST:
Creates a list item by name on an existing list. A choice from the choices field must be provided. Auth token must be provided in the header. 
#### Choices:
```bash
    ("Produce"),
    ("Dairy"),
    ("Baked Goods"),
    ("Meat and Fish"),
    ("Snacks"),
    ("Alcohol"),
    ("Baby Care"),
    ("Canned Goods"),
    ("Dry Goods"),
    ("Sauces and  Condiments"),
    ("Herbs and Spices"),
    ("Non-Alcoholic Beverages"),
    ("Household and Cleaning"),
    ("Health and Beauty"),
    ("Pet Care"),
    ("Frozen Goods"),
```
#### Response:
```bash
{
	"name": "Cucumbers",
	"item_quantity": 4,
	"choices": "Produce"
}
```
#### GET:
Gets the items on an existing list sorted by item category. Auth token must be provided in the header.
#### JSON:
```bash
{
		"pk": 14,
		"list": 2,
		"name": "Mixed Nuts",
		"item_quantity": 1,
		"choices": "Snacks"
	},
	{
		"pk": 12,
		"list": 2,
		"name": "Lentils",
		"item_quantity": 1,
		"choices": "Dry Goods"
	},
	{
		"pk": 7,
		"list": 2,
		"name": "Cinnamon",
		"item_quantity": 1,
		"choices": "Herbs and Spices"
	},
	{
		"pk": 9,
		"list": 2,
		"name": "Shampoo",
		"item_quantity": 1,
		"choices": "Health and Beauty"
	},
	{
		"pk": 11,
		"list": 2,
		"name": "Tater Tots",
		"item_quantity": 1,
		"choices": "Frozen Goods"
	}
```
```bash
https://grocerease.herokuapp.com/grocerease/item_detail/id/
```
#### Input:
Item ID in URL. Input "name," or "item_quantity." Requires an auth token in the authorization header. 
#### PUT/PATCH:
Retrieves a single item by item id. Can be used to update item information. 
#### JSON:
```bash
{
	"name": "Cucumbers",
	"item_quantity": 2
}
```
```bash
https://grocerease.herokuapp.com/grocerease/delete_item/id/
```
#### Input:
Item ID in URL.
Requires an auth token in the authorization header.   
#### DELETE: 
Once list is accessed will delete entire list giving a 204 response. 

```bash
https://grocerease.herokuapp.com/auth/users/
```
#### Input:
Desired username and password. 
#### POST:
Creates a new user. Can be used for the registration page. Will create an associated user ID.
#### JSON:
```bash
{
	"username": "TestUser",
	"password": "Badpassword"
}
```
```bash
https://grocerease.herokuapp.com/auth/token/login/
```
#### Input:
Registered user's username and password.
#### POST:
Creates a session token for login.
Returns a secure auth token for the user session.

```bash
https://grocerease.herokuapp.com/auth/token/logout/
```
#### Input:
Auth token. No body is required for this request.
#### POST:
Destroys the session token, logging the user out. While no body is required for this request, the auth token must be sent in the authorization header.






