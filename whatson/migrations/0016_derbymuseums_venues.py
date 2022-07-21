# Publicise Derby Museums venue letting service

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2019 , 7 , 10 ) ,
        title = 'Derby Museums\' Hosting of the DATA AGM' ,
        image = '/assets/img/news_items/joseph_wright_card.jpg' ,
        precis = """\
DATA extends thanks to Derby Museums for their hosting of the DATA AGM
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/joseph_wright.jpg"
width="640px" height="472px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="295px"
src="/assets/img/news_items/joseph_wright.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/joseph_wright.jpg"
width="550px" height="406px">
<p>
The DATA AGM on 9th July took place in the magnificent setting of the former
Derby Central Library building at the kind invitation, at no cost, of Derby
Museums. Following the AGM, the DATA members present were treated to a
fascinating guided tour of the building's museum and art gallery.
</p>
<p>
This building and several others that are under the management of Derby Museums
are available for <a href="https://www.derbymuseums.org/venue-hire">venue hire
</a>. They are potential performance spaces and indeed have already fulfilled
this role for DATA members.
</p>
<p>
Derby Museums' have stated that for DATA members they are happy to look at
giving at a discount to their usual commercial rates if this can arrive at a
deal that is acceptable to both parties.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0015_guildhall_news_item' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]