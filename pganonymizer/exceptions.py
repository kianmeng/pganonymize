class PgAnonymizeException(Exception):
    """Base exception for all pganonymize errors."""


class InvalidFieldProvider(PgAnonymizeException):
    """Raised if an unknown field provider was used."""
