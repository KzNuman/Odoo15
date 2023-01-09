from odoo import api, fields, models, tools

class SchoolModel(models.Model):
    _name = "school.main"
    _description = "My Model Names"

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")