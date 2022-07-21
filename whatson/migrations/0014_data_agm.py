# News item related to Derby Hippodrome appeal

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'DATA AGM Upcoming' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
The DATA AGM is scheduled for Tuesday 9th July\
""" ,
        item_text = """\
<div class="rows columns">
The DATA AGM will take place on Tuesday 9th July at 7.30pm. We're delighted to
announce that it will be held at the former Derby Central Library, The Wardwick,
at the kind invitation of <a href="https://www.derbymuseums.org/"
target="_blank">Derby Museums</a> and that the AGM will be followed by a tour of
the building’s performance spaces.
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0013_assembly_rooms' ) ,
    ]

    operations = [

        migrations.RunPython ( news_item ) ,

    ]
