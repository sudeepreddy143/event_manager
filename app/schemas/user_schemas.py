from builtins import ValueError, any, bool, str
from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid
import re

from app.utils.nickname_gen import generate_nickname

class UserRole(str, Enum):
    ANONYMOUS = "ANONYMOUS"
    AUTHENTICATED = "AUTHENTICATED"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"



class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=generate_nickname())
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer specializing in web applications.", max_length=500)
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profiles/john.jpg")
    linkedin_profile_url: Optional[str] = Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")
    
    @validator('profile_picture_url', 'linkedin_profile_url', 'github_profile_url', pre=True)
    def validate_url(cls, url: Optional[str]) -> Optional[str]:
        if url is None:
            return url
            
        # More comprehensive URL validation pattern
        url_regex = r'^(https?:\/\/)?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(\/[a-zA-Z0-9\-._~:/?#[\]@!$&\'()*+,;=]*)?$'
        
        if not re.match(url_regex, url):
            raise ValueError('Invalid URL format. URL must be properly formatted (e.g., https://example.com)')
            
        # Ensure URL has http/https scheme
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        return url
    
    class Config:
        from_attributes = True



@validator('bio')
def validate_bio_length(cls, v):
    if v is not None and len(v) > 500:
        raise ValueError('Bio must not exceed 500 characters')
    return v




class UserCreate(UserBase):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")
    @validator('password')
    def password_strength(cls, v):
        """Validate password strength."""
        min_length = 8
        if len(v) < min_length:
            raise ValueError(f'Password must be at least {min_length} characters long')
        
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
            
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
            
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
            
        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
        if not any(char in special_chars for char in v):
            raise ValueError('Password must contain at least one special character')
            
        return v


class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, example="john.doe@example.com")
    password: Optional[str] = Field(None, example="NewSecure*5678")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example="john_doe123")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer specializing in web applications.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profiles/john.jpg")
    linkedin_profile_url: Optional[str] =Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")
    
    
    
    @validator('password')
    def password_strength(cls, v):
        if v is None:
            return v
            
        min_length = 8
        if len(v) < min_length:
            raise ValueError(f'Password must be at least {min_length} characters long')
        
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
            
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
            
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
            
        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
        if not any(char in special_chars for char in v):
            raise ValueError('Password must contain at least one special character')
            
        return v

    @root_validator(pre=True)
    def check_at_least_one_value(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided for update")
        return values

class UserResponse(UserBase):
    id: uuid.UUID = Field(..., example=uuid.uuid4())
    role: UserRole = Field(default=UserRole.AUTHENTICATED, example="AUTHENTICATED")
    email: EmailStr = Field(..., example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=generate_nickname())    
    role: UserRole = Field(default=UserRole.AUTHENTICATED, example="AUTHENTICATED")
    is_professional: Optional[bool] = Field(default=False, example=True)

class LoginRequest(BaseModel):
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="The requested resource was not found.")

class UserListResponse(BaseModel):
    items: List[UserResponse] = Field(..., example=[{
        "id": uuid.uuid4(), "nickname": generate_nickname(), "email": "john.doe@example.com",
        "first_name": "John", "bio": "Experienced developer", "role": "AUTHENTICATED",
        "last_name": "Doe", "bio": "Experienced developer", "role": "AUTHENTICATED",
        "profile_picture_url": "https://example.com/profiles/john.jpg", 
        "linkedin_profile_url": "https://linkedin.com/in/johndoe", 
        "github_profile_url": "https://github.com/johndoe"
    }])
    total: int = Field(..., example=100)
    page: int = Field(..., example=1)
    size: int = Field(..., example=10)
