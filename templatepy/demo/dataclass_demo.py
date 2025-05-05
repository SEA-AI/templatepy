"""
This module demonstrates the use of dataclasses in Python.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class User:
    """A simple user dataclass example."""

    name: str = field(metadata={"description": "User's full name"})
    email: str = field(metadata={"description": "User's email address"})
    age: int = field(metadata={"description": "User's age"})
    created_at: datetime = field(
        default_factory=datetime.now,
        metadata={"description": "Timestamp when the user was created"},
        compare=False,
    )
    tags: List[str] = field(
        default_factory=list,
        metadata={"description": "List of tags associated with the user"},
    )
    is_active: bool = field(
        default=True, metadata={"description": "Whether the user account is active"}
    )


@dataclass
class Address:
    """A nested address dataclass example."""

    street: str = field(
        metadata={"description": "Street address including house number"}
    )
    city: str = field(metadata={"description": "City name"})
    country: str = field(metadata={"description": "Country name"})
    postal_code: str = field(metadata={"description": "Postal code"})


@dataclass
class Profile:
    """A more complex profile dataclass with nested dataclass."""

    user: User = field(metadata={"description": "User information"})
    address: Optional[Address] = field(
        default=None, metadata={"description": "User's address details"}
    )
    bio: Optional[str] = field(
        default=None, metadata={"description": "User's biography"}
    )
    followers: List[User] = field(
        default_factory=list,
        metadata={"description": "List of users following this profile"},
    )


def create_sample_user() -> User:
    """Create a sample user for demonstration."""
    return User(
        name="John Doe", email="john@example.com", age=30, tags=["python", "developer"]
    )


def create_sample_profile() -> Profile:
    """Create a sample profile with nested dataclasses."""
    user = create_sample_user()
    address = Address(
        street="123 Main St", city="San Francisco", country="USA", postal_code="94105"
    )
    return Profile(
        user=user,
        address=address,
        bio="Python developer and open source enthusiast",
        followers=[User(name="Jane", email="jane@example.com", age=28)],
    )
