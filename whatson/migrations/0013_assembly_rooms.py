# News item related to Derby Hippodrome appeal

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'Plan to Reopen the Assembly Rooms' ,
        image = '/assets/img/news_items/assembly_rooms_card.jpg' ,
        precis = """\
DATA consulted again on the Assembly Rooms renovation plan\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/ground-floor-entrance-area.jpg"
width="640px" height="360px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="225px"
src="/assets/img/news_items/ground-floor-entrance-area.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/ground-floor-entrance-area.jpg"
width="550px" height="310px">
<p>
DATA representatives attended a meeting on the plans to repopen the Assembly
Rooms at the Derby City Council building on 15th May 2019. This was at the
invitation of the DCC who wished to update DATA on the architectural proposals
and seek DATA input on them.
</p>
<p>
Representatives of the DCC project management as well as the lead and architect
from the subcontractor attended and gave a detailed walkthrough of the
architectural proposals. DATA was well represented, particularly thanks
to attendance from a number of experienced stage managers drawn from our
membership.
</p>
<p>
The meeting was again cordial and constructive. DATA representatives were able
give a number of inputs from the perspective of staging productions in the
Assembly Rooms. These were gratefully received but of course all confirmed plans
will be subject to budgetary constraints and planning permission.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0012_hippodrome_news_item' ) ,
    ]

    operations = [

        migrations.RunPython ( news_item ) ,

    ]
