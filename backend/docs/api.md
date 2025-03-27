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

**📝 Description:**
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

**📝 Description:**
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

**📝 Description:**
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

**📝 Description:**
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
