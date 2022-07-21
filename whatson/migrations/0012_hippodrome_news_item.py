# News item related to Derby Hippodrome appeal

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'Derby Hippodrome 2019' ,
        image = '/assets/img/news_items/hippodrome_card.jpg' ,
        precis = """\
Derby Hippodrome 2019 - Crowdfunding Campaign launched\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/New+Hippodrome.png"
width="640px" height="319px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="199px"
src="/assets/img/news_items/New+Hippodrome.png">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/New+Hippodrome.png"
width="550px" height="274px">
<p>
The Derby Hippodrome Restoration Trust has launched a Crowdfunding Campaign to
raise funds for stage one of meeting its objectives to:
</p>
<ul style="list-style-position: inside;">
<li>
Restore an historic Grade 2 public building (in 2 phases)
</li>
<li>
Create an exciting new entertainment venue & community hub
</li>
<li>
Create new jobs in an enhanced Derby cultural sector, complementing existing
venues
</li>
<li>
Provide a large boost to St Peter's Quarter regeneration, creating a vibrant
evening atmosphere
</li>
</ul>
<p>
This 2019 Crowdfunding Campaign will raise the money to make an even bigger
grant application, backed by a host of "experts" to back the restoration trust's
proposals. This is stage one of a "domino run" project that all starts with
THIS crowdfunding campaign.
</p>
<p>
You can find the Derby Hippodrome Restoration Trust's Crowdfunding page at
<a href="https://www.crowdfunder.co.uk/derbyhippodromerestoration">
crowdfunder.co.uk/derbyhippodromerestoration
</a>. Here is a a message from Gwen Taylor, patron of the trust.
</p>
<div class="responsive-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/OaM-gFyHq8Q"
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen></iframe>
</div>
<p>
Other Derby Hippodrome Restoration Trust Links:
</p>
<span style="font-size: 3rem; color: #4dac71;">
<a href="https://www.derbyhippodrometrust.org/">
<i class="fas fa-globe"></i>
</a>
</span>
&nbsp;
<a href="https://www.facebook.com/DerbyHippoRT/">
<span style="font-size: 3rem; color: #3B5998;">
<i class="fab fa-facebook"></i>
</span>
</a>
&nbsp;
<a href="https://twitter.com/DerbyHippodrome">
<span style="font-size: 3rem; color: #1DA1F2;">
<i class="fab fa-twitter"></i>
</span>
</a>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0011_guildhall_news_item' ) ,
    ]

    operations = [

        migrations.RunPython ( news_item ) ,

    ]
