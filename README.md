# User Orders

An example Flask application written in Python to demonstrate skills. It provides a REST API for managing users, items, orders, and reviews backed by PostgreSQL.

## Prerequisites

- Python 3
- PostgreSQL

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kylebessemer/user-orders.git
   cd user-orders
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:

   Create a PostgreSQL database, then set the `DATABASE_URL` environment variable:
   ```bash
   export DATABASE_URL=postgresql://user:password@localhost:5432/users_orders
   ```

5. Run database migrations:
   ```bash
   flask db upgrade
   ```

6. Start the server:
   ```bash
   python run.py
   ```
   The app runs at `http://localhost:8080`.

## API Endpoints

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/new` | Create a user (`first_name`, `last_name`) |
| GET | `/users/lookup/<id>` | Get a user with their orders and items |

### Items

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/items/new` | Create an item (`product_name`, `product_price`) |
| GET | `/items/lookup/<id>` | Get an item with paginated reviews (`page`, `page_size`) |

### Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders/new` | Create an order (`user_id`, `item_data`) |
| GET | `/orders/lookup/<id>` | Get an order with its items |

### Reviews

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/reviews/new` | Create a review for an item (`item_id`, `comment`) |

## License

This project is licensed under the [MIT License](LICENSE).
