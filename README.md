```markdown
# Django Rest Invoice Management System

This is a Django-based Invoice Management System that provides APIs for creating, updating, and retrieving invoices along with their details. It is built using Django and Django Rest Framework.

## Features

- CRUD operations for Invoices
- Create and Update operations for Invoice Details
- API endpoints for managing invoices and associated details

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Django-rest.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django-rest
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at http://localhost:8000/api/invoices/

## Usage

### API Endpoints

- **List and Create Invoices**: `GET` and `POST` requests to `/api/invoices/`

- **Retrieve, Update, and Delete Invoice**: `GET`, `PUT`, and `DELETE` requests to `/api/invoices/<int:pk>/`

- **List and Create Invoice Details**: `GET` and `POST` requests to `/api/invoices/<int:invoice_pk>/details/`

- **Retrieve, Update, and Delete Invoice Detail**: `GET`, `PUT`, and `DELETE` requests to `/api/invoices/<int:invoice_pk>/details/<int:pk>/`

## Examples

### Create Invoice:

```rest
POST http://localhost:8000/api/invoices/
Content-Type: application/json

{
  "date": "2024-01-05",
  "customer_name": "John Doe"
}
```

### Retrieve All Invoices:

```rest
GET http://localhost:8000/api/invoices/
```

### Retrieve a Specific Invoice:

```rest
GET http://localhost:8000/api/invoices/1/
```

### Update Invoice:

```rest
PUT http://localhost:8000/api/invoices/1/
Content-Type: application/json

{
  "date": "2024-01-10",
  "customer_name": "Updated Customer"
}
```

### Delete Invoice:

```rest
DELETE http://localhost:8000/api/invoices/1/
```

### Create Invoice Detail for Invoice ID 1:

```rest
POST http://localhost:8000/api/invoices/1/details/
Content-Type: application/json

{
  "description": "Product ABC",
  "quantity": 5,
  "unit_price": 10.50
}
```

### Retrieve All Invoice Details for Invoice ID 1:

```rest
GET http://localhost:8000/api/invoices/1/details/
```

### Retrieve a Specific Invoice Detail (for Invoice ID 1, Detail ID 2):

```rest
GET http://localhost:8000/api/invoices/1/details/2/
```

### Update Invoice Detail (for Invoice ID 1, Detail ID 2):

```rest
PUT http://localhost:8000/api/invoices/1/details/2/
Content-Type: application/json

{
  "description": "Updated Product ABC",
  "quantity": 7,
  "unit_price": 12.75
}
```

### Delete Invoice Detail (for Invoice ID 1, Detail ID 2):

```rest
DELETE http://localhost:8000/api/invoices/1/details/2/
```


## Testing

To run the tests, use the following command:

```bash
python manage.py test
```

## Contributing

Feel free to contribute to the project by opening issues and submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
