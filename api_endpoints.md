# Api Endpoints

Base URL: [https://quokka-cards.herokuapp.com/](https://quokka-cards.herokuapp.com/)

|  | Method | URL | Description |
| --- | --- | --- | --- |
| Authentication | POST | /api/auth/users/ | Create User |
|  | POST | /api/auth/token/login/ | Login |
|  | POST | /api/auth/token/logout/ | Logout |
| Greeting Cards | POST | /cards/new/ | New Card |
|  | GET | /cards/ | See All Cards |
|  | PATCH | /cards/:id/ | Update Card |
|  | GET | /cards/:id/ | Card Detail |
|  | DELETE | /cards/:id/ | Delete Card |
| Users and Following | GET | /users/ | All Users |
|  | GET | /profile/ | User Profile |
|  |  |  |  |

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
	"user_id": "<This field is required.>",
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

### User Profile

> /profile/
> 

Method: GET

Response: Array of all cards by User