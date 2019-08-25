
from odoo import models, fields


class PersonnePersonne(models.Model):

    _name = 'personne.personne'
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('homme', 'Homme'), ('femme', 'Femme'), ('autres', 'Autres')], string='Gender')
    personne_dob = fields.Date(string="Date de naissance")
    personne_blood_group = fields.Selection(
            [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
            ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
            string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')


