<?php

class BusinessEmailValidator
{
	/**
	* Used to check if provided email address is in list of blocked domains
	* @access public
	* @param string $email
	* The email address we want to check
	* @example 'john@doe.com'
	* @return bool
	*/
	public function isBlocked($email = '') {
		try {

		    // Domains list path
            $path = 'src/freeEmaislService.json';

            // Check if file exist
            if(file_exists($path) === FALSE) throw new Exception("error: File '{$path}' not found!");

            // Check if provided email is valid
            if(filter_var($email, FILTER_VALIDATE_EMAIL) === FALSE) throw new Exception("error: Email address '{$email}' is not valid!");

            // Convert json string to array
            $list_blocked = (array) json_decode(file_get_contents($path), true);

            // Get domain from email address
            $email_split = explode('@', $email);
            $email_domain = end($email_split);

            // Loop list to search for an email inside
            foreach ($list_blocked as $domain => $blocked) {
                if($email_domain === $domain) {
                    // email is blocked
                    return true;
                }
            }
            // Email's domain is not blocked
            return false;

        }catch (Exception $e){
            return false;
        }

	}
}
