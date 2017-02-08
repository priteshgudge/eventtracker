# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
from bson import ObjectId
from eventtracker.scripts.template.data.email_templates import *
from eventtracker.scripts.template.data.order_sms_templates import *
from eventtracker.scripts.template.data.ticket_sms_templates import *

def populate_email_templates(db):
    result = db.templates.insert_one(email_template_create)
    print "EMAIL ORDER CREATE TEMPLATE INSERT", result.acknowledged

    result = db.templates.insert_one(email_template_edit)
    print "EMAIL ORDER EDIT TEMPLATE INSERT", result.acknowledged

    result = db.templates.insert_one(email_template_cancel)
    print "EMAIL ORDER CANCEL TEMPLATE INSERT", result.acknowledged

    email_templates = db.templates.find({'type':'email'})
    for t in email_templates:
        print t
    return True

def populate_sms_templates_english(db):
    result = db.templates.insert_one(sms_template_order_create)
    print "SMS TEMPLATE ORDERCREATE INSERT", result.acknowledged

    result = db.templates.insert_one(sms_template_order_edit)
    print "SMS TEMPLATE ORDER EDIT", result.acknowledged


    result = db.templates.insert_one(sms_template_order_cancel)
    print "SMS TEMPLATE ORDER CANCEL", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_open)
    print "SMS TEMPLATE TICKET CREATE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_close)
    print "SMS TEMPLATE TICKET CLOSE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_resolve)
    print "SMS TEMPLATE TICKET Resolved", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_cust)
    print "SMS TEMPLATE TICKET PENDING CUSTOMER", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fo)
    print "SMS TEMPLATE TICKET PENDING Field Officer", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_ip)
    print "SMS TEMPLATE TICKET PENDING India Post", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fr)
    print "SMS TEMPLATE TICKET PENDING Franchisee", result.acknowledged
    sms_templates = db.templates.find({'type':'sms'})

    result = db.templates.insert_one(sms_template_ticket_pend_ag)
    print "SMS TEMPLATE TICKET PENDING Agrostar", result.acknowledged
    sms_templates = db.templates.find({'type':'sms','language':'en'})
    #print sms_templates
    for s in sms_templates:
        print s
    return True

def populate_sms_templates_hindi(db):
    result = db.templates.insert_one(sms_template_order_create_hi)
    print "SMS TEMPLATE ORDERCREATE INSERT", result.acknowledged

    result = db.templates.insert_one(sms_template_order_edit_hi)
    print "SMS TEMPLATE ORDER EDIT", result.acknowledged


    result = db.templates.insert_one(sms_template_order_cancel_hi)
    print "SMS TEMPLATE ORDER CANCEL", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_open_hi)
    print "SMS TEMPLATE TICKET CREATE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_close_hi)
    print "SMS TEMPLATE TICKET CLOSE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_resolve_hi)
    print "SMS TEMPLATE TICKET Resolved", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_cust_hi)
    print "SMS TEMPLATE TICKET PENDING CUSTOMER", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fo_hi)
    print "SMS TEMPLATE TICKET PENDING Field Officer", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_ip_hi)
    print "SMS TEMPLATE TICKET PENDING India Post", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fr_hi)
    print "SMS TEMPLATE TICKET PENDING Franchisee", result.acknowledged
    sms_templates = db.templates.find({'type':'sms'})

    result = db.templates.insert_one(sms_template_ticket_pend_ag_hi)
    print "SMS TEMPLATE TICKET PENDING Agrostar", result.acknowledged
    sms_templates = db.templates.find({'type':'sms','language':'hi'})
    #print sms_templates
    for s in sms_templates:
        print s
    return True


def populate_sms_templates_marathi(db):
    result = db.templates.insert_one(sms_template_order_create_mr)
    print "SMS TEMPLATE ORDERCREATE INSERT", result.acknowledged

    result = db.templates.insert_one(sms_template_order_edit_mr)
    print "SMS TEMPLATE ORDER EDIT", result.acknowledged


    result = db.templates.insert_one(sms_template_order_cancel_mr)
    print "SMS TEMPLATE ORDER CANCEL", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_open_mr)
    print "SMS TEMPLATE TICKET CREATE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_close_mr)
    print "SMS TEMPLATE TICKET CLOSE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_resolve_mr)
    print "SMS TEMPLATE TICKET Resolved", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_cust_mr)
    print "SMS TEMPLATE TICKET PENDING CUSTOMER", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fo_mr)
    print "SMS TEMPLATE TICKET PENDING Field Officer", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_ip_mr)
    print "SMS TEMPLATE TICKET PENDING India Post", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fr_mr)
    print "SMS TEMPLATE TICKET PENDING Franchisee", result.acknowledged
    sms_templates = db.templates.find({'type':'sms'})

    result = db.templates.insert_one(sms_template_ticket_pend_ag_mr)
    print "SMS TEMPLATE TICKET PENDING Agrostar", result.acknowledged
    sms_templates = db.templates.find({'type':'sms','language':'mr'})
    #print sms_templates
    for s in sms_templates:
        print s
    return True


def populate_sms_templates_gujarati(db):
    result = db.templates.insert_one(sms_template_order_create_gu)
    print "SMS TEMPLATE ORDERCREATE INSERT", result.acknowledged

    result = db.templates.insert_one(sms_template_order_edit_gu)
    print "SMS TEMPLATE ORDER EDIT", result.acknowledged


    result = db.templates.insert_one(sms_template_order_cancel_gu)
    print "SMS TEMPLATE ORDER CANCEL", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_open_gu)
    print "SMS TEMPLATE TICKET CREATE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_close_gu)
    print "SMS TEMPLATE TICKET CLOSE", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_resolve_gu)
    print "SMS TEMPLATE TICKET Resolved", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_cust_gu)
    print "SMS TEMPLATE TICKET PENDING CUSTOMER", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fo_gu)
    print "SMS TEMPLATE TICKET PENDING Field Officer", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_ip_gu)
    print "SMS TEMPLATE TICKET PENDING India Post", result.acknowledged

    result = db.templates.insert_one(sms_template_ticket_pend_fr_gu)
    print "SMS TEMPLATE TICKET PENDING Franchisee", result.acknowledged
    sms_templates = db.templates.find({'type':'sms'})

    result = db.templates.insert_one(sms_template_ticket_pend_ag_gu)
    print "SMS TEMPLATE TICKET PENDING Agrostar", result.acknowledged
    sms_templates = db.templates.find({'type':'sms','language':'gu'})
    #print sms_templates
    for s in sms_templates:
        print s
    return True

def populate_sms_templates(db):
    populate_sms_templates_english(db)
    populate_sms_templates_hindi(db)
    populate_sms_templates_marathi(db)
    populate_sms_templates_gujarati(db)


def create_database_indexes(db):
    result = db.templates.create_index(
        [('type', pymongo.ASCENDING), ('name', pymongo.ASCENDING), ('language', pymongo.ASCENDING)], unique=True)
    print result


def get_database():
    client = MongoClient('localhost', 27017)
    try:
        client.drop_database("notification_templates")
    except:
        print "Exception while dropping database"
    db = client.notification_templates
    return db

if __name__ == "__main__":
    db = get_database()
    create_database_indexes(db)
    populate_email_templates(db)
    populate_sms_templates(db)