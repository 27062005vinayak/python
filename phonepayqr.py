import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Page config
st.set_page_config(page_title="💸 PhonePe QR Generator ", page_icon="💰", layout="centered")

# Title
st.title("💸 PhonePe Payment QR Code Generator")
st.markdown("Generate a QR code for PhonePe/UPI payments.")

# Inputs
upi_id = st.text_input("Enter your UPI ID (e.g., vinayakpatil@xyz):")
name = st.text_input("Enter Payee Name:eg vinayak patil")
amount = st.number_input("Enter Amount (Optional)", min_value=0, step=1)

# Generate QR Code button
if st.button("Generate QR Code"):
    if upi_id.strip() == "":
        st.error("❌ Please enter a valid UPI ID")
    else:
        # Create UPI payment link
        if amount > 0:
            data = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"
        else:
            data = f"upi://pay?pa={upi_id}&pn={name}&cu=INR"

        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=12,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Display QR code
        st.image(buffer, caption="📱 Scan with PhonePe/UPI App",width=300)

        # Download option
        st.download_button(
            label="⬇️ Download QR Code",
            data=buffer,
            file_name="phonepe_qrcode.png",
            mime="image/png"
        )
