# -*- coding: utf-8 -*-
from odoo import http

# class Projet(http.Controller):
#     @http.route('/projet/projet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projet/projet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('projet.listing', {
#             'root': '/projet/projet',
#             'objects': http.request.env['projet.projet'].search([]),
#         })

#     @http.route('/projet/projet/objects/<model("projet.projet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projet.object', {
#             'object': obj
#         })