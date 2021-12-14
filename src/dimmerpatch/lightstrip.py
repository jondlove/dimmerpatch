from patchpanel import PatchPanel
from lightmap import RgbLed

class LightStrip(PatchPanel):
    def __init__(self, num_lights):
        super().__init__(num_lights)
        self.initialize_from_list([RgbLed() for i in range(num_lights)])