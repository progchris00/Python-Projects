# Week 0

def cal_energy(Mass):
    s = 300000000
    energy = Mass * pow(s, 2)
    return energy

# Week 1

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    final = hours + (minutes/60)
    if 7 <= final <= 8:
        return("breakfast time")
    elif 12 <= final <= 13:
        return("lunch time")
    elif 18 <= final <= 19:
        return("dinner time")

# Week 4

from pyfiglet import Figlet
import random

def to_fig(text):
    figlet = Figlet()
    font_lists = figlet.getFonts()
    figlet.setFont(font=random.choice(font_lists))
    return figlet.renderText(text)

# Week 8
from fpdf import FPDF

def shirtify(name):
    phrase = f"{name} took CS50"
    pdf = FPDF(format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    text_width = pdf.get_string_width(phrase)
    text_width_half = text_width / 2
    center_x = (pdf.w - text_width_half) - 80
    pdf.image("shirtificate.png", h=200, w=200, x=5, y=60)
    pdf.cell(0, 60, txt="CS50 Shirtificate", align='C')
    pdf.set_font_size(30)
    pdf.set_text_color(255,255,255)
    pdf.text(x=center_x, y=130, txt=phrase)
    pdf.output(f"static/shirtificate.pdf")


