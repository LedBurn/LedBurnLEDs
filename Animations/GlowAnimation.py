
class GlowAnimation:

    def __init__(self, ui_element):
        self.ui_element = ui_element

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = int(255 * time_percent * 0.3)
        else:
            c = int(255 * (1.0 - time_percent) * 0.3)
        c = c + 20

        for i in self.ui_element.get_all_indexes():
            self.ui_element.get_array()[i*3:i*3+3] = [c, c, c]

