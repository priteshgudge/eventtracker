# -*- coding: utf-8 -*-
#Ticketing SMS
# English
sms_ticket_open = "Dear Customer,your complaint has been registered successfully.Your AgroStar Complaint No. is {{ticketId}} and you will receive a call from us within 24 hrs."
sms_ticket_close = "Dear Customer, your AgroStar Complaint No. {{ticketId}} is now closed."
sms_ticket_resolved = "Dear Customer, we have resolved your AgroStar Complaint No. {{ticketId}}. AgroStar assures quality service and we look forward to serve you even better next time."
sms_ticket_pending_customer = "Dear Customer, Your AgroStar Complaint No. {{ticketId}} is pending from your side. Kindly help us with the required inputs. Call {{tollFreeNumber}} for any questions."
sms_ticket_pending_fo = "Dear Customer,Your AgroStar Complaint No.{{ticketId}} has been assigned to our officer who will contact you soon.We thank you for your patience and understanding."
sms_ticket_pending_ip = "Dear Customer,Your AgroStar Complaint No.{{ticketId}} is being followed up with India Post.We will keep you updated of the status.We thank you for your patience."
sms_ticket_pending_fr = "Dear Customer, Your Complaint No. {{ticketId}} is pending with our delivery partner. We will update you of the status soon. We thank you for your patience."
sms_ticket_pending_agrostar = "Dear Customer,Please be assured that your AgroStar Complaint No.{{ticketId}} is being looked into.We shall update the status soon.We thank you for your patience."

sms_template_ticket_open = { u'body': sms_ticket_open,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETCREATE',
 u'type': u'sms'}

sms_template_ticket_close = { u'body': sms_ticket_close,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETCLOSE',
 u'type': u'sms'}

sms_template_ticket_resolve = { u'body': sms_ticket_resolved,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETRESOLVED',
 u'type': u'sms'}

sms_template_ticket_pend_cust = { u'body': sms_ticket_pending_customer,
 u'fields': [u'ticketId',u'tollFreeNumber'],
 u'language': u'en',
 u'name': u'TICKETSTATUS_PENDING_CUSTOMER',
 u'type': u'sms'}


sms_template_ticket_pend_fo = { u'body': sms_ticket_pending_fo,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETSTATUS_PENDING_FIELD_OFFICER',
 u'type': u'sms'}

sms_template_ticket_pend_ip = { u'body': sms_ticket_pending_ip,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETSTATUS_PENDING_INDIAPOST',
 u'type': u'sms'}

sms_template_ticket_pend_fr = { u'body': sms_ticket_pending_fr,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETSTATUS_PENDING_FRANCHISEE',
 u'type': u'sms'}

sms_template_ticket_pend_ag = { u'body': sms_ticket_pending_agrostar,
 u'fields': [u'ticketId'],
 u'language': u'en',
 u'name': u'TICKETSTATUS_PENDING_AGROSTAR',
 u'type': u'sms'}

############################################################################################################################################
#Marathi
#Ticketing SMS

sms_ticket_open_mr = u"प्रिय ग्राहक, आपली तक्रार यशस्वीपणे नोंदवण्यात आलेली आहे. तुमच्या अॅग्रोस्टार तक्रारीचा क्र. आहे {{ticketId}} आणि तुम्हाला आमच्याकडून 24 तासांच्या आत कॉल येईल."
sms_ticket_close_mr = u"प्रिय ग्राहक, आपली अॅग्रोस्टार तक्रार क्र. {{ticketId}} आता क्लोज करण्यात आली आहे."
sms_ticket_resolved_mr = u"प्रिय ग्राहक, आपली अॅग्रोस्टार तक्रार क्र. {{ticketId}} आम्ही रीझॉल्व्ह केली आहे. अॅग्रोस्टार गुणवत्तापूर्ण सेवेची खात्री देते आणि पुढच्या वेळी आपल्याला अधिक चांगली सेवा देण्याची आम्ही वाट पाहत आहोत."
sms_ticket_pending_customer_mr = u"प्रिय ग्राहक, अॅग्रोस्टार तक्रार क्र. {{ticketId}} आपल्या बाजूने प्रलंबित आहे. कृपया आवश्यक इनपुट देऊन मदत करा. तुम्हाला काही प्रश्न असल्यास {{tollFreeNumber}} वर फोन करा."
sms_ticket_pending_fo_mr = u"प्रिय ग्राहक, आपली तक्रार क्र. {{ticketId}} आमच्या अधिकाऱ्याकडे सोपवण्यात आली आहे, तो तुम्हाला लवकरच फोन करेल. आपल्या संयमाबद्दल आणि समजून घेण्याबद्दल आभारी आहोत."
sms_ticket_pending_ip_mr = u"प्रिय ग्राहक, आपल्या तक्रार क्र.{{ticketId}} बद्दल भारतीय पोस्टाच्या बरोबर पाठपुरावा करण्यात येत आहे. आम्ही आपल्याला स्टेटस अपडेट देत राहू. आपल्या संयमाबद्दल आम्ही आपले आभारी आहोत."
sms_ticket_pending_fr_mr = u"प्रिय ग्राहक, आपली तक्रार क्र. {{ticketId}} डीलीव्हरी पार्टनरकडे प्रलंबित आहे. आम्ही आपल्याला  लवकरच स्टेटस अपडेट देऊ. आपल्या संयमाबद्दल आम्ही आपले आभारी आहोत."
sms_ticket_pending_agrostar_mr = u"प्रिय ग्राहक, आपल्या अॅग्रोस्टार तक्रार क्र. {{ticketId}} मध्ये आम्ही लक्ष घातलेले आहे, ह्याची कृपया खात्री बाळगा. आम्ही आपल्याला लवकरच स्टेटस अपडेट देऊ. आपल्या संयमाबद्दल आम्ही आपले आभारी आहोत."

sms_template_ticket_open_mr = { u'body': sms_ticket_open_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETCREATE',
 u'type': u'sms'}

sms_template_ticket_close_mr = { u'body': sms_ticket_close_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETCLOSE',
 u'type': u'sms'}

sms_template_ticket_resolve_mr = { u'body': sms_ticket_resolved_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETRESOLVED',
 u'type': u'sms'}

sms_template_ticket_pend_cust_mr = { u'body': sms_ticket_pending_customer_mr,
 u'fields': [u'ticketId',u'tollFreeNumber'],
 u'language': u'mr',
 u'name': u'TICKETSTATUS_PENDING_CUSTOMER',
 u'type': u'sms'}


sms_template_ticket_pend_fo_mr = { u'body': sms_ticket_pending_fo_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETSTATUS_PENDING_FIELD_OFFICER',
 u'type': u'sms'}

sms_template_ticket_pend_ip_mr = { u'body': sms_ticket_pending_ip_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETSTATUS_PENDING_INDIAPOST',
 u'type': u'sms'}

sms_template_ticket_pend_fr_mr = { u'body': sms_ticket_pending_fr_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETSTATUS_PENDING_FRANCHISEE',
 u'type': u'sms'}

sms_template_ticket_pend_ag_mr = { u'body': sms_ticket_pending_agrostar_mr,
 u'fields': [u'ticketId'],
 u'language': u'mr',
 u'name': u'TICKETSTATUS_PENDING_AGROSTAR',
 u'type': u'sms'}

#####################################################################################################################################################33
## Hindi
#Ticketing SMS
sms_ticket_open_hi = u"प्रिय ग्राहक, आपकी शिकायत सफलतापूर्वक दर्ज की गयी है। आपका एग्रोस्टार शिकायत नं. {{ticketId}} है और हम आप को 24 घंटे के भीतर कॉल करेंगे।"
sms_ticket_close_hi = u"प्रिय ग्राहक, आपका एग्रोस्टार शिकायत नं. {{ticketId}} अब क्लोज कर दिया गया है।"
sms_ticket_resolved_hi = u"प्रिय ग्राहक, आपका एग्रोस्टार शिकायत नं. {{ticketId}} हल कर दिया गया है। एग्रोस्टार सेवा की गुणवत्ता का भरोसा देता है और हम आपको अगली बार बेहतर सेवा देने के लिए तत्पर हैं।"
sms_ticket_pending_customer_hi = u"प्रिय ग्राहक, आपका एग्रोस्टार शिकायत नं. {{ticketId}} आपकी तरफ से विलंबित है। कृपया हमें आवश्यक इनपुट से मदद करें। पूछताछ के लिए {{tollFreeNumber}} पर कॉल करें।"
sms_ticket_pending_fo_hi = u"प्रिय ग्राहक, आपका एग्रोस्टार शिकायत नं. {{ticketId}} हमारे अधिकारी को असाइन किया गया, वे आपको जल्द ही संपर्क करेंगे। आपके धीरज और समझदारी के लिए हम आपके आभारी हैं।"
sms_ticket_pending_ip_hi = u"प्रिय ग्राहक, आपका एग्रोस्टार शिकायत नं. {{ticketId}} की भारतीय डाक द्वारा जांच की जा रही है। हम आपको स्टेटस अपडेट देते रहेंगे। आपके धीरज के लिए हम आपके आभारी हैं।"
sms_ticket_pending_fr_hi = u"प्रिय ग्राहक, आपका शिकायत नंबर {{ticketId}} हमारे डिलीवरी पार्टनर के पास विलंबित है। हम आपको जल्द ही स्टेटस अपडेट देंगे। आपके धीरज के लिए हम आपके आभारी हैं।"
sms_ticket_pending_agrostar_hi = u"प्रिय ग्राहक, आश्वस्त रहिये कि आपके शिकायत नं. {{ticketId}} पर हम ध्यान दे रहे हैं। हम जल्द ही स्टेटस अपडेट देंगे। आपके धीरज के लिए हम आपके आभारी हैं।"

sms_template_ticket_open_hi = { u'body': sms_ticket_open_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETCREATE',
 u'type': u'sms'}

sms_template_ticket_close_hi = { u'body': sms_ticket_close_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETCLOSE',
 u'type': u'sms'}

sms_template_ticket_resolve_hi = { u'body': sms_ticket_resolved_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETRESOLVED',
 u'type': u'sms'}

sms_template_ticket_pend_cust_hi = { u'body': sms_ticket_pending_customer_hi,
 u'fields': [u'ticketId',u'tollFreeNumber'],
 u'language': u'hi',
 u'name': u'TICKETSTATUS_PENDING_CUSTOMER',
 u'type': u'sms'}


sms_template_ticket_pend_fo_hi = { u'body': sms_ticket_pending_fo_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETSTATUS_PENDING_FIELD_OFFICER',
 u'type': u'sms'}

sms_template_ticket_pend_ip_hi = { u'body': sms_ticket_pending_ip_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETSTATUS_PENDING_INDIAPOST',
 u'type': u'sms'}

sms_template_ticket_pend_fr_hi = { u'body': sms_ticket_pending_fr_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETSTATUS_PENDING_FRANCHISEE',
 u'type': u'sms'}

sms_template_ticket_pend_ag_hi = { u'body': sms_ticket_pending_agrostar_hi,
 u'fields': [u'ticketId'],
 u'language': u'hi',
 u'name': u'TICKETSTATUS_PENDING_AGROSTAR',
 u'type': u'sms'}

############################################################################################################################################
# Gujarati


sms_ticket_open_gu = u"પ્રિય ગ્રાહક, તમારી ફરીયાદ સફળતાપૂર્વક નોંધવામાં આવી છે.  તમારો એગ્રોસ્ટાર ફરીયાદ નં. છે {{ticketId}} અને તમે 24 કલાકની અંદર અમારો કોલ મેળવશો."
sms_ticket_close_gu = u"પ્રિય ગ્રાહક,તમારી એગ્રોસ્ટાર ફરીયાદ નં. {{ticketId}} બંધ કરી છે."
sms_ticket_resolved_gu = u"પ્રિય ગ્રાહક,તમારી એગ્રોસ્ટાર ફરીયાદ નં. {{ticketId}} ઉકેલાયેલ છે. એગ્રોસ્ટાર ગુણવત્તાવાળી સેવાની ખાતરી આપે છે અને અમે ફરી વધુ સારી સેવા આપવાની રાહ જોશું."
sms_ticket_pending_customer_gu = u"પપ્રિય ગ્રાહક,તમારી એગ્રોસ્ટાર ફરીયાદ નં. {{ticketId}} તમારા તરફથી મુલતવી છે. જરૂરી ઇનપુટસ વડે અમને મદદ કરો. કોઈ પણ પ્રશ્નો માટે {{tollFreeNumber}} પર કોલ કરો."
sms_ticket_pending_fo_gu = u"પ્રિય ગ્રાહક,તમારી એગ્રોસ્ટાર ફરીયાદ નં. {{ticketId}} અમારા અધિકારીને સોંપવામાં આવી છે, જે તમારો સંપર્ક કરશે. આપની ધીરજ અને સમજણ માટે અમે આભારી છીએ."
sms_ticket_pending_ip_gu = u"પ્રિય ગ્રાહક, તમારો એગ્રોસ્ટાર ફરીયાદ નં. {{ticketId}} ભારતીય પોસ્ટ દ્વારા અનુસરાયો છે. અમે આપને સ્ટેટસ અપડેટ આપીશું. આપની ધીરજ માટે અમે આભારી છીએ."
sms_ticket_pending_fr_gu = u"પ્રિય ગ્રાહક, તમારી ફરિયાદ નં. {{ticketId}} અમારા ડીલીવરી ભાગીદાર પાસે બાકી છે. અમે આપને તરત સ્ટેટસ અપડેટ આપીશું. આપની ધીરજ માટે અમે આભારી છીએ."
sms_ticket_pending_agrostar_gu = u"પ્રિય ગ્રાહક,તમારી  એગ્રોસ્ટાર ફરિયાદ નં. {{ticketId}} પર ધ્યાન અપાઈ રહ્યું છે. અમે સ્ટેટસ તરત અપડેટ કરશું. આપની ધીરજ માટે અમે આભારી છીએ."

sms_template_ticket_open_gu = { u'body': sms_ticket_open_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETCREATE',
 u'type': u'sms'}

sms_template_ticket_close_gu = { u'body': sms_ticket_close_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETCLOSE',
 u'type': u'sms'}

sms_template_ticket_resolve_gu = { u'body': sms_ticket_resolved_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETRESOLVED',
 u'type': u'sms'}

sms_template_ticket_pend_cust_gu = { u'body': sms_ticket_pending_customer_gu,
 u'fields': [u'ticketId',u'tollFreeNumber'],
 u'language': u'gu',
 u'name': u'TICKETSTATUS_PENDING_CUSTOMER',
 u'type': u'sms'}


sms_template_ticket_pend_fo_gu = { u'body': sms_ticket_pending_fo_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETSTATUS_PENDING_FIELD_OFFICER',
 u'type': u'sms'}

sms_template_ticket_pend_ip_gu = { u'body': sms_ticket_pending_ip_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETSTATUS_PENDING_INDIAPOST',
 u'type': u'sms'}

sms_template_ticket_pend_fr_gu = { u'body': sms_ticket_pending_fr_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETSTATUS_PENDING_FRANCHISEE',
 u'type': u'sms'}

sms_template_ticket_pend_ag_gu = { u'body': sms_ticket_pending_agrostar_gu,
 u'fields': [u'ticketId'],
 u'language': u'gu',
 u'name': u'TICKETSTATUS_PENDING_AGROSTAR',
 u'type': u'sms'}