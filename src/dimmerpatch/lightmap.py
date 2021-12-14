from collections import OrderedDict

class LightMap():
    """The mapping of a light's channels relative to its address (zero-offset)    

    Note: the channel map itself doesn't 
    """
    _map_by_use = None
    _map_by_channel = None
    _valid_channel_types = [
        "r",            # Red
        "g",            # Green
        "b",            # Blue
        "dimmer",       # White (or primary) dimmer
        "temperature",  # Color temperature
        "wheel",        # Color wheel
        "pan",          # Pan
        "pan_fine",     # Pan fine
        "tilt",         # Tilt
        "tilt_fine",    # Tilt fine
        "gobo_select",  # Gobo Selector
        "gobo_rotate",  # Gobo Rotator
        "iris",         # Iris
        "focus",        # Focus
        "mode",         # Control mode
        "shutter",      # Shutter,
        "custom0",
        "custom1",
        "custom2",
        "custom3",
        "custom4",
        "custom5",
        "custom6",
        "custom7",
        "custom8",
        "custom9",
    ]

    def __init__(self, channel_map = {}):
        self._map_by_use = OrderedDict()
        self._map_by_channel = {}
        self.set_channel_map(channel_map)

    def get_channel_map(self):
        """Get the channel map as a dictionary"""
        return dict(self._map_by_use)
    
    def get_channel_usage(self):
        """Get the channel usage in the order of the channels"""
        return [usage for usage in self._map_by_use.keys()]
    
    def get_channel_usage_map(self):
        """Get the channel map as a dictionary, ordered by channels"""
        return dict(self._map_by_channel)
    
    def get_channels(self):
        """Get the channels used by this light map"""
        return [k for k in sorted(self._map_by_channel.keys())]

    def get_width(self):
        """Get the channel space width of the light map

            Note that not all addresses in this channel space
            may be used
        """
        channels = self.get_channels()
        return channels[-1] - channels[0] + 1

    def set_channel_map(self, channel_map = {}):
        """Reviews and sets the channel map based on supported capabilities"""
        channel_map_filtered = {usage: channel for usage, channel in channel_map.items() if usage in self._valid_channel_types}
        self._map_by_use = OrderedDict(sorted(channel_map_filtered.items(), key = lambda t: t[1]))
        self._map_by_channel = {channel: usage for usage, channel in channel_map_filtered.items()}

class Rgb(LightMap):
    """A simple RGB-addressable light"""
    def __init__(self):
        super().__init__({
            "r": 0,
            "g": 1,
            "b": 2
        })

class Dimmer(LightMap):
    """A single-channel dimmer """
    def __init__(self):
        super().__init__({
            "dimmer": 0,
        })
