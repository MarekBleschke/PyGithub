from typing import Any, List

from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class CustomProperty(CompletableGithubObject):
    """
    This class represents Custom Property. The reference can be found here: https://docs.github.com/en/rest/orgs/custom-properties
    """

    def _initAttributes(self) -> None:
        self._allowed_values: Attribute[List[str]] = NotSet
        self._default_value: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._property_name: Attribute[str] = NotSet
        self._required: Attribute[bool] = NotSet
        self._value_type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"property_name": self._property_name.value, "value_type": self._value_type.value})

    @property
    def allowed_values(self) -> List[str]:
        self._completeIfNotSet(self._allowed_values)
        return self._allowed_values.value

    @property
    def default_value(self) -> str:
        self._completeIfNotSet(self._default_value)
        return self._default_value.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def property_name(self) -> str:
        self._completeIfNotSet(self._property_name)
        return self._property_name.value

    @property
    def required(self) -> bool:
        self._completeIfNotSet(self._required)
        return self._required.value

    @property
    def value_type(self) -> str:
        self._completeIfNotSet(self._value_type)
        return self._value_type.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "allowed_values" in attributes:  # pragma no branch
            self._allowed_values = self._makeListOfStringsAttribute(attributes["allowed_values"])
        if "default_value" in attributes:  # pragma no branch
            self._default_value = self._makeStringAttribute(attributes["default_value"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "property_name" in attributes:
            self._property_name = self._makeStringAttribute(attributes["property_name"])
        if "required" in attributes:  # pragma no branch
            self._required = self._makeBoolAttribute(attributes["required"])
        if "value_type" in attributes:  # pragma no branch
            self._value_type = self._makeStringAttribute(attributes["value_type"])
