import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2020 , 4 , 8 ) ,
        title = '52 Weeks Festival' ,
        image = '/assets/img/news_items/52-weeks-festival-card.jpg' ,
        precis = """\
DATA sponsors the 52 Weeks Festival\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium"
src="/assets/img/news_items/52-weeks-festival.jpg"
width="800px" height="503px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="480px" height="302px"
src="/assets/img/news_items/52-weeks-festival.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/52-weeks-festival.jpg"
width="640px" height="403px">
<p>
DATA is proud to announce that it is a sponsor of the 52 Weeks Festival, which
is described by its organisers as:
</p>
<p>
&quot;a brand new long term project celebrating creativity and culture across
Derbyshire. The 52 WEEKS FESTIVAL will run from May 2022 – May 2023 and aims to
bring the county together through:
</p>
<ul>
<li>
Celebrating Derbyshire’s heritage and culture
</li>
<li>
Supporting individuals and organisations within Derbyshire to develop their
activities and impact
</li>
<li>
Bringing new arts, culture and entertainment into Derbyshire
</li>
<li>
Inspiring people of all ages to take part
</li>
<li>
Bringing communities together
</li>
<li>
Improving individual well-being&quot;
</li>
</ul>
<p>
You can find out more about this exciting project here:
<br>
<a href="https://www.facebook.com/52weeksfestival/" target="_blank">
<i class="fab fa-facebook"></i>facebook.com/52weeksfestival/
<br>
<a href="https://www.instagram.com/52weeksfestival/" target="_blank">
<i class="fab fa-instagram"></i>instagram.com/52weeksfestival/
</a>
<a href="https://twitter.com/52weeksfestival" target="_blank">
<i class="fab fa-twitter"></i>twitter.com/52weeksfestival
</a>
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0020_temporary_theatre_news_item' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
