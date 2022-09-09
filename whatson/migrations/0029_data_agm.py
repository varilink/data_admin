import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2022 , 9 , 5 ) ,
        title = 'DATA AGM' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
The DATA AGM will take place on 18th October 2022\
""" ,
        item_text = """\
<div class="rows columns">
<p>
The Annual General Meeting of DATA will take place on Tuesday 18th October 2022
at 7.00pm at Shakespeare House, Kedleston Road, Derby.  This will be the first
AGM for three years, because of Covid, so we hope for a good turnout.  The
agenda and reports will be sent out nearer the date.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0028_subscriptions' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
