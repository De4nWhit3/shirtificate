from fpdf import FPDF
from PIL import Image

""" PDF class inherits from super class FPDF. """
class PDF(FPDF):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    """ Get name to print on shirt from user. """
    def set_name(self, name):
        self.name = name

    """ PDF class inherits functionality from super class: FPDF. """
    def header(self):
        self.set_font("Courier", "I", 40)
        self.set_text_color(153, 187, 255) # text
        self.set_fill_color(0, 26, 77) # background
        self.set_draw_color(153, 187, 255) # border
        self.cell(
            w=0,
            txt="CS50 Shirtificate",
            border="3",
            align="C",
            fill=True
        )
        self.ln(50)

    """ Create the shirt image and center it ont he PDF document. """
    def add_image(self, filepath="shirtificate.png"):
        with Image.open(filepath)  as image:
            width, height = image.size
            width = 120
            x_pos = (self.w - width) / 2
            self.image(
                image,
                w=width,
                x=x_pos
            )
            self.ln(-(self.h/4))

    """ Add the given name onto the shirt image. """
    def add_name(self):
        self.set_font("Times", "B", 20)
        self.set_text_color(255, 255, 255)
        shirt_text = self.name + " took CS50"
        width = self.get_string_width(shirt_text)
        self.set_x((self.w - width) / 2)
        self.cell(
            txt=shirt_text,
            align="C"
        )

    """ Create and save the PDF document. """
    def conjure_pdf(self):
        self.add_page()
        self.add_image()
        self.add_name()
        self.output("shirtificate.pdf")

def main():
    pdf = PDF()
    pdf.set_name(input("Name: "))
    pdf.conjure_pdf()

if __name__ == "__main__":
    main()