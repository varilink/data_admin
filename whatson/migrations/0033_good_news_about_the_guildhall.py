import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2023 , 11 , 6 ) ,
        title = 'At last! Good news about the Guildhall' ,
        image = '/assets/img/news_items/guildhall_card.jpg' ,
        precis = """\
Grant to be diverted to the repair and refurbishment of the Guildhall and improvements to the existing Derby Theatre\
""" ,
        item_text = """\
<div class="rows columns">
<img src="/assets/img/news_items/guildhall.jpg" class="float-left" width="450"
style="margin-right: 1em;">
<p>
DATA have enthusiastically welcomed the news, announced by Derby City Council on 1st November 2023, that the £20 million Levelling Up Fund grant will be diverted to the repair and refurbishment of the Guildhall and improvements to the existing Derby Theatre.
</p>
<p>
The grant was originally intended to go to ‘Assemble’, a project that would have seen the Derby Theatre at the Derbion Centre close and be replaced by a new theatre on the Assembly Rooms site.  But the increased cost of that project has made it unviable.
</p>
<p>
It is understood that the money will be used to ensure that between the Guildhall Theatre and Derby Theatre there will be a joint capacity of 950 seats - with potentially 350 at the Guildhall Theatre, where the capacity is currently 244, and 600 at Derby Theatre, which has a current limit of 535 seats.
</p>
<p>
The Guildhall was previously the performance venue used by a number of amateur theatre groups and dance schools and its closure in 2019 forced companies to look for alternative venues including some as far afield as Long Eaton, Repton and Chesterfield.
</p>
<p>
DATA have been campaigning continually for the reopening of the Guildhall ever since its closure.  Our chair - Steve Dunning - has been in regular contact with the Derby City Council and met the Leader and Deputy Leader in June to press the case in person.  Our thanks go especially to Councillor Nadine Peatfield, Deputy Leader, for her efforts to get the Government to allow the £20 million grant to be repurposed.
</p>
<p>
We now look forward to working in partnership with the Council on the design of the Guildhall refurbishment scheme and have resubmitted our ‘wish list’ for improvements originally drawn up in 2021.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0032_youth_groups_eagle_awards_entry_form' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
