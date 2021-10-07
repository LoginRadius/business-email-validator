"use strict";
import { readFile } from 'fs/promises';

const blockedEmailServices = JSON.parse(await readFile(new URL('./freeEmailService.json', import.meta.url)));

/**
 * Gets the `email` of type `string`. If an email is valid custom business mail
 * returns `true`, otherwise returns `false`.
 *
 * @param {string} email The email id to check.
 * @returns {boolean} `true|false` the validation result.
 * @example
 *
 * isValidMail('xyz@custombusinessmail.com')
 * > true
 * isValidMail('xyz@fakeinbox.com')
 * > false
 * isValidMail('xyz@gmail.com')
 * > false
 */

export default function isValidMail( email ) {
    if (email.indexOf('@') > 0 && email.indexOf('@') < email.length - 3) {
        var emailSenderDomain = email.split('@')[1];
        return !blockedEmailServices[emailSenderDomain];
    }
    return false;
}
