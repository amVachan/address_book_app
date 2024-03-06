# Address Book API Documentation

## Introduction

Welcome to the Address Book API documentation! This document provides information on how to start and use the APIs for managing addresses in the address book application.

## Getting Started

To get started with the Address Book API, follow these steps:

1. **Install Dependencies**: Make sure you have Python installed on your system. Then, install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```
2. **Start the FastAPI Server**: Start the FastAPI application using Uvicorn:

   ```
   uvicorn main:app --reload
   ```

3. **Access the API Documentation**: Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI documentation. Here, you can explore the available endpoints and test them interactively.

## API Endpoints

The Address Book API provides the following endpoints for managing addresses:

- **Create Address**: `POST /addresses/`
  - Create a new address in the address book.
  - Required fields: 'first_name', 'last_name', 'email_address', 'phone_number', 'street', 'city', 'state', 'postal_code', 'latitude', 'longitude'.

- **Get Address by ID**: `GET /addresses/{address_id}`
  - Retrieve an address by its ID from the address book.
  - Path parameter: `address_id` (integer).

- **Update Address**: `PUT /addresses/{address_id}`
  - Update an existing address in the address book.
  - Path parameter: `address_id` (integer).
  - Required fields: 'first_name', 'last_name', 'email_address', 'phone_number', 'street', 'city', 'state', 'postal_code', 'latitude', 'longitude'.

- **Delete Address**: `DELETE /addresses/{address_id}`
  - Delete an address from the address book.
  - Path parameter: `address_id` (integer).

- **Get Addresses Within Distance**: `GET /addresses/within_distance`
  - Retrieve addresses within a given distance from a target location.
  - Query parameters: `latitude`, `longitude`, `distance`.
  - Note: Distance is specified in kilometers.

## Usage Examples

### Create Address

To create a new address, send a POST request to `/addresses/` with the following JSON payload:

```json
{
  "first_name": "string",
  "last_name": "string",
  "email_address": "string",
  "phone_number": 0,
  "street": "string",
  "city": "string",
  "state": "string",
  "postal_code": 0,
  "latitude": 0,
  "longitude": 0
}
```

### Get Address by ID

To retrieve an address by its ID, send a GET request to `/addresses/{address_id}` with the address ID in the path parameter.

Example: `/addresses/1`

### Update Address

To update an existing address, send a PUT request to `/addresses/{address_id}` with the address ID in the path parameter and the updated address data in the JSON payload.

Example: `/addresses/1`

```json
{
  "first_name": "string",
  "last_name": "string",
  "email_address": "string",
  "phone_number": 0,
  "street": "string",
  "city": "string",
  "state": "string",
  "postal_code": 0,
  "latitude": 0,
  "longitude": 0
}
```

### Delete Address

To delete an address, send a DELETE request to `/addresses/{address_id}` with the address ID in the path parameter.

Example: `/addresses/1`

### Get Addresses Within Distance

To retrieve addresses within a given distance from a target location, send a POST request to `/addresses/within_distance` with the latitude, longitude, and distance specified as query parameters.

Example: `/addresses/within_distance?latitude=40.7128&longitude=-74.0060&distance=10`
