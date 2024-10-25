from odoo import models, fields, api

import logging

_logger = logging.getLogger("Verifica fattura")


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def _create_invoices(self, grouped=False, final=False, date=None):
        _logger.info('Passou por aqui.')

