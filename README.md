# TeamMatcha-GrocerEase_BackEnd
The GrocerEase Backend API
Status	Priority	Method	BaseURL	URL	Input	Output
Complete	1	POST	https://grocerease.herokuapp.com/	grocerease/create_list	list name, user name, products	Creates a new list
Complete	1	POST	https://grocerease.herokuapp.com/	grocerease/add_list_item/id/	url id of list. In list list item id to add to list	Adds and item to a list
Complete	1	PATCH	https://grocerease.herokuapp.com/	grocerease/delete_list_item/id/	url id of list. In list list item id to delete from list	Deletes an item from a list
Complete	1	PATCH	https://grocerease.herokuapp.com/	grocerease/edit_list_item/id/	url id of list. In list list item id to edit list	Edits and item on a list
Complete	1	DELETE	https://grocerease.herokuapp.com/	grocerease/delete_list/id/	url id of list. Once list is accessed will give the option to delte entire list. 	Deletes entire saved list
Complete	2	POST	https://grocerease.herokuapp.com/	grocerease/register	username, email, password	Creates a new user
Complete	2	POST	https://grocerease.herokuapp.com/	auth/token/login/	username, email	Creates a session token for login
Complete	2	DELETE	https://grocerease.herokuapp.com/	auth/token/logout/	username, email	Destroys the session token, logging the person out. 

