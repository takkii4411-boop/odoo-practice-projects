import base64
import io
import csv
import easyocr
import numpy as np
from PIL import Image
from odoo import models, fields, api
from odoo.exceptions import UserError


class CigaretteStockReport(models.Model):
    _name = 'cigarette.stock.report'
    _description = 'Main Stock Report'

    name = fields.Char(string="Reference", default="New", copy=False)
    image_file = fields.Binary(string="Upload Bill Image")
    line_ids = fields.One2many('cigarette.stock.lines', 'report_id', string="Stock Details")
    billing_date = fields.Date(string="Billing Date", default=fields.Date.context_today)
    csv_file = fields.Binary(string="Upload CSV File")
    csv_filename = fields.Char(string="CSV Filename")

    def process_invoice_image(self):
        """EasyOCR ka use karke offline handwriting recognition"""
        for record in self:
            if not record.image_file:
                raise UserError("Kripya image upload karein!")

            record.line_ids.unlink()

            # 1. Image ko EasyOCR ke liye taiyaar karein
            img_data = base64.b64decode(record.image_file)
            image = Image.open(io.BytesIO(img_data)).convert('RGB')
            img_np = np.array(image)  # EasyOCR numpy array leta hai

            # 2. EasyOCR Reader (Pehli baar mein model download hoga)
            reader = easyocr.Reader(['en'])
            results = reader.readtext(img_np)

            new_lines = []

            # EasyOCR results format: [([[x,y],[x,y]...], 'Text', confidence), ...]
            # Hum text aur uski position ke hisaab se logic banayenge
            temp_data = []
            for (bbox, text, prob) in results:
                # Sirf wahi text lein jiski confidence 20% se upar ho
                if prob > 0.2:
                    temp_data.append(text.strip())

            # 3. Simple Logic: Agar line mein Name aur Number saath hain
            # Note: Handwriting ke liye humein thoda broad matching chahiye
            import re
            for i in range(len(temp_data)):
                text = temp_data[i]
                # Pattern: Kuch letters phir space aur phir number (decimal ke saath ya bina)
                match = re.search(r'([A-Za-z0-9\s&]+)\s+([\d\.]+)', text)

                if match:
                    brand = match.group(1).strip()
                    qty = match.group(2)
                    try:
                        new_lines.append((0, 0, {
                            'brand_name': brand,
                            'quantity': float(qty),
                        }))
                    except:
                        continue
                # Agar Number alag box mein hai toh next index check karein
                elif i + 1 < len(temp_data):
                    next_text = temp_data[i + 1].replace(',', '')
                    if re.match(r'^\d+(\.\d+)?$', next_text):
                        new_lines.append((0, 0, {
                            'brand_name': text,
                            'quantity': float(next_text),
                        }))

            if not new_lines:
                raise UserError("Data nahi mila! Koshish karein ki photo seedhi (horizontal) ho.")

            record.write({'line_ids': new_lines})
        return True

    def process_csv_file(self):
        """CSV file se data parse karke lines mein daalo - Improved Version"""
        for record in self:
            if not record.csv_file:
                raise UserError("Kripya pehle CSV file upload karein!")

            record.line_ids.unlink()

            try:
                # 'utf-8-sig' use karne se hidden Excel characters (BOM) hat jate hain
                content = base64.b64decode(record.csv_file).decode('utf-8-sig')
            except UnicodeDecodeError:
                content = base64.b64decode(record.csv_file).decode('latin-1')

            new_lines = []

            # Auto-detect separator (comma, semicolon or tab)
            sample = content[:1024]
            if not sample:
                continue

            try:
                dialect = csv.Sniffer().sniff(sample)
                reader = csv.reader(io.StringIO(content), dialect)
            except:
                # Agar fail ho jaye toh default comma reader
                reader = csv.reader(io.StringIO(content))

            for row in reader:
                # Row check: Kam se kam 2 columns hone chahiye
                if not row or len(row) < 2:
                    continue

                # Brand Name (Pehla column)
                brand_name = row[0].strip()

                # Quantity: Hum row ke saare columns check karenge jab tak number na mil jaye
                qty_val = 0.0
                found_qty = False

                # Yeh loop check karega ki row[1], row[2] ya row[3] kis mein number hai
                for cell in row[1:]:
                    clean_cell = cell.strip().replace(',', '')
                    if not clean_cell:
                        continue
                    try:
                        qty_val = float(clean_cell)
                        found_qty = True
                    except ValueError:
                        continue

                # Header line ya empty brand skip karein
                if not brand_name or any(x in brand_name for x in ["Brand", "Product", "Total"]):
                    continue

                if found_qty:
                    new_lines.append((0, 0, {
                        'brand_name': brand_name,
                        'quantity': qty_val,
                    }))

            if not new_lines:
                raise UserError("CSV file read toh hui, magar koi valid data nahi mila. Column check karein.")

            record.write({'line_ids': new_lines})
        return True



