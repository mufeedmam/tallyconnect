from __future__ import unicode_literals

import frappe
import json

@frappe.whitelist()
@frappe.whitelist()
def customer_group():
    data = json.loads(frappe.request.data)
    if not isinstance(data, dict):
         data = {'data': []}
         
    if 'data' in data:
         groups = data['data']
    else:
         groups = [data] if isinstance(data, dict) else data

    tally_response = []

    for group in groups:
        if 'doctype' not in group:
            group['doctype'] = 'Customer Group'
        group_exists = frappe.db.exists(
            group['doctype'], group['customer_group_name'])
        if not group_exists:
            try:
                doc = frappe.get_doc(group)
                doc.insert()
                tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': 'Already Exists'})
        # else:
        #     try:
        #         frappe.db.set_value(group['doctype'], group['customer_group_name'], {
        #             "customer_group_name": group['customer_group_name'],
        #             "is_group": group['is_group'],
        #             "parent_customer_group": group['parent_customer_group'],
        #         })

        #         tally_response.append(
        #             {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': group['customer_group_name'], 'tally_object': 'Group', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
@frappe.whitelist()
def supplier_group():
    data = json.loads(frappe.request.data)
    
    if 'data' in data:
         groups = data['data']
    else:
         groups = [data] if isinstance(data, dict) else data

    tally_response = []

    for group in groups:
        if 'doctype' not in group:
            group['doctype'] = 'Supplier Group'
        group_exists = frappe.db.exists(
            group['doctype'], group['supplier_group_name'])
        if not group_exists:
            try:
                doc = frappe.get_doc(group)
                doc.insert()
                tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': 'Already Exists'})
        # else:
        #     try:
        #         frappe.db.set_value(group['doctype'], group['supplier_group_name'], {
        #             "supplier_group_name": group['suppiler_group_name'],
        #             "is_group": group['is_group'],
        #             "parent_supplier_group": group['parent_supplier_group'],
        #         })

        #         tally_response.append(
        #             {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': group['supplier_group_name'], 'tally_object': 'Group', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
@frappe.whitelist()
def item_group():
    data = json.loads(frappe.request.data)
    
    if 'data' in data:
         stockgroups = data['data']
    else:
         stockgroups = [data] if isinstance(data, dict) else data

    tally_response = []

    for stockgroup in stockgroups:
        if 'doctype' not in stockgroup:
            stockgroup['doctype'] = 'Item Group'
        group_exists = frappe.db.exists(
            stockgroup['doctype'], stockgroup['item_group_name'])
        if not group_exists:
            try:
                doc = frappe.get_doc(stockgroup)
                doc.insert()
                tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': 'Already Exists'})
        # else:
        #     try:
        #         frappe.db.set_value(stockgroup['doctype'], stockgroup['item_group_name'], {
        #             "item_group_name": stockgroup['item_group_name'],
        #             "is_group": stockgroup['is_group'],
        #             "parent_item_group": stockgroup['parent_item_group'],
        #         })

        #         tally_response.append(
        #             {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': stockgroup['item_group_name'], 'tally_object': 'Stock Group', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
@frappe.whitelist()
def warehouse():
    data = json.loads(frappe.request.data)
    
    if 'data' in data:
         warehouses = data['data']
    else:
         warehouses = [data] if isinstance(data, dict) else data

    tally_response = []

    for warehouse in warehouses:
        if 'doctype' not in warehouse:
            warehouse['doctype'] = 'Warehouse'
        is_exists = frappe.db.exists(
            warehouse['doctype'], warehouse['warehouse_name'])
        if not is_exists:
            try:
                doc = frappe.get_doc(warehouse)
                doc.insert()
                tally_response.append(
                    {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': warehouse['item_group_name'], 'tally_object': 'Godown', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': 'Already Exists'})
        # else:
        #     try:
        #         frappe.db.set_value(warehouse['doctype'], warehouse['warehouse_name'], {
        #             "warehouse_name": warehouse['warehouse_name'],
        #             "is_group": warehouse['is_group'],
        #             "parent_warehouse": warehouse['parent_warehouse'],
        #             "company": warehouse['company']
        #         })

        #         tally_response.append(
        #             {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': warehouse['warehouse_name'], 'tally_object': 'Godown', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
@frappe.whitelist()
def customer():
    data = json.loads(frappe.request.data)
    
    if 'data' in data:
         customers = data['data']
    else:
         customers = [data] if isinstance(data, dict) else data

    tally_response = []

    for customer in customers:
        if 'doctype' not in customer:
            customer['doctype'] = 'Customer'
        if 'customer_code' not in customer:
            if 'name' in customer:
                customer['customer_code'] = customer['name']
            elif 'customer_name' in customer:
                customer['customer_code'] = customer['customer_name']

        is_exists = frappe.db.exists(
            customer['doctype'], customer['customer_code'])
        if not is_exists:
            try:
                create_account(customer)

                doc = frappe.get_doc(customer)
                doc.insert(set_name=customer['customer_code'])

                create_contact(customer)
                create_address(customer)


                tally_response.append(
                    {'name': customer['customer_code'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': customer['customer_code'], 'tally_object': 'Ledger', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': customer['customer_code'], 'tally_object': 'Ledger', 'message': 'Already Exists'})

        # else:
        #     try:
        #         frappe.db.set_value(customer['doctype'], customer['customer_name'], {
        #             "customer_name": customer['customer_name'],
        #             "customer_type": customer['customer_type'],
        #             "customer_group": customer['customer_group'],
        #             "territory": customer['territory'],
        #             "tax_category": customer['tax_category'],
        #             "so_required": customer['so_required'],
        #             "dn_required": customer['dn_required'],
        #             "default_currency": customer['default_currency'],
        #             "default_price_list": customer['default_price_list'],
        #             "item_group_limit": customer['item_group_limit'] if 'item_group_limit' in customer else ""
        #         })

        #         tally_response.append(
        #             {'name': customer['customer_name'], 'tally_object': 'Ledger', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': customer['customer_name'], 'tally_object': 'Ledger', 'message': str(e)})

    return {"status": True, 'data': tally_response}


@frappe.whitelist()
def customer_opening():
    payload = json.loads(frappe.request.data)
    bills = payload['data']

    tally_response = []
    for b in bills:

        for bill in b['bills']:
            try:

                if frappe.db.exists("Sales Invoice", bill['bill_name']):
                    inv = frappe.get_doc("Sales Invoice", bill['bill_name'])
                    inv.cancel()
                    inv.delete()

                req = {
                    "remarks": bill['bill_name'],
                    "customer": bill['customer'],
                    "customer_name": bill['customer'],
                    "company": bill['company'],
                    # "currency": "INR",
                    "set_posting_time": True,
                    # "price_list_currency": "INR",
                    "posting_date": bill['posting_date'],
                    "due_date": bill['due_date'],
                    "debit_to": bill['debit_to'], #"Test 3 Customer - Abbr",
                    # "party_account_currency": "INR",
                    "is_opening": 'Yes',
                    "is_return": bill['is_return'],
                    "grand_total": bill['amount'],
                    "against_income_account": bill['against_income_account'],#"Temporary Opening - Abbr",
                    "disable_rounded_total": 1,
                    "doctype": "Sales Invoice",
                    "items": [
                        {
                        "item_name": "Opening Invoice Item",
                        "description": "Opening Invoice Item",
                        "qty": 1 if bill['is_return'] == 0 else -1,
                        "stock_uom": "Nos",
                        "uom": "Nos",
                        "conversion_factor": 1,
                        "stock_qty": 1 if bill['is_return'] == 0 else -1,
                        "rate": abs(bill['amount']),
                        "amount": bill['amount'],
                        "income_account": bill['against_income_account'],
                        "doctype": "Sales Invoice Item"
                        }
                    ],
                    "payment_schedule": [
                        {
                        "due_date": bill['due_date'],
                        "invoice_portion": 100,
                        "payment_amount": bill['amount'],
                        "outstanding": bill['amount'],
                        "paid_amount": 0,
                        "base_payment_amount": bill['amount'],
                        "doctype": "Payment Schedule"
                        }
                    ],
                }

                doc = frappe.get_doc(req)
                doc.flags.ignore_mandatory = True
                doc.insert(set_name=bill['bill_name'])
                doc.submit()
                tally_response.append(
                        {'name': bill['customer'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                        {'name': bill['customer'], 'tally_object': 'Ledger', 'message': str(e)})

    return {"status": True, 'data': tally_response}    

@frappe.whitelist()
def supplier_opening():
    payload = json.loads(frappe.request.data)
    bills = payload['data']

    tally_response = []
    for b in bills:
        for bill in b['bills']:
            try:
                if frappe.db.exists("Purchase Invoice", bill['bill_name']):
                    inv = frappe.get_doc("Purchase Invoice", bill['bill_name'])
                    inv.cancel()
                    inv.delete()

                req = {
                    "remarks": bill['bill_name'],
                    "supplier": bill['supplier'],
                    "supplier_name": bill['supplier'],
                    "company": bill['company'],
                    # "currency": "INR",
                    "set_posting_time": True,
                    # "price_list_currency": "INR",
                    "posting_date": bill['posting_date'],
                    "due_date": bill['due_date'],
                    "credit_to": bill['credit_to'], #"Test 3 Customer - Abbr",
                    # "party_account_currency": "INR",
                    "is_opening": 'Yes',
                    "is_return": bill['is_return'],
                    "grand_total": bill['amount'],
                    "against_expense_account": bill['against_expense_account'],#"Temporary Opening - Abbr",
                    "disable_rounded_total": 1,
                    "doctype": "Purchase Invoice",
                    "items": [
                        {
                        "item_name": "Opening Invoice Item",
                        "description": "Opening Invoice Item",
                        "qty": 1 if bill['is_return'] == 0 else -1,
                        "stock_uom": "Nos",
                        "uom": "Nos",
                        "conversion_factor": 1,
                        "stock_qty": 1 if bill['is_return'] == 0 else -1,
                        "rate": abs(bill['amount']),
                        "amount": bill['amount'],
                        "expense_account": bill['against_expense_account'],
                        "doctype": "Purchase Invoice Item"
                        }
                    ],
                    # "payment_schedule": [
                    #     {
                    #     "due_date": bill['due_date'],
                    #     "invoice_portion": 100,
                    #     "payment_amount": bill['amount'],
                    #     "outstanding": bill['amount'],
                    #     "paid_amount": 0,
                    #     "base_payment_amount": bill['amount'],
                    #     "doctype": "Payment Schedule"
                    #     }
                    # ],
                }

                doc = frappe.get_doc(req)
                doc.flags.ignore_mandatory = True
                doc.insert(set_name=bill['bill_name'])
                doc.submit()
                tally_response.append(
                        {'name': bill['supplier'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                        {'name': bill['supplier'], 'tally_object': 'Ledger', 'message': str(e)})

    return {"status": True, 'data': tally_response}    


@frappe.whitelist()
@frappe.whitelist()
def supplier():
    data = json.loads(frappe.request.data)
    
    if 'data' in data:
         suppliers = data['data']
    else:
         suppliers = [data] if isinstance(data, dict) else data

    tally_response = []

    for supplier in suppliers:
        if 'doctype' not in supplier:
            supplier['doctype'] = 'Supplier'
        if 'customer_code' not in supplier:
             if 'supplier_name' in supplier:
                 supplier['customer_code'] = supplier['supplier_name']
             elif 'name' in supplier:
                 supplier['customer_code'] = supplier['name']

        is_exists = frappe.db.exists(
            supplier['doctype'], supplier['customer_code'])
        if not is_exists:
            try:
                create_account(supplier)

                doc = frappe.get_doc(supplier)
                doc.insert(set_name=supplier['customer_code'])

                create_contact(supplier)
                create_address(supplier)

                tally_response.append(
                    {'name': supplier['customer_code'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': supplier['customer_code'], 'tally_object': 'Ledger', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': supplier['customer_code'], 'tally_object': 'Ledger', 'message': 'Already Exists'})
        # else:
        #     try:
        #         frappe.db.set_value(supplier['doctype'], supplier['supplier_name'], {
        #             "supplier_name": supplier['supplier_name'],
        #             "supplier_type": supplier['supplier_type'],
        #             "supplier_group": supplier['supplier_group'],
        #             "territory": supplier['territory'],
        #             "tax_category": supplier['tax_category'],
        #             "default_currency": supplier['default_currency'],
        #             "default_price_list": supplier['default_price_list']
        #         })

        #         tally_response.append(
        #             {'name': supplier['supplier_name'], 'tally_object': 'Ledger', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': supplier['supplier_name'], 'tally_object': 'Ledger', 'message': str(e)})

    return {"status": True, 'data': tally_response}    

@frappe.whitelist()
@frappe.whitelist()
def account():
    data = json.loads(frappe.request.data)
    
    if 'data' in data:
         accounts = data['data']
    else:
         accounts = [data] if isinstance(data, dict) else data

    tally_response = []

    for account in accounts:
        if 'doctype' not in account:
            account['doctype'] = 'Account'
        is_exists = frappe.db.exists(
            account['doctype'], {'account_name': account['account_name'], 'company': account['company']})
        if not is_exists:
            try:

                doc = frappe.get_doc(account)
                doc.insert()

                tally_response.append(
                    {'name': account['account_name'], 'tally_object': 'Ledger', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': account['account_name'], 'tally_object': 'Ledger', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': account['account_name'], 'tally_object': 'Ledger', 'message': 'Already Exists'})
        
    return {"status": True, 'data': tally_response}    


def create_account(customer):
    doctype = customer['doctype']
    cus_name = customer['customer_name'] if doctype == 'Customer' else customer['supplier_name']

    abbr = frappe.get_value("Company", customer['company'], "abbr")
    if not abbr:
         frappe.throw("Company Abbreviation not found")

    parent_account = 'Accounts Receivable - {}'.format(abbr) if doctype == 'Customer' else 'Accounts Payable - {}'.format(abbr)
    account_type = 'Receivable' if doctype == 'Customer' else 'Payable'

    req = {
        "company": customer['company'],
        "account_name": cus_name,
        "account_currency": "INR",
        "doctype": "Account",
        "parent_account": parent_account,
        "account_type": account_type
    }

    if not frappe.db.exists("Account", {"account_name": cus_name, "company": customer['company']}):
        doc = frappe.get_doc(req)
        doc.insert()

    # return {'name': customer['customer_name'], 'tally_object': 'Ledger_Contact', 'message': 'Success'}
    print('Success- Account')


def create_contact(customer):
    doctype = customer['doctype']
    cus_name = customer['customer_code'] if doctype == 'Customer' else customer['supplier_name']

    req = {
        "name": customer['ledgercontact'],
        "first_name": customer['ledgercontact'],
        "email_id": customer['email']  if 'email' in customer else "",
        "status": "Passive",
        "phone": customer['ledgermobile'] if 'ledgermobile' in customer else "",
        "mobile_no": customer['ledgermobile'] if 'ledgermobile' in customer else "",
        "is_primary_contact": 1,
        "is_billing_contact": 1,
        "doctype": "Contact",
        "email_ids": [
            {
                "parent": customer['ledgercontact'],
                "parentfield": "email_ids",
                "parenttype": "Contact",
                "email_id": customer['email'] if 'email' in customer else "a@b.com",
                "is_primary": 1,
                "doctype": "Contact Email"
            }
        ],
        "phone_nos": [
            {
                "parent": customer['ledgercontact'],
                "parentfield": "phone_nos",
                "parenttype": "Contact",
                "phone": customer['ledgermobile'] if 'ledgermobile' in customer else "9999999999",
                "is_primary_phone": 1,
                "is_primary_mobile_no": 1,
                "doctype": "Contact Phone"
            }
        ],
        "links": [
            {
                "parent": customer['ledgercontact'],
                "parentfield": "links",
                "parenttype": "Contact",
                "link_doctype": doctype,
                "link_name": cus_name,
                "link_title": cus_name,
                "doctype": "Dynamic Link"
            }
        ],
    }

    if not frappe.db.exists("Contact", customer['ledgercontact']):
        doc = frappe.get_doc(req)
        doc.insert()

    # return {'name': customer['customer_name'], 'tally_object': 'Ledger_Contact', 'message': 'Success'}
    print('Success- Contact')


def create_address(customer):
    address1 = customer['address1'] if 'address1' in customer else ""
    address2 = customer['address2'] if 'address2' in customer else ""
    address3 = customer['address3'] if 'address3' in customer else ""
    address4 = customer['address4'] if 'address4' in customer else ""
    doctype = customer['doctype']
    cus_name = customer['customer_code'] if doctype == 'Customer' else customer['supplier_name']
    
    name = cus_name+"-Billing"

    req = {
        "name": name,
        "address_title": cus_name,
        "address_type": "Billing",
        "address_line1": address1 + " " + address2,
        "address_line2": address3 + " " + address4,
        "city": customer['city'] if 'city' in customer else "",
        "state": customer['state'] if 'state' in customer else "",
        "country": customer['country'] if 'country' in customer else "",
        "pincode": customer['pincode'] if 'pincode' in customer else "",
        # "phone": customer['customer_code'],
        "gstin": customer['partygstin'] if 'partygstin' in customer else "",
        "gst_state": customer['state'] if 'state' in customer else "",
        "gst_state_number": customer['state_code'] if 'state_code' in customer else "",
        "tax_category": customer['tax_category'] if 'tax_category' in customer else "",
        "is_primary_address": 1,
        "is_shipping_address": 1,
        "doctype": "Address",
        "links": [
            {
                "parent": name,
                "parentfield": "links",
                "parenttype": "Address",
                "link_doctype": doctype,
                "link_name": cus_name,
                "link_title": cus_name,
                "doctype": "Dynamic Link"
            }
        ]
    }
    # print(req)
    if not frappe.db.exists("Address", name):
        doc = frappe.get_doc(req)
        doc.insert()

    print('Success- Address') # return {'name': customer['customer_code'], 'tally_object': 'Ledger_Address', 'message': 'Success'}




@frappe.whitelist()
def uom():
    payload = json.loads(frappe.request.data)
    uoms = payload['data']

    tally_response = []

    for uom in uoms:
        if 'doctype' not in uom:
            uom['doctype'] = 'UOM'
        uom_exists = frappe.db.exists(
            uom['doctype'], uom['uom_name'])
        if not uom_exists:
            try:
                doc = frappe.get_doc(uom)
                doc.insert()
                tally_response.append(
                    {'name': uom['uom_name'], 'tally_object': 'Unit', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': uom['uom_name'], 'tally_object': 'Unit', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': uom['uom_name'], 'tally_object': 'Unit', 'message': 'Already Exists'})

    return {"status": True, 'data': tally_response}



@frappe.whitelist()
def item():
    payload = json.loads(frappe.request.data)
    items = payload['data']

    tally_response = []

    for item in items:
        create_hsn(item)
        item_exists = frappe.db.exists(
            'Item', item['item_name'])
        if not item_exists:
            try:
                doc = frappe.get_doc(item)
                doc.insert()
                tally_response.append(
                    {'name': item['item_name'], 'tally_object': 'Stock Item', 'message': 'Success'})
            except Exception as e:
                tally_response.append(
                    {'name': item['item_name'], 'tally_object': 'Stock Item', 'message': str(e)})
        else:
            tally_response.append(
                    {'name': item['item_name'], 'tally_object': 'Stock Item', 'message': 'Already Exists'})
        # else:
        #     try:
        #         frappe.db.set_value(item['doctype'], item['item_name'], {
        #             "item_group_name": item['item_group_name'],
        #             "is_group": item['is_group']
        #         })

        #         tally_response.append(
        #             {'name': item['item_name'], 'tally_object': 'Stock Item', 'message': 'Success'})
        #     except Exception as e:
        #         tally_response.append(
        #             {'name': item['item_name'], 'tally_object': 'Stock ITem', 'message': str(e)})

    return {"status": True, 'data': tally_response}

def create_hsn(item):
    if 'gst_hsn_code' in item:
        if not frappe.db.exists('GST HSN Code', item['gst_hsn_code']):

            req = {
                "hsn_code": item['gst_hsn_code'],
                "doctype": "GST HSN Code"
            }

            doc = frappe.get_doc(req)
            doc.insert()

import traceback

def sanitize_voucher_data(data):
    """
    Sanitizes voucher data by converting None values to 0.0 for numeric fields.
    This prevents 'unsupported operand type(s) for -: NoneType and float' errors.
    """
    numeric_fields = [
        'qty', 'stock_qty', 'actual_qty', 'rate', 'base_rate', 
        'amount', 'base_amount', 'base_price_list_rate', 
        'discount_percentage', 'price_list_rate', 'conversion_factor'
    ]
    
    tax_numeric_fields = [
        'tax_amount', 'tax_amount_after_discount_amount', 
        'base_tax_amount', 'base_tax_amount_after_discount_amount', 
        'rate', 'base_total'
    ]

    # Sanitize Item details
    if 'items' in data:
        for item in data['items']:
            for field in numeric_fields:
                if field in item and item[field] is None:
                    item[field] = 0.0
    
    # Sanitize Tax details
    if 'taxes' in data:
        for tax in data['taxes']:
            for field in tax_numeric_fields:
                if field in tax and tax[field] is None:
                    tax[field] = 0.0

@frappe.whitelist()
def voucher():
    payload = json.loads(frappe.request.data)
    sales = payload['data']
    
    tally_response = []

    for sale in sales:
        sales_exists = frappe.db.exists(
            sale['doctype'], sale['webstatus_docname'])
        if not sales_exists:
            try:
                sanitize_voucher_data(sale)
                doc = frappe.get_doc(sale)
                doc.insert(set_name=sale['tally_voucherno'])
                # doc.save()
                # doc.submit()
                tally_response.append(
                    {'name': sale['tally_masterid'], 'docname': doc.name, 'tally_object': 'voucher', 'message': 'Success'})
            except Exception as e:
                # Capture full traceback for debugging
                error_message = "{}: {}".format(str(e), traceback.format_exc())
                # Truncate if too long for Tally (optional, but good practice if Tally has limits)
                # But for now, we want to see the error.
                tally_response.append(
                    {'name': sale['tally_masterid'], 'tally_object': 'voucher', 'message': str(e)}) # Keeping str(e) for Tally display, but could log full error
                frappe.log_error(title="Tally Voucher Error", message=traceback.format_exc())
        else:
            tally_response.append(
                    {'name': sale['tally_masterid'], 'docname': doc.name, 'tally_object': 'voucher', 'message': 'Already Exists'})

    return {"status": True, 'data': tally_response}
    
