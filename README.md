# Rentify

Rentify is a web application designed to help people find the correct tenants and assist tenants in finding the perfect home based on their key requirements. This README provides a detailed overview of the application, including its features, tech stack, and development guidelines.

## Note:
 This project is currently in an incomplete state. Achieving a complete and polished version of Rentify will take more time. Future updates and enhancements are planned to bring the project to its full potential.

## Features

### User Authentication

- **Sign Up**: Users can register with their first name, last name, email, and phone number. Users can be either buyers or sellers.
- **Login**: Users can log in to access the application's features.

### Seller Flow

- **Post Property**: Sellers can post properties by providing details such as place, area, number of bedrooms, bathrooms, nearby hospitals, and colleges.
- **View Posted Properties**: Sellers can view the properties they have posted.
- **Update/Delete Property**: Sellers can update or delete their posted properties.

### Buyer Flow

- **View Properties**: Buyers can view all the posted rental properties.
- **Interested Button**: Buyers can click the "I'm Interested" button on a property widget to view seller details.
- **Filters**: Buyers can apply filters based on property details (e.g., place, number of bedrooms, number of bathrooms).

### Additional Features

- **Pagination**: Proper pagination to handle the listing of properties.
- **Form Validation**: Ensure all forms have proper validation.
- **Authorization**: Mandate that only logged-in users can view property details, redirect unauthorized users to the login page.
- **Like Button**: Each property has a like button to track the count in real-time.

## Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Flask

### Database

- SQLite (for development purposes)

## Development Guidelines

This project is intended to be built within 4 hours. Below is the mandatory flow and features that need to be implemented:

### Part 1: User Authentication & Property Management

#### User Authentication

- Implement user registration (sign up) and login.
- Use Flask-Login for handling user sessions.

#### Seller Flow

- Create a form for sellers to post property details.
- Display a list of properties posted by the seller.
- Allow sellers to update or delete their properties.

#### Buyer Flow

- Display a list of all posted properties for buyers.
- Implement a button on each property widget that reveals seller details when a buyer is interested.
- Implement filters for buyers to narrow down their search based on property details.

### Part 2: Additional Features

- Implement pagination for property listings.
- Add form validation to ensure all required fields are filled out correctly.
- Ensure only logged-in users can view property details; redirect unauthorized users to the login page.
- Add a like button to each property and track the like count in real-time using JavaScript and backend updates.

## Setup

To run this project, the following packages are important to download and install:

- Python should be installed.
- Flask
- Flask-Login
- Flask-CORS
- Flask-SQLAlchemy
- Werkzeug Security

After successfully installing these packages, you can run the `app.py` file, and the app will be ready to use.

# Future Improvements

- **Complete the Implementation**:
  - Continue developing and finalizing all the features listed in this README. 
  - This project is currently in a preliminary state and is **absolutely not complete**. Achieving a fully functional version will take additional time and effort.

- **Enhance UI/UX**:
  - Focus on improving the user interface and user experience to make the application more intuitive and user-friendly.
  - Implement modern design principles to ensure a visually appealing and easy-to-navigate interface.

- **Optimize Backend**:
  - Work on optimizing the backend code for better scalability and performance.
  - Refactor existing code to improve efficiency and handle a larger number of concurrent users and data.

- **Expand Property Attributes and Filters**:
  - Add more detailed property attributes to provide comprehensive information to users.
  - Introduce additional filters to allow users to refine their searches based on more specific criteria.

---
