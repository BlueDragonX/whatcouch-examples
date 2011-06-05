<%inherit file="/base.mako" />

<%def name="title()">Please Log In</%def>

<%def name="body()">
	<h1>Please Log In</h1>
	<form action="/auth/login" method="post">
		<dl>
			<dt><label for="login">Username</label></dt>
			<dd><input type="text" name="login" /></dd>
			<dt><label for="password">Password</label></dt>
			<dd><input type="password" name="password" /></dd>
		</dl>
		<input type="hidden" name="came_from" value="${came_from}" />
		<input type="submit" value="Login" /><br/>
		<span style="color: red;">${error}</span>
	</form>
</%def>

