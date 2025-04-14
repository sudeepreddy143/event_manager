import pytest
from uuid import UUID, uuid4
from datetime import datetime

@pytest.fixture
def user_base_data():
    """Fixture for valid UserBase data"""
    return {
        "email": "john.doe@example.com",
        "nickname": "johndoe123",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_base_data_invalid():
    """Fixture for invalid UserBase data with incorrect email format"""
    return {
        "email": "john.doe.example.com",  # Invalid email format
        "nickname": "johndoe123",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_create_data():
    """Fixture for valid UserCreate data"""
    return {
        "email": "john.doe@example.com",
        "password": "Secure*1234",
        "nickname": "johndoe123",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "I am a software engineer with over 5 years of experience.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe"
    }

@pytest.fixture
def user_update_data():
    """Fixture for valid UserUpdate data"""
    return {
        "email": "john.doe.new@example.com",
        "first_name": "John H.",
        "last_name": "Doe",
        "bio": "I specialize in backend development with Python and Node.js.",
        "profile_picture_url": "https://example.com/profile_pictures/john_doe_updated.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe_updated",
        "github_profile_url": "https://github.com/johndoe_updated"
    }

@pytest.fixture
def user_response_data():
    """Fixture for valid UserResponse data"""
    return {
        "id": uuid4(),  # Generate a valid UUID
        "email": "test@example.com",
        "nickname": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "bio": "Test user bio",
        "profile_picture_url": "https://example.com/profiles/test.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/testuser",
        "github_profile_url": "https://github.com/testuser",
        "role": "AUTHENTICATED",
        "is_professional": False
    }

@pytest.fixture
def login_request_data():
    """Fixture for valid LoginRequest data"""
    return {
        "email": "john.doe@example.com",
        "password": "SecurePassword123!"
    }