import pyodbc
import xmlrpc.client

def import_data_from_sql_to_odoo():
    url = 'http://localhost:8068'
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
                                        SERVER=DESKTOP-UON5RMU\SQLEXPRESS;\
                                        DATABASE=BORO_EACCOUNTING;\
                                        UID=sa;\
                                        PWD=Tamkhoa@123;\
                                        Trusted_Connection=yes')

    cursor = cnxn.cursor()
    cursor.execute("SELECT PhieuChi.NgayHt,PhieuChi.PhieuChi_id,KhachHang.KhachHang_ud,KhachHang.KhachHang_nm,PhieuChi.TienVND, PhieuChi._User, PhieuChi.Duyet \
                                    FROM PhieuChi, KhachHang \
                                   where PhieuChi.KhachHang_id = KhachHang.KhachHang_id")
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
            models.execute_kw(db, uid, password, 'management.payment', 'create', [
                {'time': time, 'payment_id': payment_id, 'customer_id': customer_id, 'customer_name': customer_name,
                 'current_amount': current_amount, 'user_name': user_name, 'status': status}])
