# Copyright (c) 2023, jan@gmail.com and contributors
# For license information, please see license.txt

import frappe
import qrcode
from frappe.model.document import Document

class Table(Document):
	def validate(self):
		if not self.qrcode:
			qr = qrcode.QRCode(version=5,
							   box_size=5,
							   border=5)
			qr_value = frappe.utils.get_url() + "/menu?table=" + self.name.replace(" ","%20")
			# qr_value = "http://192.168.1.13:8002/menu?table=" + self.name
			qr.add_data(qr_value)  # Adding the data to be encoded to the QRCode object
			qr.make(fit=True)  # Making the entire QR Code space utilized
			img = qr.make_image()  # Generating the QR Code
			qrcode_name = "/public" + "/files/" + self.name + '.png'
			img.save(frappe.get_site_path() + qrcode_name)  # Saving the QR Code
			self.qrcode = "/files/" + self.name + '.png'

