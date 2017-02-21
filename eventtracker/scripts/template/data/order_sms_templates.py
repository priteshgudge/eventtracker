# -*- coding: utf-8 -*-

#English
sms_content_create="Thank you for placing Order No.{{orderId}} with AgroStar!Your order is confirmed & you will get the dispatch details by SMS soon.Call {{tollFreeNumber}} for any queries."
sms_template_order_create = { u'body': sms_content_create,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'en',
 u'name': u'ORDERCREATE',
 u'type': u'sms'}


sms_content_cancel = "Your AgroStar Order No.{{orderId}} has been cancelled as per your request.Hope you give us another chance to serve you again soon.Call on {{tollFreeNumber}} for queries."
sms_template_order_cancel = { u'body': sms_content_cancel,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'en',
 u'name': u'ORDERCANCEL',
 u'type': u'sms'}


sms_content_edit = "Your order is updated and the new AgroStar Order No. is {{orderId}}.You will get the dispatch details soon by SMS.Call us on {{tollFreeNumber}} for any queries."
sms_template_order_edit = { u'body': sms_content_edit,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'en',
 u'name': u'ORDEREDIT',
 u'type': u'sms'}


##########################################################################################################################################################
# Marathi

sms_content_create_mr= u"अॅग्रोस्टारला ऑर्डर क्र. {{orderId}} देण्यासाठी धन्यवाद! तुमच्या ऑर्डरची पुष्टी करण्यात आली आहे आणि तुम्हाला लवकरच SMSने पाठवल्याचे तपशील येतील.काही शंका असल्यास {{tollFreeNumber}} वर फोन करा."
sms_template_order_create_mr = { u'body': sms_content_create_mr,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'mr',
 u'name': u'ORDERCREATE',
 u'type': u'sms'}

sms_content_cancel_mr = u"अॅग्रोस्टार ऑर्डर क्र.{{orderId}} तुमच्या विनंतीनुसार रद्द केली आहे. तुम्ही लवकरच सेवा करण्याची दुसरी संधी द्याल अशी आशा आहे.शंका असल्यास {{tollFreeNumber}} वर फोन करा."
sms_template_order_cancel_mr = { u'body': sms_content_cancel_mr,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'mr',
 u'name': u'ORDERCANCEL',
 u'type': u'sms'}

sms_content_edit_mr = u"अॅग्रोस्टार ऑर्डर अपडेट करण्यात आली आहे, नवीन ऑर्डर क्र.{{orderId}} आहे. तुम्हाला लवकरच SMSने पाठवल्याचे तपशील येतील. काही शंका असल्यास आम्हाला {{tollFreeNumber}} वर फोन करा."
sms_template_order_edit_mr = { u'body': sms_content_edit_mr,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'mr',
 u'name': u'ORDEREDIT',
 u'type': u'sms'}

##########################################################################################################################################################
#Hindi
sms_content_create_hi = u"एग्रोस्टार को ऑर्डर नं. {{orderId}} देने के लिए धन्यवाद! आपका ऑर्डर कन्फर्म है। आपको जल्द ही SMS से इसकी जानकारी मिलेगी। पूछताछ के लिए {{tollFreeNumber}} पर कॉल करें।"
sms_template_order_create_hi = { u'body': sms_content_create_hi,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'hi',
 u'name': u'ORDERCREATE',
 u'type': u'sms'}

sms_content_cancel_hi = u"आपका एग्रोस्टार ऑर्डर नं. {{orderId}} आपकी मांग से रद्द किया गया। आशा है, आप हमें जल्द सेवा का मौका देंगे। पूछताछ के लिए {{tollFreeNumber}} पर कॉल करें।"
sms_template_order_cancel_hi = { u'body': sms_content_cancel_hi,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'hi',
 u'name': u'ORDERCANCEL',
 u'type': u'sms'}

sms_content_edit_hi = u"आपका एग्रोस्टार ऑर्डर अपडेट हो गया। आपका नया ऑर्डर नं. {{orderId}} है। ऑर्डर के डिस्पैच की जानकारी SMS से जल्द ही मिलेगी। पूछताछ के लिए {{tollFreeNumber}} पर कॉल करें।"
sms_template_order_edit_hi = { u'body': sms_content_edit_hi,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'hi',
 u'name': u'ORDEREDIT',
 u'type': u'sms'}



##########################################################################################################################################################
#Gujarati
sms_content_create_gu= u"એગ્રોસ્ટાર પાસે તમારો ઓર્ડર-{{orderId}} મુકવા બદલ આભાર  તમારો ઓર્ડર નિશ્ચિત છે અને તમે રવાના થવાની વિગતો તરતમાં SMS થી મેળવશો. પુછપરછમાટે {{tollFreeNumber}} પર કોલ કરો."
sms_template_order_create_gu = { u'body': sms_content_create_gu,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'gu',
 u'name': u'ORDERCREATE',
 u'type': u'sms'}


sms_content_cancel_gu = u"તમારી વિનંતી મુજબ તમારો એગ્રોસ્ટાર ઓર્ડર નં.{{orderId}} રદ કરેલ છે. આશા છે તમે તરતમાં ફરી સેવાની તક આપશો.પુછપરછમાટે {{tollFreeNumber}} કોલ કરો."
sms_template_order_cancel_gu = { u'body': sms_content_cancel_gu,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'gu',
 u'name': u'ORDERCANCEL',
 u'type': u'sms'}

sms_content_edit_gu = u"તમારો ઓર્ડર સુધારેલ છે અને નવો એગ્રોસ્ટાર ઓર્ડર નં.{{orderId}} છે. આપ રવાના થયાની વિગતો તરતમાં SMSથી મેળવશો. પુછપરછમાટે {{tollFreeNumber}} પર કોલ કરો."
sms_template_order_edit_gu = { u'body': sms_content_edit_gu,
 u'fields': [u'orderId', u'tollFreeNumber'],
 u'language': u'gu',
 u'name': u'ORDEREDIT',
 u'type': u'sms'}

