function(doc) {
	if (doc.doc_type == 'User') {
		for (var i = 0; i < doc.groups.length; i++) {
			for (var j = 0; j < doc.groups[i].permissions.length; j++) {
				emit(doc.username, doc.groups[i].permissions[i]);
			}
		}
	}
}
