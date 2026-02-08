# Initializing a "private" class containing app information
class _Info:
    # Dunder Method, to initialize attributes of the class
    def __init__(self, app_name, app_version, app_release, app_developer) -> None:
        object.__setattr__(self, "APP_NAME", app_name)
        object.__setattr__(self, "APP_VERSION", app_version)
        object.__setattr__(self, "APP_RELEASE", app_release)
        object.__setattr__(self, "APP_DEVELOPER", app_developer)

    # Returns info, dependant on given string value argument
    def get_info(self, info_type: str) -> str | dict[str, str]:
        match info_type.upper().strip():
            case "NAME":
                return self.APP_NAME
            case "VERSION":
                return self.APP_VERSION
            case "RELEASE":
                return self.APP_RELEASE
            case "DEVELOPER":
                return self.APP_DEVELOPER
            case "TITLE": # Returns an f-string (CTk window title)
                return f"{self.APP_NAME} {self.APP_VERSION} {self.APP_RELEASE}"
            case "ALL": # Returns a dictionary containing the object attributes and values
                return dict(self.__dict__)
            case _: # In any other case, return an f-string prompting valid argument
                return "ERROR: Invalid Argument"

    # "self.attribute = value" raises the following method, preventing attribute modification
    def __setattr__(self, attribute, value) -> None:
        raise TypeError("Error. Unable to modify information")

    # "del self.attribute" raises the following method, preventing attribute deletion
    def __delattr__(self, attribute) -> None:
        raise TypeError("Error. Unable to delete information")

# Creating an instance that contains the app information
APP_INFO = _Info("Calc Lite", "v1.0.2", "Stable", "Wahab & Zikang")