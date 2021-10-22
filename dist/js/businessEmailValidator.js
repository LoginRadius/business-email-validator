const blockedDomains = require("../../src/freeEmailService.json");

/**
 * 
 * @param email | email id you want to validate 
 * @returns valid: boolean, errored: optional boolean, message: optional string
 */
const BusinessEmailValidtor = (email) => {
	if (email && email.trim().length > 0) {
		if (email.indexOf('@') > 0 && email.indexOf('@') < email.length - 3) {
			const emailDomain = email.split('@')[1];
			return {
				valid: !blockedDomains[emailDomain]
			}
		}
		return {
			valid: false,
			errored: true,
			message: "Invalid email format!"
		}
	}
	return {
		valid: false,
		errored: true,
		message: "Email is Required and cannot be empty!"
	}
}
