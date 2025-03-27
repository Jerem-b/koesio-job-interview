## API Documentation
Notes:
- To connect to the API there are no credentials required.
- To access the API go to localhost:4000

---

# Authors
## 📖 Retrieve All Authors

### `GET /authors`

**Description:**
Fetches a list of all authors along with their associated book IDs.

---

### Request Parameters
_None_

---

### Responses

#### ✅ 200 OK (Success)
```json
{
  "count": 3,
  "authors": [
    {
      "id": 1,
      "name": "Victor Hugo",
      "book_ids": [10, 12, 15]
    },
    {
      "id": 2,
      "name": "J.K. Rowling",
      "book_ids": [20, 22]
    },
    {
      "id": 3,
      "name": "J.R.R. Tolkien",
      "book_ids": [30, 31, 32]
    }
  ]
}
```

## ✍️ Create a New Author
### `POST /authors`
**Description:**
Creates a new author and saves it to the database.
### Request Body:
| Parameter | Type   | Required | Description           |
|-----------|--------|----------|-----------------------|
| `name`    | string | ✅ Yes    | The name of the author |
### Example Request:
```json
{
  "name": "Victor Hugo"
}
```
### Responses:
✅ 200 OK (Success)
```json
{
  "message": "Author Victor Hugo has been created successfully."
}
```
❌ 400 Bad Request (Invalid or missing JSON)
```json
{
  "error": "The request payload is not in JSON format."
}
```
❌ 500 Internal Server Error (Unexpected issue)
```json
{
  "error": "An unexpected error occurred."
}
```
## 📖 Retrieve a Specific Author

### `GET /authors/{author_id}`

**Description:**
Fetches details of a specific author by their ID, including the books they have written.

---

### Request Parameters
| Name       | Type   | Required | Description                |
|------------|--------|----------|----------------------------|
| `author_id` | `int`  | ✅       | The ID of the author to retrieve |

---

### Responses

✅ 200 OK (Success)
```json
{
  "message": "Success",
  "author": {
    "id": 1,
    "name": "Victor Hugo",
    "books": [10, 12, 15]
  }
}
```
❌ 404 Not Found
```json
{
  "message": "Author not found."
}
```

## ✏️ Update an Author

### `PATCH /authors/{author_id}`

**Description:**
Updates an existing author’s information.

---

### Request Parameters
| Name       | Type   | Required | Description                  |
|------------|--------|----------|------------------------------|
| `author_id` | `int`  | ✅       | The ID of the author to update |

---

### Request Body
| Name  | Type   | Required | Description                    |
|--------|--------|----------|--------------------------------|
| `name` | `string` | ❌       | The new name of the author (optional) |

---

### Responses

✅ 200 OK (Success)
```json
{
  "message": "Author Victor Hugo successfully updated."
}
```
❌ 400 Bad Request
```json
{
  "message": "Invalid request data."
}
```
❌ 404 Not Found
```json
{
  "message": "Author not found."
}
```

## 🗑️ Delete an Author

### `DELETE /authors/{author_id}`

**Description:**
Deletes an existing author from the database.

---

### Request Parameters
| Name       | Type   | Required | Description                  |
|------------|--------|----------|------------------------------|
| `author_id` | `int`  | ✅       | The ID of the author to delete |

---

### Responses

✅ 200 OK (Success)
```json
{
  "message": "Author Victor Hugo successfully deleted."
}
```
❌ 404 Not Found
```json
{
  "message": "Author not found."
}
```
❌ 500 Internal Server Error
```json
{
  "message": "Error while deleting author."
}
```

## 📚 Retrieve Books by Author

### `GET /authors/{author_id}/books`

**Description:**
Retrieves all books written by a specific author.

---

### Request Parameters
| Name       | Type   | Required | Description                  |
|------------|--------|----------|------------------------------|
| `author_id` | `int`  | ✅       | The ID of the author whose books are being retrieved |

---

### Responses

✅ 200 OK (Success)
```json
{
  "message": "Success",
  "books": [
    {
      "id": 1,
      "name": "Victor Hugo",
      "books": [101, 102, 103]
    }
  ]
}
```
❌ 404 Not Found
```json
{
  "message": "Author not found."
}
```

---
# Books
## 📚 Retrieve All Books
### `GET /books`

**Description:**
Fetch all books from the database.
---

### Request Parameters
_None_

---

### Responses

#### ✅ 200 OK (Success)
```json
    {
      "count": 2,
      "books": [
        {
          "id": 1,
          "name": "1984",
          "author_id": 1,
          "author_name": "George Orwell",
          "is_available": true,
          "type": "Dystopian"
        },
        {
          "id": 2,
          "name": "The Hobbit",
          "author_id": 2,
          "author_name": "J.R.R. Tolkien",
          "is_available": false,
          "type": "Fantasy"
        }
      ]
    }
```

## ✍️ Create a New Book
### `POST /books`
**Description:**
Creates a new book and saves it to the database.

### Request Body:
| Parameter     | Type    | Required | Description                          |
|--------------|---------|----------|--------------------------------------|
| `name`       | string  | ✅ Yes    | The name of the book                |
| `author_id`  | integer | ✅ Yes    | The ID of the author                |
| `is_available` | boolean | ✅ Yes    | Availability status of the book     |
| `type`       | string  | ✅ Yes    | The genre of the book   |

### Responses:
✅ 200 OK (Success)
```json
{
  "message": "Book '1984' has been created successfully."
}
```
❌ 400 Bad Request (Invalid JSON)
```json
{
  "error": "The request payload is not in JSON format."
}
```

## 📚 Retrieve a Book by ID

### `GET /books/{book_id}`
**Description:**
Retrieve details of a specific book by its ID.

### Request Parameters:
| Parameter  | Type    | Required | Description              |
|------------|---------|----------|--------------------------|
| `book_id`  | integer | ✅ Yes    | The ID of the book       |

### Responses:
✅ 200 OK (Success)
```json
{
  "message": "Success",
  "book": {
    "id": 1,
    "name": "1984",
    "author_id": 3,
    "author_name": "George Orwell",
    "is_available": true,
    "type": "Dystopian"
  }
}
```
❌ 404 Not Found
```json
{
  "message": "Book not found."
}
```

## ✏️ Update a Book

### `PATCH /books/{book_id}`
**Description:**
Update an existing book's details.

### Request Parameters:
| Parameter  | Type    | Required | Description              |
|------------|---------|----------|--------------------------|
| `book_id`  | integer | ✅ Yes    | The ID of the book       |

### Request Body:
| Parameter      | Type     | Required | Description                      |
|---------------|----------|----------|----------------------------------|
| `name`        | string   | ❌ No     | The updated name of the book    |
| `author_id`   | integer  | ❌ No     | The updated author ID           |
| `is_available`| boolean  | ❌ No     | Update availability status      |
| `type`        | string   | ❌ No     | The updated book category       |

### Responses:
✅ 200 OK (Success) 
```json
{
  "message": "Book '1984' successfully updated."
}
```
❌ 404 Not Found
```json
{
  "message": "Book not found."
}
```
❌ 400 Bad Request (Invalid JSON)
```json
{
  "error": "Invalid request body."
}
```

## 🗑️ Delete a Book

### `DELETE /books/{book_id}`
**Description:**
Remove a book from the database.

### Request Parameters:
| Parameter  | Type    | Required | Description              |
|------------|---------|----------|--------------------------|
| `book_id`  | integer | ✅ Yes    | The ID of the book       |

### Responses:
✅ 200 OK (Success)
```json
{
  "message": "Book '1984' successfully deleted."
}
```
❌ 404 Not Found
```json
{
  "message": "Book not found."
}
```
❌ 500 Internal Server Error
```json
{
  "message": "Error while deleting book."
}
```

## ✅ Get Available Books

### `GET /books/available`
**Description:**
Retrieve a list of books that are currently available.

### Responses:
✅ 200 OK (Success)
```json
{
  "count": 1,
  "books": [
    {
      "id": 1,
      "name": "1984",
      "author_id": 3,
      "author_name": "George Orwell",
      "is_available": true,
      "type": "Dystopian"
    },
  ]
}
```
✅ 200 OK (No available books)
```json
{
  "count": 0,
  "books": []
}
```

## 🔎 Search Books

### `GET /books/search`
**Description:**
Search for books based on name, author, or type.

### Request Parameters:
| Parameter  | Type   | Required | Description                          |
|------------|--------|----------|--------------------------------------|
| `name`     | string | ❌ No    | Filter books by name (partial match) |
| `author`   | string | ❌ No    | Filter books by author's name (partial match) |
| `type`     | string | ❌ No    | Filter books by type (partial match) |

### Responses:
✅ 200 OK (Success)
```json
{
  "count": 2,
  "books": [
    {
      "id": 1,
      "name": "The Hobbit",
      "author_id": 10,
      "author_name": "J.R.R. Tolkien",
      "is_available": true,
      "type": "Fantasy"
    },
    {
      "id": 2,
      "name": "Harry Potter",
      "author_id": 12,
      "author_name": "J.K. Rowling",
      "is_available": true,
      "type": "Fantasy"
    }
  ]
}
```
✅ 200 OK (No matches found)
```json
{
  "count": 0,
  "books": []
}
```

---
# Users
## 👤 User Creation
### `POST /register`

**Description:**
Creates a new user account and stores it in the database. The user provides a username and password. The password is hashed before being stored for security purposes.

### Request Body:
| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| `username` | string | ✅ Yes    | The username of the user   |
| `password` | string | ✅ Yes    | The password of the user   |

### Example Request:
```json
{
  "username": "john_doe",
  "password": "securePassword123"
}
```
### Responses:
✅ 200 OK (Success)
```json
{
  "message": "User john_doe has been created successfully."
}
```
❌ 400 Bad Request (Invalid JSON)
```json
{
  "error": "The request payload is not in JSON format."
}
```
❌ 500 Internal Server Error
```json
{
  "error": "An unexpected error occurred."
}
```

## 🔑 User Login
### `POST /login`

**Description:**
Logs in a user by verifying their username and password. The password is checked against the stored hashed password in the database.

### Request Body:
| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| `username` | string | ✅ Yes    | The username of the user   |
| `password` | string | ✅ Yes    | The password of the user   |

### Example Request:
```json
{
  "username": "john_doe",
  "password": "securePassword123"
}
```

### Responses:
✅ 200 OK (Success)
```json
{
  "message": "User john_doe successfully login."
}
```
❌ 400 Bad Request (Invalid JSON)
```json
{
  "error": "The request payload is not in JSON format."
}
```
❌ 401 Unauthorized (Invalid Credentials)
```json
{
  "error": "Invalid username or password."
}
```
❌ 500 Internal Server Error
```json
{
  "error": "An unexpected error occurred."
}
```

## 👥 List Users
### `GET /users`

**Description:**
Retrieves a list of all users in the system, including their borrows.

### Response:
| Parameter  | Type   | Description                                       |
|------------|--------|---------------------------------------------------|
| `count`    | int    | The number of users returned                      |
| `users`    | array  | A list of users, each containing their borrowings |

Each user object contains:  
| Parameter   | Type   | Description                                  |
|------------|--------|----------------------------------------------|
| `id`       | int    | The unique ID of the user                   |
| `username` | string | The username of the user                    |
| `borrows`  | array  | A list of books the user has borrowed       |

Each borrow object contains:  
| Parameter  | Type   | Description                         |
|-----------|--------|-------------------------------------|
| `id`      | int    | The unique ID of the borrow record |
| `book_id` | int    | The ID of the borrowed book        |
| `user_id` | int    | The ID of the user who borrowed it |

### Example Response:
✅ 200 OK (Success)
```json
{
  "count": 2,
  "users": [
    {
      "id": 1,
      "username": "john_doe",
      "borrows": [
        {
          "id": 101,
          "book_id": 5,
          "user_id": 1
        }
      ]
    },
    {
      "id": 2,
      "username": "jane_doe",
      "borrows": []
    }
  ]
}
