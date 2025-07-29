# -*- coding: utf-8 -*-

# from odoo import models.fields, api
#
#
# class Al_Dana(models.Model):
#     _name = 'it_assets_custom'
#     _description = 'it_assets_custom'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     name_of_event = fields.Char(string='Name of event', tracking=True)
#     insurance_policy = fields.Char(string='Insurance Policy', tracking=True)
#     Date = fields.Date('Date of event', tracking=True)
#     total_seats = fields.Integer(compute='_compute_total_seats', string='Total seats', export_string_translation=False)
#     name_of_person = fields.Many2one('res.partner', string='Person', domain="[('is_company', '=', False)]",
#                                      tracking=True)
