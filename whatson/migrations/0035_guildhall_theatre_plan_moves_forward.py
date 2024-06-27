import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2024 , 4 , 22 ) ,
        title = 'Guildhall Theatre plan moves forward' ,
        image = '/assets/img/news_items/guildhall_card.jpg' ,
        precis = """\
Plan to restore Guildhall Theatre moves forward as part of major investment\
""" ,
        item_text = """\
<div class="rows columns clearfix">
<img src="/assets/img/news_items/guildhall.jpg" class="float-left" width="400"
style="margin-right: 1em;">
<p>
DATA welcome the news that the project to refurbish and reopen the Guildhall Theatre, Derby is to go ahead. Read the <a href="https://www.derby.gov.uk/news/2024/april/big-plans-for-city-theatres-leap-forward/" target="_blank">Derby City Council press release</a>.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0034_entry_deadline_for_derby_arts_festival' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
