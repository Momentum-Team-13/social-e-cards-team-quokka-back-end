# Api Endpoints

Base URL: [https://quokka-cards.herokuapp.com/](https://quokka-cards.herokuapp.com/)

|  | Method | URL | Description |
| --- | --- | --- | --- |
| Authentication | POST | /api/auth/users/ | Create User |
|  | POST | /api/auth/token/login/ | Login |
|  | POST | /api/auth/token/logout/ | Logout |
| Greeting Cards | POST | /cards/new/ | New Card |
|  | GET | /cards/ | All Cards List |
|  | GET | /cards/timeline/ | Card Timeline for Following |
|  | PATCH | /cards/:id/ | Update Card |
|  | GET | /cards/:id/ | Card Detail |
|  | DELETE | /cards/:id/ | Delete Card |
| Users and Following | GET | /users/ | All Users List |
|  | GET | /users/?username=<searched username> | Search for User |
|  | GET | /profile/ | User Profile |
|  | POST | /users/follow | Follow a User |
|  | DELETE | /users/unfollow/:id | Unfollow a User |
|  | GET | /following/ | Following List |
|  | GET | /followers/ | Followers List |

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

### See All Cards

> /cards/
> 

Method: GET

Response: Array of Greeting Cards

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

### Card Timeline for Following

Method: GET

Response: Array of cards from people the user follows

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

### Card Detail

> /cards/:id/
> 

Method: GET

Response: Singular Card Object

### Delete Card

> /cards/:id/
> 

Method: DELETE

Response: 204 No Content

---

## Users and Following

---

### All Users

> /users/
> 

Method: GET

Response: Array of All Users

### Search for a User

> /users/?username=<searched username>
> 

Method: GET

Response: Array of All users meeting the criteria of the search term

### User Profile

> /profile/
> 

Method: GET

Response: Array of all cards by User

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

Note: Id is the id of the user you want to unfollow

Method: DELETE

Data json

Response: 204 No Content

### Following List

> /following/
> 

Method: GET

Response: Array of everyone you follow

### Followers List

> /followers/
> 

Method: GET

Response: Array of everyone that follows you