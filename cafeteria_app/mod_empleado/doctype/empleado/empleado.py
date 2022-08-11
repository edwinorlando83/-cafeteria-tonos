# Copyright (c) 2022, Orlando and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Empleado(Document):
	def validate(self):
		self.nombres_completo = self.nombre + " " + self.apellidos