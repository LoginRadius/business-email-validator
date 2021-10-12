var BusinessEmailValidtor = (function () {

	const blockedEmailServices = require('../../src/freeEmailService.json');	
	var module = {};

	module.validate = function (email) {
		if (email.indexOf('@') > 0 && email.indexOf('@') < email.length - 3) {
			var emailDomain = email.split('@')[1];
			return !blockedEmailServices[emailDomain];
		}
		return false;
	}

	return module;
})();

