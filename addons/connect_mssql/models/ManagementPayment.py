from odoo import models, fields, api
import pyodbc
import xmlrpc.client


class ManagementPayment(models.Model):
    _name = 'management.payment'
    _description = 'Payment Management'

    time = fields.Date(string='Time')
    payment_id = fields.Char(string='Payment ID')
    customer_id = fields.Char(string='Customer ID')
    customer_name = fields.Char(string='Customer Name')
    current_amount = fields.Float(string='Current Amount')
    user_name = fields.Char(string='User Name')
    status = fields.Selection([('accept', 'Accept'), ('refuse', 'Refuse')], string='Status')

    @api.model
    def load_payment_line(self):
        url = 'http://localhost:8069'  # Update with your Odoo server URL
        db = 'odoo'
        username = 'admin'
        password = 'admin'

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()

        uid = common.authenticate(db, username, password, {})

        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        records = [record['payment_id'] for record in
                   models.execute_kw(db, uid, password, 'management.payment', 'search_read', [],
                                     {'fields': ['payment_id']})]

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                                            SERVER=YourSQLServerName;\
                                            DATABASE=YourDatabaseName;\
                                            UID=YourUsername;\
                                            PWD=YourPassword;\
                                            Trusted_Connection=yes')

        cursor = cnxn.cursor()
        cursor.execute("SELECT NgayHt,PhieuChi_id,KhachHang_ud,KhachHang_nm,TienVND, _User, Duyet FROM PhieuChi")
        for row in cursor:
            payment_id = str(row[1]).strip()
            if payment_id not in records:
                time = str(row[0]).split(" ")[0]
                payment_id = str(row[1])
                customer_id = str(row[2])
                customer_name = str(row[3])
                current_amount = int(row[4])
                user_name = str(row[5])

                status = str(row[6])
                if status == 'True':
                    status = 'accept'
                else:
                    status = 'refuse'
                self.create({
                    'time': time, 'payment_id': payment_id, 'customer_id': customer_id, 'customer_name': customer_name,
                    'current_amount': current_amount, 'user_name': user_name, 'status': status
                })