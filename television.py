class Television:
    """
    A class to represent a Television remote that can adjust the power, volume and channels

    Attributes:
        min_volume (int): The minimum volume level.
        max_volume (int): The maximum volume level.
        min_channel (int): The minimum channel number.
        max_channel (int): The maximum channel number.
    """
    # Class Constants
    min_volume: int = 0
    max_volume: int = 2
    min_channel: int = 0
    max_channel: int = 3

    def __init__(self) -> None:
        """
        Initializes the Television object with default settings:
        - Power off
        - Not muted
        - Volume set to minimum
        - Channel set to minimum
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.min_volume
        self.__channel: int = self.min_channel

    def power(self) -> None:
        """
        Toggles the TV power status between on and off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the TV only if it's powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the TV channel by one. Loops back to the minimum channel if at the maximum channel.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) if self.__channel < self.max_channel else self.min_channel

    def channel_down(self) -> None:
        """
        Decreases the TV channel by one. Loops back to the maximum channel if at the minimum channel.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > self.min_channel else self.max_channel

    def volume_up(self) -> None:
        """
        Increases the TV volume by one. Unmutes the TV if it is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.max_volume:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the TV volume by one. Unmutes the TV if it is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.min_volume:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of the TV's status in the format:
                 Power = [status], Channel = [channel], Volume = [volume]
        """
        volume_display = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"
