import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2020 , 6 , 3 ) ,
        title = 'Theatres and the Coronavirus Crisis' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
DATA lobbies MPs prompted by COVID-19\
""" ,
        item_text = """\
<div class="row">
<div class="column">
<p>
Derby Arts and Theatre Association (DATA) are encouraging everyone to lobby
their MP to provide adequate funding to help theatres and concert halls survive
the current crisis.  We have sent a letter to the five MPs who represent the
area covered by DATA.  The text of our letter is as follows:
</p>
<em>
<p>
“THEATRES AND THE CORONAVIRUS CRISIS
</p>
<p>
Derby Arts and Theatre Association represents over forty amateur theatre and
music groups in the Derby area.  Because of the Covid 19 restrictions, the whole
of the live entertainment sector has been forced to close down.  For amateur
groups, this has resulted in the cancellation and/or rescheduling of all
productions and performances, with consequent financial losses for some.  All
these groups will be keen to recommence their activities as soon as the
situation allows.
</p>
<p>
As you will appreciate, amateur companies are dependent upon the availability of
venues in which to rehearse and perform.  Rehearsals take place in local
community facilities such as halls and schools, but performances are usually in
theatres, concert halls and other entertainment venues.
</p>
<p>
I am sure you will have seen the publicity about the dire financial position of
most of our theatres.  It is good that the Government has provided support
through, for example, the Arts Council England Emergency Fund and the Furlough
Scheme but this is clearly not going to be enough to save some theatres,
especially the many regional theatres, from financial ruin.  Andrew Lloyd Weber
and others have said that it will be completely impractical and unviable to
reopen theatres under the current social distance restrictions, so it is
unlikely theatres will reopen before 2021.
</p>
<p>
The country is celebrating the restarting of competitive sport this week, but
the arts are just as important to the social, economic and mental wellbeing of
our society.  Indeed, we have heard many accounts of how much people are missing
the stimulation, fellowship and stress relief that active participation in
amateur theatre and music activities provides.
</p>
<p>
I am writing, therefore, to ask that you do all you can to encourage the
Government to research appropriate audience safety measures and to provide the
necessary funding to ensure that our national, regional and local theatres and
concert halls can survive.”
</p>
</em>
<p>
If you care about amateur theatre and music - indeed all theatre and music -
please write to your MP asking them to help.  You can find out who your MP is by
following this link: <a href="https://members.parliament.uk/constituencies/"
target="_blank">Constituencies - MPs and Lords - UK Parliament</a>. You can
adapt the text above or use you own words. The important thing is to get the
message across to the Government. There are thousands of people who either
actively participate in amateur theatre or support it as friends or audience
members.
</p>
</div>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0021_52_weeks_festival' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
