<%inherit file="/base.mako" />

<%def name="title()">Pages</%def>

<%def name="body()">
	<h1>Couch What? Choose a Page!</h1>
	<ul>
		<li>
			<a href="/page/public">Public</a>
		</li>
		<li>
			<a href="/page/private">Private</a>
		</li>
	</ul>
</%def>

