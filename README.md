																																
				GrocerEease RESTful API																					
																									
			This API is to support the front end of the GrocerEase list sorting application.
     

https://grocerease.herokuapp.com/grocerease/lists/	

List name as a string. Must have an auth token/be logged in so that list is associated with respective user.
POST: Creates a list with a list name, associated user, tags, and date created. 
GET: Provides all created lists for a given logged in user. 

https://grocerease.herokuapp.com/grocerease/list_detail/id/	

GET: Requires an auth token in the authorization header. This endpoint will retrieve a single list, excluding items, by a given list id.

https://grocerease.herokuapp.com/grocerease/edit_list/id/
	
ID of the respective list in the URL. List name(as a string) and tags(as IDS) can be updated. 
PUT/PATCH: Retrieves and updates exisiting lists. This is for updating the name of a list or tags, but not for adding new items to a list.
Name will take a string and tags take a tag ID.

https://grocerease.herokuapp.com/grocerease/delete_list/id/	

ID of the respective list in the URL. 
DELETE: Once list is accessed will delete entire list.

https://grocerease.herokuapp.com/auth/users/	

Username, email, and password. Creates a new user. 
POST: Can be used for the registration page. Will create an associated user ID.

https://grocerease.herokuapp.com/auth/token/login/

Registered user's username and password.
POST: Creates a session token for login(Make sure FE is passing auth token)

https://grocerease.herokuapp.com/auth/token/logout/	

Auth token. (No body is required for this request)	
POST: Destroys the session token, logging the person out. While no body is required for this request, the auth token must be sent in the Authorization header.

https://grocerease.herokuapp.com/grocerease/create_tag/	

Tag name as a string .	
POST:Creates a tag which can then later be assocaited with a list by ID.

https://grocerease.herokuapp.com/grocerease/lists/list_id/items/	

List ID in Url. For PATCH will require item name. Both require an auth token.	
GET: Gets the items on an exisiting list. Auth token must be provided in the header.
POST: Creates a list item by name on an existing list. Auth token must be provided in the header. "																									
