# Product CRUD application

## This application is built using Flask, a Python web framework, and provides a RESTful API for managing product data.

### Features
- **CRUD Operations:** Supports Create, Read, Update, and Delete actions for product records.
- **Product Attributes:** Manages data points such as `product_name`, `product_type`, `price`, and `stock`.    
- **Pagination & Filtering:** The listing endpoint includes built-in pagination (defaulting to 10 records per page) and supports filtering by product type.
  
### API Endpoints
- **POST** `/product/create` Create a new product record.
- **GET** `/product/list?page_number=1&page_size=100&product_type=electronics` Retrieve a paginated list of products with optional type filtering.
- **GET** `/product/<int:product_id>/details` Retrieve details for a specific product by ID.
- **PUT** `/product/<int:product_id>/update` Update existing product information.
- **DELETE** `/product/<int:product_id>/delete` Remove a product record from the system.

### Setup Instructions
- **Create a Virtual Environment** Run the following command to create a Python virtual environment: `python -m venv ~/.virtualenvs/SMB_TASk`
- **Install Dependencies** Install the necessary packages using the requirements file: `pip install -r requirements.txt`
- **Configure Environment Variables** Since this project uses a Supabase PostgreSQL database, you must create a `.env` file in the root directory and add your credentials in the following format:
	`SMB_ENV=development SQLALCHEMY_DATABASE_URI=your_database_uri_here SQLALCHEMY_POOL_SIZE=10`
- **Run the Application** Execute the following command to start the server: `python manage.py run --port 5500`
