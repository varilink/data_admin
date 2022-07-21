import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2021 , 5 , 21 ) ,
        title = 'DATA Membership Renewal Fees' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
In light of COVID-19, DATA waives membership renewal fees\
""" ,
        item_text = """\
<div class="row">
<div class="column">
<p>
As our <a href="/diary_scheme">Diary Scheme</a> page states, &quot;DATA member
societies pay a small fee to cover DATA&#39;s costs (currently £10 for two
years&#39; subscription)&quot. Renewals have recently become due. However, in
light of the COVID-19 situation, DATA has elected to waive those renewal fees at
this time.
</p>
</div>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0022_theatres_and_coronavirus' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
