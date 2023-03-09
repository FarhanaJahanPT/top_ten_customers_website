import itertools
import operator

from odoo import http
from odoo.http import request

class WebsiteSnippetPage(http.Controller):
    @http.route('/customer/top', type='json', auth='public', website=True)
    def snippet_pages(self, **kw):

        dict_customer=[rec.partner_id for rec in request.env['sale.order'].search([])]
        dict_cus = {}
        dict_count = []
        for partner in dict_customer:
            dict_cus.update({
                    partner: dict_customer.count(partner)
                })
        sort = dict(sorted(dict_cus.items(), key=lambda x: x[1], reverse=True))
        limit = dict(itertools.islice(sort.items(), 10))
        for i in limit:
            dict_count.append([
                i.name, i.id
            ])
        top_customer = [dict_count[i:i+4] for i in range(0, len(dict_count), 4)]
        return top_customer

    @http.route('/customer/top/new', type='http', auth='public', website=True, csrf=False)
    def snippet_page(self, **kw):
        customer_id = kw.get('customer_id')
        customer = request.env['res.partner'].sudo().browse(int(customer_id))

        values = {
                'customer':  customer
            }

        return request.render('top_customers.customers_snippet_img', values)
