"""This module demonstrates the use of pydantic in Python."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl, field_validator


class UserBase(BaseModel):
    """Base user model with common attributes."""

    name: str = Field(description="User's full name - must contain a space")
    email: str = Field(
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="User's email address",
    )
    age: int = Field(gt=0, lt=120, description="User's age - must be between 0 and 120")
    is_active: bool = Field(
        default=True, description="Whether the user account is active"
    )


class UserCreate(UserBase):
    """Model for creating a new user."""

    password: str = Field(
        min_length=8, description="User's password - minimum 8 characters"
    )


class User(UserBase):
    """Complete user model with additional fields."""

    id: int = Field(description="Unique identifier for the user")
    created_at: datetime = Field(
        default_factory=datetime.now, description="Timestamp when the user was created"
    )
    tags: List[str] = Field(
        default_factory=list, description="List of tags associated with the user"
    )
    website: Optional[HttpUrl] = Field(
        default=None, description="User's personal website URL"
    )

    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        """Validate that the name contains a space."""
        if " " not in v:
            raise ValueError("name must contain a space")
        return v.title()


class Address(BaseModel):
    """Address model with validation."""

    street: str = Field(description="Street address including house number")
    city: str = Field(description="City name")
    country: str = Field(description="Country name")
    postal_code: str = Field(
        pattern=r"^\d{5}(-\d{4})?$",
        description="US postal code in format: 12345 or 12345-6789",
    )


class Profile(BaseModel):
    """Profile model with nested models."""

    user: User = Field(description="User information")
    address: Optional[Address] = Field(
        default=None, description="User's address details"
    )
    bio: Optional[str] = Field(
        default=None,
        max_length=500,
        description="User's biography - maximum 500 characters",
    )
    followers: List[User] = Field(
        default_factory=list, description="List of users following this profile"
    )


def create_sample_user() -> User:
    """Create a sample user for demonstration."""
    return User(
        id=1,
        name="John Doe",
        email="john@example.com",
        age=30,
        tags=["python", "developer"],
        website="https://johndoe.com/",
    )


def create_sample_profile() -> Profile:
    """Create a sample profile with nested models."""
    user = create_sample_user()
    address = Address(
        street="123 Main St", city="San Francisco", country="USA", postal_code="94105"
    )
    return Profile(
        user=user,
        address=address,
        bio="Python developer and open source enthusiast",
        followers=[User(id=2, name="Jane Smith", email="jane@example.com", age=28)],
    )
