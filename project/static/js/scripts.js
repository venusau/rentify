// Define functions in the global scope


const showPropertyDetail = async (id) => {
    const response = await fetch(`http://127.0.0.1:5000/properties/${id}`);
    const property = await response.json();
    window.location.href = '/property_detail';
    window.addEventListener('load', () => {
        updatePropertyDetails(property);
    });
};
const updatePropertyDetails = (property) => {
    document.getElementById('propertyTitle').innerText = property.title;
    document.getElementById('propertyDescription').innerText = property.description;
    document.getElementById('propertyPlace').innerText = property.place;
    document.getElementById('propertyArea').innerText = property.area;
    document.getElementById('propertyBedrooms').innerText = property.bedrooms;
    document.getElementById('propertyBathrooms').innerText = property.bathrooms;
    document.getElementById('propertyHospitalsNearby').innerText = property.hospitals_nearby;
    document.getElementById('propertyCollegesNearby').innerText = property.colleges_nearby;
    document.getElementById('propertyLikes').innerText = property.likes;
};
window.showPropertyDetail = showPropertyDetail;

const likeProperty = async (id) => {
    const response = await fetch(`http://127.0.0.1:5000/properties/${id}/like`, { method: 'POST' });
    const result = await response.json();
    document.querySelector(`.property[data-id="${id}"] span`).innerText = result.likes;
};

const showSellerDetails = async (id) => {
    const response = await fetch(`http://127.0.0.1:5000/properties/${id}`);
    const property = await response.json();
    const sellerResponse = await fetch(`http://127.0.0.1:5000/users/${property.seller_id}`);
    const sellerData = await sellerResponse.json();
    document.getElementById('sellerEmail').innerText = sellerData.email;
    document.getElementById('sellerPhone').innerText = sellerData.phone;
    document.getElementById('sellerDetails').style.display = 'block';
};


const applyFilters = async () => {
    const place = document.getElementById('filterPlace').value;
    const bedrooms = document.getElementById('filterBedrooms').value;
    const bathrooms = document.getElementById('filterBathrooms').value;

    const response = await fetch(`http://127.0.0.1:5000/properties/filter?place=${place}&bedrooms=${bedrooms}&bathrooms=${bathrooms}`);
    const properties = await response.json();
    propertiesList.innerHTML = properties.map(property => `
        <div class="property" data-id="${property.id}">
            <h3>${property.title}</h3>
            <p>${property.description}</p>
            <ul>
                <li>Place: ${property.place}</li>
                <li>Area: ${property.area} sq ft</li>
                <li>Bedrooms: ${property.bedrooms}</li>
                <li>Bathrooms: ${property.bathrooms}</li>
                <li>Hospitals Nearby: ${property.hospitals_nearby}</li>
                <li>Colleges Nearby: ${property.colleges_nearby}</li>
            </ul>
            <button onclick="likeProperty(${property.id})">Like</button> <span>${property.likes}</span> Likes
            <button onclick="showPropertyDetail(${property.id})">View Details</button>
        </div>
    `).join('');
    console.log(`/properties/filter?place=${place}&bedrooms=${bedrooms}&bathrooms=${bathrooms}`);
};

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const propertyForm = document.getElementById('propertyForm');
    const propertiesList = document.getElementById('propertiesList');
    const filters = document.getElementById('filters');

    if (filters) {
        filters.addEventListener('click', applyFilters);
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const response = await fetch('http://127.0.0.1:5000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });
            const result = await response.json();
            if (response.status === 200) {
                alert('Login successful');
                window.location.href = 'http://127.0.0.1:5000/seller_dashboard';
            } else {
                alert(result.message);
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const firstName = document.getElementById('firstName').value;
            const lastName = document.getElementById('lastName').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const password = document.getElementById('password').value;
            const isSeller = document.getElementById('isSeller').checked;

            const response = await fetch('http://127.0.0.1:5000/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ first_name: firstName, last_name: lastName, email, phone, password, is_seller: isSeller })
            });
            const result = await response.json();
            if (response.status === 201) {
                alert('Registration successful');
                window.location.href = 'http://127.0.0.1:5000/login';
            } else {
                alert(result.message);
            }
        });
    }

    if (propertyForm) {
        propertyForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const description = document.getElementById('description').value;
            const place = document.getElementById('place').value;
            const area = document.getElementById('area').value;
            const bedrooms = document.getElementById('bedrooms').value;
            const bathrooms = document.getElementById('bathrooms').value;
            const hospitals_nearby = document.getElementById('hospitals_nearby').value;
            const colleges_nearby = document.getElementById('colleges_nearby').value;

            const response = await fetch('http://127.0.0.1:5000/properties', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, description, place, area, bedrooms, bathrooms, hospitals_nearby, colleges_nearby })
            });
            const result = await response.json();
            if (response.status === 201) {
                alert('Property posted successfully');
                loadProperties();
            } else {
                alert(result.message);
            }
        });
    }

    const loadProperties = async () => {
        const response = await fetch('http://127.0.0.1:5000/properties');
        const properties = await response.json();
        propertiesList.innerHTML = properties.map(property => `
            <div class="property" data-id="${property.id}">
                <h3>${property.title}</h3>
                <p>${property.description}</p>
                <ul>
                    <li>Place: ${property.place}</li>
                    <li>Area: ${property.area} sq ft</li>
                    <li>Bedrooms: ${property.bedrooms}</li>
                    <li>Bathrooms: ${property.bathrooms}</li>
                    <li>Hospitals Nearby: ${property.hospitals_nearby}</li>
                    <li>Colleges Nearby: ${property.colleges_nearby}</li>
                </ul>
                <button onclick="likeProperty(${property.id})">Like</button> <span>${property.likes}</span> Likes
                <button onclick="showPropertyDetail(${property.id})">View Details</button>
            </div>
        `).join('');
    };

    if (propertiesList) {
        loadProperties();
    }

    
    window.logout = () => {
        fetch('http://127.0.0.1:5000/logout').then(() => {
            window.location.href = '/login';
        });
    };
});
