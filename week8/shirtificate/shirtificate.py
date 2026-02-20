from fpdf import FPDF


def main():
    # prompt user for name
    name = input("Name: ")

    # create pdf
    pdf = FPDF()
    pdf.add_page()

    # title
    pdf.set_font("helvetica", size=40)
    pdf.cell(0, 36, "CS50 Shirtificate", align='C')
    pdf.ln(10)

    # insert image
    # print("To align img in the middle x value should be", (pdf.w - 200)/2)
    pdf.image("shirtificate.png", 5, 60, 200)

    # insert white text on shirt
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size=24)
    pdf.cell(0, 220, text=f"{name} took CS50", align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
