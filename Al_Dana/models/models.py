# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AlDana(models.Model):
    _name = 'al.dana'
    _description = 'Al.Dana'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name_of_event = fields.Char(string='Name of event', tracking=True)
    Date = fields.Date('Date of event', tracking=True)
    total_seats = fields.Integer(string='Total seats')
    name_of_person = fields.Many2one('res.partner', string='Person', tracking=True)
    type_of_ticket = fields.Selection([
        ('vvib', 'Vvib'),
        ('vib', 'Vib'),
        ('regular', 'Regular')], string='ticket', default='regular', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm')
    ], string='State', default='draft')

    persons_ids = fields.One2many('event.persons.lines', 'al_dana_id', string='persons')

    persons_count = fields.Integer(string='Number of persons', compute="_compute_persons_count")

    @api.onchange('persons_ids')
    def _compute_persons_count(self):
        for rec in self:
            rec.persons_cont = len(rec.persons_ids)

    def action_to_get_smart_button(self):
        return {
            'name': 'persons',
            'type': 'ir.actions.act_window',
            'res_model': 'list,form',
            'view_mode': 'event.persons.lines',
            'domain': [('id', 'in', self.persons_ids.ids)],
            'context': {'default_al_dana_id': self.id},
            'target': 'current',
        }

    def action_to_draft(self):
        self.state = "draft"

    def action_to_confirm(self):
        self.state = "confirm"

    # form action
    def action_to_persons(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'persons.lines.wizard',
            'view_id': self.env.ref('Al_Dana.add_person_action_form').id,
            'view_mode': 'form',
            'name': 'add person',
            'target': 'new',
            'context': {'active_data': self._name, 'active_id': self.id},
        }

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    @api.onchange('start_date', 'end_date')
    def onchange_date_of_exp(self):
        print('working' * 10)
        answer = 0
        if not self.end_date >= self.start_date:
            answer = self.end_date - self.start_date
            print(answer)
            self.Date = answer.days
            print(answer.days)
        else:
            print("you entered the wrong date")
            raise ValidationError(_("you entered the wrong date"))


class EventPersonsLines(models.Model):
    _name = 'event.persons.lines'
    _description = 'Event Persons Lines'

    # type_of_ticket = fields.Selection('ticket', string='ticket')

    person = fields.Many2one('res.partner', string='Person')
    al_dana_id = fields.Many2one('al.dana', string='al_dana_id')
