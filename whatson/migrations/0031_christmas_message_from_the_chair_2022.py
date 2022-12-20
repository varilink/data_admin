import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.date ( 2022 , 12 , 20 ) ,
        title = 'Christmas Message from the Chair' ,
        image = '/assets/img/news_items/data-logo-card-christmas.png' ,
        precis = """\
The Christmas 2022 Message from the DATA Chair\
""" ,
        item_text = """\
<div class="rows columns">
<p>Dear DATA Members</p>
<p>
I circulated a full report for the DATA Annual General Meeting on 18 October
2022 so, for this bulletin, I'm going to tell you about the latest developments
on the key issues we've been dealing with on your behalf.
</p>
<p class="lead">The Guildhall Theatre, Derby</p>
<p>
The Guildhall Theatre has been closed since January 2019 and this issue has been
our main focus since then.  The eleven amateur companies, plus dance studios,
who used to hire the Guildhall have faced major problems finding alternative
venues – including locations in Repton, Long Eaton and Chesterfield – and, in
one or two cases, this has threatened their future viability.
</p>
<p>
The Council's position is that they are taking an holistic view of the repair
and refurbishment of the building and that feasibility studies are in progress.
These studies include looking into using adjoining buildings which are in the
Council's ownership.  However, funding will be a challenge and it is likely that
the Council will be seeking grants from appropriate bodies.  DATA has submitted
its wish list of improvements including moving the bar to the adjoining building
which would make the existing bar area available for additional dressing-room
and storage purposes.
</p>
<p>
In July 2022, we conducted a short survey to ascertain the interest from amateur
groups in using the Guildhall if and when it reopens.  Of the thirteen groups
who responded, twelve said they were either likely or very likely to use the
venue.
</p>
<p>
On your behalf, DATA has continued to press Derby City Council for a commitment
to reopen the Guildhall as soon as possible. Our main challenge has been a lack
of helpful communication from the Council about its intentions and so, in July
2022, we submitted a Freedom of Information request for details of the Guildhall
scheme.  The Council missed two statutory deadlines for the supply of the
information and finally sent us its response on 2nd December! 
</p>
<p>The response contains the following statements:</p>
<blockquote>
&ldquo;The options are conceptual/not finalised and will need to be considered
by the Council Cabinet in March 2023.&rdquo;
</blockquote>
<blockquote>
&ldquo;Funding options for the project are to be developed and will form part of
the cabinet report, which is yet to be concluded. It is likely that any works
will be fully council funded unless external funding opportunities are
identified and successfully bid for to reduce the burden on council funds. At
the time of writing this response, no external funding opportunities contribute
to the project.&rdquo;
</blockquote>
<p>
It is clear from these statements that the future of the Guildhall is far from
certain so I have had a meeting with the Councillor Jonathan Smale, who is the
new Cabinet Member with responsibility for Culture, to open dialogue and to get
an assurance that a report will go to the March 2023 Cabinet meeting with firm
proposals to repair, refurbish and reopen the Guildhall. Councillor Smale
acknowledged that the communication about the Guildhall had not been acceptable.
He assured me that he would chase up the progress of the proposed report and
come back to me with an update by the first week in January. He did say that
the estimates for the remedial works at the Guildhall ran into many millions,
which is not a surprise, and that a number of options were being looked at.
</p>
<p>
Rest assured that DATA will continue to pursue the Guildhall issue vigorously
in the New Year.
</p>
<p class="lead">
Possible Relocation of Derby Theatre to Derby Assembly Rooms Site
</p>
<p>
As you will have seen in the media, there is a proposal to relocate the Derby
Theatre from the Derbion Centre to the Assembly Rooms site. The Eagle Market is
to be closed and the owners of the Derbion Centre have published plans for their
own development to improve public access from the bus station, build a new
entrance to Derbion on East Street, add additional shops and leisure outlets and
create a new public boulevard. Derby City Council have said in an email to me
that &ldquo;The proposed development of a new theatre on part of the site of the
Assembly Rooms complex (incl. the Multi Storey Car Park) is currently the
subject of a bid to Government for £20M from its Levelling Up Fund. The
Government has stated that an announcement of funding awards will be &lsquo;in
the Autumn&rsquo;. So far we have not received any notifications whether we have
been successful.&rdquo;
</p>
<p>
A report to the Council Cabinet on the Levelling up Fund bid on 5 July 2022
shows that the Levelling Up bid covers three projects:
</p>
<ul>
<li>&lsquo;Assemble&rsquo; (New Learning Theatre), Assembly Rooms site</li>
<li>New Hotel, Becketwell</li>
<li>Friar Gate Goods Yard and Bridge.</li>
</ul>
<p>
We will monitor the situation but we acknowledge that there must be a risk that
this project may not go ahead if the Levelling Up Fund bid is unsuccessful.
</p>
<p class="lead">And finally &#8230;</p>
<p>
The lack of suitable performance venues continues to detrimentally affect the
cultural offer of the city and, therefore, the amateur community.  I
congratulate our corporate members for your ingenuity in finding imaginative
solutions to the problem.  Our music and concert groups seem to have had success
in utilising local churches for their performances and this is an excellent
example of finding good ways to keep going.
</p>
<p>
The amount of talent and creativity amongst our members never ceases to amaze me
and makes me very proud to lead an organisation which strives to help us work
together for the benefit of all.  The efforts of you all - on and off stage and
especially those on your management committees - are very much appreciated.
</p>
<p>
I encourage you to use the DATA Diary to publicise your events - it's part of
your membership benefits at no extra cost!
</p>
<p>
Don't forget, DATA is your Association; if you have any views or suggestions,
please get in touch.
</p>
<p>
Please circulate a link to this bulletin on our website to your members so that
as many people as possible are kept informed.
</p>
<p>
With all good wishes for the festive season and for your future productions.
</p>
<img src="/assets/img/chair-signature.jpg">
<p>
Steve Dunning<br>
Chair, Derby Arts and Theatre Association (DATA)<br>
<a href="mailto:chair@derbyartsandtheatre.org.uk">
chair@derbyartsandtheatre.org.uk</a><br>
December 2022
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0030_data_agm_2022_chair_report' ) ,
    ]

    operations = [
        migrations.RunPython ( news_item ) ,
    ]
