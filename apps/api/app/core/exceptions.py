class ApplicationError(Exception):
    code = "application_error"


class NotFoundError(ApplicationError):
    code = "not_found_error"


class ValidationError(ApplicationError):
    code = "validation_error"


class BusinessRuleError(ApplicationError):
    code = "business_rule_error"
