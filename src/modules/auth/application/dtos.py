from dataclasses import dataclass


@dataclass
class RegisterUserInputDTO:
    email: str
    password: str

@dataclass
class UserOutputDTO:
    id: str
    email: str
    is_active: bool



@dataclass
class LoginUserInputDTO:
    email: str
    password: str