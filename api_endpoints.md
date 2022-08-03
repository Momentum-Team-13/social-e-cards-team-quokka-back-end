# Api Endpoints

Base URL: [https://quokka-cards.herokuapp.com/](https://quokka-cards.herokuapp.com/)

|  | Method | URL | Description |
| --- | --- | --- | --- |
| Authentication | POST | /api/auth/users/ | Create User |
|  | POST | /api/auth/token/login/ | Login |
|  | POST | /api/auth/token/logout/ | Logout |
| Users and Following | GET | /users/ | All Users List |
|  | GET | /users/?username=<searched username> | Search for User |
|  | POST | /users/follow | Follow a User |
|  | DELETE | /users/unfollow/:id | Unfollow a User |
|  | GET | /following/ | Following List |
|  | GET | /followers/ | Followers List |
| Greeting Cards | POST | /cards/new/ | New Card |
|  | GET | /cards/:id/ | Card Detail |
|  | PUT/PATCH | /cards/:id/ | Update Card |
|  | DELETE | /cards/:id/ | Delete Card |
|  | GET | /cards/ | All Cards List |
|  | GET | /cards/timeline/ | Timeline for Following Cards |
|  | GET | /profile/ | Profile |

---

## Authentication

---

### Create User

> /api/auth/users/
> 
- Method: POST
- Data json:

```python
{ 
	"username": "<username>", 
	"password": "<password>" 
}
```

- Response: User json object

### Login

> /api/auth/token/login/
> 
- Method: POST
- Data json:

```python
{ 
	"username": "<username>", 
	"password": "<password>" 
}
```

- Response: Example Authentication Token

```python
{
	"auth_token": "a65751fc4fa58a41cce703fb4deee8a9fe367618"
}
```

### Logout

> /api/auth/token/logout/
> 

Method: POST

Data: Authentication Token (See Example Auth Token in Login Section)

Response: No Data

---

## Users and Following

---

### All Users

> /users/
> 

Method: GET

Response: Array of all users

### Search for a User

> /users/?username=<searched username>
> 

Method: GET

Response: Array of all users meeting the criteria of the search term

### Follow a User

> /users/follow
> 

Method: POST

Data json

```python
{
	"following": "<id of user to be followed>",
}
```

Response: 201 Created

### Unfollow a User

> /users/unfollow/:id
> 

Note: Id is the id of the user to unfollow

Method: DELETE

Data json

Response: 204 No Content

### Following List

> /following/
> 

Method: GET

Response: Array of all users that the logged in user is following

### Followers List

> /followers/
> 

Method: GET

Response: Array of all users that are following the logged in user

---

## Greeting Cards

---

### New Card

> /cards/new/
> 

Method: POST

Data json: 

```python
{
	"user_id": "<This field is automatically populated.>",
	"title": "<Not required>",
	"message": "<This field is required.>",
	"font": "<Default = Roboto>",
	"font_color": "<Default = Black>",
	"bg_color": "<Default = White>",
	"border_color": "<Default = Black>",
	"border_style": "<Not required>",
	"img_src": "<Not required>"
}
```

Response: 201 Created

### Card Detail

> /cards/:id/
> 

Note: Id is the id of the card object

Method: GET

Response: Single card object

### Update Card

> /cards/:id/
> 

Method: PATCH

Data json: Example

```python
{
	"title": "This is a New Title",
}
```

Response: 200 OK

### Delete Card

> /cards/:id/
> 

Note: Id is the id of the card to delete

Method: DELETE

Response: 204 No Content

### See All Cards

> /cards/
> 

Method: GET

Response: Array of all greeting cards

```python
[
	{
		"id": 3,
		"user_id": 2,
		"username": "TestUser",
		"created_at": "2022-07-27T19:07:35.258685Z",
		"title": "Happy 4th of July",
		"message": "Boom! I like fireworks!",
		"font": "font-family: 'Dancing Script', cursive;",
		"font_color": "#0086FF",
		"bg_color": "#FF0000",
		"border_color": "#FFFFFF",
		"border_style": "",
		"img_src": ""
	},
	{
		"id": 4,
		"user_id": 1,
		"username": "admin",
		"created_at": "2022-07-29T12:33:24.863761Z",
		"title": "<Not required>",
		"message": "Test Message",
		"font": "font-family: 'Roboto', sans-serif;",
		"font_color": "#000000",
		"bg_color": "#FFFFFF",
		"border_color": "#000000",
		"border_style": "",
		"img_src": ""
	},
]
```

### Timeline for Following Cards

Method: GET

Response: Array of cards created by users the logged in user is following

### Profile

> /profile/
> 

Method: GET

Response: Array of all cards created by the logged in user

---