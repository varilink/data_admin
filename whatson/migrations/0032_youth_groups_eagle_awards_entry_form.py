import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2023 , 5 , 4 ) ,
        title = 'Youth Production Eagle Awards Category' ,
        image = '/assets/img/news_items/eagles-youth-groups-2023-card.png' ,
        precis = """\
Invitation for Entries in the New Eagle Awards Youth Production Category\
""" ,
        item_text = """\
<div class="rows columns">
<p>
On behalf of Derby Theatre, DATA would like to encourage entries in the new
Eagle Awards category for youth productions. To enter in this category, 80% of
the company must be under 18. Unfortunately, schools cannot be included in this
category.
</p>
<p>
To enter please complete and send in this <a href=
"/assets/docs/eagles-entry-form-youth-groups-2023.pdf">entry form</a>. Entries
must be sent in FOUR weeks before opening night.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0031_christmas_message_from_the_chair_2022' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
