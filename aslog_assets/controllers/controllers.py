# -*- coding: utf-8 -*-
from odoo import http

# class AslogAssets(http.Controller):
#     @http.route('/aslog_assets/aslog_assets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aslog_assets/aslog_assets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aslog_assets.listing', {
#             'root': '/aslog_assets/aslog_assets',
#             'objects': http.request.env['aslog_assets.aslog_assets'].search([]),
#         })

#     @http.route('/aslog_assets/aslog_assets/objects/<model("aslog_assets.aslog_assets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aslog_assets.object', {
#             'object': obj
#         })