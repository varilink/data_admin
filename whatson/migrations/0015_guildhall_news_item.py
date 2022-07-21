# News item related to Derby Hippodrome appeal

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'Guildhall Theatre - Latest Statement' ,
        image = '/assets/img/news_items/guildhall_card.jpg' ,
        precis = """\
Derby Live notifies DATA of a delay to the schedule\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="640px" height="525px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="328px"
src="/assets/img/news_items/guildhall.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="550px" height="451px">
<p>
Derby Live has notified DATA that it is not yet in a position to confirm
that the Guildhall Theatre will re-open after September. It had been hoped that
this would be confirmed during May but due to further investigative work being
required it now looks likely that it will be the end of June at the earliest
before it can be confirmed when the venue will re-open.
</p>
<p>
At this stage this is not yet confirmation that the re-opening of the Guildhall
Theatre will be delayed. However, Derby Live recognise that this now
mean that for many companies, an Autumn production in the Guildhall Theatre will
not be an option.
</p>
<p>
A future update is promised as soon as there is any clearer
information. In the meantime, Derby Live would be very grateful if
companies with pencilled-in Autumn bookings could indicate whether they wish to
retain those bookings or release them. If companies have already made
alternative plans could they let Derby Live know so that they can share that
information wherever possible.
</p>
<p>
DATA continues to be in close communication with Derby Live about this matter,
both to represent our members' views and also to ensure as timely communication
as possible.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0014_data_agm' ) ,
    ]

    operations = [

        migrations.RunPython ( news_item ) ,

    ]
