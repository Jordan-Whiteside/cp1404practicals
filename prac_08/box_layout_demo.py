from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle gretting."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear(self):
        """Clear text box and rest to enter name"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"

BoxLayoutDemo().run()
