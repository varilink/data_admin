import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2024 , 4 , 22 ) ,
        title = 'Save the date for the DATA AGM' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
Our AGM will be held on 18th July at 7.30pm at Derby Rugby Club\
""" ,
        item_text = """\
<div class="rows columns">
<p>
Save the date, our AGM will be held on Thursday 18th July at 7.30pm at Derby Rugby Club, Haslams Lane, Darley Abbey, Derby DE22 1EB. Robbie Kerr, Head of Leisure, Culture and Tourism at Derby City Council, will attend to give us more information about the Guildhall and answer questions from the floor.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0035_guildhall_theatre_plan_moves_forward' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
