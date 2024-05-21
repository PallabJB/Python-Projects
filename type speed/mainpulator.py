class SpeedCalc:
    def __init__(self, new_paragraph):
        self.new_paragraph = new_paragraph
        self.typed_words = " "
        self.counter = 0
        self.running = False

    def display_sample_paragraph(self):
        return self.new_paragraph

    def display_type_words(self):
        return self.typed_words