# -*- coding: utf-8 -*-
from odoo import http

# class Foobar(http.Controller):
#     @http.route('/foobar/foobar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/foobar/foobar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('foobar.listing', {
#             'root': '/foobar/foobar',
#             'objects': http.request.env['foobar.foobar'].search([]),
#         })

#     @http.route('/foobar/foobar/objects/<model("foobar.foobar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('foobar.object', {
#             'object': obj
#         })
