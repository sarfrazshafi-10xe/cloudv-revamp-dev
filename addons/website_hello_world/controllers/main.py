from odoo import http
from odoo.http import request

class HelloWorldController(http.Controller):

	@http.route('/hello', type='http', auth='public', website=True)
	def hello_page(self, **kwargs):
		return request.render('website_hello_world.hello_template')