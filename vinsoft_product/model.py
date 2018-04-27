# -*- coding: utf-8 -*- 
from odoo import models, fields, api
from openerp.exceptions import Warning, ValidationError
from odoo import tools, _
from odoo.modules.module import get_module_resource
# from odoo.tools import odoo,image_colorize, image_resize_image_big
# from openerp.tools import openerp,image_colorize, image_resize_image_big


# class ProductTheme(models.Model): 
# 	_name = 'product.code'
# 	_rec_name = "rec_name"

# 	name = fields.Char('Name')
# 	product_code = fields.Many2one('product.template',string="Product Code")
# 	pre_price = fields.Float(string ="Pre Price")
# 	sale_price = fields.Float(string ="Sale Price")
# 	vat = fields.Float(string ="Value With Vat")
# 	product_cost = fields.Float(string ="Product Cost")
# 	curr_rate = fields.Many2one('ecube.currency',string="Currency")

# 	groupo = fields.Many2one('groupo',string="Grupo")
# 	sub_groupo = fields.Many2one('sub.groupo',string="Sub Grupo")
# 	property_account_creditor_price_difference = fields.Many2one('account.account')

# 	barcode = fields.Char(string="Barcode")
# 	inventariable = fields.Boolean(string="Código Producto")
# 	kit = fields.Boolean(string="Kit")
# 	active = fields.Boolean(string="active", default=True)
# 	# set_active = fields.Boolean(string="active")
# 	price_list_id = fields.One2many('product.pricelist.item', 'price_link')
# 	kit_id = fields.One2many('kit.tree', 'kit_link')
# 	property_account_income_id = fields.Many2one('account.account')
# 	property_account_expense_id = fields.Many2one('account.account')
# 	uom_id = fields.Many2one('product.uom',default=1)

# 	pre_price = fields.Float(string ="Pre Price")
# 	curr_rate = fields.Many2one('ecube.currency',string="Currency")

# 	state = fields.Selection([
# 		('vigente','Vigente'),
# 		('2','2'),
# 		('3','3'),
# 		],string="Estado")

# 	set_active = fields.Selection([
# 		('active','Activo'),
# 		('inactive','Inactivo'),
# 		],default='active')

# 	description = fields.Text(string="Descripcion")
# 	minimun_lvl = fields.Integer(string="Nivel Minimo")
# 	maximum_lvl = fields.Integer(string="Nivel Maximo")
# 	reposition = fields.Char(string="Nive de Reposicion")
# 	default_code = fields.Char(string="Internal Reference")
# 	taxes_tree_id = fields.One2many('taxes.tree','taxes_tree')
# 	check = fields.Boolean(string="Check")
# 	type = fields.Selection([
# 		('consu', 'Consumible'),
# 		('service', 'Service'),
# 		('product','Inventariable'),], string='Product Type', default='product', required=True,
# 		help='A stockable product is a product for which you manage stock. The "Inventory" app has to be installed.\n'
# 			 'A consumable product, on the other hand, is a product for which stock is not managed.\n'
# 			 'A service is a non-material product you provide.\n'
# 			 'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
# 			 'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')
# 	list_price = fields.Float(
# 		'Sale Price', default=1.0,
# 		help="Base price to compute the customer price. Sometimes called the catalog price.")
# 	volume = fields.Float('Volume', help="The volume in m3.")
# 	weight = fields.Float(
# 		'Weight',
# 		help="The weight of the contents in Kg, not including any packaging, etc.")
# 	standard_price = fields.Float(
# 		'Cost',
# 		help="Cost of the product, in the default unit of measure of the product.")
# 	attribute_line_ids = fields.One2many('product.attribute.line', 'product_tmpl_id')
# 	sale_ok = fields.Boolean(
# 		'Can be Sold', default=True,
# 		help="Specify if the product can be selected in a sales order line.")
# 	purchase_ok = fields.Boolean('Can be Purchased', default=True)
# 	barcode = fields.Char('Barcode', oldname='ean13')
# 	description_sale = fields.Text(
# 		'Sale Description', translate=True,
# 		help="A description of the Product that you want to communicate to your customers. "
# 			 "This description will be copied to every Sale Order, Delivery Order and Customer Invoice/Refund")
# 	categ_id = fields.Many2one(
# 		'product.category', 'Internal Category',
# 		change_default=True, domain="[('type','=','normal')]",
# 		required=True, help="Select category for the current product",default=1)
# 	product_variant_count = fields.Integer(
# 		'# Product Variants',)
# 	image_medium = fields.Binary(
# 		"Medium-sized image", attachment=True,
# 		help="Medium-sized image of the product. It is automatically "
# 			 "resized as a 128x128px image, with aspect ratio preserved, "
# 			 "only when the image exceeds one of those sizes. Use this field in form views or some kanban views.", default=lambda self:self._get_default_image())
# 	seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id', 'Vendors')
# 	in_hand = fields.Integer(string="On Hand", compute='get_on_hand')
# 	rec_name = fields.Char(compute='set_rec')
# 	in_stock = fields.Integer(string="In Stock", compute='get_in_stock')
# 	in_sale = fields.Integer(string="In Sale", compute='get_in_sale')

# 	@api.multi
# 	def stock_button(self):
# 		return {'name': 'Stock Move',
# 				'domain': [('product_id.product_tmpl_id','=',self.product_code.id),('state','=','confirmed')],
# 				'res_model': 'stock.move',
# 				'type': 'ir.actions.act_window',
# 				'view_mode': 'tree',
# 				'view_type': 'form',
# 				}

# 	@api.one
# 	def get_in_stock(self):
# 		self.in_stock = self.env['stock.move'].search_count([('product_id.product_tmpl_id','=',self.product_code.id),('state','=','confirmed')])

# 	@api.one
# 	def set_rec(self):
# 		if self.name:
# 			self.rec_name = self.name
# 		else:
# 			self.rec_name = "Nuevo producto"
# 	# @api.model
# 	# def _get_default_image(self, colorize=False):
# 	# 	image = image_colorize(open(odoo.modules.get_module_resource('base','static/src/img', 'image7.png')).read())
# 	# 	return image_resize_image_big(image.encode('base64'))
# 	@api.model
# 	def _get_default_image(self):
# 		image_path = get_module_resource('vinsoft_product', 'static/src/img', 'place.png')
# 		return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

# 	@api.multi
# 	def sale_order(self):
# 		return {'name': 'Sale Order',
# 				'domain': [('order_line.product_id.product_tmpl_id','=',self.product_code.id),('state','!=','done')],
# 				'res_model': 'sale.order',
# 				'type': 'ir.actions.act_window',
# 				'view_mode': 'tree',
# 				'view_type': 'form',
# 				}

# 	@api.one
# 	def get_in_sale(self):
# 		self.in_sale = self.env['sale.order'].search_count([('order_line.product_id.product_tmpl_id','=',self.product_code.id),('state','!=','done')])

# 	@api.multi
# 	def taxes_view(self):
# 		return {'name': 'Taxes',
# 				'domain': [],
# 				'res_model': 'account.tax',
# 				'type': 'ir.actions.act_window',
# 				'view_mode': 'form',
# 				'view_type': 'form',
# 				'target': 'new', 
# 				}

# 	@api.multi
# 	def action_open_wizard(self):
# 		# self.check = True
# 		return {'name': 'Búsqueda De Productos',
# 			'domain': [],
# 			'res_model': 'product.wizard',
# 			'type': 'ir.actions.act_window',
# 			'view_mode': 'form',
# 			'view_type': 'form',
# 			'target': 'new', 
# 			}

# 	@api.multi
# 	def product(self):
# 		return {'name': 'Product',
# 				'domain': [],
# 				'res_model': 'product.code',
# 				'type': 'ir.actions.act_window',
# 				'view_mode': 'form',
# 				'view_type': 'form',
# 				'target': 'new', 
# 				}

# 	@api.multi
# 	def pending(self):
# 		pass


# 	@api.multi
# 	def action_open_code(self):
# 		if self.product_code:
# 			action = self.env.ref('stock.product_open_quants').read()[0]
# 			action['domain'] = [('product_id', '=', self.product_code.id)]
# 			action['context'] = {'search_default_locationgroup': 1, 'search_default_internal_loc': 1}
# 			return action

# 	@api.one
# 	def get_on_hand(self):
# 		self.in_hand = self.env['stock.quant'].search_count([('product_id', '=', self.product_code.id)])

# 	@api.onchange('curr_rate','pre_price')
# 	def _change_sale_price(self):
# 		if self.pre_price > 0:
# 			self.sale_price = self.pre_price * self.curr_rate.rate



# 	@api.onchange('taxes_tree_id','sale_price')
# 	def _get_vai(self):
# 		if self.taxes_tree_id:
# 			value = 0
# 			for x in self.taxes_tree_id:
# 				value = value + x.rates
# 			value = value / 100
# 			value = value * self.sale_price
# 			self.vat = value + self.sale_price

# 	@api.onchange('inventariable')
# 	def get_inven(self):
# 		if self.inventariable == True:
# 			self.type = 'product'
# 		else:
# 			self.type = 'consu'


# 	global boolean
# 	boolean = 0

# 	@api.model
# 	def create(self, vals):
# 		new_record = super(ProductTheme, self).create(vals)
# 		if not new_record.product_code and new_record.name:
# 			new_record.save()

# 		return new_record

# 	@api.multi
# 	def write(self, vals):

# 		global boolean

# 		res = super(ProductTheme, self).write(vals)

# 		if not self.product_code and self.name:

# 			self.save()
# 		if self.product_code and self.name and boolean != 100:

# 			self.modify()

# 		return res


# 	@api.multi
# 	def unlink(self):

# 		if self.product_code:
# 			self.product_code.unlink()
		
# 		super(ProductTheme, self).unlink()



# 	@api.multi
# 	def save(self):
# 		# if self.price_list_id:
# 		# 	raise ValidationError('Pricelist can be Linked once the product is created')
# 		create_record = self.env['product.template'].create({
# 				'name': self.name,
# 				'default_code': self.default_code,
# 				'categ_id': self.categ_id.id,
# 				'weight': self.weight,
# 				'volume': self.volume,
# 				'kit': self.kit,
# 				'image_medium': self.image_medium,
# 				'purchase_ok': self.purchase_ok,
# 				'sale_ok': self.sale_ok,
# 				'inventariable': self.inventariable,
# 				'barcode': self.barcode,
# 				'curr_rate': self.curr_rate.id,
# 				'pre_price': self.pre_price,
# 				'minimun_lvl': self.minimun_lvl,
# 				'maximum_lvl': self.maximum_lvl,
# 				'reposition': self.reposition,
# 				'description': self.name,
# 				'list_price': self.sale_price,
# 				'vat': self.vat,
# 				'standard_price': self.product_cost,
# 				'uom_id': self.uom_id.id,
# 				'groupo': self.groupo.id,
# 				'sub_groupo': self.sub_groupo.id,
# 				# 'price_list_id': self.price_list_id,
# 				# 'taxes_id':self.taxes_tree_id,
# 				'taxes_tree_id': self.taxes_tree_id,
# 				'kit_id': self.kit_id,
# 				'property_account_expense_id': self.property_account_expense_id.id,
# 				'property_account_income_id': self.property_account_income_id.id,
# 				'property_account_creditor_price_difference': self.property_account_creditor_price_difference.id,
# 			})

# 		self.product_code = create_record.id
# 		taxes = []
# 		for x in self.taxes_tree_id:
# 			taxes.append(x.desc.id)
# 		self.product_code.taxes_id = [(6,0,taxes)]
# 	@api.multi
# 	def modify(self):
# 		self.product_code.name = self.name 
# 		self.product_code.default_code = self.default_code
# 		self.product_code.categ_id = self.categ_id.id
# 		self.product_code.weight = self.weight
# 		self.product_code.volume = self.volume
# 		self.product_code.barcode = self.barcode
# 		self.product_code.image_medium = self.image_medium
# 		self.product_code.minimun_lvl = self.minimun_lvl
# 		self.product_code.maximum_lvl = self.maximum_lvl 
# 		self.product_code.reposition = self.reposition
# 		self.product_code.description = self.name
# 		self.product_code.list_price = self.sale_price
# 		self.product_code.curr_rate = self.curr_rate.id
# 		self.product_code.pre_price = self.pre_price
# 		self.product_code.vat = self.vat
# 		self.product_code.standard_price = self.product_cost
# 		self.product_code.uom_id = self.uom_id.id
# 		self.product_code.groupo = self.groupo.id
# 		self.product_code.kit = self.kit
# 		self.product_code.inventariable = self.inventariable
# 		self.product_code.sub_groupo= self.sub_groupo.id
# 		self.product_code.property_account_expense_id = self.property_account_expense_id.id
# 		self.product_code.property_account_income_id = self.property_account_income_id.id
# 		self.product_code.property_account_creditor_price_difference = self.property_account_creditor_price_difference
# 		self.product_code.attribute_line_ids = self.attribute_line_ids
# 		self.product_code.taxes_tree_id = self.taxes_tree_id
# 		self.product_code.price_list_id = self.price_list_id
# 		self.product_code.kit_id = self.kit_id
# 		self.product_code.purchase_ok = self.purchase_ok
# 		self.product_code.sale_ok = self.sale_ok

# 		taxes = []
# 		for x in self.taxes_tree_id:
# 			taxes.append(x.desc.id)
# 		self.product_code.taxes_id = [(6,0,taxes)]


# 		for items in self.price_list_id:
# 			product = self.env['product.product'].search([('product_tmpl_id','=',self.product_code.id)])
# 			items.product_id = product.id




# 	@api.onchange('product_code')
# 	def get_product_data(self):
# 		if self.product_code:
# 			self.attribute_line_ids = False
# 			self.taxes_tree_id = False
# 			self.price_list_id = False
# 			self.kit_id =False
# 			self.kit = self.product_code.kit
# 			self.sale_ok = self.product_code.sale_ok
# 			self.purchase_ok = self.product_code.purchase_ok
# 			self.inventariable = self.product_code.inventariable
# 			self.name = self.product_code.name
# 			self.barcode = self.product_code.barcode
# 			self.default_code = self.product_code.default_code
# 			self.list_price = self.product_code.list_price
# 			self.standard_price = self.product_code.standard_price
# 			self.categ_id = self.product_code.categ_id.id
# 			self.weight = self.product_code.weight
# 			self.volume = self.product_code.volume
# 			self.kit = self.product_code.kit
# 			self.image_medium = self.product_code.image_medium
# 			self.curr_rate = self.product_code.curr_rate.id
# 			self.pre_price = self.product_code.pre_price
# 			self.minimun_lvl =self.product_code.minimun_lvl
# 			self.maximum_lvl = self.product_code.maximum_lvl
# 			self.reposition = self.product_code.reposition
# 			self.description = self.product_code.name
# 			self.sale_price = self.product_code.list_price
# 			self.vat = self.product_code.vat
# 			self.product_cost = self.product_code.standard_price
# 			self.uom_id = self.product_code.uom_id.id
# 			self.groupo = self.product_code.groupo.id
# 			self.sub_groupo = self.product_code.sub_groupo.id
# 			self.property_account_expense_id = self.product_code.property_account_expense_id.id
# 			self.property_account_income_id = self.product_code.property_account_income_id.id
# 			self.property_account_creditor_price_difference = self.product_code.property_account_creditor_price_difference.id
# 			for items in self.product_code.taxes_tree_id:
# 				items.taxes_tree = self.id

# 			for items in self.product_code.price_list_id:
# 				items.price_link = self.id

# 			for items in self.product_code.kit_id:
# 				items.kit_link = self.id


# 	@api.multi
# 	def elimniate(self):
# 		if self.product_code:
# 			self.name = False
# 			self.product_code.unlink()
# 			self.cancel()






# 	@api.multi
# 	def cancel(self):
# 		global boolean
# 		boolean = 100

# 		self.attribute_line_ids = False
# 		self.taxes_tree_id = False
# 		self.price_list_id = False
# 		self.kit_id =False
# 		self.barcode = False
# 		self.default_code = False
# 		self.list_price = False
# 		self.standard_price = False
# 		self.weight = False
# 		self.volume = False
# 		self.name = False
# 		self.maximum_lvl = False
# 		self.minimun_lvl = False
# 		self.reposition = False
# 		self.property_account_creditor_price_difference = False
# 		self.property_account_income_id = False
# 		self.property_account_expense_id = False
# 		self.sale_price = False
# 		self.pre_price = False
# 		self.curr_rate = False
# 		self.vat = False
# 		self.product_cost = False
# 		self.groupo = False
# 		self.sub_groupo = False
# 		self.kit = False
# 		self.image_medium = False
# 		self.inventariable = False
# 		self.product_code = False
# 		self.sale_ok = False
# 		self.purchase_ok = False
# 		boolean = 0

class ProductTemplate(models.Model): 
	_inherit = 'product.template'


	name = fields.Char('Name',required=False,default=" ")
	# product_code = fields.Many2one('product.template',string="Product Code")
	pre_price = fields.Float(string ="Pre Price")
	sale_price = fields.Float(string ="Sale Price")
	vat = fields.Float(string ="Value With Vat")
	product_cost = fields.Float(string ="Product Cost")
	curr_rate = fields.Many2one('ecube.currency',string="Currency")

	groupo = fields.Many2one('groupo',string="Groupo")
	sub_groupo = fields.Many2one('sub.groupo',string="Sub Groupo")
	property_account_creditor_price_difference = fields.Many2one('account.account')

	product_name = fields.Char(string="Product Name")
	inventariable = fields.Boolean(string="Código Producto")
	kit = fields.Boolean(string="Kit")
	active = fields.Boolean(string="active")
	price_list_id = fields.One2many('product.pricelist.item', 'price_link_temp')
	kit_id = fields.One2many('kit.tree', 'kit_link_temp')
	# uom_id = fields.Many2one('product.uom')


	state = fields.Selection([
		('vigente','Vigente'),
		('2','2'),
		('3','3'),
		],string="Estado")

	description = fields.Text(string="Descripcion")
	minimun_lvl = fields.Integer(string="Nivel Minimo")
	maximum_lvl = fields.Integer(string="Nivel Maximo")
	reposition = fields.Char(string="Nive de Reposicion")
	default_code = fields.Char(string="Internal Reference")
	taxes_tree_id = fields.One2many('taxes.tree','taxes_tree_temp')
	kit_tree = fields.One2many('mrp.bom.line','tree_link')
	type = fields.Selection([
		('consu', 'Consumable'),
		('service', 'Service'),
		('product','Stockable Product'),], string='Product Type', default='product', required=True,
		help='A stockable product is a product for which you manage stock. The "Inventory" app has to be installed.\n'
			 'A consumable product, on the other hand, is a product for which stock is not managed.\n'
			 'A service is a non-material product you provide.\n'
			 'A digital content is a non-material product you sell online. The files attached to the products are the one that are sold on '
			 'the e-commerce such as e-books, music, pictures,... The "Digital Product" module has to be installed.')
	list_price = fields.Float(
		'Sale Price', default=1.0,
		help="Base price to compute the customer price. Sometimes called the catalog price.")
	volume = fields.Float('Volume', help="The volume in m3.")
	weight = fields.Float(
		'Weight',
		help="The weight of the contents in Kg, not including any packaging, etc.")
	standard_price = fields.Float(
		'Cost',
		help="Cost of the product, in the default unit of measure of the product.")
	attribute_line_ids = fields.One2many('product.attribute.line', 'product_tmpl_id')
	sale_ok = fields.Boolean(
		'Can be Sold', default=True,
		help="Specify if the product can be selected in a sales order line.")
	purchase_ok = fields.Boolean('Can be Purchased', default=True)
	barcode = fields.Char('Barcode', oldname='ean13')
	description_sale = fields.Text(
		'Sale Description', translate=True,
		help="A description of the Product that you want to communicate to your customers. "
			 "This description will be copied to every Sale Order, Delivery Order and Customer Invoice/Refund")
	categ_id = fields.Many2one(
		'product.category', 'Internal Category',
		change_default=True, domain="[('type','=','normal')]",
		required=True, help="Select category for the current product")
	product_variant_count = fields.Integer(
		'# Product Variants',)
	image_medium = fields.Binary(
		"Medium-sized image", attachment=True,
		help="Medium-sized image of the product. It is automatically "
			 "resized as a 128x128px image, with aspect ratio preserved, "
			 "only when the image exceeds one of those sizes. Use this field in form views or some kanban views.", default=lambda self:self._get_default_image())
	seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id', 'Vendors')
	in_hand = fields.Integer(string="On Hand", compute='get_on_hand')
	in_stock = fields.Integer(string="In Stock", compute='get_in_stock')
	in_sale = fields.Integer(string="In Sale", compute='get_in_sale')

	pre_price = fields.Float(string ="Pre Price")
	curr_rate = fields.Many2one('ecube.currency',string="Currency")


	@api.model
	def _get_default_image(self):
		image_path = get_module_resource('vinsoft_product', 'static/src/img', 'place.png')
		return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

	@api.multi
	def action_open_code(self):
		action = self.env.ref('stock.product_open_quants').read()[0]
		action['domain'] = [('product_id', '=', self.id)]
		action['context'] = {'search_default_locationgroup': 1, 'search_default_internal_loc': 1}
		return action


	@api.multi
	def stock_button(self):
		return {'name': 'Stock Move',
				'domain': [('product_id.product_tmpl_id','=',self.id),('state','=','confirmed')],
				'res_model': 'stock.move',
				'type': 'ir.actions.act_window',
				'view_mode': 'tree',
				'view_type': 'form',
				}

	@api.one
	def get_in_stock(self):
		self.in_stock = self.env['stock.move'].search_count([('product_id.product_tmpl_id','=',self.id),('state','=','confirmed')])


	@api.multi
	def sale_order(self):
		return {'name': 'Sale Order',
				'domain': [('order_line.product_id.product_tmpl_id','=',self.id),('state','!=','done')],
				'res_model': 'sale.order',
				'type': 'ir.actions.act_window',
				'view_mode': 'tree',
				'view_type': 'form',
				}


	@api.one
	def get_in_sale(self):
		self.in_sale = self.env['sale.order'].search_count([('order_line.product_id.product_tmpl_id','=',self.id),('state','!=','done')])

	@api.multi
	def taxes_view(self):
		return {'name': 'Taxes',
				'domain': [],
				'res_model': 'account.tax',
				'type': 'ir.actions.act_window',
				'view_mode': 'form',
				'view_type': 'form',
				'target': 'new', 
				}


	@api.multi
	def action_open_wizard(self):
		# self.check = True
		return {'name': 'Búsqueda De Productos',
			'domain': [],
			'res_model': 'product.wizard',
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'view_type': 'form',
			'target': 'new', 
			}



	@api.multi
	def pending(self):
		pass

	@api.multi
	def action_open_quants(self):
		products = self.mapped('product_variant_ids')
		action = self.env.ref('stock.product_open_quants').read()[0]
		action['domain'] = [('product_id', 'in', products.ids)]
		action['context'] = {'search_default_locationgroup': 1, 'search_default_internal_loc': 1}
		return action

	@api.one
	def get_on_hand(self):
		self.in_hand = self.env['stock.quant'].search_count([('product_id', '=', self.id)])


	@api.onchange('inventariable')
	def get_inven(self):
		if self.inventariable == True:
			self.type = 'product'
		else:
			self.type = 'consu'



	@api.onchange('curr_rate','pre_price')
	def _change_sale_price(self):
		if self.pre_price > 0:
			self.sale_price = self.pre_price * self.curr_rate.rate



	@api.onchange('taxes_id','sale_price')
	def _get_vai(self):
		if self.taxes_id:
			value = 0
			for x in self.taxes_id:
				value = value + x.amount
			value = value / 100
			value = value * self.sale_price
			self.vat = value + self.sale_price


	@api.model
	def create(self, vals):

		new_record = super(ProductTemplate, self).create(vals)
		if new_record.name != " ":
			product_data = self.env['product.new']
			product_id = product_data.create({
					'name': new_record.id,
				})

		return new_record



class EcubeCurrency(models.Model):
	_name = 'ecube.currency'


	name = fields.Char(string="Name")
	rate = fields.Float(string="Rate")

class EcubeGrupo(models.Model):
	_name = 'groupo'

	name = fields.Char(string="Nombre")

class EcubeSubGrupo(models.Model):
	_name = 'sub.groupo'

	name = fields.Char(string="Nombre")
	group = fields.Many2one('groupo',string="Grupo")

class EcubeTaxesTree(models.Model):
	_name = 'taxes.tree'

	desc = fields.Many2one('account.tax',string="Description")
	rates = fields.Float(string="Impuesto")
	taxes_tree = fields.Many2one('product.code')
	taxes_tree_temp = fields.Many2one('product.template')

	@api.onchange('desc')
	def get_taxes(self):
		if self.desc:
			self.rates = self.desc.amount

class PriceListExtend(models.Model):
	_inherit = 'product.pricelist.item'

	price_link  = fields.Many2one('product.code', string="Product Id")
	price_link_temp = fields.Many2one('product.template', string="Product Id")
	applied_on = fields.Selection([
		('3_global', 'Global'),
		('2_product_category', ' Product Category'),
		('1_product', 'Product'),
		('0_product_variant', 'Product Variant')], "Apply On",
		default='0_product_variant', required=True,
		help='Pricelist Item applicable on selected option')
	
class EcubeKitTree(models.Model):
	_name = 'kit.tree'

	product = fields.Many2one('product.product',string="Descripción")
	code = fields.Char(string="Cod. Producto")
	qty = fields.Float(string="Cantidad")
	lst_price = fields.Float(string="Precio Venta")
	kit_link  = fields.Many2one('product.code', string="Kit Id")
	kit_link_temp  = fields.Many2one('product.template', string="Kit Id")

	

	@api.onchange('product')
	def get_record(self):
		if self.product:
			self.code = self.product.default_code
			self.qty = self.product.qty
			self.lst_price = self.product.lst_price



class ProductExtend(models.Model):
	_inherit = 'product.product'

	qty = fields.Float(string="Quantity")


class EcubeCurrency(models.Model):
	_name = 'ecube.currency'

	name = fields.Char(string="Name")
	rate = fields.Float(string="Rate")

class ProductThemeTreeOne(models.Model): 
	_name = 'product.tree.one'

	field28 = fields.Char(string="Nombre Lista de Precio")
	field29 = fields.Float(string="Vigencia")
	field30 = fields.Float(string="Valor Neto")
	field31 = fields.Float(string="Valor Total")
	field32 = fields.Many2one('product.code',string="Código Producto")

class MRPBomLine(models.Model): 
	_inherit = 'mrp.bom.line'

	tree_link = fields.Many2one("product.code",string="Tree Link")

class ProductWizard(models.Model): 
	_name = 'product.wizard'

	products = fields.Many2one('product.new',string="Búsqueda de Productos")


	@api.multi
	def get_product(self):
		rec = self.env['product.template'].search([('id','=',self.products.name.id)]).id
		view_id = self.env.ref('vinsoft_product.product_form_extension').id
		active_id = self.env.context.get('active_id')
		records = self.env['product.template'].search([('id','=',active_id)])
		if records.name == " ":
			records.unlink()
		return {
				'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'product.template',
                'view_id' : view_id,
                'target': 'main',
                'res_id': rec,
				}


class ProductProductextend(models.Model): 
	_inherit = 'product.product'
	applied_on = fields.Selection([
		('3_global', 'Global'),
		('2_product_category', ' Product Category'),
		('1_product', 'Product'),
		('0_product_variant', 'Product Variant')], "Apply On",
		default='3_global', required=True,
		help='Pricelist Item applicable on selected option')

	@api.model
	def create(self, vals):
		new_record = super(ProductProductextend, self).create(vals)
		if new_record:
			create_reorder = self.env['stock.warehouse.orderpoint'].create({
				'product_id': new_record.id,
				'product_min_qty': new_record.minimun_lvl,
				'product_max_qty':new_record.maximum_lvl,
				})

		return new_record


	@api.multi
	def write(self, vals):
		super(ProductProductextend, self).write(vals)
		for x in self.orderpoint_ids:
			x.product_max_qty = self.maximum_lvl
			x.product_min_qty = self.minimun_lvl

		return True


class ProductCodeExtend(models.Model): 
	_name = 'product.new'


	name = fields.Many2one('product.template',string="name")

# class ProductPricelistItem(models.Model): 
# 	_inherit = 'product.pricelist.item'
# 	applied_on = fields.Selection([
#         ('3_global', 'Global'),
#         ('2_product_category', ' Product Category'),
#         ('1_product', 'Product'),
#         ('0_product_variant', 'Product Variant')], "Apply On",
#         default='0_product_variant', required=True,
#         help='Pricelist Item applicable on selected option')

# 	base = fields.Selection([
#         ('list_price', 'Public Price'),
#         ('standard_price', 'Cost'),
#         ('pricelist', 'Other Pricelist')], "Based on",
#         default='pricelist', required=True,
#         help='Base price for computation.\n'
#              'Public Price: The base price will be the Sale/public Price.\n'
#              'Cost Price : The base price will be the cost price.\n'
#              'Other Pricelist : Computation of the base price based on another Pricelist.')



