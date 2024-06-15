from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def create_payment_receipt(customer_name, amount_paid, payment_method):
    # Create a unique file name based on current timestamp
    file_name = f"payment_receipt_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    # Create a canvas (PDF document)
    c = canvas.Canvas(file_name, pagesize=letter)

    # Set font and size for the title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 750, "Payment Receipt")

    # Set font and size for the details
    c.setFont("Helvetica", 12)
    text = f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    c.drawString(100, 700, text)

    text = f"Customer Name: {customer_name}"
    c.drawString(100, 680, text)

    text = f"Amount Paid: ${amount_paid:.2f}"
    c.drawString(100, 660, text)

    text = f"Payment Method: {payment_method}"
    c.drawString(100, 640, text)

    # Draw a line under the details
    c.line(100, 630, 500, 630)

    # Save the PDF document
    c.save()

    print(f"Payment receipt saved as: {file_name}")

# Example usage:
customer_name = "John Doe"
amount_paid = 100.50
payment_method = "Credit Card"

create_payment_receipt(customer_name, amount_paid, payment_method)
