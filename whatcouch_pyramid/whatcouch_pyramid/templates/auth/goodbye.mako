<%inherit file="/base.mako" />

<%def name="title()">Goodbye!</%def>

<%def name="body()">
	<h1>You Have Been Logged Out.  Goodbye!</h1>
	<a href="/page">Go Home</a> -
	<a href="/auth/login">Log In Again</a> -
</%def>

