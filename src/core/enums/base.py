from enum import Enum


class BaseEnum(Enum):
    """
    Base class for all enums in the application.
    Provides a common interface for enum classes.
    """

    @classmethod
    def choices(cls):
        """
        Returns a list of tuples containing the enum value and its name.
        """
        return [(item.value, item.name) for item in cls]

    @classmethod
    def names(cls):
        """
        Returns a list of enum names.
        """
        return [item.name for item in cls]