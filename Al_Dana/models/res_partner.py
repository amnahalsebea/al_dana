from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cpr = fields.Char(string='CPR', tracking=True)
