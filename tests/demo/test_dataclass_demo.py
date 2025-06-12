from datetime import datetime

from templatepy.demo.dataclass_demo import (
    Address,
    Profile,
    User,
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


def test_create_address():
    """Test creating an address."""
    address = Address(
        street="123 Main St", city="San Francisco", country="USA", postal_code="94105"
    )
    assert isinstance(address, Address)
    assert address.street == "123 Main St"
    assert address.city == "San Francisco"
    assert address.country == "USA"
    assert address.postal_code == "94105"


def test_create_profile():
    """Test creating a profile with nested dataclasses."""
    profile = create_sample_profile()
    assert isinstance(profile, Profile)
    assert isinstance(profile.user, User)
    assert isinstance(profile.address, Address)
    assert profile.bio == "Python developer and open source enthusiast"
    assert len(profile.followers) == 1
    assert isinstance(profile.followers[0], User)


def test_user_equality():
    """Test user equality comparison."""
    user1 = User(name="John Doe", email="john@example.com", age=30)
    user2 = User(name="John Doe", email="john@example.com", age=30)
    assert user1 == user2


def test_user_immutability():
    """Test that user fields can be modified."""
    user = create_sample_user()
    user.tags.append("new_tag")
    assert "new_tag" in user.tags
