EMAIL_CREATE = """
<html>
<body>
<h5 style="font-size: 18px;"> Dear {{storeName}} {{sourceName}} Partner </h5>
<p> Thank you for confirming the order of <u>{{farmer.firstName}} {{farmer.lastName}}</u> (Phone Number: {{phoneNumber}}) </p>

<p>The order has been confirmed for: </p>

<table style="border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #000;">Sr. No.</th>
            <th style="border: 1px solid #000;">Item Name</th>
            <th style="border: 1px solid #000;">Quantity</th>
            <th style="border: 1px solid #000;">Price</th>
        </tr>

        {% for oi in orderItems%}
           <tr>
            <td style="border: 1px solid #000;">{{loop.index}}</td>
            <td style="border: 1px solid #000;">{{oi.name}}</td>
            <td style="border: 1px solid #000;">{{oi.quantity}}</td>
            <td style="border: 1px solid #000;">{{oi.totalPrice}}</td>
           </tr>
        {% endfor %}
    </thead>
    <tbody>
    </tbody>
</table>

<p> The Order ID is <b>{{orderId}}</b> and the total order amount is <b>Rs.{{orderAmount}}</b>. </p>

<p>Kindly collect the total order amount mentioned and update the collection in the Google spreadsheet too.</p>

<p>For any queries, please feel free to give a missed call on 020-49494950 again.</p>


<div class="m_3580056201794708194gmail_signature" data-smartmail="gmail_signature"><p style="margin:0in 0in 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif"><a href="http://agrostar.in/" style="font-family:&quot;Times New Roman&quot;;font-size:medium" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://agrostar.in/&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNHnclaMeuviFyy5uyW39AQPNwguig"><img src="https://ci5.googleusercontent.com/proxy/FvXuu5oNQ78R8x11U3AS0a2th0B2WCCFbWnVKmuVYcrA7dt-tChX3ddz2aBjca7JDz54UQG5qKGflnSk3EgSCViMRQ9id6UhxV904jViW4fje9FtFSkG2_dohtb9Jxv8qG1r2MhA=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_3.jpg" alt="Agrostar signature" class="CToWUd"></a><span style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium"></span></p><table width="270" cellspacing="8" cellpadding="0" style="font-family:&quot;Times New Roman&quot;;padding:0px"><tbody><tr><td><a href="http://tech.economictimes.indiatimes.com/news/startups/et-startup-awards-2016-how-agrostar-is-making-a-profit-while-making-a-difference/53591261" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://tech.economictimes.indiatimes.com/news/startups/et-startup-awards-2016-how-agrostar-is-making-a-profit-while-making-a-difference/53591261&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNFBuuGruBE4kes7pClXlbj885oUDA"><img src="https://ci6.googleusercontent.com/proxy/l0fi2AhTMTqxtVd9yET0Op_WZl3r2B8I-Y-nScLbeA2UrOBd67WBB1JPeNDVLs9YOEnU3o4Gjl9kHk0j3I1AkcLWxtSj4KsywldCf28WWV7dMsJxmQAnf6eTR2jSAkiy4Ig=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/ET_link.png" alt="Google play" class="CToWUd"></a></td><td><a href="https://play.google.com/store/apps/details?id=com.ulink.agrostar" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://play.google.com/store/apps/details?id%3Dcom.ulink.agrostar&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNHg3UhpmFEHxy8lSNL-tU2BHBCR8A"><img src="https://ci6.googleusercontent.com/proxy/waSKVw16gEwPfpmO-RX8T6BcPyRiEzzDXFNktZ9BCvUtPrQhonUWNwQuPB5JXPIZkU1zpoVV1F9v9x2MpHE-BP319LXFoQcNIxnf0-4wcekUQE9qbgMnyughYyQrxDYGiAPvxdzbshMnIw=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/PlayStore_White.jpg" alt="Google play" class="CToWUd"></a></td><td><a href="https://www.facebook.com/AgroStar.India/" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.facebook.com/AgroStar.India/&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGlAm8DhpQzMa3xZTIA0Vh4X73eWA"><img src="https://ci3.googleusercontent.com/proxy/9COntQHrH4cspNszlsOcth239yiZr8YLciagewY_lqYAKn4O8BOVCchbG6FLstYn-cqVHiHC3ekaVrUlr8ShATM1Xm5cI3qukKncaCD-9VfGegJP9AN7r08NNUQXYsP3XfkQjEtGPg=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_Fb.png" alt="Facebook" class="CToWUd"></a></td><td><a href="https://twitter.com/agrostar_in" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/agrostar_in&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGJtE6YgkJAaUQ8coeu10Q82fPRcQ"><img src="https://ci6.googleusercontent.com/proxy/5T4CvHgiPnMegLhAj5Vi-o_KF6mKJR8JjtOnqd7oJsfO0ygsQXrHq7YPXzxGCCmtQR3SYVEVJH2_69y3m6XmXvnxM3ORCMPYMZGV0GjmovVdwpSFLElmhO-1fNxHEX8crZa3xd6X=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_T.png" alt="Twitter" class="CToWUd"></a></td><td><a href="https://www.linkedin.com/company/agrostar-in?trk=biz-companies-cym" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.linkedin.com/company/agrostar-in?trk%3Dbiz-companies-cym&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNEOjL26x3t5l-nvEj9bASFunivG_A"><img src="https://ci6.googleusercontent.com/proxy/6rC5pOepOqqpB-sBwrhXihS2wAzOGWBqH4LE5m0s-Gm5eLi9C09nzbjYveiAUD_wZgsmbWb7S8OhxOOdHx6yFlNl5IMi4ZQuASH9yGfSDWzPjuhSa5hqRvQV_ndchYDmv7Xhva2QbA=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_LI.png" alt="Linkedin" class="CToWUd"></a></td><td><a href="https://www.youtube.com/channel/UCnEo71tCmqMQyS0ZoP6P4gg" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.youtube.com/channel/UCnEo71tCmqMQyS0ZoP6P4gg&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGWUUrApoihYuSl-IxIv-0oMkH11Q"><img src="https://ci6.googleusercontent.com/proxy/ccGBAczb_AWDYRg-9R8HScdsNy2eEiQr3eDoJn8taX6EE9LD8YXnmLs28HY6ANFwpVDWNDxJJXYdiNDXOUGpGUEL5nLVNMLRJswFus7ctVf6_xYFS6E7Eih_FOhbqCI6P27Fe7X_9PCAEL45=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_YouTube.png" alt="YouTube" class="CToWUd"></a></td></tr></tbody></table><p style="width:590px;font-family:&quot;Trebuchet MS&quot;,&quot;Lucida Grande&quot;,&quot;Lucida Sans Unicode&quot;,&quot;Lucida Sans&quot;,Tahoma,sans-serif;color:rgb(137,137,137);font-size:10px;margin:0px 0px 5px;font-weight:lighter">Disclaimer:<br>"The information contained herein (including any accompanying documents) is confidential and is intended solely for the addressee(s). If you have erroneously received this message, please immediately delete it and notify the sender. Also, if you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution or taking any action in reliance on the contents of this message or any accompanying document is strictly prohibited and is unlawful. The organization is not responsible for any damage caused by a virus or alteration of the e-mail by a third party or otherwise."</p><p style="margin:0in 0in 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif"><br style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium"><span style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium">&nbsp;</span><br></p></div></div></div></div></div></div>


</body>
</html>

"""

EMAIL_EDIT = """
<html>
<body>
<h5 style="font-size: 18px;"> Dear {{storeName}} {{sourceName}} Partner </h5>
<p> Please ignore Order No. {{oldOrderId}}. The order is now edited for <u>{{farmer.firstName}} {{farmer.lastName}}</u> (Phone Number: {{phoneNumber}}) </p>

<p>The order has been confirmed for: </p>

<table style="border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #000;">Sr. No.</th>
            <th style="border: 1px solid #000;">Item Name</th>
            <th style="border: 1px solid #000;">Quantity</th>
            <th style="border: 1px solid #000;">Price</th>
        </tr>

        {% for oi in orderItems%}
           <tr>
            <td style="border: 1px solid #000;">{{loop.index}}</td>
            <td style="border: 1px solid #000;">{{oi.name}}</td>
            <td style="border: 1px solid #000;">{{oi.quantity}}</td>
            <td style="border: 1px solid #000;">{{oi.totalPrice}}</td>
           </tr>
        {% endfor %}
    </thead>
    <tbody>
    </tbody>
</table>

<p> The new Order No. is <b>{{orderId}}</b> and the new total order amount is <b>Rs.{{orderAmount}}</b>. </p>

<p>Kindly collect the total order amount mentioned and update the collection in the Google spreadsheet too.</p>

<p>For any queries, please feel free to give a missed call on 020-49494950 again.</p>


<div class="m_3580056201794708194gmail_signature" data-smartmail="gmail_signature"><p style="margin:0in 0in 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif"><a href="http://agrostar.in/" style="font-family:&quot;Times New Roman&quot;;font-size:medium" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://agrostar.in/&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNHnclaMeuviFyy5uyW39AQPNwguig"><img src="https://ci5.googleusercontent.com/proxy/FvXuu5oNQ78R8x11U3AS0a2th0B2WCCFbWnVKmuVYcrA7dt-tChX3ddz2aBjca7JDz54UQG5qKGflnSk3EgSCViMRQ9id6UhxV904jViW4fje9FtFSkG2_dohtb9Jxv8qG1r2MhA=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_3.jpg" alt="Agrostar signature" class="CToWUd"></a><span style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium"></span></p><table width="270" cellspacing="8" cellpadding="0" style="font-family:&quot;Times New Roman&quot;;padding:0px"><tbody><tr><td><a href="http://tech.economictimes.indiatimes.com/news/startups/et-startup-awards-2016-how-agrostar-is-making-a-profit-while-making-a-difference/53591261" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://tech.economictimes.indiatimes.com/news/startups/et-startup-awards-2016-how-agrostar-is-making-a-profit-while-making-a-difference/53591261&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNFBuuGruBE4kes7pClXlbj885oUDA"><img src="https://ci6.googleusercontent.com/proxy/l0fi2AhTMTqxtVd9yET0Op_WZl3r2B8I-Y-nScLbeA2UrOBd67WBB1JPeNDVLs9YOEnU3o4Gjl9kHk0j3I1AkcLWxtSj4KsywldCf28WWV7dMsJxmQAnf6eTR2jSAkiy4Ig=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/ET_link.png" alt="Google play" class="CToWUd"></a></td><td><a href="https://play.google.com/store/apps/details?id=com.ulink.agrostar" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://play.google.com/store/apps/details?id%3Dcom.ulink.agrostar&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNHg3UhpmFEHxy8lSNL-tU2BHBCR8A"><img src="https://ci6.googleusercontent.com/proxy/waSKVw16gEwPfpmO-RX8T6BcPyRiEzzDXFNktZ9BCvUtPrQhonUWNwQuPB5JXPIZkU1zpoVV1F9v9x2MpHE-BP319LXFoQcNIxnf0-4wcekUQE9qbgMnyughYyQrxDYGiAPvxdzbshMnIw=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/PlayStore_White.jpg" alt="Google play" class="CToWUd"></a></td><td><a href="https://www.facebook.com/AgroStar.India/" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.facebook.com/AgroStar.India/&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGlAm8DhpQzMa3xZTIA0Vh4X73eWA"><img src="https://ci3.googleusercontent.com/proxy/9COntQHrH4cspNszlsOcth239yiZr8YLciagewY_lqYAKn4O8BOVCchbG6FLstYn-cqVHiHC3ekaVrUlr8ShATM1Xm5cI3qukKncaCD-9VfGegJP9AN7r08NNUQXYsP3XfkQjEtGPg=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_Fb.png" alt="Facebook" class="CToWUd"></a></td><td><a href="https://twitter.com/agrostar_in" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/agrostar_in&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGJtE6YgkJAaUQ8coeu10Q82fPRcQ"><img src="https://ci6.googleusercontent.com/proxy/5T4CvHgiPnMegLhAj5Vi-o_KF6mKJR8JjtOnqd7oJsfO0ygsQXrHq7YPXzxGCCmtQR3SYVEVJH2_69y3m6XmXvnxM3ORCMPYMZGV0GjmovVdwpSFLElmhO-1fNxHEX8crZa3xd6X=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_T.png" alt="Twitter" class="CToWUd"></a></td><td><a href="https://www.linkedin.com/company/agrostar-in?trk=biz-companies-cym" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.linkedin.com/company/agrostar-in?trk%3Dbiz-companies-cym&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNEOjL26x3t5l-nvEj9bASFunivG_A"><img src="https://ci6.googleusercontent.com/proxy/6rC5pOepOqqpB-sBwrhXihS2wAzOGWBqH4LE5m0s-Gm5eLi9C09nzbjYveiAUD_wZgsmbWb7S8OhxOOdHx6yFlNl5IMi4ZQuASH9yGfSDWzPjuhSa5hqRvQV_ndchYDmv7Xhva2QbA=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_LI.png" alt="Linkedin" class="CToWUd"></a></td><td><a href="https://www.youtube.com/channel/UCnEo71tCmqMQyS0ZoP6P4gg" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.youtube.com/channel/UCnEo71tCmqMQyS0ZoP6P4gg&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGWUUrApoihYuSl-IxIv-0oMkH11Q"><img src="https://ci6.googleusercontent.com/proxy/ccGBAczb_AWDYRg-9R8HScdsNy2eEiQr3eDoJn8taX6EE9LD8YXnmLs28HY6ANFwpVDWNDxJJXYdiNDXOUGpGUEL5nLVNMLRJswFus7ctVf6_xYFS6E7Eih_FOhbqCI6P27Fe7X_9PCAEL45=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_YouTube.png" alt="YouTube" class="CToWUd"></a></td></tr></tbody></table><p style="width:590px;font-family:&quot;Trebuchet MS&quot;,&quot;Lucida Grande&quot;,&quot;Lucida Sans Unicode&quot;,&quot;Lucida Sans&quot;,Tahoma,sans-serif;color:rgb(137,137,137);font-size:10px;margin:0px 0px 5px;font-weight:lighter">Disclaimer:<br>"The information contained herein (including any accompanying documents) is confidential and is intended solely for the addressee(s). If you have erroneously received this message, please immediately delete it and notify the sender. Also, if you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution or taking any action in reliance on the contents of this message or any accompanying document is strictly prohibited and is unlawful. The organization is not responsible for any damage caused by a virus or alteration of the e-mail by a third party or otherwise."</p><p style="margin:0in 0in 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif"><br style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium"><span style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium">&nbsp;</span><br></p></div></div></div></div></div></div>


</body>
</html>

"""


EMAIL_CANCEL = """
<html>
<body>
<h5 style="font-size: 18px;"> Dear {{storeName}} {{sourceName}} Partner </h5>
<p> As request, Order No. {{orderId}} is now cancelled for <u>{{farmer.firstName}} {{farmer.lastName}}</u> (Phone Number: {{phoneNumber}}) </p>

<p>The order has been cancelled for the following products: </p>

<table style="border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #000;">Sr. No.</th>
            <th style="border: 1px solid #000;">Item Name</th>
            <th style="border: 1px solid #000;">Quantity</th>
            <th style="border: 1px solid #000;">Price</th>
        </tr>

        {% for oi in orderItems%}
           <tr>
            <td style="border: 1px solid #000;">{{loop.index}}</td>
            <td style="border: 1px solid #000;">{{oi.name}}</td>
            <td style="border: 1px solid #000;">{{oi.quantity}}</td>
            <td style="border: 1px solid #000;">{{oi.totalPrice}}</td>
           </tr>
        {% endfor %}
    </thead>
    <tbody>
    </tbody>
</table>

<p>Kindly refer the total order amount <b>Rs.{{orderAmount}}</b> mentioned and update the collection in the Google spreadsheet too.</p>

<p>For any queries, please feel free to give a missed call on 020-49494950 again.</p>


<div class="m_3580056201794708194gmail_signature" data-smartmail="gmail_signature"><p style="margin:0in 0in 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif"><a href="http://agrostar.in/" style="font-family:&quot;Times New Roman&quot;;font-size:medium" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://agrostar.in/&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNHnclaMeuviFyy5uyW39AQPNwguig"><img src="https://ci5.googleusercontent.com/proxy/FvXuu5oNQ78R8x11U3AS0a2th0B2WCCFbWnVKmuVYcrA7dt-tChX3ddz2aBjca7JDz54UQG5qKGflnSk3EgSCViMRQ9id6UhxV904jViW4fje9FtFSkG2_dohtb9Jxv8qG1r2MhA=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_3.jpg" alt="Agrostar signature" class="CToWUd"></a><span style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium"></span></p><table width="270" cellspacing="8" cellpadding="0" style="font-family:&quot;Times New Roman&quot;;padding:0px"><tbody><tr><td><a href="http://tech.economictimes.indiatimes.com/news/startups/et-startup-awards-2016-how-agrostar-is-making-a-profit-while-making-a-difference/53591261" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=http://tech.economictimes.indiatimes.com/news/startups/et-startup-awards-2016-how-agrostar-is-making-a-profit-while-making-a-difference/53591261&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNFBuuGruBE4kes7pClXlbj885oUDA"><img src="https://ci6.googleusercontent.com/proxy/l0fi2AhTMTqxtVd9yET0Op_WZl3r2B8I-Y-nScLbeA2UrOBd67WBB1JPeNDVLs9YOEnU3o4Gjl9kHk0j3I1AkcLWxtSj4KsywldCf28WWV7dMsJxmQAnf6eTR2jSAkiy4Ig=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/ET_link.png" alt="Google play" class="CToWUd"></a></td><td><a href="https://play.google.com/store/apps/details?id=com.ulink.agrostar" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://play.google.com/store/apps/details?id%3Dcom.ulink.agrostar&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNHg3UhpmFEHxy8lSNL-tU2BHBCR8A"><img src="https://ci6.googleusercontent.com/proxy/waSKVw16gEwPfpmO-RX8T6BcPyRiEzzDXFNktZ9BCvUtPrQhonUWNwQuPB5JXPIZkU1zpoVV1F9v9x2MpHE-BP319LXFoQcNIxnf0-4wcekUQE9qbgMnyughYyQrxDYGiAPvxdzbshMnIw=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/PlayStore_White.jpg" alt="Google play" class="CToWUd"></a></td><td><a href="https://www.facebook.com/AgroStar.India/" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.facebook.com/AgroStar.India/&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGlAm8DhpQzMa3xZTIA0Vh4X73eWA"><img src="https://ci3.googleusercontent.com/proxy/9COntQHrH4cspNszlsOcth239yiZr8YLciagewY_lqYAKn4O8BOVCchbG6FLstYn-cqVHiHC3ekaVrUlr8ShATM1Xm5cI3qukKncaCD-9VfGegJP9AN7r08NNUQXYsP3XfkQjEtGPg=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_Fb.png" alt="Facebook" class="CToWUd"></a></td><td><a href="https://twitter.com/agrostar_in" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://twitter.com/agrostar_in&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGJtE6YgkJAaUQ8coeu10Q82fPRcQ"><img src="https://ci6.googleusercontent.com/proxy/5T4CvHgiPnMegLhAj5Vi-o_KF6mKJR8JjtOnqd7oJsfO0ygsQXrHq7YPXzxGCCmtQR3SYVEVJH2_69y3m6XmXvnxM3ORCMPYMZGV0GjmovVdwpSFLElmhO-1fNxHEX8crZa3xd6X=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_T.png" alt="Twitter" class="CToWUd"></a></td><td><a href="https://www.linkedin.com/company/agrostar-in?trk=biz-companies-cym" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.linkedin.com/company/agrostar-in?trk%3Dbiz-companies-cym&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNEOjL26x3t5l-nvEj9bASFunivG_A"><img src="https://ci6.googleusercontent.com/proxy/6rC5pOepOqqpB-sBwrhXihS2wAzOGWBqH4LE5m0s-Gm5eLi9C09nzbjYveiAUD_wZgsmbWb7S8OhxOOdHx6yFlNl5IMi4ZQuASH9yGfSDWzPjuhSa5hqRvQV_ndchYDmv7Xhva2QbA=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_LI.png" alt="Linkedin" class="CToWUd"></a></td><td><a href="https://www.youtube.com/channel/UCnEo71tCmqMQyS0ZoP6P4gg" target="_blank" data-saferedirecturl="https://www.google.com/url?hl=en&amp;q=https://www.youtube.com/channel/UCnEo71tCmqMQyS0ZoP6P4gg&amp;source=gmail&amp;ust=1484057137010000&amp;usg=AFQjCNGWUUrApoihYuSl-IxIv-0oMkH11Q"><img src="https://ci6.googleusercontent.com/proxy/ccGBAczb_AWDYRg-9R8HScdsNy2eEiQr3eDoJn8taX6EE9LD8YXnmLs28HY6ANFwpVDWNDxJJXYdiNDXOUGpGUEL5nLVNMLRJswFus7ctVf6_xYFS6E7Eih_FOhbqCI6P27Fe7X_9PCAEL45=s0-d-e1-ft#https://s3-ap-southeast-1.amazonaws.com/emailsignatureimagefiles/Signature_YouTube.png" alt="YouTube" class="CToWUd"></a></td></tr></tbody></table><p style="width:590px;font-family:&quot;Trebuchet MS&quot;,&quot;Lucida Grande&quot;,&quot;Lucida Sans Unicode&quot;,&quot;Lucida Sans&quot;,Tahoma,sans-serif;color:rgb(137,137,137);font-size:10px;margin:0px 0px 5px;font-weight:lighter">Disclaimer:<br>"The information contained herein (including any accompanying documents) is confidential and is intended solely for the addressee(s). If you have erroneously received this message, please immediately delete it and notify the sender. Also, if you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution or taking any action in reliance on the contents of this message or any accompanying document is strictly prohibited and is unlawful. The organization is not responsible for any damage caused by a virus or alteration of the e-mail by a third party or otherwise."</p><p style="margin:0in 0in 0.0001pt;font-size:11pt;font-family:Calibri,sans-serif"><br style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium"><span style="color:rgb(0,0,0);font-family:&quot;Times New Roman&quot;;font-size:medium">&nbsp;</span><br></p></div></div></div></div></div></div>


</body>
</html>

"""

email_template_create = {
    u'type': u'email',
    u'name': u'ORDERCREATE',
    u'language': u'en',
    'body': EMAIL_CREATE,
    u'fields': [u'farmer.firstName',u'farmer.lastName',u'phoneNumber',
            u'orderItems:[{name, quantity, totalPrice}]',u'orderId',u'orderAmount'],
            u'subject': u'Order confirmation of {{farmer.firstName}} {{farmer.lastName}}',
            u'subjectFields': [u'farmer.firstName', u'farmer.lastName']
}

email_template_edit = {
    u'type': u'email',
    u'name': u'ORDEREDIT',
    u'language': u'en',
    'body': EMAIL_EDIT,
    u'fields': [u'farmer.firstName',u'farmer.lastName',u'phoneNumber',
            u'orderItems:[{name, quantity, totalPrice}]',u'orderId',u'orderAmount'],
            u'subject': u'Edited Order confirmation of {{farmer.firstName}} {{farmer.lastName}}',
            u'subjectFields': [u'farmer.firstName', u'farmer.lastName']
}

email_template_cancel = {
    u'type': u'email',
    u'name': u'ORDERCANCEL',
    u'language': u'en',
    'body': EMAIL_CANCEL,
    u'fields': [u'farmer.firstName',u'farmer.lastName',u'phoneNumber',
            u'orderItems:[{name, quantity, totalPrice}]',u'orderId',u'orderAmount',u'oldOrderId'],
            u'subject': u'Cancelled Order confirmation of {{farmer.firstName}} {{farmer.lastName}}',
            u'subjectFields': [u'farmer.firstName', u'farmer.lastName']
}