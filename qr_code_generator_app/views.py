from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from datetime import datetime
from pathlib import Path
import qrcode

QR_IMAGE_NAME = "qr_code.png"

def generate_qr(request):
    qr_image_path = None
    input_text = ""

    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        if input_text:
            # Generate QR code
            qr = qrcode.QRCode(version=None, box_size=10, border=4)
            qr.add_data(input_text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save QR image to static folder
            qr_image_full_path = Path(settings.STATICFILES_DIRS[0]) / QR_IMAGE_NAME
            img.save(qr_image_full_path) # type: ignore
            qr_image_path = QR_IMAGE_NAME

    return render(request, "qr_code_generator/qr_form.html", {
        "qr_image_path": qr_image_path,
        "input_text": input_text
    })

def download_qr(request):
    qr_image_full_path = Path(settings.STATICFILES_DIRS[0]) / QR_IMAGE_NAME
    if qr_image_full_path.exists:
        return FileResponse(
            open(qr_image_full_path, "rb"),
            as_attachment=True,
            filename=QR_IMAGE_NAME
        )
    else:
        return render(request, "qr_code_generator/qr_form.html", {
            "error": "No QR code available to download"
        })
