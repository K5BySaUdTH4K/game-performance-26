from typing import Dict, Any

class GameConfig:
    """Class to load and hold game configuration settings."""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        """Initializes game configuration with the provided settings.
        
        Args:
            config (Dict[str, Any]): A dictionary containing configuration settings.
        """
        self.settings = config

    def get_setting(self, key: str) -> Any:
        """Retrieves a setting from the configuration.
        
        Args:
            key (str): The key of the setting to retrieve.
        
        Returns:
            Any: The value of the setting if it exists, otherwise None.
        """
        return self.settings.get(key)

    def set_setting(self, key: str, value: Any) -> None:
        """Sets a new value for a specific configuration key.
        
        Args:
            key (str): The key of the setting to update.
            value (Any): The new value to set for the configuration.
        """
        self.settings[key] = value

    def all_settings(self) -> Dict[str, Any]:
        """Returns all current configuration settings.
        
        Returns:
            Dict[str, Any]: A dictionary of all settings.
        """  
        return self.settings
