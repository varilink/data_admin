import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2022 , 10 , 28 ) ,
        title = 'DATA AGM' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
The Chair's report to the 2022 DATA AGM\
""" ,
        item_text = """\
<div class="rows columns">
<p>
The DATA AGM of 2022 took place on 18th October 2022. The main topic of Steve
Dunning's annual report as DATA Chair, was DATA's lobbying of Derby City Council
to repopen the Guildhall as soon as possible. His report also included the
latest status in respect of Derby Assembly Rooms and the Becketwell Arena
development, the design of which incorporates a smaller performance space,
though details of this are yet to be revealed.
</p>
<p>
On other, non-venue related, topics, Steve reminded the AGM of the DATA Diary
service and reported on the future plans for the Eagle Awards. Why not download
the <a href="/assets/docs/agm2022/Annual Report 2022.pdf">Chair's report to the 2022 DATA AGM</a> and read it in full?
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0029_data_agm' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
