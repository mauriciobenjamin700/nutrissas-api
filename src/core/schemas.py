from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    BaseSchema is a Pydantic model that serves as a base class for other schemas.

    Methods:
        to_dict: Converts the model instance to a dictionary, excluding specified fields and including additional fields
    """

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        extra="ignore"
    )
    
    def to_dict(self, exclude: list[str] = [], include: dict = {}) -> dict:
        """
        Converts the model instance to a dictionary.

        Args:
            exclude (list[str]): List of field names to exclude from the dictionary.
            include (dict): Dictionary of additional fields to include in the output.

        Returns:
            dict: A dictionary representation of the model instance, excluding specified fields and including additional fields.
        """
        data = self.model_dump(exclude_none=True)

        for field in exclude:
            data.pop(field, None)

        if include:
            data.update(include)

        return data