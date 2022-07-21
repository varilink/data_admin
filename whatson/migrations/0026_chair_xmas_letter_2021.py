import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2021 , 11 , 28 ) ,
        title = 'Christmas Letter from Chair 2021' ,
        image = '/assets/img/news_items/data_logo_card.jpg' ,
        precis = """\
Please share this letter with your members and supporters\
""" ,
        item_text = """\
<div class="rows columns">
<p>
Dear Friends
</p>
<p>
It is an understatement to say that the <strong>Covid-19</strong> pandemic has
been challenging for local amateur theatre and music groups.  Productions and
concerts had to be cancelled or postponed from March 2020, in some cases even as
they were very close to actual performance. Some groups were able to continue
with online rehearsals and performances whilst others decided to suspend
operations.  We missed not only performing but also the fellowship of meeting at
rehearsals to act, sing or play our instruments together, and to socialise.
</p>
<p>
It is fantastic that groups are now restarting and some performances have
already happened.  But it is a sobering reality that many members of our
traditional audiences – even though fully inoculated – do not yet feel safe
enough to go into a theatre, church or concert hall.  It will take time for this
to sort itself out.  Getting bums on seats has always been a challenge –
especially for those companies whose production budgets rely on 80%+ attendance
– and Covid-19 has only made this worse.
</p>
<p>
But we remain positive and look forward to continuing to put on the top class
performances that audiences have come to expect from the amateur sector in the
Derby area.
</p>
<p>
I am afraid that news about the future of the <strong>Guildhall Theatre, Derby
</strong> does not improve with time.  Unfortunately the Council's position
remains that they are taking an holistic view of the repair and refurbishment of
the building and that feasibility studies are in progress.  These studies
include looking into using adjoining buildings which are in the Council's
ownership.  However, funding will be a challenge and it is likely that the
Council will be seeking grants from appropriate bodies.  DATA has submitted its
wish list of improvements including moving the bar to the adjoining building
which would make the existing bar area available for additional dressing-room
and storage purposes.
</p>
<p>
On your behalf, DATA has continued to press Derby City Council for a commitment
to reopen the Guildhall as soon as possible.  When I asked Councillor Ross
McCristal, the Council's Cabinet Member for Leisure and Culture, for a
timescale, his response was: &#8220;In my opinion it is unlikely to reopen
before 2025 but everything possible will be done to reopen the Guildhall as soon
as possible inline with our aspirational vision for the Guildhall.&#8221;
</p>
<p>
Whilst the situation with regard to the Guildhall is very disappointing, one
positive aspect is that the Council has fulfilled its promise to provide a
<strong>Temporary Performance Area in the Market Place</strong>.  At least two
DATA member societies have used the facility and this has helped to maintain
their presence and profile in the city.
</p>
<p>
You will have seen in the media that Derby City Council have obtained planning
permission to demolish the <strong>Assembly Rooms</strong> and are in
discussions with the University of Derby over the possibility of building a
replacement for <strong>Derby Theatre</strong> on the site.  Yes that means yet
another feasibility study by consultants but, if the project actually happens
(some may say that's a big 'if') then a new theatre plus a refurbished Guildhall
would potentially transform not only the Market Place but also the whole of the
Cathedral Quarter.  We await further developments with interest but we're not
holding our breath!
</p>
<p>
One project which does seem to be progressing is the proposed <strong>Becketwell
Arena</strong> on the old Debenhams / Duckworth Square site.  This is a joint
development by Derby City Council and St James Securities for various uses
including a 3,500 capacity arena located on the site of the former Pennine
Hotel, Pink Coconut nightclub and Laurie House offices.  The arena design also
incorporates a smaller performance space but details of this are yet to be
revealed.  Planning permission has been granted and ASM Global has been selected
to manage the venue.
</p>
<p>
Another item of positive news is that Derby has been long-listed to be <strong>
City of Culture</strong> in 2025 together with seven other cities.  Given the
long-term closure of the Guildhall and the Assembly Rooms, one could be forgiven
for viewing this with a degree of amused skepticism.  However, if Derby is
successful, it would result in a huge increase in investment and profile for the
cultural scene in the city and this would provide great opportunities for
amateurs to participate and benefit.  DATA is therefore fully supporting the
City of Culture bid.  The Bid Director is Adam Buss who many of you will know
has supported amateur theatre by compering the annual Eagle Awards ceremony.
</p>
<p>
Speaking of the <strong>Eagle Awards</strong>, Cheryl Mitchell of Derby Theatre
tells me that the plan is that &#8220;judging will not be returning until June
2022. This is to ensure a fair and level playing field for all companies as not
everyone has been able to produce a show for the 21/22 season. Therefore, we are
hoping that a return to normal will be expected ready for the 22/23 season and
we can start accepting entries in June 2022.&#8221;
</p>
<p>
Do please continue to submit your organisation's productions for inclusion in
the DATA Diary.  It is a free service as part of your very reasonable membership
subscription.  You can either do this yourself online by logging into the Diary
system, or submit details to our DATA Diary Administrator – Dave Williamson – at
<a href="mailto:admin@derbyartsandtheatre.org.uk">
admin@derbyartsandtheatre.org.uk</a> The  monthly Diary email has a wide
circulation and events are simultaneously posted on the DATA Facebook page and
Twitter feed for sharing through social media channels.  Overall it's a very
cost-effective and simple marketing tool.
</p>
<p>
Finally, may I wish all a very happy festive season and all good fortune for
your future ventures.
</p>
<p>
Steve Dunning<br>
Chair<br>
Derby Arts and Theatre Association (DATA)<br>
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0025_noc_md' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
