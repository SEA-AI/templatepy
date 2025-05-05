from datetime import datetime

import pytest
from pydantic import ValidationError

from templatepy.demo.pydantic_demo import (
    Address,
    Profile,
    User,
    UserCreate,
    create_sample_profile,
    create_sample_user,
)


def test_create_user():
    """Test creating a basic user."""
    user = create_sample_user()
    assert isinstance(user, User)
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.age == 30
    assert isinstance(user.created_at, datetime)
    assert user.tags == ["python", "developer"]
    assert user.is_active is True
    assert str(user.website) == "https://johndoe.com/"


def test_user_validation():
    """Test user validation rules."""
    # Test age validation
    with pytest.raises(ValidationError):
        User(
            id=1,
            name="John Doe",
            email="john@example.com",
            age=150,  # Too old
        )

    # Test name validation
    with pytest.raises(ValidationError):
        User(
            id=1,
            name="John",  # No space
            email="john@example.com",
            age=30,
        )

    # Test email validation
    with pytest.raises(ValidationError):
        User(
            id=1,
            name="John Doe",
            email="invalid-email",  # Invalid email
            age=30,
        )


def test_user_create():
    """Test user creation with password."""
    user = UserCreate(
        name="John Doe", email="john@example.com", age=30, password="secure123"
    )
    assert user.password == "secure123"

    # Test password length validation
    with pytest.raises(ValidationError):
        UserCreate(
            name="John Doe",
            email="john@example.com",
            age=30,
            password="short",  # Too short
        )


def test_address_validation():
    """Test address validation rules."""
    # Test valid postal code
    address = Address(
        street="123 Main St", city="San Francisco", country="USA", postal_code="94105"
    )
    assert address.postal_code == "94105"

    # Test invalid postal code
    with pytest.raises(ValidationError):
        Address(
            street="123 Main St",
            city="San Francisco",
            country="USA",
            postal_code="invalid",  # Invalid postal code
        )


def test_create_profile():
    """Test creating a profile with nested models."""
    profile = create_sample_profile()
    assert isinstance(profile, Profile)
    assert isinstance(profile.user, User)
    assert isinstance(profile.address, Address)
    assert profile.bio == "Python developer and open source enthusiast"
    assert len(profile.followers) == 1
    assert isinstance(profile.followers[0], User)


def test_profile_validation():
    """Test profile validation rules."""
    # Test bio length validation
    with pytest.raises(ValidationError):
        Profile(
            user=create_sample_user(),
            bio="x" * 501,  # Too long
        )


def test_model_serialization():
    """Test model serialization to/from JSON."""
    user = create_sample_user()
    user_dict = user.model_dump()
    assert isinstance(user_dict, dict)
    assert user_dict["name"] == "John Doe"

    # Test deserialization
    new_user = User.model_validate(user_dict)
    assert new_user == user
